## Cliente
cliente_username = []
cliente_cpf = []
cliente_senha = []
cliente_email = []
cliente_limitecredito = []

## Carrinho
carrinho_total = []
carrinho_itens = []

## Produtos
produtos_nome = [
    'Farinha de Trigo 5kg', 'Arroz 5kg', 'Feijão 1kg', 'Açucar 1 kg', 'Sal 1kg',
    'Espaguete 500g', 'Biscoito Agua e Sal 370g', 'Biscoito Recheado 150g', 'Macarrão Instantâneo 90g', 'Pão Francês 100g',
    'Água Mineral 1.5L', 'Refrigerante 2L', 'Leite Integral 1L', 'Óleo de Soja 900ml', 'Café Solúvel 160g',
    'Sabão em pó 1kg', 'Shampoo 325ml', 'Papel Higiênico 4x30m', 'Sabonete 100g', 'Pasta de dente 90g',
    ]
produtos_preco = [
    18.00, 19.50, 4.75, 4.50, 2.50,
    4.75, 5.00, 2.00, 1.75, 1.50,
    4.00, 7.00, 3.75, 4.75, 13.00,
    10.00, 8.50, 5.50, 2.75, 5.00,
    ]

## Validar o CPF:
def validacpf(cpfstr):
    # Verifica se CPF digitado é somente números, tem 11 digitos ou tem todos números iguais
    if not cpfstr.isdecimal() or len(cpfstr) != 11 or cpfstr == cpfstr[::-1]:
        return False
    cpf = [int(x) for x in cpfstr]
    verificador = []
    for n in range(9, 11):
        # Acumula multiplicacao dos digitos
        multipl = sum((cpf[digit] * (n+1 - digit) for digit in range(0, n)))
        # Confere os digitos verificadores
        if (multipl%11) < 2:
            verificador.append(True) if cpf[n] == 0 else verificador.append(False)
        else:
            verificador.append(True) if cpf[n] == (11-(multipl%11)) else verificador.append(False)
    if verificador[0] and verificador[1]:
        return True
    return False

## Entrada de LOGIN para os MENUS
def login():
    if cliente_cpf:
        print("Informe o seu LOGIN")
        cpf = input("CPF: ")
        if validacpf(cpf):
            # Verifica se o CPF já está cadastrado
            if cpf in cliente_cpf:
                index = cliente_cpf.index(cpf)
                senha = input("Senha: ")
                # Verifica se a senha digitada confere no cadastro
                if senha == cliente_senha[index]:
                    return index
                else:
                    menu = input("\nSenha incorreta.\n\nPressione ENTER para continuar.")
                    return 'ERRO'
            else:
                opt = input("\nCliente não encontrado.\nDeseja cadastrar novo cliente?(s/n): ")
                if opt == 's':
                    cadastro()
                return 'ERRO'
        else:
            menu = input("\nCPF Inválido.\n\nPressione ENTER para continuar.")
            return 'ERRO'
    else:
        menu = input("Nenhum cliente cadastrado!\n\nPressione ENTER para continuar.")
        return 'ERRO'

## Cadastra novos clientes e verifica se o cliente já existe a partir do cpf
def cadastro():
    print("\n** CADASTRO CLIENTE **")
    cpf = input("\nDigite o CPF (somente números)\nou pressione ENTER para voltar ao MENU: ")
    if cpf == "":
        return
    # Verifica se o CPF é válido para iniciar o cadastro
    if validacpf(cpf): 
        if not cpf in cliente_cpf:
            cliente_cpf.append(cpf)
            # Verifica entrada de nome válido (não vazio e somente a-z)
            while True: 
                print()
                nome = input("Digite o nome do usuário: ")
                if len(nome) < 1:
                    print("ERRO: Digite pelo menos um caractere.")
                elif not nome.replace(' ','').isalpha():
                    print("ERRO: Somente letras de a-z são permitidas.")
                else:
                    break
            cliente_username.append(nome)
            # Verifica entrada de senha válida (total 6 caracteres e confere senha)
            while True: 
                print()
                while True:
                    criasenha = input("Criar uma senha (6 caracteres): ")
                    if len(criasenha) != 6:
                        print("Sua senha precisa ter 6 caracteres!")
                    else:
                        break                       
                conferesenha = input("Confirmar a senha: ")
                if criasenha != conferesenha:
                    print("As senhas digitadas são diferentes.")
                else:
                    break
            cliente_senha.append(criasenha)
            cliente_email.append(input("\nDigite o email: "))
            # Inicia carrinho do cliente
            cliente_limitecredito.append(1000.00)
            carrinho_itens.append([0]*20)
            carrinho_total.append(0)
            menu = input("\nCadastro efetuado!\n\nPressione ENTER para continuar.")
            return
        else:
            index = cliente_cpf.index(cpf)
            menu = input(f"\nCliente já cadastrado com o nome: {cliente_username[index]}\n\nPressione ENTER para continuar.")
            return
    else:
        menu = input("\nCPF Inválido.\n\nPressione ENTER para continuar.")
        return

## Menu compras para CPF
def comprar():
    print("\n** MENU COMPRAS **\n")
    index = login()
    if index != 'ERRO':
        while True:
            print("\n(1) Comprar itens\n(2) Remover itens\n(3) Ver o carrinho\n(4) Listar produtos\n(5) Voltar")
            buyoption = input("\nOPÇÃO: ")
            if buyoption == '5':
                break
            elif buyoption == '4':
                mostra_produtos()
                continue
            elif buyoption == '3':
                mostrar_carrinho(index)
                continue
            elif buyoption == '2':
                removeitens(index)
                continue
            elif buyoption != '1':
                continua = input("\nOpção inválida!\n\nPressione ENTER para continuar.")
                continue
            # Verifica se o código digitado é válido
            while True:
                try:
                    coditem = int(input("\nCódigo do item: "))
                    if coditem > len(produtos_nome) or coditem < 1:
                        print("Item inexistente.")
                        continue
                    break
                except ValueError:
                    print("Entrada inválida. Digite o código do produto.")
            print(f"{produtos_nome[coditem-1]} -- R$ {produtos_preco[coditem-1]:.2f}")
            # Verifica se a quantidade a adicionar é válida
            while True:
                try:
                    quantia_add = int(input("\nQuantidade: "))
                    break
                except ValueError:
                    print("Entrada inválida. Digite um número inteiro positivo.")
            if quantia_add < 1:
                continua = input("Nenhum item adicionado!\n\nPressione ENTER para continuar.")
                continue
            else:
                if carrinho_total[index] + (produtos_preco[coditem-1]*quantia_add) > cliente_limitecredito[index]: # verifica limite
                    print(f"\nNão foi possível adicionar este item ao seu carrinho\npois estoura seu limite de R$ {cliente_limitecredito[index]:.2f}")
                    print(f"\nO valor atual do seu carrinho é R$ {carrinho_total[index]:.2f}")
                    continua = input("Faça o pagamento das compras para liberar seu saldo!\n\nPressione ENTER para continuar.")
                    continue
                else:
                    # Adiciona os itens ao carrinho e atualiza o valor total
                    carrinho_total[index] += (produtos_preco[coditem-1]*quantia_add)
                    carrinho_itens[index][coditem-1] += quantia_add
                    print(f"\n{quantia_add} un. de {produtos_nome[coditem-1]} adicionado ao carrinho!\n\nTOTAL do Carrinho: R$ {carrinho_total[index]:.2f}")
                    continua = input("\nPressione ENTER para continuar.")
                    continue
    return

# Remover itens do carrinho
def removeitens(index):
    print("\n** REMOVER ITENS **\n")
    if carrinho_total[index] > 0:
        for codigo in range(len(produtos_nome)):
            # Printa a lista de produtos que tem quantia maior que zero no carrinho
            if carrinho_itens[index][codigo] > 0:
                print(f"({codigo+1}) {produtos_nome[codigo]} -- {carrinho_itens[index][codigo]} un. ")
        while True:
            try:
                coditem = int(input("\nCódigo do produto: "))
                break
            except ValueError:
                print("Entrada inválida. Digite o código do produto.")
        if carrinho_itens[index][coditem-1] < 1:
            volta = input("\nProduto não está no carrinho.\n\nPressione ENTER para voltar às compras.")
            return
        while True:
            try:
                quantia_remov = int(input("\nQuantos deseja remover: "))
                break
            except ValueError:
                print("Entrada inválida. Digite um número inteiro positivo.")
        if quantia_remov < 1:
            volta = input("\nNenhum item removido!\n\nPressione ENTER para voltar às compras.")
            return
        elif quantia_remov > carrinho_itens[index][coditem-1]:
            volta = input("\nQuantia maior do que a atual no carrinho.\n\nPressione ENTER para voltar às compras.")
            return
        else:
            # Remove itens e atualiza valor total do carrinho
            carrinho_total[index] -= (produtos_preco[coditem-1]*quantia_remov)
            carrinho_itens[index][coditem-1] -= quantia_remov
            volta = input(f"\n{quantia_remov} un. de {produtos_nome[coditem-1]} removido do carrinho!\n\nPressione ENTER para voltar às compras.")
            return
    else:
        volta = input("Carrinho Vazio!\n\nPressinone ENTER para voltar às compras.")
    return

# Prateleira de produtos
def mostra_produtos():
    print("\n********** LISTA DE PRODUTOS ***********")
    print("========================================")
    print("(CÓDIGO)     DESCRIÇÃO           PREÇO")
    print("========================================")
    for n in range(len(produtos_nome)):
        print((f"({n+1})").ljust(4), (produtos_nome[n]).center(25),f" R$ {produtos_preco[n]:.2f}")
    print("========================================")
    volta = input("\nPressione ENTER para continuar.")
    return

# Mostra o carrinho de compras do cliente
def mostrar_carrinho(index):
    print("\n****** CARRINHO ******\n")
    if carrinho_total[index] > 0:
        print(f"Carrinho de {cliente_username[index]}:")
        print("______________________")
        for codigo in range(len(produtos_nome)):
            # Mostra somente itens com quantia maior que ZERO no carrinho
            if carrinho_itens[index][codigo] > 0:
                print(f"{carrinho_itens[index][codigo]} un. de {produtos_nome[codigo]}.")
        print("______________________")
        print(f"TOTAL: R$ {carrinho_total[index]:.2f}")
    else:
        print("Carrinho Vazio!")
    volta = input("\nPressione ENTER para continuar.")
    return

## Mostra um cliente a partir do CPF
def consulta_cliente():
    print("\n** CONSULTA CLIENTE **")
    if cliente_cpf:
        cpf = input("\nDigite o CPF do cliente: ")
        if validacpf(cpf):
            if cpf in cliente_cpf:
                index = cliente_cpf.index(cpf)
                menu = input(f"Nome: {cliente_username[index]}\nEmail: {cliente_email[index]}\n\nPressione ENTER para continuar.")
                return
            else:
                menu = input("\nCliente não encontrado.\n\nPressione ENTER para continuar.")
                return
        else:
            menu = input("\nCPF inválido.\n\nPressione ENTER para continuar.")
            return
    else:
        menu = input("\nNenhum cliente cadastrado!\n\nPressione ENTER para continuar.")
        return

## Pagamento para zerar carrinho
def pagamento():
    print("\n** PAGAMENTO **\n")
    index = login()
    if index != 'ERRO':
        while True:
            import time
            if carrinho_total[index] == 0:
                menu = input("\nCarrinho vazio! Selecione alguns itens antes de gerar uma cobrança.\n\nPressione ENTER para continuar.")
                return
            print(f"\nValor total da conta: R$ {carrinho_total[index]:.2f}\n")
            print("OPÇÕES:\n1- Pagamento à vista\n2- Pagamento por transferência\n3- Voltar ao MENU")
            formapagamento = input("\nComo deseja pagar: ")
            if formapagamento == "1": 
                print("\nDevolvendo o troco... Aguarde.")
                time.sleep(3) # "Simula" processamento da operação
                carrinho_itens[index].clear()
                carrinho_itens[index] += [0]*20
                carrinho_total[index] = 0
                menu = input("\nPagamento aceito! Você já pode retirar suas compras.\n\nPressione ENTER para continuar.")
                return
            elif formapagamento == "2":
                print("\nConfirmando recebimento da transferência... Aguarde.")
                time.sleep(3) # "Simula" processamento da operação
                carrinho_itens[index].clear()
                carrinho_itens[index] += [0]*20
                carrinho_total[index] = 0
                menu = input("\nPagamento confirmado! Você já pode retirar suas compras.\n\nPressione ENTER para continuar.")
                return
            elif formapagamento == "3":
                return
            continua = input("\nOpção inválida.\n\nPressione ENTER para continuar.")
            continue
    return

## MENU DE OPÇÕES
def menu():
    opcao = "-1"
    while opcao != "0":
        print("""\nMENU:
1 - Cadastro
2 - Comprar/remover produtos
3 - Mostrar carrinho
4 - Pagar conta
5 - Consultar cliente
6 - Mostrar produtos
0 - Sair""")
        opcao = input("\nDigite o código da opção: ")

        if opcao == "1":
            cadastro()

        elif opcao == "2":
            comprar()

        elif opcao == "3":
            print("\n** MOSTRAR CARRINHO **\n")
            # Login externo para permitir acessar diretamente do menu compra.
            index = login()
            if index != 'ERRO':
                mostrar_carrinho(index)

        elif opcao == "4":
            pagamento()

        elif opcao == "5":          
            consulta_cliente()

        elif opcao == "6":         
            mostra_produtos()

        elif opcao == "0":
            print("Saindo!")

        else:
            continua = input("\nOpção inválida!\n\nPressione ENTER para continuar.")

menu()

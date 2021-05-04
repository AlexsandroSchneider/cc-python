## Inicia classe e variáveis cliente
class Clientes:
    nome = ''
    senha = ''
    email = ''
    limite = 1000
    total = 0
    itens = []

cliente_cpf = []
cliente = []

## Produtos
produtos_nome = [
    'Farinha de Trigo 5kg', 'Arroz 5kg', 'Feijão 1kg', 'Açucar 1 kg', 'Sal 1kg',
    'Espaguete 500g', 'Biscoito Agua e Sal 370g', 'Biscoito Recheado 150g', 'Macarrão Instantâneo 90g', 'Pão Francês 100g',
    'Água Mineral 1.5L', 'Refrigerante 2L', 'Leite Integral 1L', 'Óleo de Soja 900ml', 'Café Solúvel 160g',
    'Sabão em pó 1kg', 'Shampoo 325ml', 'Papel Higiênico 4x30m', 'Sabonete 100g', 'Pasta de dente 90g',
    ]
produtos_preco = [
    17.99, 19.50, 4.69, 4.49, 2.29, 4.69, 4.99, 1.99, 1.75, 1.50,
    4.00, 6.90, 3.79, 4.69, 12.90, 9.98, 8.39, 5.59, 2.65, 4.89
    ]

## Validar o CPF:
def validacpf(cpfstr):
    if not cpfstr.isdecimal() or len(cpfstr) != 11 or cpfstr in ('00000000000', '11111111111', '22222222222', '33333333333', '44444444444', '55555555555', '66666666666', '77777777777', '88888888888', '99999999999', '01234567890'):
        return False
    cpf = []
    verificador = []
    base = [9, 10]
    digit = [-2, -1] # digitos verificadores n° 10 e 11
    for i in cpfstr:
        cpf.append(int(i))
    for n in range(2): # duas verificações
        mult = base[n]+1
        soma = 0
        for i in range(base[n]): # soma num acumulador a multiplicação das posições [0] até [n] do CPF
            soma += cpf[i]*mult
            mult -= 1
        resto = soma - (11*(soma//11))
        if resto < 2:
            verificador.append(True) if cpf[digit[n]] == 0 else verificador.append(False)  
        else:
            verificador.append(True) if cpf[digit[n]] == (11-resto) else verificador.append(False)
    if verificador[0] and verificador[1]:
        return True
    return False

## Verifica se cadastro já existe e se senha confere
def login():
    if cliente_cpf:
        print("Informe o seu LOGIN")
        cpf = input("CPF: ")
        if validacpf(cpf):
            if cpf in cliente_cpf:
                index = cliente_cpf.index(cpf)
                senha = input("Senha: ")
                if senha == cliente[index].senha:
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
    if validacpf(cpf): # valida CPF para realizar cadastro
        if not cpf in cliente_cpf:
            cliente_cpf.append(cpf)
            cadastra = Clientes()
            while True: # verifica entrada de nome válido (não vazio e somente a-z)
                print()
                nome = input("Digite o nome do usuário: ")
                if len(nome) == 0:
                    print("ERRO: Digite pelo menos um caractere.")
                elif not nome.replace(' ','').isalpha():
                    print("ERRO: Somente letras de a-z são permitidas.")
                else:
                    break
            cadastra.nome = nome
            while True: # verifica entrada de senha válida (total 6 caracteres e confirma senha)
                print()
                while True:
                    criasenha = input("Criar uma senha (6 caracteres): ")
                    if len(criasenha) != 6:
                        print("Sua senha precisa ter 6 caracteres!")
                    else:
                        break                       
                conferesenha = input("Confirmar a senha: ")
                if criasenha != conferesenha:
                    print("Senhas não são iguais.")
                else:
                    break
            cadastra.senha = criasenha
            cadastra.email = input("\nDigite o email: ")
            cadastra.itens = [0]*20 # inicia itens do carrinho para o cliente
            cliente.append(cadastra)
            menu = input("\nCadastro efetuado!\n\nPressione ENTER para continuar.")
            return
        else:
            index = cliente_cpf.index(cpf)
            menu = input(f"\nCliente já cadastrado com o nome: {cliente[index].nome}\n\nPressione ENTER para continuar.")
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
            opcao = '2'
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
            while True:
                try:
                    quantia = int(input("\nQuantidade: "))
                    break
                except ValueError:
                    print("Entrada inválida. Digite um número inteiro positivo.")
            if quantia <= 0:
                continua = input("Nenhum item adicionado!\n\nPressione ENTER para continuar.")
                continue
            else:
                if cliente[index].total+(produtos_preco[coditem-1]*quantia) > cliente[index].limite:
                    print(f"\nNão foi possível adicionar este item ao seu carrinho\npois estoura seu limite de R$ {cliente[index].limite:.2f}")
                    continua = input("\nFaça o pagamento das compras para comprar mais!\n\nPressione ENTER para continuar.")
                    continue
                else:
                    cliente[index].total+=(produtos_preco[coditem-1]*quantia)
                    cliente[index].itens[coditem-1]+=quantia
                    print(f"\n{quantia} un. de {produtos_nome[coditem-1]} adicionado ao carrinho!\n\nTOTAL do Carrinho: R$ {cliente[index].total:.2f}")
                    continua = input("\nPressione ENTER para continuar.")
                    continue
    return

# Remover itens do carrinho
def removeitens(index):
    print("\n** REMOVER ITENS **\n")
    if cliente[index].total > 0:
        for codigo in range(len(produtos_nome)):
            if cliente[index].itens[codigo]>0:
                print(f"({codigo+1}) {produtos_nome[codigo]} -- {cliente[index].itens[codigo]} un. ")
        while True:
            try:
                coditem = int(input("\nCódigo do produto: "))
                break
            except ValueError:
                print("Entrada inválida. Digite o código do produto.")
        if cliente[index].itens[coditem-1]<1:
            volta = input("\nProduto não está no carrinho.\n\nPressione ENTER para voltar às compras.")
            return
        while True:
            try:
                quantia = int(input("\nQuantos deseja remover: "))
                break
            except ValueError:
                print("Entrada inválida. Digite um número inteiro positivo.")
        if quantia <= 0:
            volta = input("\nNenhum item removido!\n\nPressione ENTER para voltar às compras.")
            return
        elif quantia > cliente[index].itens[coditem-1]:
            volta = input("\nQuantia maior do que a atual no carrinho.\n\nPressione ENTER para voltar às compras.")
            return
        else:
            cliente[index].total-=(produtos_preco[coditem-1]*quantia)
            cliente[index].itens[coditem-1]-=quantia
            volta = input(f"\n{quantia} un. de {produtos_nome[coditem-1]} removido do carrinho!\n\nPressione ENTER para voltar às compras.")
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
        print((f"({n+1})").rjust(4), (produtos_nome[n]).center(25),f" R$ {produtos_preco[n]:.2f}")
    print("========================================")
    volta = input("\nPressione ENTER para continuar.")
    return

# Carrinho de compras do cliente
def mostrar_carrinho(index):
    print("\n****** CARRINHO ******\n")
    if not cliente[index].total == 0:   
        print(f"Carrinho de {cliente[index].nome}:")
        for codigo in range(len(produtos_nome)):
            if cliente[index].itens[codigo] > 0:
                print(f"{cliente[index].itens[codigo]} un. de {produtos_nome[codigo]}.")
        print("______________________")
        print(f"TOTAL: R$ {cliente[index].total:.2f}")
    else:
        print("Carrinho Vazio!")
    volta = input("\nPressione ENTER para continuar.")
    return

## Mostra um cliente a partir do CPF
def consulta_cliente():
    print("\n** CONSULTA CLIENTE **")
    if cliente_cpf: # somente se existir cliente cadastrado
        cpf = input("\nDigite o CPF do cliente: ")
        if validacpf(cpf):
            if cpf in cliente_cpf:
                index = cliente_cpf.index(cpf)
                menu = input(f"Nome: {cliente[index].nome}\nEmail: {cliente[index].email}\n\nPressione ENTER para continuar.")
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

## pagamento para liberar saldo
def pagamento():
    print("\n** PAGAMENTO **\n")
    index = login()
    if index != 'ERRO':
        while True:
            import time
            if cliente[index].total==0:
                menu = input("\nCarrinho vazio! Selecione alguns itens antes de gerar uma cobrança.\n\nPressione ENTER para continuar.")
                return
            print(f"\nValor total da conta: R$ {cliente[index].total:.2f}\n")
            print("FORMAS DE PAGAMENTO:\n1- À vista\n2- Transferência")
            formapagamento = input("\nComo deseja pagar: ")
            if formapagamento == "1":
                print("\nDevolvendo o troco... Aguarde.")
                time.sleep(5)
                cliente[index].itens.clear()
                cliente[index].itens+=[0]*20
                cliente[index].total=0
                menu = input("\nPagamento aceito! Você já pode retirar suas compras.\n\nPressione ENTER para continuar.")
                return
            elif formapagamento == "2":
                print("\nConfirmando recebimento da transferência... Aguarde.")
                time.sleep(7)
                cliente[index].itens.clear()
                cliente[index].itens+=[0]*20
                cliente[index].total=0
                menu = input("\nPagamento confirmado! Você já pode retirar suas compras.\n\nPressione ENTER para continuar.")
                return
            else:
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
            continue

        elif opcao == "2":
            comprar()
            continue

        elif opcao == "3":
            print("\n** MOSTRAR CARRINHO **\n")
            index = login()
            if index != 'ERRO':
                mostrar_carrinho(index)
            continue

        elif opcao == "4":
            pagamento()
            continue

        elif opcao == "5":          
            consulta_cliente()
            continue

        elif opcao == "6":         
            mostra_produtos()
            continue

        elif opcao == "0":
            print("Saindo!")
            
        #REMOVER
        elif opcao == "42":
            for i in cliente:
                print(i.nome)
                print(i.senha)
                print(i.itens)
                print(i.limite)
                print(i.total)
            
        else:
            continua = input("\nOpção inválida!\n\nPressione ENTER para continuar.")
            continue

menu()

### FIXME MENU PAGAMENTO e Aperfeiçoamentos

### WHAT'S NEW! atualizado verificaCPF;
### adicionado estrutura de classe;
### passa index ao inves de var global;
### tratamento de diversas exceções

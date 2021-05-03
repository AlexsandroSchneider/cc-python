## Inicia variáveis
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
produtos_nome = ['Pasta de dente', 'Arroz 5kg', 'Feijão 1kg', 'Açucar 1 kg', 'Refrigerante 2L', 'Energético 1L', 'asdasd', 'asdaasdsd', 'aosjpd', 'asdaseqwe2', 'poaisjhd']
produtos_preco = [5.00, 20.00, 5.00, 4.00, 6.00, 8.00, 1.00, 1.00, 1.00, 1.00, 1.00]


## Retorna ao menu após pausa
def voltamenu():
    continuar=input("\nPressione ENTER para continuar.\n")
    menu()


## Validar o CPF:
def validacpf(cpfstr):
    if len(cpfstr)!=11 or cpfstr in ('00000000000', '11111111111', '22222222222', '33333333333', '44444444444', '55555555555', '66666666666', '77777777777', '88888888888', '99999999999', '01234567890'):
        return False
    cpf=[]
    verificador=[]
    base=[9, 10]
    digit=[-2, -1] # digitos verificadores n° 10 e 11
    for i in cpfstr:
        cpf.append(int(i))
    for n in range(2): # duas verificações
        mult=base[n]+1
        soma=0
        for i in range(base[n]): # soma num acumulador a multiplicação das posições [0] até [n] do CPF
            soma += cpf[i]*mult
            mult -= 1
        resto = soma - (11*(soma//11))
        if resto < 2:
            if cpf[digit[n]] == 0:
                verificador.append(True)
            else:
                verificador.append(False)
        else:
            if cpf[digit[n]]==(11-resto):
                verificador.append(True)
            else:
                verificador.append(False)
    if verificador[0] and verificador[1]:
        return True
    return False


## Cadastra novos clientes e verifica se o cliente já existe a partir do cpf
def cadastro():
    print("\n** CADASTRO CLIENTE **")
    cpf=input("\nPressione ENTER para voltar ou\ndigite o CPF (somente números): ")
    if cpf=="":
        menu()
    elif validacpf(cpf):
        if not cpf in cliente_cpf:
            cliente_cpf.append(cpf)
            while True: # verifica entrada de nome válido (não vazio e somente a-z)
                print()
                nome = input("Digite o nome do usuário: ")
                if len(nome) == 0:
                    print("ERRO: Digite pelo menos um caractere.")
                elif not nome.replace(' ','').isalpha():
                    print("ERRO: Somente letras de a-z são permitidas.")
                else:
                    break
            cliente_username.append(nome)
            while True: # verifica entrada de senha válida (total 6 caracteres e confirma senha)
                print()
                while True:
                    criasenha  = input("Criar uma senha (6 caracteres): ")
                    if len(criasenha) != 6:
                        print("Sua senha precisa ter 6 caracteres!")
                    else:
                        break                       
                conferesenha = input("Confirmar a senha: ")
                if criasenha != conferesenha:
                    print("Senhas não são iguais.")
                else:
                    break
            cliente_senha.append(criasenha)
            cliente_email.append(input("\nDigite o email: "))
            cliente_limitecredito.append(1000.00)
            carrinho_itens.append([0]*20) # inicia itens do carrinho para o cliente
            carrinho_total.append(0)
            index=cliente_cpf.index(cpf)
            print("\nCadastro efetuado!")
            voltamenu()
        else:
            index=cliente_cpf.index(cpf)
            print("\nCliente já cadastrado com o nome:", cliente_username[index])
            voltamenu()
    else:
        volta = input("\nCPF Inválido.\n\nPressione ENTER para continuar.")
        cadastro()


## Mostra um cliente a partir do CPF
def consulta_cliente():
    print("\n** CONSULTA CLIENTE **")
    if cliente_username:
        cpf=input("\nDigite o CPF do cliente: ")
        if validacpf(cpf):
            if cpf in cliente_cpf:
                index=cliente_cpf.index(cpf)
                print(f"Nome: {cliente_username[index]}\nEmail: {cliente_email[index]}")
                voltamenu()
            else:
                opt=input("\nCliente não encontrado. Deseja cadastrar novo cliente?(s/n): ")
                if opt=="s":
                    cadastro()
                else:
                    menu()
        else:
            print("\nCPF inválido.")
            voltamenu()
    else:
        print("\nNenhum cliente cadastrado!")
        voltamenu()


## Verifica se cadastro já existe e se senha confere
def login():
    global cpf
    if cliente_cpf:
        cpf=input("Digite o CPF: ")
        if validacpf(cpf):
            if cpf in cliente_cpf:
                index=cliente_cpf.index(cpf)
                senha= input("Digite a senha: ")
                if senha==cliente_senha[index]:
                    return True
                else:
                    print("\nSenha incorreta.")
                    voltamenu()
            else:
                opt=input("\nCliente não encontrado. Deseja cadastrar novo cliente?(s/n): ")
                if opt=='s':
                    cadastro()
                else:
                    menu()
        else:
            print("\nCPF Inválido.")
            voltamenu()
    else:
        print("Nenhum cliente cadastrado!")
        voltamenu()


## Menu compras para CPF
def comprar(cpf):
    global carrinho_itens
    global carrinho_total
    opcao = '2'
    index=cliente_cpf.index(cpf)
    print()
    print("(1) Comprar itens\n(2) Remover itens\n(3) Ver o carrinho\n(4) Listar produtos\n(5) Voltar")
    buyoption=input("Opção: ")
    if buyoption == '5':
        menu()
    elif buyoption == '4':
        mostra_produtos(opcao)
    elif buyoption == '3':
        mostrar_carrinho(cpf, opcao)
    elif buyoption == '2':
        removeitens(cpf)
    elif buyoption != '1':
        volta = input("\nOpção inválida!\n\nPressione ENTER para continuar.")
        comprar(cpf)
    while True:
        try:
            coditem = int(input("\nCódigo do item: "))
            if coditem > len(produtos_nome)-1 or coditem < 0:
                print("Item inexistente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Digite o código do produto.")
    print(f"{produtos_nome[coditem]} -- R$ {produtos_preco[coditem]:.2f}")
    while True:
        try:
            quantia = int(input("\nQuantidade: "))
            if quantia > 0:
                break
            volta= input("Nenhum item adicionado!\n\nPressione ENTER para continuar.")
            comprar(cpf)
        except ValueError:
            print("Entrada inválida. Digite um número inteiro positivo.")
    if carrinho_total[index]+(produtos_preco[coditem]*quantia) > cliente_limitecredito[index]:
        print(f"\nNão foi possível adicionar este item ao seu carrinho\npois estoura seu limite de R$ {cliente_limitecredito[index]}0.")
        comprar(cpf)
    else:
        carrinho_total[index]+=(produtos_preco[coditem]*quantia)
        carrinho_itens[index][coditem]+=quantia
        volta = input(f"\n{quantia} un. de {produtos_nome[coditem]} adicionado ao carrinho!\n\nPressione ENTER para continuar.")
        comprar(cpf)


# Remover itens do carrinho
def removeitens(cpf):
    global carrinho_itens
    global carrinho_total
    index=cliente_cpf.index(cpf)
    print("\n** REMOVER ITENS **\n")
    if carrinho_total[index] > 0:
        for codigo in range(len(produtos_nome)):
            if carrinho_itens[index][codigo]>0:
                print(f"({codigo}) {produtos_nome[codigo]} -- {carrinho_itens[index][codigo]} un. ")
        while True:
            try:
                coditem = int(input("\nCódigo do produto: "))
                if carrinho_itens[index][coditem]<1:
                    volta = input("\nProduto não está no carrinho.\nPressione ENTER para continuar.")
                    comprar(cpf)
                break
            except ValueError:
                print("Entrada inválida. Digite o código do produto.")
        while True:
            try:
                quantia = int(input("\nQuantos deseja remover: "))
                if quantia > carrinho_itens[index][coditem]:
                    volta = input("\nQuantia maior do que a atual no carrinho.\n\nPressione ENTER para continuar.")
                    comprar(cpf)
                if quantia <= 0:
                    volta = input("\nNenhum item removido!\n\nPressione ENTER para continuar.")
                    comprar(cpf)
                break
            except ValueError:
                print("Entrada inválida. Digite um número inteiro positivo.")
        carrinho_total[index]-=(produtos_preco[coditem]*quantia)
        carrinho_itens[index][coditem]-=quantia
        volta = input(f"\n{quantia} un. de {produtos_nome[coditem]} removido do carrinho!\n\nPressione ENTER para voltar às compras.")
        comprar(cpf)
    else:
        volta = input("Carrinho Vazio!\n\nPressinone ENTER para voltar às compras.")
    comprar(cpf)

                
# Prateleira de produtos
def mostra_produtos(opcao):
    global cpf
    print("\n** LISTA DE PRODUTOS **\n")
    print("=============================")
    print("|(CÓDIGO) Descrição -- Preço|")
    print("=============================")
    for n in range(len(produtos_nome)):
        print(f"({n}) {produtos_nome[n]} -- R$ {produtos_preco[n]:.2f}")
    if opcao == "2":
        goback = input("\nPressione ENTER para voltar às compras.")
        comprar(cpf)
    voltamenu()
    

# Carrinho de compras do cliente
def mostrar_carrinho(cpf, opcao):
    index=cliente_cpf.index(cpf)
    print("\n****** CARRINHO ******\n")
    print(f"Carrinho de {cliente_username[index]}:")
    for codigo in range(len(produtos_nome)):
        if carrinho_itens[index][codigo]>0:
            print(f"{carrinho_itens[index][codigo]} un. de {produtos_nome[codigo]}.")
    print(f"TOTAL: R$ {carrinho_total[index]:.2f}")
    if opcao == '2':
        goback = input("\nPressione ENTER para voltar às compras.")
        comprar(cpf)
    voltamenu()


## pagamento para liberar saldo
def pagamento(cpf):
    import time
    global carrinho_itens
    global carrinho_total
    index=cliente_cpf.index(cpf)
    if carrinho_total[index]==0:
        print("\nCarrinho vazio! Selecione alguns itens antes de gerar uma cobrança.")
        voltamenu()
    print(f"\nValor total da conta: R$ {carrinho_total[index]:.2f}\n")
    print("FORMAS DE PAGAMENTO:\n1- Boleto Bancário\n2- Transferência\n3- À vista\n4- Cheque")
    formapagamento = input("\nComo deseja pagar: ")
    if formapagamento == "1":
        voltamenu()
    elif formapagamento == "2":
        voltamenu()
    elif formapagamento == "3":
        print("\nAGUARDE um momento.")
        time.sleep(5)
        carrinho_itens[index].clear()
        carrinho_itens[index]+=[0]*20
        carrinho_total[index]=0
        print("\nPagamento aceito! Você já pode retirar suas compras.")
        voltamenu()
    elif formapagamento == "4":
        voltamenu()
    else:
        print("Opção inválida.")
        pagamento(cpf)


## MENU DE OPÇÕES
def menu():
    global cpf
    print()
    opcao = "-1"
    while opcao != "0":

        print("""MENU:
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
            print("\n** MENU COMPRAS **\n")
            if login():
                comprar(cpf)

        elif opcao == "3":
            print("\n** MOSTRAR CARRINHO **\n")
            if login():
                mostrar_carrinho(cpf, opcao)

        elif opcao == "4":
            print("\n** PAGAMENTO **\n")
            if login():
                pagamento(cpf)

        elif opcao == "5":          
            consulta_cliente()

        elif opcao == "6":         
            mostra_produtos(opcao)

        elif opcao == "0":
            raise SystemExit("Saindo!")
            
        #REMOVER
        elif opcao == "42":
            print(cliente_cpf)
            print(cliente_username)
            print(cliente_email)
            print(cliente_limitecredito)
            print(cliente_senha)
            print(carrinho_itens)
            print(carrinho_total)

        else:
            print("\nOpção inválida! Tente novamente.")
            voltamenu()

menu()

### FIXME MENU PAGAMENTO e Aperfeiçoamentos
### modelo valida email https://www.devmedia.com.br/function-para-validar-email/16012
### modelo valida CPF http://www.dbins.com.br/dica/como-funciona-a-logica-da-validacao-do-cpf

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
produtos_nome = ['Pasta de dente', 'Arroz 5kg', 'Feijão 1kg', 'Açucar 1 kg', 'Refrigerante 2L', 'xsda', 'asdasd', 'asdaasdsd', 'aosjpd', 'asdaseqwe2', 'poaisjhd']
produtos_preco = [5.00, 20.00, 5.00, 4.00, 6.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00]


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
    global index
    cpf=input("\nDigite o CPF (somente números), ou * para voltar: ")
    if cpf=="*":
        menu()
    if validacpf(cpf):
        if not cpf in cliente_cpf:
            print()
            cliente_username.append(input("Digite o nome do usuário: "))
            cliente_cpf.append(cpf)
            while True:
                print()
                while True:
                    try:
                        criasenha  = input("Criar uma senha (6 caracteres): ")
                        if len(criasenha) != 6:
                            raise ValueError
                        break
                    except ValueError:
                        print("Sua senha precisa ter 6 caracteres.")
                conferesenha = input("Confirmar a senha: ")
                if criasenha != conferesenha:
                    print("Senhas não são iguais.")
                else:
                    break
            cliente_senha.append(criasenha)
            print()
            cliente_email.append(input("Digite o email: "))
            cliente_limitecredito.append(1000.00)
            carrinho_itens.append([0]*20)
            carrinho_total.append(0)
            index=cliente_cpf.index(cpf)
            print("\nCadastro efetuado!")
            voltamenu()
        else:
            index=cliente_cpf.index(cpf)
            print("\nCliente já cadastrado com o nome de:", cliente_username[index])
            voltamenu()
    else:
        print("CPF Inválido.")
        cadastro()
    
## Mostra um cliente a partir do CPF
def consulta_cliente():
    print("\n** CONSULTA CLIENTE **")
    global index
    if cliente_username:
        for i in cliente_username:
            cpf=input("\nDigite o CPF que deseja consultar: ")
            if validacpf(cpf):
                if cpf in cliente_cpf:
                    index=cliente_cpf.index(cpf)
                    print(f"Nome: {cliente_username[index]}\nEmail: {cliente_email[index]}")
                    voltamenu()
                else:
                    opt=input("\nCliente não encontrado. Deseja cadastrar novo cliente?(s/n): ")
                    if opt=='s':
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
def login(cpf, senha):
    if validacpf(cpf):
        if cpf in cliente_cpf:
            index=cliente_cpf.index(cpf)
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

## Menu compras para CPF
def comprar(cpf):
    global index
    global carrinho_itens
    global carrinho_total
    opcao = '2'
    index=cliente_cpf.index(cpf)
    print()
    print("(c) Comprar itens\n(v) Ver o carrinho\n(s) Sair: ")
    buyoption=input("Opção: ")
    if buyoption == 'v':
        mostrar_carrinho(opcao)
    elif buyoption!='c':
        menu()
    while True:
        try:
            coditem = int(input("Código do item: "))
            break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
    if coditem > len(produtos_nome)-1:
        print("\nItem inexistente.")
        comprar(cpf)
    while True:
        try:
            quantia = int(input("Quantidade: "))
            break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
    somavalor=produtos_preco[coditem]*quantia
    if carrinho_total[index]+somavalor > cliente_limitecredito[index]:
        print(f"\nNão foi possível adicionar este item ao seu carrinho.\nSeu limite é R$ {cliente_limitecredito[index]}0.")
        voltamenu()
    else:
        add=carrinho_itens[index][coditem]
        carrinho_itens[index].pop(coditem)
        carrinho_total[index]+=somavalor
        carrinho_itens[index].insert(coditem, quantia+add)
        print(f"\n{quantia} un. de {produtos_nome[coditem]} adicionado ao carrinho!")
        comprar(cpf)

# Prateleira de produtos
def mostra_produtos():
    print("\n** LISTA DE PRODUTOS **")
    print()
    for n in range(len(produtos_nome)):
        item=produtos_nome[n]
        preco=produtos_preco[n]
        print(f"({n+1}) {item} -- R$ {preco}0")
    voltamenu()

# Carrinho de compras do cliente
def mostrar_carrinho(opcao):
    print("\n****** CARRINHO ******")
    global cpf
    if not cliente_cpf:
        print("\nNenhum cliente cadastrado!")
        voltamenu()
    print()
    print(f"Carrinho de {cliente_username[index]}:")
    for codigo in range(len(produtos_nome)):
        if carrinho_itens[index][codigo]>0:
            item=produtos_nome[codigo]
            qts_carrinho=carrinho_itens[index][codigo]
            print(f"{qts_carrinho} un. de {item}.")
    print(f"TOTAL: R$ {carrinho_total[index]:.2f}")
    if opcao == '2':
        ircomprar = input("\nPressione ENTER para voltar às compras.")
        comprar(cpf)
    voltamenu()

## MENU DE OPÇÕES
def menu():
    global cpf
    print()
    opcao = "-1"
    while opcao != "0":

        print("""MENU:
1 - Cadastro
2 - Comprar
3 - Mostrar carrinho
4 - Pagar conta
5 - Consultar cliente
6 - Mostrar produtos
0 - Sair""")
        opcao = input("\nDigite o número da opção: ")

        if opcao == "1":
            cadastro()

        elif opcao == "2":
            print("\n** COMPRAR PRODUTOS **\n")
            if cliente_cpf:
                cpf=input("Digite o CPF: ")
                senha= input("Digite a senha: ")
                if login(cpf, senha):
                    comprar(cpf)
            else:
                print("Nenhum cliente cadastrado!")
                voltamenu()

        elif opcao == "3":
            mostrar_carrinho(opcao)

        elif opcao == "4":
            print("Opção selecionada: Pagar conta")
            if login(cpf, senha):
                pagamento(cpf)

        elif opcao == "5":          
            consulta_cliente()

        elif opcao == "6":         
            mostra_produtos()

        elif opcao == "0":
            raise SystemExit("Saindo!")
            
        elif opcao == "42":
            print(index)
            print(cliente_cpf)
            print(cliente_username)
            print(cliente_email)
            print(cliente_limitecredito)
            print(cliente_senha)
            print(carrinho_itens)
            print(carrinho_total)

        else:
            print("Opção inválida! Tente novamente.")
            voltamenu()

menu()


### FALTA MENU PAGAMENTO e Aperfeiçoamentos
### ADD Acesso a lista de produtos e ao carrinho pelo menu Compra
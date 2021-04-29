# retorna ao menu após pausa
def voltamenu():
    continuar=input("\nPressione ENTER para continuar.\n")
    return

# validar o CPF:
# http://www.dbins.com.br/dica/como-funciona-a-logica-da-validacao-do-cpf
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

# Inicia variaveis
# Cliente
cliente_username = []
cliente_cpf = []
cliente_senha = []
cliente_email = []
cliente_limitecredito = []

# Carrinho
carrinho_total = []
carrinho_itens = []

# Produtos
produtos_nome = ['Pasta de dente', 'Arroz 5 kg', 'Feijão 1 kg', 'Açucar 1 kg', 'Refrigerante 2L', 'xsda', 'asdasd', 'asdaasdsd', 'aosjpd', 'asdaseqwe2', 'poaisjhd']
produtos_preco = [5.00, 20.00, 5.00, 4.00, 6.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00]


# Cadastro de novos clientes
# Verificar se o cliente já existe a partir do cpf
def cadastro():
    global index
    print("Digite * para voltar ao menu principal ou")
    cpf=input("Digite o CPF(somente números): ")
    if cpf=="*":
        menu()
    if validacpf(cpf):
        if not cpf in cliente_cpf:
            cliente_username.append(input("Digite o nome do usuário: "))
            cliente_cpf.append(cpf)
            cliente_senha.append(input("Digite a senha: "))
            cliente_email.append(input("Digite o email: "))
            cliente_limitecredito.append(1000.00)
            carrinho_itens.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
            carrinho_total.append(0)
            index=cliente_cpf.index(cpf)
            voltamenu()
        else:
            for index in range(len(cliente_cpf)):
                if cliente_cpf[index]==cpf:
                    print("\nCliente já cadastrado com o nome de: ", cliente_username[index])
                    index = cliente_cpf.index(cpf)
                    voltamenu()
    else:
        print("CPF Inválido.")
        cadastro()
    

#mostra um cliente a partir do cpf
def consulta_cliente():
    global index
    if cliente_username:
        for i in cliente_username:
            #print("Qual o cpf que deseja consultar? ")
            cpf=input("Digite o CPF que deseja consultar: ")
            if validacpf(cpf):
                if cpf in cliente_cpf:
                    index=cliente_cpf.index(cpf)
                    print(f"Nome: {cliente_username[index]}\nEmail: {cliente_email[index]}")
                    voltamenu()
                    return
            else:
                print("CPF inválido.\n")
    else:
        print("\nERRO: Nenhum cliente cadastrado.")
        voltamenu()

# Verifica se cadastro já existe e se senha confere
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
            opt=input("Cliente não encontrado. Deseja cadastrar novo cliente?(s/n): ")
            if opt=='s':
                cadastro()
            else:
                menu()
    else:
        print("CPF Inválido.")
        voltamenu()

## MENU DE COMPRAS
def comprar(cpf):
    global index
    index=cliente_cpf.index(cpf)
    global carrinho_itens
    global carrinho_total
    print()
    additem=input("Deseja adicionar itens ao carrinho?(s/n): ")
    if additem!='s':
        menu()
    coditem=int(input("Código do item: "))
    if len(produtos_nome)-1 < coditem:
        print("\nItem inexistente.")
        comprar(cpf)
    quantia=int(input("Quantidade: "))
    somavalor=produtos_preco[coditem]*quantia
    if carrinho_total[index]+somavalor > cliente_limitecredito[index]:
        print("Não foi possível adicionar este item ao seu carrinho.\nLimite de R$ 1000,00 seria ultrapassado.")
        print("Deseja ver seu carrinho? (s/n): ")
        vercarrinho = input()
        if vercarrinho == 's':
            mostrar_carrinho()
        menu()
    else:
        add=carrinho_itens[index][coditem]
        carrinho_itens[index].pop(coditem)
        carrinho_total[index]+=somavalor
        carrinho_itens[index].insert(coditem, quantia+add)
        print(f"\n{quantia} un. de {produtos_nome[coditem]} adicionado ao carrinho!")
        print(carrinho_itens[index][coditem])
        comprar(cpf)

# Prateleira de produtos
def mostra_produtos():
    print()
    for n in range(len(produtos_nome)):
        item=produtos_nome[n]
        preco=produtos_preco[n]
        print(f"({n+1}) {item} -- R$ {preco}0")
    voltamenu()

# Carrinho de compras do cliente
def mostrar_carrinho():
    global index
    print(index)
    if index==None:
        cpf=input("Digite o CPF para ver o carrinho: ")
        if validacpf(cpf):
            if cpf in cliente_cpf:
                index=cliente_cpf.index(cpf)
            else:
                print("Carrinho inexistente.")
                voltamenu()
        else:
            print("CPF Inválido.")
            voltamenu()
    print()
    print(f"Carrinho de {cliente_username[index]}:")
    for codigo in range(len(produtos_nome)):
        if carrinho_itens[index][codigo]>0:
            item=produtos_nome[codigo]
            qts_carrinho=carrinho_itens[index][codigo]
            print(f"{qts_carrinho} un. de {item}.")
    print(f"Valor total: R$ {carrinho_total[index]:.2f}")
    voltamenu()

## MENU DE OPÇÕES
def menu():
    print()
    opcao = "-1"
    while opcao != "0":

        print("""Menu:
1 - Cadastro
2 - Comprar
3 - Mostrar carrinho
4 - Pagar conta
5 - Consultar cliente
6 - Mostrar produtos
0 - Sair""")
        opcao = input()

        if opcao == "1":
            print("Opção selecionada: Cadastro")
            cadastro()

        elif opcao == "2":
            print("Opção selecionada: Comprar")
            cpf=input("Digite  o CPF: ")
            senha= input("Digite  a senha: ")
            if login(cpf, senha):
                comprar(cpf)

        elif opcao == "3":
            print("Opção selecionada: Mostrar carrinho")
            mostrar_carrinho()

        elif opcao == "4":
            print("Opção selecionada: Pagar conta")
            login()

        elif opcao == "5":
            print("Opção selecionada: Consultar cliente")            
            consulta_cliente()

        elif opcao == "6":
            print("Opção selecionada: Mostrar produtos na prateleira")            
            mostra_produtos()

        elif opcao == "0":
            print("Saindo...")
            
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

index=None
menu()


## FIX SAIR DO MENU APOS USAR FUNCOES
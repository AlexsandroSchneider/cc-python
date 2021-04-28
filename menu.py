# buscar item na lista
def encontrar(elemento):
    pos_i = 0 # variável provisória de índice
    pos_j = 0 # idem

    for i in range (len(lista)): # procurar em todas as listas internas
        for j in range (i): # procurar em todos os elementos nessa lista
            if elemento in lista[i][j]: # se encontrarmos elemento ('ana')
                pos_i = i # guardamos o índice i
                pos_j = j # e o índice j
                break # saímos do loop interno
            break # e do externo
    return (pos_i, pos_j) # e retornamos os índices


# retorna ao menu após pausa
def voltamenu():
    continuar=input("\nPressione ENTER para continuar.\n")
    menu()

# validar o CPF:
# http://www.dbins.com.br/dica/como-funciona-a-logica-da-validacao-do-cpf
def validacpf(cpfstr):
    if len(cpfstr)!=11 or cpfstr in ('00000000000', '11111111111', '22222222222', '33333333333', '44444444444', '55555555555', '66666666666', '77777777777', '88888888888', '99999999999', '01234567890'):
        return False
    cpf=[]
    verificador=[]
    base=[9, 10] # multiplica digitos do CPF
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

# Cliente
cliente_username = []
cliente_cpf = []
cliente_senha = []
cliente_email = []
cliente_limitecredito = []

# Carrinho
carrinho_total = []
carrinho_itens = []
carrinho_itens_quantia = []

# Produtos
produtos_nome = ['Pasta de dente', 'Arroz 5 kg', 'Feijão 1 kg', 'Açucar 1 kg', 'Refrigerante 2L', ]
produtos_preco = [5.00, 20.00, 5.00, 4.00, 6.00, ]


# Cadastro de novos clientes
# Verificar se o cliente já existe a partir do cpf
def cadastro():
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
            carrinho_itens.append([])
            return len(cliente_cpf)-1
        else:
            for index in range(len(cliente_cpf)):
                if cliente_cpf[index]==cpf:
                    print("Cliente já cadastrado com o nome de: ", cliente_username[index])
                    index = cliente_cpf.index(cpf)
            return index
    else:
        print("CPF Inválido.")
        cadastro()
    

#mostra um cliente a partir do cpf
def consulta_cliente():
    if cliente_username:
        for i in cliente_username:
            #print("Qual o cpf que deseja consultar? ")
            cpf=input("Digite o CPF que deseja consultar: ")
            if validacpf(cpf):
                if cpf in cliente_cpf:
                    index=cliente_cpf.index(cpf)
                    print(f"Nome: {cliente_username[index]}\nEmail: {cliente_email[index]}\nLimite disponível: R${cliente_limitecredito[index]}")
                    #continuar=input("\nPressione ENTER para continuar.\n")
                    voltamenu()
                    return index
            else:
                print("CPF inválido.\n")
    else:
        print("\nERRO: Nenhum cliente cadastrado.")
        #continuar=input("\nPressione ENTER para continuar.\n")
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
            print("Cliente não encontrado. Deseja cadastrar novo cliente?")
            print("Informe 1 para menu cadastro ou * para voltar ao menu inicial.")
            opt=input()
            if opt=='1':
                cadastro()
            else:
                menu()
    else:
        print("CPF Inválido.")
        voltamenu()

## MENU DE COMPRAS
def comprar(cpf):
    index=cliente_cpf.index(cpf)
    global carrinho_itens
    print()
    for n in range(len(produtos_nome)):
        item=produtos_nome[n]
        preco=produtos_preco[n]
        print(f"({n}) {item} -- R$ {preco}0")
    print("Qual item você deseja adicionar ao carrinho?")
    adicionait=int(input())
    print("Quantidade para adicionar ao carrinho?")
    adicionaqt=int(input())
    #if adicionait in carrinho_itens[index]:
    #    indexit = carrinho_itens[index].index(adicionait)
    #    add = carrinho_itens[indexit]+adicionait
    #    carrinho_itens[index].clear(adicionait)
    #    carrinho_itens[index].append((adicionait, adicionaqt))
    #else:
    carrinho_itens[index].append((adicionait, adicionaqt))
    print("Deseja adicionar mais algum item ao carrinho?(s/n):")
    maisitem=input()
    if maisitem == "s":
        comprar(cpf)
    menu()

# Prateleira de produtos
def mostra_produtos():
    print()
    for n in range(len(produtos_nome)):
        item=produtos_nome[n]
        preco=produtos_preco[n]
        print(f"({n+1}) {item} -- R$ {preco}0")
    voltamenu()

# Carrinho de compras do cliente
def mostrar_carrinho(index):
    print(carrinho_itens[index])
    return

index=None

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
            index=cadastro()

        elif opcao == "2":
            print("Opção selecionada: Comprar")
            cpf=input("Digite  o CPF: ")
            senha= input("Digite  a senha: ")
            if login(cpf, senha):
                index=comprar(cpf)

        elif opcao == "3":
            print("Opção selecionada: Mostrar carrinho")
            index=mostrar_carrinho(index)

        elif opcao == "4":
            print("Opção selecionada: Pagar conta")
            login()

        elif opcao == "5":
            print("Opção selecionada: Consultar cliente")            
            index=consulta_cliente()

        elif opcao == "6":
            print("Opção selecionada: Mostrar produtos na prateleira")            
            mostra_produtos()

        elif opcao == "0":
            print("Saindo...")

        elif opcao == "42":
            print(cliente_cpf)
            print(cliente_username)
            print(cliente_email)
            print(cliente_limitecredito)
            print(cliente_senha)
            print(carrinho_itens)

        else:
            print("Opção inválida! Tente novamente.")

menu()
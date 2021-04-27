# Limpa tela
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear') #"cls" para windows e "clear" p/ linux.

# validar o CPF:
# http://www.dbins.com.br/dica/como-funciona-a-logica-da-validacao-do-cpf
def validacpf(cpfstr):
    if len(cpfstr)!=11 or cpfstr in ('00000000000', '11111111111', '22222222222', '33333333333', '44444444444', '55555555555', '66666666666', '77777777777', '88888888888', '99999999999', '01234567890'):
        return False
    cpf=[]
    verificador=[]
    posit=[9, 10]
    digit=[-2, -1]
    for i in cpfstr:
        cpf.append(int(i))
    for n in range(2):
        mult=posit[n]+1
        soma=0
        for i in range(posit[n]): # soma num acumulador a multiplicação das posições [0] até [n] do CPF
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
carrinho_itens = [[0,0,0,0]] # atualizar com o número de produtos, ou seja comprou 0 pasta de dentes...
#####
#carrinho_itens[0][1]=2 cliente 0  comprou 2 arroz 5 kilos
#carrinho_itens[0][3]=1 cliente 0  comprou 1 acuçar

#carrinho_itens[1][3]=1 cliente 1  comprou 1 acuçar

#carrinho_itens[X][Y]=W   cliente X  comprou W de Y


# Produtos - pode adicionar quantos produtos desejar
produtos_nome = ['Pasta de dente', 'Arroz 5 kg', 'Feijão 1 kg', 'Açucar 1 kg']
produtos_preco = [5.00, 10.00, 4.00, 2.00]
#cadastro de novos clientes
#verificar se o cliente já existe a partir do cpf
def cadastro():
    print("Digite * para voltar ao menu principal ou")
    cpf=input("Digite o CPF(somente números): ")
    if cpf=="*":
        return
    if validacpf(cpf):
        if not cpf in cliente_cpf:
            cliente_username.append(input("Digite o nome do usuário: "))
            cliente_cpf.append(cpf)
            cliente_senha.append(input("Digite a senha: "))
            cliente_email.append(input("Digite o email: "))
            cliente_limitecredito.append(1000.00)
            return len(cliente_cpf)-1
        else:
            for index in range(len(cliente_cpf)):
                if cliente_cpf[index]==cpf:
                    print("Cliente já cadastrado com o nome de: ", cliente_username[index])
                    return index
            index = cliente_cpf.index(cpf)
    else:
        print("CPF Inválido.")
        cadastro()
    

#mostra um cliente a partir do cpf
def consulta_cliente():
    for i in cliente_username:
        print("Qual o cpf que deseja consultar? ")
        cpf=input("Digite o cpf: ")
        if cpf in cliente_cpf:
            index=cliente_cpf.index(cpf)
            print(cliente_username[index])

##
def comprar(cpf, senha):
  print("implementar com o cpf e a senha", cpf, " ", senha)

  

index=None
def menu():
    cls()
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
            cpf=input("Digite  o cpf: ")  
            senha= input("Digite  a senha: ")  
            comprar(cpf,senha)

        elif opcao == "3":
            print("Opção selecionada: Mostrar carrinho")

        elif opcao == "4":
            print("Opção selecionada: Pagar conta")

        elif opcao == "5":
            print("Opção selecionada: Consultar cliente")            
            consulta_cliente()

        elif opcao == "6":
            print("Opção selecionada: Mostrar produtos na prateleira")            
            mostra_produtos()

        elif opcao == "0":
            print("Saindo...")
            
        else:
            print("Opção inválida! Tente novamente.")

menu()

# VALIDADOR DE CPF:
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


while True:
    cpf = input("Digite o CPF (somente números): ")
    if cpf == "sair":
        break
    else:
        if validacpf(cpf):
            print("CPF Válido.\n")
        else:
            print("CPF Invalido.\n")
print("FIM")
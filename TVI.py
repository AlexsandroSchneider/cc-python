import math as m

def f(x):
    if x < 0:
        return m.pow(x, 2)-(2*-m.pow(-x, 1/3))-2
    return m.pow(x, 2)-(2*m.pow(x, 1/3))-2

def intervalo(x, y):
    if (f(x)>=0 and f(y)>=0) or (f(x)<0 and f(y)<0):
        return "invalido"
    return

def menu():
    opcao = 's'
    while opcao != 'n':
        while True:
            try:
                x = float(input("Intervalo n1: "))
                y = float(input("Intervalo n2: "))
                if intervalo(x, y)=="invalido":
                    raise Exception
                break
            except ValueError:
                print("Digite dois números reais.\n")
            except Exception:
                print("Não é possível afirmar que existe solução neste intervalo, tente outros dois números.\n")
        if x > y:
            menor = y
            maior = x
        else:
            menor = x
            maior = y
        while maior - menor > 0.1:
            media = (maior+menor)/2
            if intervalo(menor, media)=="invalido":
                menor = media
            else:
                maior = media
        print(f"\nA equação tem pelo menos uma solução neste intervalo. x ∈ [{menor}, {maior}]")
        opcao = input("\nContinuar? (s/n)\n")
    print("Saindo!")
    return

menu()
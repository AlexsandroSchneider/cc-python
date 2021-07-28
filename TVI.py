import math as m

#def f_i(x):
#    return x**3+x**2+m.sin(x)-2
#
#def f_ii(x):
#    return (m.exp(x)-(3*m.cos(x))-2)

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
                if intervalo(x, y)=="invalido": #caso f(n1) e f(n2) sejam ambos >= 0 ou ambos < 0
                    raise Exception
                break
            except ValueError: #caso entrada não seja número
                print("Digite dois números reais.\n")
            except Exception:
                print("Não é possível afirmar que existe solução neste intervalo, tente outros dois números.\n")
        if x > y:
            menor = y
            maior = x
        else:
            menor = x
            maior = y
        #print(f"Intervalo: x={menor}, f({menor})= {f(menor):.4f} e x={maior}, f({maior})= {f(maior):.4f}") #Printa aproximação
        while maior - menor > 0.1: #intervalo menor que 1/10
            media = (maior+menor)/2
            if intervalo(menor, media)=="invalido":
                menor = media
            else:
                maior = media
            #print(f"Intervalo: x={menor}, f({menor})= {f(menor):.4f} e x={maior}, f({maior})= {f(maior):.4f}") #Printa aproximação
        print(f"\nA equação tem pelo menos uma solução neste intervalo. x ∈ [{menor}, {maior}]")
        opcao = input("\nContinuar? (s/n)\n")
    print("Saindo!")
    return

menu()
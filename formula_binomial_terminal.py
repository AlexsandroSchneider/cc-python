def fatorial(x):
    multiplica = 1
    fator = x
    while fator > 0:
        multiplica = multiplica*fator
        fator -= 1
    return multiplica

def binomial(n, x, p):
    nFat = fatorial(n)
    xFat = fatorial(x)
    nxFat = fatorial(n-x)
    return (nFat/(xFat*nxFat))*(p**x)*((1-p)**(n-x))

def cumulativa(n, x, p, alc):
    soma = 0
    for i in alc:
        soma += binomial(n, i, p)
    return soma
    
def menu():
    while True:
        while True:
            try:
                n = int(input("Digite o valor de n:\n"))
                break
            except:
                print("\nDigite um valor válido.")
        while True:
            x = int(input("Digite o valor de x:\n"))
            if x > n:
                print('\nPara binomial, "x" deve ser menor ou igual a "n".')
                continue
            else:
                break
        while True:
            try:
                p = float(input("Digite o valor de p (absoluto):\n"))
                break
            except:
                print('\nDigite o valor absoluto.\nUtilize "." para decimal.')
        binom = binomial(n,x,p)
        menorQue = cumulativa(n,x,p,range(x-1, -1, -1))
        menorIgualQue = cumulativa(n,x,p,range(x, -1, -1))
        maiorQue = cumulativa(n,x,p,range(x+1, n, 1))
        maiorIgualQue = cumulativa(n,x,p,range(x, n, 1))
        #print(f"\nDistribuição Binomial\nValor absoluto: {binom:.4f}\nValor relativo: {binom*100:.2f}%")
        print("Probabilidade | Absoluto | Relativo")
        print("===================================")
        print(f"  P(x = {x})    |  {binom:.4f}  |  {binom*100:.2f}%")
        print(f"  P(x < {x})    |  {menorQue:.4f}  |  {menorQue*100:.2f}%")
        print(f"  P(x ≤ {x})    |  {menorIgualQue:.4f}  |  {menorIgualQue*100:.2f}%") 
        print(f"  P(x > {x})    |  {maiorQue:.4f}  |  {maiorQue*100:.2f}%")
        print(f"  P(x ≥ {x})    |  {maiorIgualQue:.4f}  |  {maiorIgualQue*100:.2f}%")
        continuar = input("\nContinuar?(s/n)\n")
        if continuar == "n":
            print("SAINDO!")
            break
        print()
    
menu()
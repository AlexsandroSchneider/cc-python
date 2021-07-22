from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = 20
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["padx"] = 20
        self.quintoContainer.pack()

        self.sextoContainer = Frame(master)
        self.sextoContainer["padx"] = 20
        self.sextoContainer.pack()

        self.setimoContainer = Frame(master)
        self.setimoContainer["padx"] = 20
        self.setimoContainer.pack()

        self.oitavoContainer = Frame(master)
        self.oitavoContainer["padx"] = 20
        self.oitavoContainer.pack()

        self.nonoContainer = Frame(master)
        self.nonoContainer["padx"] = 20
        self.nonoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Probabilidade Binomial")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.tentativasLabel = Label(self.segundoContainer,text="n ", font=self.fontePadrao)
        self.tentativasLabel.pack(side=LEFT)

        self.tentativas = Entry(self.segundoContainer)
        self.tentativas["width"] = 10
        self.tentativas["font"] = self.fontePadrao
        self.tentativas.pack(side=LEFT)

        self.sucessosLabel = Label(self.terceiroContainer, text="x ", font=self.fontePadrao)
        self.sucessosLabel.pack(side=LEFT)

        self.sucessos = Entry(self.terceiroContainer)
        self.sucessos["width"] = 10
        self.sucessos["font"] = self.fontePadrao
        self.sucessos.pack(side=LEFT)

        self.probabilidadeLabel = Label(self.quartoContainer, text="p ", font=self.fontePadrao)
        self.probabilidadeLabel.pack(side=LEFT)

        self.probabilidade = Entry(self.quartoContainer)
        self.probabilidade["width"] = 10
        self.probabilidade["font"] = self.fontePadrao
        self.probabilidade.pack(side=LEFT)

        self.calcular = Button(self.quintoContainer)
        self.calcular["text"] = "Calcular"
        self.calcular["font"] = ("Calibri", "8")
        self.calcular["width"] = 10
        self.calcular["command"] = self.verificaBinomios
        self.calcular.pack()

        self.msg0Label = Label(self.quintoContainer,text="P(X = x): ", font=self.fontePadrao)
        self.msg0Label.pack(side=LEFT)

        self.mensagem0 = Label(self.quintoContainer, text="", font=self.fontePadrao)
        self.mensagem0.pack(side=LEFT)

        self.msg1Label = Label(self.sextoContainer,text="P(X < x): ", font=self.fontePadrao)
        self.msg1Label.pack(side=LEFT)

        self.mensagem1 = Label(self.sextoContainer, text="", font=self.fontePadrao)
        self.mensagem1.pack(side=LEFT)

        self.msg2Label = Label(self.setimoContainer,text="P(X ≤ x): ", font=self.fontePadrao)
        self.msg2Label.pack(side=LEFT)

        self.mensagem2 = Label(self.setimoContainer, text="", font=self.fontePadrao)
        self.mensagem2.pack(side=LEFT)

        self.msg3Label = Label(self.oitavoContainer,text="P(X > x): ", font=self.fontePadrao)
        self.msg3Label.pack(side=LEFT)

        self.mensagem3 = Label(self.oitavoContainer, text="", font=self.fontePadrao)
        self.mensagem3.pack(side=LEFT)

        self.msg4Label = Label(self.nonoContainer,text="P(X ≥ x): ", font=self.fontePadrao)
        self.msg4Label.pack(side=LEFT)

        self.mensagem4 = Label(self.nonoContainer, text="", font=self.fontePadrao)
        self.mensagem4.pack(side=LEFT)

    def fatorial(self, x):
        multiplica = 1
        fator = x
        while fator > 0:
            multiplica = multiplica*fator
            fator -= 1
        return multiplica

    def binomial(self, n, x, p):
        nFat = self.fatorial(n)
        xFat = self.fatorial(x)
        nxFat = self.fatorial(n-x)
        return (nFat/(xFat*nxFat))*(p**x)*((1-p)**(n-x))

    def cumulativa(self, alc):
        n = int(self.tentativas.get())
        p = float(self.probabilidade.get())
        soma = 0
        for i in alc:
            soma += self.binomial(n, i, p)
        return soma

    #Método verificar sucessos
    def verificaBinomios(self):

        self.mensagem0["text"] = (f"{self.binomial(int(self.tentativas.get()),int(self.sucessos.get()),float(self.probabilidade.get())):.4f}")
        self.mensagem1["text"] = (f"{self.cumulativa(range(int(self.sucessos.get())-1, -1, -1)):.4f}")
        self.mensagem2["text"] = (f"{self.cumulativa(range(int(self.sucessos.get()), -1, -1)):.4f}")
        self.mensagem3["text"] = (f"{self.cumulativa(range(int(self.sucessos.get())+1, int(self.tentativas.get()), 1)):.4f}")
        self.mensagem4["text"] = (f"{self.cumulativa(range(int(self.sucessos.get()), int(self.tentativas.get()), 1)):.4f}")
        

root = Tk()
Application(root)
root.mainloop()
class No:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self, cabeca=None):
        self.cabeca = cabeca

    def busca(self, k):
        noAtual = self.cabeca
        while noAtual:
            if noAtual.chave == k:
                return noAtual
            noAtual = noAtual.proximo
        return None

    def print(self):
        noAtual = self.cabeca
        while noAtual:
            print(noAtual.valor)
            noAtual = noAtual.proximo

    def insereFinal(self, novoNo):
        if self.cabeca is None:
            self.cabeca = novoNo
        else:
            noAtual = self.cabeca
            while noAtual.proximo:
                noAtual = noAtual.proximo
            noAtual.proximo = novoNo

    def insereInicio(self, novoNo):
        novoNo.proximo = self.cabeca
        self.cabeca = novoNo

    def insereOrdenada(self, novoNo):
        if self.cabeca is None or self.cabeca.chave > novoNo.chave:
            novoNo.proximo = self.cabeca
            self.cabeca = novoNo
        else:
            noAtual = self.cabeca
            while noAtual.proximo and noAtual.proximo.chave < novoNo.chave:
                noAtual = noAtual.proximo
            novoNo.proximo = noAtual.proximo
            noAtual.proximo = novoNo

e0=No(0,'Joao')
Lista=ListaEncadeada(e0)
k0=Lista.busca(0)
print(k0.valor)
Lista.print()
e1=No(1,'Maria')
Lista.insereFinal(e1)
Lista.print()
e2=No(-1,'Ana')
Lista.insereInicio(e2)
Lista.print()
e3=No(2,'Arthur')
Lista.insereOrdenada(e3)
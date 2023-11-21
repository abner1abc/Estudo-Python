def inserirnoinicio(self, novoNo):
    novoNo.proximo = self.cabeca
    self.cabeca=novoNo

def insereFinal(self,novoNo):
    noAtual = self.cabeca
    if noAtual:
        while noAtual.proximo:
            noAtual = noAtual.proximo
        noAtual.proximo = novoNo
    else:
        self.cabeca = novoNo
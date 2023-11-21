def removeLista(self, k):
    noAtual = self.cabeca
    if noAtual == None:
        return None
    if noAtual.chave == k:
        self.cabeca = noAtual.proximo
        return 0
    noAnterior = noAtual
    noAtual = noAtual.proximo
    while(noAtual != None):
        if noAtual.chave == k:
            noAnterior.proximo = noAtual.proximo
            return k
        else:
            noAnterior = noAtual
            noAtual = noAtual.proximo
    return -1
def busca(self, k):
    noAtual = self.cabeca
    if noAtual.chave == k:
        return noAtual                # chave encontrada
    while noAtual.proximo != None:
        noAtual = noAtual.proximo    # passe para o próximo nó
        if noAtual.chave == k:
            return noAtual            # chave encontrada
    return None                      # chave não encontrada
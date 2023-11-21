def removeLista(self, k):
    noAtual = self.cabeca
    if noAtual == None:          				#erro lista vazia
        return None             
    if noAtual.chave == k:        				#primeiro nó é o alvo
        self.cabeca = noAtual.proximo
        return 0
    noAnterior = noAtual					#continua a busca
    noAtual = noAtual.proximo
    while(noAtual != None):
        if noAtual.chave == k:                		#chave encontrada
            noAnterior.proximo = noAtual.proximo 	#removeu o nó
            return k
        else:
            noAnterior = noAtual			#continua a busca
            noAtual = noAtual.proximo
    return -1                          			 #erro chave não encontrada


def removeCircular(k):
    noAnterior = buscarAnterior(k)                  #busca o nó anterior ao que será removido
    if noAnterior==None:
        return None                                 #erro: nó Alvo não encontrado
    if finalLista==inicioLista:                     #lista com nó único
        lista=None                                  # remove o nó
        return 0                                    #lista agora está vazia, saída normal
    if noAnterior==finalLista:                      #remover nó inicial da lista
        finalLista.proximo=inicioLista.proximo
        inicioLista=finalLista.proximo
    elif noAnterior.proximo==finalLista:            #remover nó final da lista
        finalLista=noAnterior
        noAnterior.proximo=inicioLista
    else:                                           # remoção de um nó que não está nas pontas
        noAtual=noAnterior.proximo
        noAnterior.proximo=noAtual.proximo
    return 0                                        # saída normal
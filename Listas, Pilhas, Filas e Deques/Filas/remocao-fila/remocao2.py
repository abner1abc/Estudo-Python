def removeFila():
    global inicioFila                               #indica o acesso a variáveis globais
    global maxFila
    global finalFila
    global fila
    if inicioFila == None:                          #fila vazia
        return None                                 #erro fila vazia
    k = fila[inicioFila]                            #salva o nó removido
    if finalFila == inicioFila:
        inicioFila = None                           #fila vazia após remoção
    else:
        inicioFila = (inicioFila + 1) % maxFila     #remove o nó
    return k                                        # retorne k=o nó consumido
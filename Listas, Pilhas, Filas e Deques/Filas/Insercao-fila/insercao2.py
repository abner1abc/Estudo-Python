def insereFila(novoNo):
    global inicioFila				                 #indica o acesso a variáveis globais
    global maxFila
    global finalFila
    global fila
    if inicioFila == None:				             #fila vazia
        fila[0] = novoNo			                 #insere o nó
        inicioFila = 0				                 #atualiza o início da fila
        finalFila = 0				                 #atualiza o final da fila
    elif (finalFila + 1) % maxFila == inicioFila:	 #fila cheia
        return -1				                     # -1 indica erro de fila cheia
    else:
        finalFila = (finalFila + 1) % maxFila	   	 #atualiza o final da fila
        fila[finalFila] = novoNo                     #insere o nó 
    return finalFila				                 #saída normal

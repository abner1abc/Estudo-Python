def popBack():
    global inicioDeque			                       #indica o acesso a variáveis globais
    global maxDeque
    global finalDeque
    global deque
    if inicioDeque == None:				               #Deque vazia
        return None				                       #erro Deque vazia
    k = deque[inicioDeque]				               #salva o nó removido
    if finalDeque == inicioDeque: 
        inicioDeque = None 			                   #Deque vazia após remoção
    else:
        finalDeque = (finalDeque - 1) % maxDeque       #remove o nó
    return k			               	   	           # retorne k=o nó consumido
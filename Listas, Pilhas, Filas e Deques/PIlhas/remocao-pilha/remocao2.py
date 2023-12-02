def pop():
    global pilha
    global topoPilha
    global maxPilha
    if topoPilha == None: 			       # erro -pilha vazia
        return  None			           # None indica erro pilha vazia
    else:
        k = pilha[topoPilha]	           # salva o nó removido
        if topoPilha == 0:
            topoPilha = None	           #pilha vazia após remoção
        else:
            topoPilha = topoPilha - 1	   #remove o nó
        return k	                       #retorne k=o nó consumido

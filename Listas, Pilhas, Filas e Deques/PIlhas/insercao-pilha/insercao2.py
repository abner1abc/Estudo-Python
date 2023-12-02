def push(novoNo):
    global pilha
    global topoPilha
    global maxPilha
    if topoPilha == None:				         #pilha vazia
        pilha[0] = novoNo			             #insere o nó
        topoPilha = 0			      	         #atualiza o topo da pilha
    elif topoPilha == maxPilha - 1:		         #pilha cheia
        return -1		          		         # -1 → erro de pilha cheia
    else:
        topoPilha = topoPilha + 1			     #atualiza o topo da pilha
        pilha[topoPilha] = novoNo	  	         #insere o nó
    return  topoPilha				             #saída normal
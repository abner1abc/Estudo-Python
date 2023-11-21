def insereOrdenada (self, novoNo):
    noAtual = self.cabeca				        	   	     #inicio da busca da posição
    if noAtual.chave > novoNo.chave:
        novoNo.proximo = self.cabeca
        self.cabeca = novoNo        		  	  	  	  	     #insere no inicio
        return 0
    if noAtual.proximo != None:
        while (noAtual.chave < novoNo.chave):
            if (noAtual.proximo == None):
                noAtual.proximo = novoNo  	 #insere no final
                return 0
            noAnterior = noAtual
            noAtual = noAtual.proximo	    	  	 #continue a busca
        #fim da busca
    novoNo.proximo = noAtual				  		     	 #apontar novo nó
    noAnterior.proximo = novoNo			 	  		     #inserir novo nó

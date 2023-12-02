def popBack(self):
    if self.inicio == None:		                # erro -deque vazia
        return None			                    # None indica erro deque vazia
    else:
        k = self.final			                #salva o nó removido
        self.final = self.final.anterior	    #remove o nó
        self.final.proximo = None	            #aponta o próximo do final para λ
        return k		                 	    #retorne k=o nó consumido
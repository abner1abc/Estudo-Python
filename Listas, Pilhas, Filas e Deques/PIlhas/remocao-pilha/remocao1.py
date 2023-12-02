def pop(self):
    if self.topo==None:
        return None             	#erro pilha vazia
    k=self.topo                 	#salva o nó removido
    self.topo=self.topo.proximo 	#remove o nó
    return k                    	#retorna o nó removido
def remove(self):
    if self.inicio == None:				     # erro -fila vazia
        return None			 	             # None indica erro fila vazia
    else:
        k = self.inicio				         #salva o nó removido
        self.inicio = self.inicio.proximo  	 #remove o nó
        return k			                 #retorne k=o nó consumido

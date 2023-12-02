def insere(self, novoNo):
    if self.inicio == None:				#fila vazia
        self.inicio = novoNo			#atualiza o início da fila
        self.final = novoNo			    #atualiza o final da fila
    else:
        self.final.proximo = novoNo		#insere o nó
        self.final = novoNo			    #atualiza o final da fila

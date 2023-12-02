class No:    
    def __init__(self, chave, valor):        
        self.chave = chave
        self.valor = valor        
        self.proximo = None
        self.anterior = None

class DequeEncadeada:
    def __init__(self, inicio=None):
        self.inicio = inicio
        self.final = inicio
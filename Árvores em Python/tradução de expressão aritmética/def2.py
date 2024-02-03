def Infixo(raiz):
   if (raiz):
      Infixo(raiz.esquerda)
      print(raiz.chave)
      Infixo(raiz.direita)
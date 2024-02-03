def Posfixo(raiz):
    if (raiz):
      Posfixo(raiz.esquerda)
      Posfixo(raiz.direita)
      print(raiz.chave)
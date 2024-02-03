def Prefixa(raiz):
   if (raiz):
      print(raiz.chave)
      Prefixa(raiz.esquerda)
      Prefixa(raiz.direita)
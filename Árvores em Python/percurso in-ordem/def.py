def VisitaInOrdem(raiz):
   if (raiz):
      VisitaInOrdem(raiz.esquerda)
      print(raiz.chave)
      VisitaInOrdem(raiz.direita)
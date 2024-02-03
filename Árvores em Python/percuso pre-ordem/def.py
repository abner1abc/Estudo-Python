def VisitaPreOrdem(raiz):
   if (raiz):
      print(raiz.chave)
      VisitaPreOrdem(raiz.esquerda)
      VisitaPreOrdem(raiz.direita)
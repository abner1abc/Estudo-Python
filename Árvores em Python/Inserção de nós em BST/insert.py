class NoArvore:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None

def ImprimeArvore(raiz):
    if raiz:
        ImprimeArvore(raiz.esquerda)
        print(raiz.chave),
        ImprimeArvore(raiz.direita)

def InserirBST(raiz, chave):
   if raiz is None:
      return NoArvore(chave)
   else:
      if raiz.chave == chave:
         return raiz
      elif raiz.chave < chave:
         raiz.direita = InserirBST(raiz.direita, chave)
      else:
         raiz.esquerda = InserirBST(raiz.esquerda, chave)
   return raiz

if __name__ == '__main__':
      raiz = NoArvore(55)
      InserirBST(raiz, 35)
      InserirBST(raiz, 75)
      InserirBST(raiz, 25)
      InserirBST(raiz, 45)
      InserirBST(raiz, 65)
      InserirBST(raiz, 85)
      ImprimeArvore(raiz)
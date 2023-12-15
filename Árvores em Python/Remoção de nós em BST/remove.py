def ValorNo(no):
    atual = no
    while(atual.esquerda is not None):
        atual = atual.esquerda
    return atual

def DeleteBST(raiz, chave):
    if raiz is None: 
        return raiz
    if chave < raiz.chave:
        raiz.esquerda = DeleteBST(raiz.esquerda, chave)
    elif(chave > raiz.chave):
        raiz.direita = DeleteBST(raiz.direita, chave)
    else:
        if raiz.esquerda is None:
            temp = raiz.direita
            raiz = None
            return temp
        elif raiz.direita is None:
            temp = raiz.esquerda
            raiz = None
            return temp
        temp = ValorNo(raiz.direita)
        raiz.chave = temp.chave
        raiz.direita = DeleteBST(raiz.direita, temp.chave)
    return raiz

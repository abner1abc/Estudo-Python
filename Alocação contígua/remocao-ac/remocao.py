nomes =['Joao', 'Maria', 'Ana', 'Arthur']
nomes.remove('Arthur')
print(nomes)
nomes.pop(2)
print(nomes)

def removeL (k,L,n):
    i=0                          #início da busca do nó
    posRemocao=-1
    while (i<n):
        if L[i] == k:
            posRemocao=i   #chave encontrada
            i=n+1          #sair do laço
        else:
            i=i+1          #continuar busca
    if i==n:
        return -1              #erro, chave não existe
    #final da busca do nó
    i=posRemocao                #início do ajuste da lista
    while (i<n-1):
        L[i]=L[i+1]   #puxa cada nó posterior 1 posição
        i=i+1
    L.pop(n-1)                  #ajusta o tamanho da lista
    return posRemocao           #saída normal da função

nomes =['Joao', 'Maria', 'Ana', 'Arthur']
i=removeL('Arthur', nomes, len(nomes))
print(nomes)
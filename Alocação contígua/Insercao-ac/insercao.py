nomes=['Joao','Maria','Ana']
nomes.append('Arthur')       #insere um novo nó contenho Arthur
print(nomes)

def insereL (k, L, n):
       L.append('')     #aumenta um índice na lista
       L [n]=k          #índices na lista iniciam em 0
       n += 1             #incrementar o número de nós n

def insereOrdenada (k,L,n):             
    i=0                                  #início da busca da posição
    posInsercao=-1
    while (i<n):
        if L[i]>= k:
            if L[i] == k:
                return -1       #erro, chave já existe
            else:
                posInsercao =i    #posição achada
                i=n+1             #sair do laço
        else: 
            i=i+1                #continuar busca
    if i==n: 
        posInsercao=n        #inserção no final da lista
    #final da busca de posição
    L.append('')                           #aumenta um índice na lista
    i=n                                    #inicio do ajuste da lista
    while (i>posInsercao):
        L[i]=L[i-1]                 #empurra cada nó para o final
        i=i-1
    L[posInsercao]=k                       #insere novo nó
    return posInsercao                     #saída normal da função

numeros=[1,2,3,4,6,7,8,9,10]
insereL(12,numeros,len(numeros))
print(numeros)
insereOrdenada(5,numeros,len(numeros))
print(numeros)
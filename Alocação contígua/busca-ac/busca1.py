nomes=['Joao','Maria','Ana']
i=nomes.index('Joao')         #busca o índice do nó com a chave Joao
print(i)

def buscaLista(k, L, n):
        i=0
        índiceL=-1
        while i<n:
                if L[i]==k:           #nó encontrado
                         indiceL=i    #salva o índice
                         i=n+1        #sair do laço
                i=i+1                 #segue a procura
        return indiceL

nomes =['Arthur', 'Joao', 'Maria', 'Ana']
i = buscaLista ('Ana', nomes, len(nomes))
print (i)


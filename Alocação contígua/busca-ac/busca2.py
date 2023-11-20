def buscaOrdenada(k, L, n):
    i=0
    indiceL=-1
    while (i<n):
        if L[i]>= k:
            if L[i] == k:
                indiceL=i 		#chave encontrada
                i=n+1		    #sair do laço
            else:
                i=n+1	    	#chave>k, sair do laço
        else:
            i=i+1			            #continuar busca
    return indiceL		                  		    #-1 indica chave não achada

numeros=[1,2,3,4,5,6,7,8,9,10]
i=buscaOrdenada(5,numeros,len(numeros))
print (i)
i=buscaOrdenada(3,numeros,len(numeros))
print(i)
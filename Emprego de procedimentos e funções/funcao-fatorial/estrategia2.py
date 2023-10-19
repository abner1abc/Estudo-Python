numero = 5

def fatorial_recursivo(n):
    if((n==0) or (n==1)):
        return 1
    return n*fatorial_recursivo(n-1)

print(f'O fatorial de {numero} é: {fatorial_recursivo(numero)}')
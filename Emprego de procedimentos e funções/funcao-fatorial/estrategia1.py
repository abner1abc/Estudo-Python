numero = 5

def fatorial_iterativo(n):
    f=1

    for i in range(1,n+1):
        f=f*i
    return f

print(f'O fatorial de {numero} é : {fatorial_iterativo(numero)}')
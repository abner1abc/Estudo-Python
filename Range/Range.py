# sintaxe básica da função
# range(inicio, fim, passo)

# Iterar de 0 a 4 (0, 1, 2, 3):
for i in range(4):
    print(i)

# Iterar de 2 a 9 (2, 3, 4, 5, 6, 7, 8):
for i in range(2, 9):
    print(i)

# Iterar de 1 a 10 com passo de 2 (1, 3, 5, 7, 9):
for i in range(1, 10, 2):
    print(i)

# Criar uma lista de números de 0 a 9:
lista_de_numeros = list(range(10))
print(lista_de_numeros)
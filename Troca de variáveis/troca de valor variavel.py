a = 1
b = 2
# troca de variáveis usando variável auxiliar ‘temp’
temp = a
a = b
b = temp
print(f"O valor da variável a é: {a}")
print(f"O valor da variável b é: {b}")

# troca de variáveis através de atribuição múltipla
a, b = b, a
print(f"O valor da variável a é: {a}")
print(f"O valor da variável b é: {b}")
import sqlite3 as conector

conexao = None
cursor = None
try:
    conexao = conector.connect("meu_banco.db")

except conector.DatabaseError as erro:
    print("Erro de Banco de Dados", erro)

finally:
    #fechamento das conexões e cursores
    if cursor:
        cursor.close()
    if conexao:
        conexao.close()
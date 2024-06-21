import sqlite3 as conector

# Abertura de conexão
conexao = conector.connect("caminho/para/seu/banco_de_dados.db")

# Aquisição de um cursor
cursor = conexao.cursor()

# Execução de comandos: exemplo SELECT
cursor.execute("SELECT * FROM sua_tabela")

# Recuperação dos resultados
resultados = cursor.fetchall()
for linha in resultados:
    print(linha)

# Efetivação do comando (não necessário para SELECT, mas sim para INSERT, UPDATE, DELETE, etc.)
# conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()
import sqlite3 as conector

# Abertura de conexão
conexao = conector.connect("caminho/para/seu/banco_de_dados.db")

# Aquisição de um cursor
cursor = conexao.cursor()

# Criação de uma tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS sua_tabela (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INTEGER
)
""")

# Inserção de dados
cursor.execute("INSERT INTO sua_tabela (nome, idade) VALUES ('Alice', 30)")
cursor.execute("INSERT INTO sua_tabela (nome, idade) VALUES ('Bob', 25)")

# Efetivação dos comandos de inserção
conexao.commit()

# Execução de um comando SELECT
cursor.execute("SELECT * FROM sua_tabela")

# Recuperação dos resultados
resultados = cursor.fetchall()
for linha in resultados:
    print(linha)

# Fechamento das conexões
cursor.close()
conexao.close()
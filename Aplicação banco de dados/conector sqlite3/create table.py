# Criar tabela
import sqlite3
# Abrir muma conexão com o banco de dados
conn = sqlite3.connect('exemplo.db')
# Criar um cursor para executar comando SQL
cursor = conn.cursor()
# Criar uma tabela 
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        idade INTEGER
    )
''')

# Inserir registros
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)",
    ('Alice', 30))

cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?,?)",
    ('Bob', 25))
conn.commit()
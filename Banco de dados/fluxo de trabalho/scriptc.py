import psycopg2 as conector

# Abertura de conexão
conexao = conector.connect("URL PostgreSQL")

# Aquisição de um cursor
cursor = conexao.cursor()

# Execução comandos : SELECT..CREATE...
cursor.execute("...")
cursor.fetchall()

# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()
import psycopg2 as conector

# Abertura de conexão
conexao = conector.connect(
    dbname="nome_do_banco",
    user="seu_usuario",
    password="sua_senha",
    host="localhost",  # ou o endereço do servidor PostgreSQL
    port="5432"  # porta padrão do PostgreSQL
)

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
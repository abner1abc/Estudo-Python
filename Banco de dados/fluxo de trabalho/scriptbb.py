import mysql.connector as conector

# Abertura de conexão
conexao = conector.connect(
    host="URL MySQL",  # Endereço do servidor MySQL
    user="seu_usuario",  # Usuário do banco de dados
    password="sua_senha",  # Senha do banco de dados
    database="nome_do_banco"  # Nome do banco de dados
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
import sqlite3

conexao = sqlite3.connect('reprovados.db') # Conectar ao banco de dados (será criado se não existir)
cursor = conexao.cursor() # Criar um cursor para executar comandos SQL ( O cursor percore o banco como ponteiro)

# Criar a tabela "reprovados" (se ela não existir) e 
cursor.execute('''CREATE TABLE IF NOT EXISTS reprovados 
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, curso TEXT, alunos TEXT)''')

curso = 'ads' # Inserir valores na tabela
alunos = 'todos'
cursor.execute("INSERT INTO reprovados (curso, alunos) VALUES (?, ?)", (curso, alunos))

conexao.commit() # Salvar as mudanças e
conexao.close() #  fechar a conexão

conexao = sqlite3.connect('reprovados.db') # Conectar novamente para fazer uma consulta
cursor = conexao.cursor()

cursor.execute("SELECT * FROM reprovados") # Consulta para verificar os dados inseridos
dados = cursor.fetchall()

for dado in dados: # Imprimir os dados
    print(f"ID: {dado[0]}, Curso: {dado[1]}, Alunos: {dado[2]}")

conexao.close() # Fechar a conexão

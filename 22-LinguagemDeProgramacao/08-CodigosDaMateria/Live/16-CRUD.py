import sqlite3
import os as os 

def criar_registro(conexao, curso, alunos):  # Função para criar registro no banco de dados
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO reprovados (curso, alunos) VALUES (?, ?)", (curso, alunos))
    conexao.commit()
    print("Registro criado com sucesso!")

def listar_registros(conexao): # Função para ler os registros no banco de dados
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM reprovados")
    dados = cursor.fetchall()
    for dado in dados:
        print(f"ID: {dado[0]}, Curso: {dado[1]}, Alunos: {dado[2]}")

def atualizar_registro(conexao, id, novo_curso, novos_alunos): # Função para atualizar o registro no bando de dados
    cursor = conexao.cursor()
    cursor.execute("UPDATE reprovados SET curso = ?, alunos = ? WHERE id = ?", (novo_curso, novos_alunos, id))
    conexao.commit()
    print("Registro atualizado com sucesso!")

def deletar_registro(conexao, id): # Função para deletar registro no bando de dados
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM reprovados WHERE id = ?", (id,))
    conexao.commit()
    print("Registro deletado com sucesso!")

conexao = sqlite3.connect('reprovados.db')

os.system("cls")
while True:
    print("\nOperações CRUD: (1)Create, (2)Read, (3)Update, (4)Delete")
    print("1. C - Criar registro")
    print("2. R - Listar registros")
    print("3. U - Atualizar registro")
    print("4. D - Deletar registro")
    print("5. Sair")
    
    escolha = input("Escolha uma operação: ")

    if escolha == '1':
        curso = input("Digite o curso: ")
        alunos = input("Digite os alunos: ")
        os.system("cls")
        criar_registro(conexao, curso, alunos)
    elif escolha == '2':
        os.system("cls")
        listar_registros(conexao)
    elif escolha == '3':
        id = input("Digite o ID do registro que deseja atualizar: ")
        novo_curso = input("Digite o novo curso: ")
        novos_alunos = input("Digite os novos alunos: ")
        os.system("cls")
        atualizar_registro(conexao, id, novo_curso, novos_alunos)
    elif escolha == '4':
        os.system("cls")
        listar_registros(conexao)
        print('')
        id = input("Digite o ID do registro que deseja deletar: ")
        os.system("cls")
        deletar_registro(conexao, id)
    elif escolha == '5':
        break
    else:
        print("Escolha inválida. Tente novamente.")

conexao.close()

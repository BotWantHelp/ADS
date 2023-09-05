import pandas as pd
import os
import matplotlib.pyplot as plt

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
clear_terminal()
              
banco_aluno = {}
numero_de_alunos = int(input("Insira o número de alunos: "))

for i in range(numero_de_alunos):
    nome_aluno = str(input("Digite o nome do aluno: "))
    nota_aluno = float(input("Digite aqui o valor da nota do aluno: "))
    banco_aluno[nome_aluno] = nota_aluno
    
opcao = 0

def selecione_resultado():
    if opcao == 1:
        print("Opção 1 - selecionada:")
        consulta_nome_aluno = str(input("Digite o nome do aluno para consultar: "))
        if consulta_nome_aluno in banco_aluno:
            print(f"Nome do aluno: {consulta_nome_aluno}. Nota: {banco_aluno[consulta_nome_aluno]}")
            nota = banco_aluno[consulta_nome_aluno]
            if nota >= 7.0:
                print("Aluno aprovado!\n")
            elif nota >= 5.0:
                print("Aluno em Recuperação!\n")
            else:
                print("Aluno Reprovado\n")
        else:
            print("Nome não encontrado. Por favor, digite o nome novamente\n")
    elif opcao == 2:
        print("Opção 2 - selecionada:")
        df = pd.DataFrame(list(banco_aluno.items()), columns=['Aluno', 'Nota'])
        print(df)
    elif opcao == 3:
        print("Opção 3 - selecionada:")
        media_notas = sum(banco_aluno.values()) / len(banco_aluno)
        plt.bar(banco_aluno.keys(), banco_aluno.values(), color='blue')
        plt.axhline(y=media_notas, color='red', linestyle='--', label='Média')
        plt.xlabel('Alunos')
        plt.ylabel('Notas')
        plt.title('Médias de Notas dos Alunos')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        print("\n")
    else:
        print("Escolha inválida.\n")


while True:

    opcao = int(input("Selecione uma opção: \n1 - Para consultar nome de aluno. \n2 - para mostrar no terminal. \n3 - para plotar o gráfico:\n4 - Sair\n "))
    clear_terminal()
    if(opcao == 4):
        print("Você saiu do programa")
        break
    else:
        selecione_resultado()
import numpy as np  # precisa instalar no console - pip install numpy

notas_alunos = np.array([     # Criando uma matriz de notas de alunos (3 alunos e 4 disciplinas)
    
    
  #  Nota1, Nota2, Nota3
     [5,    2,      7],  #Aluno 1 (nas disciplinas 1, 2, 3)
     [0,    8,      7],  #Aluno 2 (nas disciplinas 1, 2, 3)
     [7,    5,      8]   #Aluno 3 (nas disciplinas 1, 2, 3)
])

nota_aluno_2_disciplina_3 = notas_alunos[1][2]  #  Acessando Nota do Aluno 2 na Disciplina 3
print(f"Nota do aluno 2 na disciplina 3: {nota_aluno_2_disciplina_3}\b")

print("Matriz de Notas dos Alunos:") # Print da matriz de notas dos alunos
print(notas_alunos)

print("\nNotas dos Alunos:")
for i, notas in enumerate(notas_alunos, start=1): # Print das notas dos alunos usando um loop
    print(f"Aluno {i}: {notas}")

media_por_disciplina = np.mean(notas_alunos, axis=0)  # Operações Média das notas por disciplina
print("\nMédia por Disciplina:", media_por_disciplina)

media_por_aluno = np.mean(notas_alunos, axis=1)       # Operações Média das notas por aluno
print("Média por Aluno:", media_por_aluno)


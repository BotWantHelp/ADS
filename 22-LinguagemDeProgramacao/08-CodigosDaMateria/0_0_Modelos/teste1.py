# import pandas as pd

# dataFrame = {
#     'Aprovado': [1, 1, 1, 1, 0],
#     'Classe': [3, 1, 3, 1, 3],
#     'Nome': ['Matheus',
#              'Naty',
#              'Gabi',
#              'Andressa',
#              'Vini'],
#     'Sexo': ['Homem', 'Mulher', 'Mulher', 'Mulher', 'Nao-Binario'],
#     'Idade': [24, 22, 21, 26, 39],
#     'Irmaos': [1, 1, 0, 1, 0],
#     'Filhos': [0, 0, 0, 0, 0],
#     'Gastou': [7.250, 71.283, 7.920, 53.100, 8.500]
# }
# df_titanic = pd.DataFrame(dataFrame)
# print(df_titanic)

import pandas

#Posição-X 0    1    2    Posição-Y
matriz= [['1', '2', '3'],# 0
         ['4', '5', '6'],# 1
         ['7', '8', '9'],# 2
         ['0', ' ', ' ']]# 3

df_matriz = pandas.DataFrame(matriz)
print(df_matriz[2][1])  # imprime o valor encontrado na orientação X / Y
print(df_matriz[2][2])  # imprime o valor encontrado na orientação X / Y

import pandas as pd
# DataFrames da biblioteca pandas possuem uma propriedade chamada loc. 
# Essa propriedade permite acessar um conjunto de linhas (filtrar linhas), 
# por meio do índice ou por um vetor booleano (vetor de True ou False).

dataFrame = {
    'Survived': [0, 1, 1, 1, 0],
    'Pclass': [3, 1, 3, 1, 3],
    'Name': ['Mr. Owen Harris Braund',
             'Mrs. John Bradley (Florence Briggs Thayer Cumings)',
             'Miss. Laina Heikkinen',
             'Mrs Jacques Heath (Lily May Peel) Futrelle',
             'Mr. William Henry Allen'],
    'Sex': ['male', 'female', 'female', 'female', 'male'],
    'Age': [22.0, 38.0, 26.0, 35.0, 35.0],
    'Siblings/Spouses Aboard': [1, 1, 0, 1, 0],
    'Parents/Children Aboard': [0, 0, 0, 0, 0],
    'Fare': [7.2500, 71.2833, 7.9250, 53.1000, 8.0500]
}
df_titanic = pd.DataFrame(dataFrame)

'''Filtrar somente os homens que estavam a bordo e guardar dentro de um novo DataFrame.'''
filtro_homem = df_titanic['Sex'] == 'male'
df_titanic_homens = df_titanic.loc[filtro_homem]
print(df_titanic_homens)

'''Ou ainda, criar um novo DataFrame somente com os passageiros que sobreviveram:'''
filtro_sobreviventes = df_titanic['Survived'] == 1
df_titanic_sobreviventes = df_titanic[filtro_sobreviventes]   
print(df_titanic_sobreviventes)
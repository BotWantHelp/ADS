import pandas as pd
# Filtros com operadores relacionais e lógicos É possível criar filtros usando operadores 
# relacionais e lógicos para criar condições compostas. Cada condição deve estar entre parênteses 
# e deve ser conectada pelos operadores lógicos AND (&), OR (|).

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

'''Por exemplo, criar um novo DataFrame contendo todos os homens que sobreviveram.'''
filtro_sobreviventes = df_titanic['Survived'] == 1
filtro_homem = df_titanic['Sex'] == 'male'

df_titanic_homens_sobreviventes = df_titanic.loc[(filtro_sobreviventes) & (filtro_homem)] 
print(df_titanic_homens_sobreviventes) # O Print nao ira funcionar pois nao houve homens sobreviventes

'''Ou um novo DataFrame com todos os passageiros do sexo feminino que estavam na primeira 
   ou segunda classe. Nesse caso, é preciso utilizar um parênteses extra para garantir a ordem 
   de execução: primeiro faz o OU entre pessoas que estavam na primeira e segunda classe e depois 
   faz o E com pessoas do sexo feminino.'''
filtro_mulher = df_titanic['Sex'] == 'female'
filtro_classe1 = df_titanic['Pclass'] == 1
filtro_classe2 = df_titanic['Pclass'] == 3

df_titanic_mulheres_c1_c2 = df_titanic.loc[(filtro_mulher) & ((filtro_classe1) | (filtro_classe2))] 
print(df_titanic_mulheres_c1_c2)


''' Algumas das maneiras mais comuns de usar o loc[] são:

♥ Selecionar todas as linhas para colunas específicas: dataframe.loc[:, colunas]
♥ Selecionar linhas específicas para todas as colunas: dataframe.loc[linhas, :]
♥ Selecionar linhas e colunas específicas: dataframe.loc[linhas, colunas]
A
lém disso, você também pode usar filtros booleanos, como você fez no seu código, 
para criar condições mais complexas para selecionar as informações desejadas.

No seu código, você estava usando df_titanic.loc[(filtro_sobreviventes) & (filtro_homem)] 
para selecionar as linhas onde tanto o filtro de sobreviventes quanto o filtro de homens eram verdadeiros.

Portanto, o pandas.DataFrame.loc[] é uma ferramenta poderosa para seleção e filtragem de 
dados em um DataFrame do Pandas.'''
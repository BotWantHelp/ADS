# vamos utilizar um dos datasets (conjunto de dados) clássicos para quem inicia o estudo 
# na área de ciência de dados, o Titanic. ele possui 8 colunas.
import pandas as pd
import seaborn as sns

dataFrame = {
    'Survived':                [0, 1, 1, 1, 0],
    'Pclass':                  [3, 1, 3, 1, 3],
    'Name':                    ['Mr. Owen Harris Braund',
                                'Mrs. John Bradley (Florence Briggs Thayer Cumings)',
                                'Miss. Laina Heikkinen',
                                'Mrs Jacques Heath (Lily May Peel) Futrelle',
                                'Mr. William Henry Allen'],
    'Sex':                     ['male', 'female', 'female', 'female', 'male'],
    'Age':                     [22.0, 38.0, 26.0, 35.0, 35.0],
    'Siblings/Spouses Aboard': [1, 1, 0, 1, 0],
    'Parents/Children Aboard': [0, 0, 0, 0, 0],
    'Fare':                    [7.2500, 71.2833, 7.9250, 53.1000, 8.0500],
    'Birth Date':              ['1980-05-10', '1985-12-20', '1997-04-03', '1987-09-15', '1988-02-28']
}

df_titanic = pd.DataFrame(dataFrame)                                 # Converte-se em datetime para nao exibir como objeto
df_titanic['Birth Date'] = pd.to_datetime(df_titanic['Birth Date'])  # Linha convertendo a coluna para datetime64[ns]

print(df_titanic)

'''Para selecionar uma coluna usa-se a sintaxe: meu_df['coluna']'''
print(df_titanic['Age'])
print(df_titanic['Survived']) 

'''Para selecionar mais de uma coluna é preciso passar uma lista de 
   colunas: meu_df[['coluna1', 'coluna2', 'coluna3']]'''
print(df_titanic[['Age', 'Fare']])
print(df_titanic[['Name', 'Pclass', 'Fare']])

filtro_homem = df_titanic['Sex'] == 'male'
df_titanic_homens = df_titanic.loc[filtro_homem]
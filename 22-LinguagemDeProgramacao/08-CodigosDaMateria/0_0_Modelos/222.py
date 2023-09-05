import pandas as pd

dados = {
    'nomes': ['Howard', 'Ian', 'Peter', 'Jonah', 'Kellie'],
    'cpfs': ['111.111.111-11', '222.222.222-22', '333.333.333-33', '444.444.444-44', '555.555.555-55'],
    'emails': ['risus.varius@dictumPhasellusin.ca', 'Nunc@vulputate.ca', 'fames.ac.turpis@cursusa.org', 'non@felisullamcorper.org', 'eget.dictum.placerat@necluctus.co.uk'],
    'idades': [32, 22, 25, 29, 38]
}

df_dados = pd.DataFrame(dados)

print('\nInformações do DataFrame:\n')
print(df_dados.info()) # Apresenta informações sobre a estrutura do DF

print('\nQuantidade de linhas e colunas = ', df_dados.shape) # Retorna uma tupla com o número de linhas e colunas
print('\nTipo de dados:\n', df_dados.dtypes) # Retorna o tipo de dados, para cada coluna, se for misto será object

print('\nQual o menor valor de cada coluna?\n', df_dados.min()) # Extrai o menor de cada coluna 
print('\nQual o maior valor?\n', df_dados.max()) # Extrai o valor máximo e cada coluna 
print('\nQual a média aritmética?\n', df_dados.mean()) # Extrai a média aritmética de cada coluna numérica
print('\nQual o desvio padrão?\n', df_dados.std()) # Extrai o desvio padrão de cada coluna numérica
print('\nQual a mediana?\n', df_dados.median()) # Extrai a mediana de cada coluna numérica

print('\nResumo:\n', df_dados.describe()) # Exibe um resumo

df_dados.head() # Exibe os 5 primeiros registros do DataFrame

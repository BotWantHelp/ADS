import pandas as pd 
''' A biblioteca pandas é uma das bibliotecas mais populares em Python para análise e manipulação de dados. 
Ela oferece estruturas de dados e funções eficientes para trabalhar com dados em tabelas, séries temporais 
e outras estruturas semelhantes a planilhas. O pandas é amplamente utilizado em tarefas como limpeza de dados, 
análise exploratória, processamento de dados, transformação e visualização.
As duas principais estruturas de dados fornecidas pelo pandas são: '''
# DataFrame: É uma estrutura bidimensional semelhante a uma tabela, onde cada coluna pode conter 
# diferentes tipos de dados. Um DataFrame é especialmente útil para representar dados tabulares 
# e é comparável a uma planilha do Excel ou a uma tabela de um banco de dados.

# Series: É uma estrutura unidimensional que representa uma única coluna de dados. 
# Uma Series pode ser vista como uma lista indexada.
#----------------------------------------------------------------------------------------------------
data = {'Nome': ['Pedro', 'Naty', 'Tiago'],# Exemplo de DataFrame
        'Idade': [25, 30, 22]}

df = pd.DataFrame(data)
print("DataFrame:\n",(df))

coluna_nome = df['Nome']# Acessando uma coluna inteira
print(coluna_nome)

valor_idade = df.at[1, 'Idade']# Acessando um valor específico
print(valor_idade)

linha_0 = df.iloc[0]# Acessando uma linha inteira
print(linha_0)

valor_nome_2 = df.iloc[2, 0]# Acessando um valor específico usando índices numéricos
print(valor_nome_2)

valor_nome_Pedro = df.loc[0, 'Nome']# Acessando um valor específico por rótulos de índice
print(valor_nome_Pedro)

novo_nome = 'Ezequiel'# Substituindo o nome "Pedro" por "Ezequiel"
df.loc[df['Nome'] == 'Pedro', 'Nome'] = novo_nome
print("DataFrame:\n",(df))

#-----------------------------------------------------
# Tipos de dados que podem ser extraidos de uma series
print("\nModelos para extrair dados se Series\n")
series_dados = pd.Series([10.2, -1, None, 15, 23.4])
print("Quantidade de linhas = ", series_dados.shape)    # Retorna uma tupla com o numero de linhas
print("Tipo de dados = ", series_dados.dtype)           # Retorna o tipo de dados, se for misto será object
print("Os valores sao unicos? ", series_dados.is_unique)# Verifica se nao tem duplicidade
print("Existem valores nulos?", series_dados.hasnans)   # Verifica se há valores nulos
print("Quantos valores existem?", series_dados.count()) # Conta a quantidade de valores
#-----------------------------------------------------
# Tratando funções matematicas e estatisticas
print("Qual o menor valor? ", series_dados.min())       # Extrai o menor valos
print("Qual o maior valor? ", series_dados.max())       # Extrai o maior valor
print("Qual a média dos valores? ", series_dados.mean())# Extrai a média
print("Qual o desvio padrao? ", series_dados.std())     # Extrai o desvio padrao
print("Qual a mediana? ", series_dados.median())        # Extrai a mediana
print("\nResumo\n", series_dados.describe())            # Exibe o resumo sobre os dados

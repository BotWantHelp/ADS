import pandas as pd

# Criar um DataFrame de exemplo para ser salvo em CSV
data = {'Nome': ['Vini', 'Rapha', 'Vitor', 'Tiago'],
        'Idade': [25, 30, 22, 28],
        'Cidade': ['São Paulo', 'Nova Iorque', 'Londres', 'Toronto']}

df = pd.DataFrame(data)

# Especifique o caminho do arquivo onde você deseja salvar os dados
caminho_arquivo = 'dados.csv'

# Salvar o DataFrame em um arquivo CSV no caminho especificado
df.to_csv(caminho_arquivo, index=False)  # index=False para não salvar o índice do DataFrame

# Criar uma variavel para exibir o DataFrame
caminho_arquivo = 'dados.csv'     # armazenando nome do arquivo na variavel
df = pd.read_csv(caminho_arquivo) # utilizando a variavel como PATH

# Exibir o DataFrame no console
print(df)
import pandas as pd
from datetime import date

lista_nomes = "Ana Bia Matheus Lia Paula".split()

dfs = pd.DataFrame(lista_nomes, columns=['nome'])
print(dfs)
print("\n" * 3)

data_extração = date.today()
dfs['data_extração'] = data_extração
dfs['data_extração'] = dfs['data_extração'].astype('datetime64[ns]')
dfs.sort_values(by='data_extração', ascending=False, inplace=True)

print(dfs.head())
print("\n")
print("@" * 30)
print("\n")

linhas = [{'nome': 'TESTE', 'idade': 25}]
dfs1 = pd.DataFrame(linhas)
dfs1['nome'] = dfs1['nome'].astype(str)
dfs = pd.concat([dfs, dfs1], ignore_index=True)

print(dfs.loc[(dfs['idade'] < 30)])
print(dfs)

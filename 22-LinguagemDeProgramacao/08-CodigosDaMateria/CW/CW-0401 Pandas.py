import pandas as pd # pandas é um pacote Python que fornece estruturas de dados projetadas para facilitar 
                    # o trabalho com dados estruturados (tabelas) e de séries temporais.       
                
'''Séries''' # Uma Series é um como um vetor de dados (unidimensional), 
# capaz de armazenar diferentes tipos de dados.
# -- Uma Series possui somente "uma coluna" de informação e seus rótulos (índices). 
# o método Series() do pacote pandas. O método possui o seguinte construtor:
serie = pd.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)
serie = pd.Series(data=5) # Cria uma Series com o valor a
serie = pd.Series('Howard Ian Peter Jonah Kellie'.split()) # Cria uma Series com uma lista de nomes
print(serie)

'''DataFrame''' # Um DataFrame é um conjunto de Series, ou, como a 
# documentação apresenta, um contêiner para Series.
# -- DataFrame pode ter uma ou mais colunas e, além dos índices, também há um rótulo
# de identificação com o nome da coluna. 
# O método DataFrame() do pacote pandas. O método possui o seguinte construtor: 
dataframe = pd.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
# Cria um DataFrame, de uma coluna a partir de uma lista
dataframe = pd.DataFrame('Howard Ian Peter Jonah Kellie'.split(), columns=['nome']) 
dataframe = lista_nomes = 'Howard Ian Peter Jonah Kellie'.split()
dataframe = lista_cpfs = '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split()
dataframe = lista_emails = 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split()
dataframe = lista_idades = [32, 22, 25, 29, 38]
dados = list(zip(lista_nomes, lista_cpfs, lista_idades, lista_emails)) # criauma lista de tuplas # Cria um DataFrame a partir de uma lista de tuplas
dataframe = pd.DataFrame(dados, columns=['nome', 'cpfs', 'idade', 'email']) 
print(dataframe)
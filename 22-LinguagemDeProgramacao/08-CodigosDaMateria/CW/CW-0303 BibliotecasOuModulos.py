# Falamos em módulo, mas em Python se ouve muito o termo biblioteca.
# Veja a seguir que temos o módulo math, que possui diversas funções matemáticas, 
# e o módulo os, que possui funções de sistema operacional, como capturar o caminho (getcwd), 
# listar um diretório (listdir), criar uma nova pasta (mkdir), dentre inúmeras outras. 

'''Para utilizar um módulo, é preciso importá-lo para o arquivo. 
Essa importação pode ser feita de maneiras distintas:

1. import moduloXX
1.2 import moduloXX as apelido'''

'''Exemplo 1: Importando todas as funcionalidades da biblioteca'''
import math
math.sqrt(25)
math.log2(1024)
math.cos(45)

'''Exemplo 2: Importando todas as funcionalidades da biblioteca'''
import math as m # importanto a biblioteca "math" com o ALIAS "m" usando o "as"
m.sqrt(25)       # o alias serve apenas para abreviar o math usando m no codigo.
m.log2(1024)
m.cos(45)

'''Exemplo 3: Importando todas as funcionalidades da biblioteca com Alias'''
from math import sqrt, log2, cos # importanto apenas algumas funcionalidades da
sqrt(25)                       # da biblioteca math.
log2(1024)
cos(45)

'''Classificação dos módulos (bibliotecas)'''
# Podemos classificar os módulos (bibliotecas) em três categorias:

'''>> Módulos built-in'''
# São embutidos no interpretador. Ao instalar o interpretador Python, também é feita 
# a instalação de uma biblioteca de módulos, que pode variar um de sistema operacional para outro.

'''>> Módulos de terceiros'''
# São criados por terceiros e disponibilizados via PyPI. 
# PyPI é a abreviação para Python Package Index, que é um repositório para programas 
# Python. Programadores autônomos e empresas podem criar uma solução em Python e disponibilizá-la 
# em forma de biblioteca no repositório PyPI. Dessa forma, todos usufruem e contribuem para o 
# crescimento da linguagem.

'''>> Módulos próprios'''
# São criados pelo desenvolvedor. Cada módulo pode importar outros módulos, tanto os 
# pertencentes ao mesmo projeto, quanto os built-in ou de terceiros.'''
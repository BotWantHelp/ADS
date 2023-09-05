#  criação de gráficos em Python, o profissional precisa conhecer a biblioteca 
#  matplotlib, pois diversas outras são construídas a partir desta. 

from matplotlib import pyplot as plt

'''Para criar uma figura com um eixo, de forma explícita, usamos: '''
# fig, ax = plt.subplots(1, 1)

'''Para criar uma figura com dois eixos, de forma explícita, usamos: '''
fig, ax = plt.subplots(1, 2)

'''Ao criar uma figura com mais de um eixo, temos que informar em qual vamos criar um gráfico. 
A variável “ax”, criada no último exemplo, é um vetor de eixos, ou seja, 
podemos acessar cada eixo pelo índice, começando por 0. Portanto, para plotar na figura mais à 
esquerda escolhemos ax[0].plot() e na da direita, ax[1].plot().'''
Dados = range(5)
 
ax[0].plot(Dados)
ax[1].plot(Dados)

plt.show()
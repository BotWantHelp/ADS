# o primeiro valor ocupa a posição zero da lista, já o último ocupa a posição n – 1, 
# em que n é a quantidade de elementos que a lista é capaz de armazenar.

# Uma das maneiras de criar uma lista é colocando os valores entre colchetes.
vogais1 = ['a', 'e', 'i', 'o', 'u']

# A lista pode ser criada sem nenhum elemento, e a inserção pode ser feita posteriormente:
vogais2 = []            # Cria lista Vazia
vogais2.append('A')     # Adiciona A no fim da lista
vogais2.append('E')     # Adiciona E no fim da lista
vogais2.append('I')     # Adiciona I no fim da lista
vogais2.append('O')     # Adiciona O no fim da lista
vogais2.append('U')     # Adiciona U no fim da lista

#Para acessar o valor guardado em uma lista, basta indicar o nome da variável e, 
# entre colchetes, a posição do elemento, ou a fatia (slice) de valores que se deseja:

print(vogais2)      # Mostra a lista completa
print(vogais2[2])   # Mostra o item 2 da lista
print(vogais2[:2])  # Mostra a lista até o item 2
print(vogais2[2:])  # Mostra a partir do item 2


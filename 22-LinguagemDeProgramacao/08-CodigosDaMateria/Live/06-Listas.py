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

#-----------------------------------------------------------------------------
# MANIPULANDO AS LISTAS ------------------------------------------------------
#-----------------------------------------------------------------------------

#Inserindo itens no fim da lista:
lista = [1, 2, 3]
lista.append(4) #append(): Adiciona um elemento ao final da lista.
print(lista)  # Fica: [1, 2, 3, 4]

# Inserindo Itens
lista = [1, 2, 3]
lista.insert(1, 4) # insert(): Insere um elemento em uma posição específica na lista.
print(lista)  # Fica: [1, 4, 2, 3]

#Apagando itens:
lista = [1, 2, 3, 4]
lista.remove(2) # remove(): Remove a primeira ocorrência de um elemento específico.
print(lista)  # Fica: [1, 3, 4]

lista = [1, 2, 3]
elemento = lista.pop(1) # pop(): Remove o item e o armazena na variavel elemento.
print(elemento)  # Fica: 2
print(lista)     # Fica: [1, 3]

#Substituindo itens:
lista = [1, 2, 3, 4]
lista[2] = 5  # A substituição de itens em uma lista geralmente envolve a atribuição direta a uma posição específica.
print(lista)  # Fica: [1, 2, 5, 4]

#Apagando o ultimo item
lista = [1, 2, 3, 4]
lista.pop()
print(lista) # Fica: [1, 2, 3]


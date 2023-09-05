# Para procurar elementos em uma lista por meio de algoritmo de busca sequencial, 
# é necessário percorrer todos os elementos da lista até encontrar o elemento procurado. 
# Para isso, é realizada uma comparação do valor do elemento que se deseja encontrar
# na lista com o valor de cada posição na lista caso nao encontre retorna n -1.

def busca_sequencial(lista, elemento):
    pos = 0 
    encontrado = False
     
    while pos < len(lista) and not encontrado: # Permitirá percorrer a lista e comparar o elemento procurado
          if lista[pos] == elemento:           # traz a condição para encontrar ou não o elemento
               encontrado = True
          else:
              pos = pos+1                      #  observe que todas posições serão percorridas 1 a 1
    return encontrado
   
testelista = [2, 10, 8, 15, 18, 20, 12, 1]

print(busca_sequencial(testelista, 5))  # Retorna False, pois nao encontrou na lista
print(busca_sequencial(testelista, 15)) # Retorna True, pois encontrou na lista
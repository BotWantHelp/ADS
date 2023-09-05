# se a lista já estiver ordenada, como é realizada a busca do elemento procurado? 
# Muito bem já conhecemos como se processa uma busca sequencial que considera um 
# vetor de entrada com números desordenados. Mas e, se a lista já estiver ordenada, 
# como é realizada a busca do elemento procurado? Observe a seguinte estrutura.

def busca_sequencial_ordenada(lista, elemento):
    pos = 0
    encontrado = False
    para = False
    while pos < len(lista) and not encontrado and not para:
            if lista[pos] == elemento:
                encontrado = True
            else:
                if lista[pos] > elemento:
                    para = True
                else:  
                    pos = pos+1

    return encontrado
    
testelista = [1, 2, 8, 10, 13, 15, 18, 20]
print(busca_sequencial_ordenada(testelista, 5))
print(busca_sequencial_ordenada(testelista, 15))
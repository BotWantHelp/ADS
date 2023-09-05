
def ordenacao_sequencial(lista):
    tamanho = len(lista)
    
    for i in range(tamanho - 1):                              # Vamos até o penúltimo elemento
        for j in range(i + 1, tamanho):                       # Começamos a partir do próximo elemento
            if lista[i] > lista[j]:                           # Troca se o elemento atual for maior
                lista[i], lista[j] = lista[j], lista[i]       # Aqui é feito a troca se i for maior que j
                print(f"Passo {i+1}: {lista}")                # Aqui cria um print para acompanhar o processo
    
    return lista

numeros = [4, 5, 2, 3, 1]
print("Lista original:", numeros)
numeros_ordenados = ordenacao_sequencial(numeros.copy())
print("Lista ordenada:", numeros_ordenados)


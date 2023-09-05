# Quick_Sort e Merge_sort, são mais utilizados por conta de dividir para acelerar a busca
# eles são otimos para desempenho.

# Bubble Sort: O Bubble Sort é um algoritmo simples que percorre 
# repetidamente a lista, compara pares adjacentes e troca elementos se estiverem na ordem errada. 
# Ele continua fazendo isso até que nenhuma troca seja necessária, indicando que a lista está ordenada.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Selection Sort: O Selection Sort percorre a lista em busca do menor (ou maior) elemento 
# e o coloca no início (ou final) da lista. Em seguida, repete esse processo para o restante da lista,
# excluindo os elementos já ordenados.
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        indice_minimo = i
        for j in range(i+1, n):
            if arr[j] < arr[indice_minimo]:
                indice_minimo = j
        arr[i], arr[indice_minimo] = arr[indice_minimo], arr[i]

# Insertion Sort: O Insertion Sort constrói a lista ordenada um elemento de cada vez, 
# movendo os elementos não ordenados para a posição correta. Ele percorre a lista e insere cada 
# elemento na posição apropriada entre os elementos já ordenados.
def insertion_sort(arr):
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >= 0 and chave < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave

# Merge Sort: O Merge Sort é um algoritmo de ordenação baseado na técnica 
# "dividir para conquistar". Ele divide a lista em duas metades, ordena cada metade separadamente e, 
# em seguida, combina as metades ordenadas para obter a lista final ordenada.
def merge_sort(arr):
    if len(arr) > 1:
        meio = len(arr) // 2
        metade_esquerda = arr[:meio]
        metade_direita = arr[meio:]

        merge_sort(metade_esquerda)
        merge_sort(metade_direita)

        i = j = k = 0
        while i < len(metade_esquerda) and j < len(metade_direita):
            if metade_esquerda[i] < metade_direita[j]:
                arr[k] = metade_esquerda[i]
                i += 1
            else:
                arr[k] = metade_direita[j]
                j += 1
            k += 1

        while i < len(metade_esquerda):
            arr[k] = metade_esquerda[i]
            i += 1
            k += 1

        while j < len(metade_direita):
            arr[k] = metade_direita[j]
            j += 1
            k += 1

# Quick Sort: O Quick Sort também é um algoritmo "dividir para conquistar". 
# Ele seleciona um elemento pivô da lista, divide a lista em duas partes (elementos menores que o pivô e 
# elementos maiores que o pivô) e, em seguida, recursivamente ordena essas partes.
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivo = arr[len(arr) // 2]
    esquerda = [x for x in arr if x < pivo]
    meio = [x for x in arr if x == pivo]
    direita = [x for x in arr if x > pivo]
    return quick_sort(esquerda) + meio + quick_sort(direita)


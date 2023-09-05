def executar_selection_sort(lista):
    n = len(lista)
    print(n) 

    for i in range(0, n):
        index_menor = i
        for j in range(i+1, n):
            if lista[j] < lista[index_menor]:
                index_menor = j
        lista[i], lista[index_menor] = lista[index_menor], lista[i]
    return lista

print('-♥'*20)

lista = [10, 9, 5, 8, 11, -1, 3]
executar_selection_sort(lista)   # Essa linha usa o print da linha 3 e exibe o numero 
resultado = executar_selection_sort(lista) # Essa linha pega o que a linha de cima faz e armazena na variavel
print(resultado) # Essa linha printa o resultado que a de cima armazenou 
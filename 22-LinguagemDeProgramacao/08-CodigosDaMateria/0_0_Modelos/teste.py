def executar_busca_linear(lista, valor):
    tamanho_lista = len(lista)
    for i in range(tamanho_lista):
        if valor == lista[i]:
            return i  # Retorna a posição do valor encontrado
    return -1  # Retorna -1 se o valor não for encontrado

lista = ['Valor1', 'Valor2', 'Valor3', 'Valor4', 'Valor5']
valor_procurado = input("Buscar: ")
posicao = executar_busca_linear(lista, valor_procurado)
if posicao != -1:
    print(f"O {valor_procurado} foi encontrado na posição {posicao} da lista")
else:
    print(f"O {valor_procurado} não consta na lista")
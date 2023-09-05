def executar_busca_binaria(lista, valor):
#  1- Inicialmente, você define minimo como 0 (índice inicial da lista) e maximo como o comprimento 
#  da lista menos 1 (índice final da lista).
    minimo = 0
    maximo = len(lista) - 1
#  2- Você entra em um loop while que continua enquanto minimo for menor ou igual a maximo.    
    while minimo <= maximo:
#  3- Dentro do loop, você calcula o índice do elemento do meio da faixa de busca utilizando a 
#  fórmula (minimo + maximo) // 2. Isso encontra o índice do elemento do meio entre minimo e maximo.
        meio = (minimo + maximo) // 2
#  4- Agora, você verifica se o valor procurado (valor) é igual ao valor no índice meio. Se for, 
#  você retorna True, indicando que o valor foi encontrado na lista.       
        if valor == lista[meio]:
            return True
        elif valor < lista[meio]:
#  5- Se o valor for menor que o valor no índice meio, você ajusta o valor de maximo para meio - 1, 
#  restringindo a busca para a metade esquerda da lista.            
            maximo = meio - 1
#  6- Se o valor for maior que o valor no índice meio, você ajusta o valor de minimo para meio + 1, 
#  restringindo a busca para a metade direita da lista.            
        else:
            minimo = meio + 1
#  7- Se o loop terminar sem encontrar o valor, você retorna False, indicando que o valor não está na lista.            
    return False

lista = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(executar_busca_binaria(lista=lista, valor=3))


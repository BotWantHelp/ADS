# algoritmo usado para buscar um valor em uma sequência é o de busca binária. 
# A primeira grande diferença entre o algoritmo de busca linear e o algoritmo
# de busca binária é que neste os valores precisam estar ordenados

def busca_binaria(lista, elemento):
        minimo = 0 
        maximo = len(lista)-1
        encontrado = False
    
        while minimo <= maximo and not encontrado:
            meio_lista = (minimo + maximo)//2        # Encontra o item no meio da sequência.
            print(meio_lista)
            if lista[meio_lista] == elemento:        # Se o valor for igual ao item do meio, a busca encerra.
                encontrado = True
            else:
                if elemento < lista[meio_lista]:     # verifica se o valor é maior ou menor que o valor central
                    maximo = meio_lista-1
                    print(maximo)
                else:
                    minimo = meio_lista+1
                    print(minimo)
            # Se for maior, então a busca acontecerá na metade superior da sequência (a inferior é descartada)
            # Se não for maior, a busca acontecerá na metade inferior da sequência (a superior é descartada).
        return encontrado
    
testelista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(busca_binaria(testelista, 15))

# Na linha 10, temos a estrutura de repetição “while”, 
# que será executada enquanto o primeiro elemento da lista (mínimo) 
# for menor ou igual ao máximo (último elemento) e o elemento procurado não for encontrado.

# Na linha 11, identificamos o índice associado à metade da lista.

# Na linha 12, temos uma estrutura de condição “if” em razão da qual, 
# basicamente, verifica-se que, se o elemento do meio da lista for o valor procurado, 
# será retornado o True (linha 9).

# Na linha 13, temos a condição “else”, que verifica se o elemento procurado
# é menor que o valor do meio da lista. Se for maior, então a busca acontecerá na metade
# superior da sequência (a inferior é descartada); se não for, a busca acontecerá na
# metade inferior da sequência (a superior é descartada).

# Algoritmos de busca compõem o arsenal de algoritmos tradicionais da computação. 
# Quando é conhecida a sequência de passos, ou seja, o pseudocódigo, basta escolher
# uma linguagem de programação e implementá-la.
# Algoritmo de Ordenação por inserção (Insertion Sort) O algoritmo de ordenação por 
# inserção é iniciado a partir do segundo valor no vetor, pois o primeiro elemento 
# será uma referência para a ordenação. Ou seja, o segundo elemento do vetor será 
# comparado com o primeiro. O vetor é percorrido da esquerda para a direita. Nesse 
# caminho, compara-se sempre o elemento da direita com os elementos à esquerda de 
# modo que os elementos mais à esquerda sejam organizados e ordenados. O algoritmo 
# de ordenação por inserção tem funcionamento similar ao das pessoas que ordenam 
# cartas em um jogo de baralho.

a = [5, 6, 1, 4, 2, 0, 3]                  # Inicializa a lista 'a' com os valores dados: [5, 6, 1, 4, 2, 0, 3]

for i in range(1, 7):                      # Inicia um loop de 1 a 6 (inclusive) usando a variável 'i'
    j = i - 1                              # Define a variável 'j' como 'i - 1', representando o índice do elemento à esquerda
    while j >= 0 and a[j] > a[j + 1]:      # Entra em um loop 'enquanto' 'j' for maior ou igual a 0 e o valor em 'a[j]' for maior que o valor em 'a[j + 1]'
        a[j], a[j + 1] = a[j + 1], a[j]    # Troca os valores em 'a[j]' e 'a[j + 1]', reordenando elementos adjacentes
        j = j - 1                          # Decrementa 'j' em 1, movendo a comparação para a esquerda
print(a)

# Após as iterações, a lista 'a' estará ordenada em ordem crescente: [0, 1, 2, 3, 4, 5, 6]

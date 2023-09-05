# Busca linear ou sequencial O algoritmo de busca sequencial, ou busca exaustiva, 
# percorre os itens da sequência procurando o valor de destino, conforme ilustra a figura.



#Código                                   #  Explicação
def executar_busca_linear(lista, valor):  #  Definição da função
    tamanho_lista = len(lista)            #  Definição do tamanho da lista
    for i in range(tamanho_lista):        #  Estrutura de repetição para percorrer toda a lista
        if valor == lista[i]:             #  Condição para verificar se é o valor.
            return i                      #  Retorno, caso encontre o valor
    return -1                             #  Retorno, caso não encontre o valor

lista = ['Valor1', 'Valor2', 'Valor3', 'Valor4', 'Valor5']
valor_procurado = input("Buscar: ")       # Abaixo solicita que digite a Busca

for i, item in enumerate(lista):          # Lista todos os itens e suas posições na lista
    print(f"Item: {item}, Posição: {i}")
    
posicao = executar_busca_linear(lista,valor_procurado)

if posicao != -1:
    print(f"O {valor_procurado}, Foi encontado na lista na posição {posicao}")
else:
    print(f"O {valor_procurado}, Não consta na lista")
# No exemplo de algoritmo de busca sequencial que considera um vetor de entrada 
# com números desordenados. Temos uma estrutura de repetição “while”.


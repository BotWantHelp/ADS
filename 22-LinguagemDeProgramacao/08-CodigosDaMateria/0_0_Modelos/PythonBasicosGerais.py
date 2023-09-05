# Funções mais comuns em python

# Exibe mensagens no console.
mensagem = "Olá, mundo!"
print(mensagem)
# Explicação: A função print() exibe a mensagem "Olá, mundo!" no console.

# len(): Retorna o número de itens em um objeto (como lista, string, etc.).
lista = [1, 2, 3, 4, 5]
tamanho = len(lista)
print(tamanho)
# Explicação: A função len() retorna o tamanho da lista, que é 5.

# range(): Gera uma sequência de números.
numeros = list(range(1, 6))
print(numeros)
#Explicação: A função range(1, 6) gera uma sequência de números de 1 a 5, que é convertida em uma lista.

#int() e float(): Convertem valores em números inteiros ou de ponto flutuante.
texto_numero = "42"
numero_inteiro = int(texto_numero)
numero_decimal = float(texto_numero)
print(type(numero_inteiro))
print(type(numero_decimal))
#Explicação: As funções int() e float() convertem uma string "42" em números 42 inteiro e de ponto flutuante, respectivamente.

# str(): Converte valores em strings.
numero = 42
texto_numero = str(numero)
# Explicação: A função str() converte o número 42 em uma string "42".

# list(): Converte sequências em listas.
texto = "Python"
lista_caracteres = list(texto)
print(lista_caracteres)
# Explicação: A função list() converte a string "Python" em uma lista ['P', 'y', 't', 'h', 'o', 'n'].

# max() e min(): Encontram o maior e o menor valor em uma sequência.
numeros = [10, 3, 8, 15, 5]
maior_valor = max(numeros)
menor_valor = min(numeros)
print(maior_valor)
print(menor_valor)
# Explicação: As funções max() e min() encontram o maior valor (15) e o menor valor (3) na lista.

# sum(): Calcula a soma dos elementos em uma sequência numérica.
numeros = [1, 2, 3, 4, 5]
soma = sum(numeros)
print(soma)
# Explicação: A função sum() calcula a soma dos números na lista, que é 15.

# sorted(): Ordena uma sequência.
numeros = [5, 2, 8, 1, 9]
numeros_ordenados = sorted(numeros)
print(numeros_ordenados)
# Explicação: A função sorted() retorna uma nova lista com os números ordenados: [1, 2, 5, 8, 9].

#input(): Permite a entrada de dados do usuário via console.
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")
# Explicação: A função input() solicita ao usuário que digite seu nome, e o nome é exibido em seguida.
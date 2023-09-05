'''Em Python, as funções anônimas são definidas utilizando a expressão lambda. 
Essas funções não possuem um nome atribuído e geralmente são utilizadas quando 
é necessário uma função simples que será usada apenas em um contexto específico. 
Abaixo estão alguns exemplos de funções anônimas em Python:'''

# Função que calcula o quadrado de um número:
square = lambda x: x ** 2

# Função que soma dois números:
add = lambda a, b: a + b
print(add(3, 7))   # Output: 10

# Função que verifica se um número é par:
is_even = lambda x: x % 2 == 0
print(is_even(4))  # Output: True
print(is_even(5))  # Output: False

# Função que retorna o primeiro elemento de uma lista:
get_first_element = lambda lst: lst[0] if lst else None
print(get_first_element([10, 20, 30]))  # Output: 10
print(get_first_element([]))            # Output: None

# Função que transforma uma string em maiúsculas:
uppercase = lambda s: s.upper()
print(uppercase("hello"))      # Output: "HELLO"

# Função que retorna a soma de todos os elementos de uma lista:
sum_list = lambda lst: sum(lst)
print(sum_list([1, 2, 3, 4]))  # Output: 10

print(square(5))  # Output: 25
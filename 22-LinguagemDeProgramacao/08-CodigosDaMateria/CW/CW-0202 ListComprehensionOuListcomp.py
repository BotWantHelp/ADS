# Uma maneira muito elegante de criar uma lista é usando a 
# list comprehension. Também chamada de listcomp
# Sua sintaxe básica é: [item for item in lista]

                                   # List Comprehension
list = [1*x+1 for x in range(10)]  # Essa merda doida aqui.
print(f' Lista Modelo 1 - {list}')

#--------------------------------------------------------------------------

listy = []
for y in range(1,11):              # Faz Igual essa merda aqui mas resumido
    1 * y + 1
    listy.append(y)
print(f' Lista Modelo 2 - {listy}')
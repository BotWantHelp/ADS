
def Soma(x,y):     # Aqui temos a função de somar, onde qualquer valor sera somado
    R = x + y      # os valores da função serão substituidos pelo usuario abaixo
    return R       # aqui selecionamos que queremos retornar o resultado da soma

def subtrair(x,y): # Aqui temos a função de somar, onde qualquer valor sera somado
    R = x - y      # os valores da função serão substituidos pelo usuario abaixo
    return R       # aqui selecionamos que queremos retornar o resultado da soma

a = int(input("Digite um valor para a: "))
b = int(input("Digite um valor para b: "))
c = int(input("Digite um valor para c: "))

s = Soma(a,b)    # aqui chamamos a função e passamos os valores (a e b) que irão substituir (x e y) da função
print(f'\na soma de {a} + {b} é igual a {s}')
s = Soma(a,c)    # aqui chamamos a função e passamos os valores (a e c) que irão substituir (x e y) da função
print(f'a soma de {a} + {c} é igual a {s}')
s = Soma(b,c)    # aqui chamamos a função e passamos os valores (b e c) que irão substituir (x e y) da função
print(f'a soma de {b} + {c} é igual a {s}\n')

s1 = subtrair(b,c)    # aqui chamamos a função e passamos os valores (b e c) que irão substituir (x e y) da função
print(f'a subtração de {b} - {c} é igual a {s1}\n')


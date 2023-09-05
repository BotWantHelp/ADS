import pandas as pd

dic = {
    'nome' :   'Matheus Júlia André'  .split(),
    'idade':   '28      22    30'     .split(),
    'Q.I'  :   '130     121   57'     .split()
}

indice = ['a', 'b', 'c']

ver_DataFrame = pd.DataFrame(dic, index=indice)

print(ver_DataFrame,'\n')

for nome, idade, qi in zip(dic['nome'], dic['idade'], dic['Q.I']):
    if int(qi) <= 100:
        print(f"Olá {nome}, seu Q.I é de {qi}, o que indica que tu estás lascado, meu amigo...\n")
    else:
        print(f"Olá {nome}, seu Q.I é de {qi}, o que indica que você tem futuro!\n")


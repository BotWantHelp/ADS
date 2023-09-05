
def exemplo(*args, **kwargs):
    print("Argumentos posicionais:")
    for arg in args:
        print(arg)

    print("\nArgumentos do tipo palavra-chave:")
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')

exemplo(1, 2, 3, 4, 5, 6, 7, nome='Rapha', idade=36, altura=1.35, peso=127.5)


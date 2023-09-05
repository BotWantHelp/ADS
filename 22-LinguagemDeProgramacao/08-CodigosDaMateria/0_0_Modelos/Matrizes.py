
matriz= [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9],
         [0]]

print(matriz)        # Imprimindo a matriz linear no terminal

print("♥ "*20)       # Imprimindo a matriz no formato correto
for linha in matriz:
    print(linha)
    
print("♥ "*20)               # Aqui voce procura e define o elemento indicando posição Y e X iniciando em ZERO
elemento_06 = matriz[1][2]   # Linha 2 x Coluna 3
elemento_09 = matriz[2][2]   # Linha 3 x Coluna 3

print(f"O numero encontrado é: {elemento_06}{elemento_09}, HMMMMMMMMMMM")
print("♥ "*20)

def calcular_imc():
    nome = input("Digite seu nome: ")
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): ").replace(",","."))
    
    imc = peso / (altura ** 2)
    
    classificacao = ""
    if imc < 18.59:
        classificacao = "Abaixo do peso"
    elif imc < 24.99:
        classificacao = "Peso normal"
    elif imc < 29.99:
        classificacao = "Sobrepeso"
    elif imc < 34.99:
        classificacao = "Obesidade Grau I"
    elif imc < 39.99:
        classificacao = "Obesidade Grau II"
    else:
        classificacao = "Obesidade Grau III"
    
    print(f"{nome}, seu IMC é de {imc:.2f} e a classificação do IMC é '{classificacao}'.")

def ver_tabela_imc():
    print("Tabela IMC:")
    print("Abaixo do peso:     IMC < 18.5")
    print("Peso normal:        18.5 <= IMC < 24.9")
    print("Sobrepeso:          24.9 <= IMC < 29.9")
    print("Obesidade Grau I:   29.9 <= IMC < 34.9")
    print("Obesidade Grau II:  34.9 <= IMC < 39.9")
    print("Obesidade Grau III: IMC >= 39.9")

while True:
    print("♥ - "*10,"\n\n")
    print("♥ ♥  Bora calcular as GORDURENHAS  ♥ ♥\n\n")
    print("♥ - "*10,"\n")
    print("Menu:\n")
    print("1 - Calcular IMC")
    print("2 - Ver Tabela IMC")
    print("3 - Fechar\n")
    
    escolha = input("Escolha uma das 3 opções: ")
    
    if escolha == "1":
        calcular_imc()
    elif escolha == "2":
        ver_tabela_imc()
    elif escolha == "3":
        print("Vai sair? ta gordinho? Fica triste não papai do céu te acha lindo(a).")
        break
    else:
        print("Sério?  Não sabe ler? é 1, 2 ou 3 apenas, Escolha novamente.\n")

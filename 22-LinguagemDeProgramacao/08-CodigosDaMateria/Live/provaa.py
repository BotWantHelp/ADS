def calcular(operacao):
    return {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y
    }[operacao]

while True:
    try:
        primeiro_num = float(input("Digite o primeiro número: "))
        operacao = input("Digite a operação (+, -, *, /): ")
        segundo_num = float(input("Digite o segundo número: "))
    except ValueError:
        print("Valor inválido! Digite novamente.")
        continue

    if operacao not in ['+', '-', '*', '/']:
        print("Operação inválida! Digite novamente.")
        continue

    resultado = calcular(operacao)(primeiro_num, segundo_num)
    print(f"O resultado é = {resultado}")

    fim = input('Pressione [r] para repetir ou [s] para sair ').lower()

    if fim == 's':
        break
    elif fim != 'r':
        print("Escolha inválida. Fim do programa.")
        break

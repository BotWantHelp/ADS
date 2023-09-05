def calculadora():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            operacao = input("Digite a operação (+ , - , * , / ): ")
            num2 = float(input("Digite o segundo número: "))

            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                resultado = num1 / num2
                break
            else:
                print("Operação inválida. Tente novamente. CHUPA VITAO")
                continue

            print("Resultado:", resultado, "\n")

        except ValueError:
            print("Entrada inválida. Certifique-se de digitar números válidos.")

calculadora()

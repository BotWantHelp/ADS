def calculadoraIMC():
    while True:
        try:
            nome = input("Digite seu nome: ")
            peso = input("Digite seu peso: ").replace(',', '.').replace('.','')
            altura = input("Digite sua altura: ").replace(',', '.').replace('.','')
            alturaMetros = float(altura) / 100
            imc = float(peso) / (float(alturaMetros) * float(alturaMetros))
            if imc < 18.49:
                print(f'{nome}, seu IMC e: {imc:.2f}, Seu IMC esta abaixo do peso\n')
            elif imc >= 18.5 or imc <= 24.5:
                print(f'{nome}, seu IMC e: {imc:.2f}, Seu IMC esta normal\n')
            else:
                print(f'{nome}, seu IMC e: {imc:.2f},Seu IMC esta acima do peso\n')
            print("Parabens por se preocupar com sua saude",nome)
        except ValueError:
            print("Entrada inválida. Certifique-se de digitar números válidos.\n")
calculadoraIMC()

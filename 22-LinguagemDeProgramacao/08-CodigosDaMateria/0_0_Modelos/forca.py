def exibir_palavra(palavra, letras_adivinhadas):
    exibicao = ''
    for letra in palavra:
        if letra in letras_adivinhadas:
            exibicao += letra
        else:
            exibicao += '_'
    return exibicao

def desenhar_forca(tentativas_restantes):
    etapas = [
        '''
           -----
           |   |
               |
               |
               |
               |
        ''',
        '''
           -----
           |   |
           O   |
               |
               |
               |
        ''',
        '''
           -----
           |   |
           O   |
           |   |
               |
               |
        ''',
        '''
           -----
           |   |
           O   |
          /|   |
               |
               |
        ''',
        '''
           -----
           |   |
           O   |
          /|\  |
               |
               |
        ''',
        '''
           -----
           |   |
           O   |
          /|\  |
          /    |
               |
        ''',
        '''
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
        '''
    ]

    print(etapas[6 - tentativas_restantes])

def jogo_da_forca():
    palavra = "mostro"
    letras_adivinhadas = []
    tentativas_restantes = 6

    print("Bem-vindo ao Jogo da Forca!")
    print(exibir_palavra(palavra, letras_adivinhadas))

    while True:
        palpite = input("Digite uma letra: ").lower()

        if palpite in letras_adivinhadas:
            print("Você já tentou essa letra.")
            continue

        letras_adivinhadas.append(palpite)

        if palpite not in palavra:
            tentativas_restantes -= 1
            desenhar_forca(tentativas_restantes)
            print(f"Letra '{palpite}' não está na palavra. Você tem {tentativas_restantes} tentativas restantes.")
            if tentativas_restantes == 0:
                print("Você perdeu! A palavra era:", palavra)
                break
        else:
            print("Letra correta!")

        exibicao_palavra = exibir_palavra(palavra, letras_adivinhadas)
        print(exibicao_palavra)

        if '_' not in exibicao_palavra:
            print("Parabéns! Você venceu!")
            break

jogo_da_forca()

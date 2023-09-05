import pygame
import sys
import random
from pygame.locals import *

pygame.init()

# Configurações da janela
largura, altura = 400, 400
tamanho_quadrado = largura // 8
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo de Damas")

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)
cinza = (128, 128, 128)
vermelho = (255, 0, 0)

# Tabuleiro
tabuleiro = [[0, 2, 0, 2, 0, 2, 0, 2],
             [2, 0, 2, 0, 2, 0, 2, 0],
             [0, 2, 0, 2, 0, 2, 0, 2],
             [0] * 8,
             [0] * 8,
             [1, 0, 1, 0, 1, 0, 1, 0],
             [0, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 0]]

peca_selecionada = None
turno_computador = False
pontuacao_jogador = 0
pontuacao_computador = 0

# Função para verificar se um movimento é válido
def movimento_valido(linha_de, coluna_de, linha_para, coluna_para):
    return 0 <= linha_para < 8 and 0 <= coluna_para < 8 and tabuleiro[linha_para][coluna_para] == 0

# Função para verificar se uma captura é válida
def captura_valida(linha_de, coluna_de, linha_para, coluna_para):
    linha_meio = (linha_de + linha_para) // 2
    coluna_meio = (coluna_de + coluna_para) // 2
    return 0 <= linha_para < 8 and 0 <= coluna_para < 8 and tabuleiro[linha_meio][coluna_meio] == 2 and tabuleiro[linha_para][coluna_para] == 0

# Função para mover a peça da máquina com captura
def mover_peca_computador():
    movimentos_validos = []
    for linha in range(8):
        for coluna in range(8):
            if tabuleiro[linha][coluna] == 2:
                if captura_valida(linha, coluna, linha + 2, coluna - 2):
                    movimentos_validos.append((linha, coluna, linha + 2, coluna - 2))
                if captura_valida(linha, coluna, linha + 2, coluna + 2):
                    movimentos_validos.append((linha, coluna, linha + 2, coluna + 2))
    if movimentos_validos:
        movimento = random.choice(movimentos_validos)
        linha_de, coluna_de, linha_para, coluna_para = movimento
        linha_meio = (linha_de + linha_para) // 2
        coluna_meio = (coluna_de + coluna_para) // 2
        tabuleiro[linha_para][coluna_para] = tabuleiro[linha_de][coluna_de]
        tabuleiro[linha_de][coluna_de] = 0
        tabuleiro[linha_meio][coluna_meio] = 0

# Função para verificar se o jogo terminou
def verificar_vitoria():
    global pontuacao_jogador, pontuacao_computador
    if all(peca == 0 for linha in tabuleiro for peca in linha):
        return True
    if all(peca == 0 for linha in tabuleiro[:3] for peca in linha if peca == 1):
        pontuacao_computador += 1
        return True
    if all(peca == 0 for linha in tabuleiro[5:] for peca in linha if peca == 2):
        pontuacao_jogador += 1
        return True
    return False

# Loop do jogo
clock = pygame.time.Clock()
running = True

while running:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            running = False
        if evento.type == MOUSEBUTTONDOWN and evento.button == 1:
            coluna_clicada = evento.pos[0] // tamanho_quadrado
            linha_clicada = evento.pos[1] // tamanho_quadrado

            if not turno_computador:
                if peca_selecionada is None and tabuleiro[linha_clicada][coluna_clicada] == 1:
                    peca_selecionada = (linha_clicada, coluna_clicada)
                elif peca_selecionada is not None:
                    linha_de, coluna_de = peca_selecionada
                    if movimento_valido(linha_de, coluna_de, linha_clicada, coluna_clicada) or captura_valida(linha_de, coluna_de, linha_clicada, coluna_clicada):
                        tabuleiro[linha_clicada][coluna_clicada] = tabuleiro[linha_de][coluna_de]
                        tabuleiro[linha_de][coluna_de] = 0
                        if captura_valida(linha_de, coluna_de, linha_clicada, coluna_clicada):
                            linha_meio = (linha_de + linha_clicada) // 2
                            coluna_meio = (coluna_de + coluna_clicada) // 2
                            tabuleiro[linha_meio][coluna_meio] = 0
                            peca_selecionada = None
                            if not captura_valida(linha_clicada, coluna_clicada, linha_clicada + 2, coluna_clicada - 2) and not captura_valida(linha_clicada, coluna_clicada, linha_clicada + 2, coluna_clicada + 2):
                                turno_computador = True
                        else:
                            peca_selecionada = None
                            turno_computador = True

    if turno_computador:
        mover_peca_computador()
        turno_computador = False

    tela.fill(branco)

    # Desenha o tabuleiro e as peças
    for linha in range(8):
        for coluna in range(8):
            cor = preto if (linha + coluna) % 2 == 1 else cinza
            pygame.draw.rect(tela, cor, (coluna * tamanho_quadrado, linha * tamanho_quadrado, tamanho_quadrado, tamanho_quadrado))
            if tabuleiro[linha][coluna] == 1:
                pygame.draw.circle(tela, preto, (coluna * tamanho_quadrado + tamanho_quadrado // 2, linha * tamanho_quadrado + tamanho_quadrado // 2), tamanho_quadrado // 2 - 5)
            elif tabuleiro[linha][coluna] == 2:
                pygame.draw.circle(tela, vermelho, (coluna * tamanho_quadrado + tamanho_quadrado // 2, linha * tamanho_quadrado + tamanho_quadrado // 2), tamanho_quadrado // 2 - 5)

    pygame.display.flip()
    clock.tick(60)

    if verificar_vitoria():
        print("Jogo terminou!")
        print(f"Pontuação do Jogador: {pontuacao_jogador}")
        print(f"Pontuação do Computador: {pontuacao_computador}")
        running = False

pygame.quit()
sys.exit()

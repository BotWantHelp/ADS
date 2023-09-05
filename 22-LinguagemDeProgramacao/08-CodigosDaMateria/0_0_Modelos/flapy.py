import pygame
import sys
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

# Cores
white = (255, 255, 255)
blue = (0, 0, 255)

# Bird
bird_x = 100
bird_y = 250
bird_velocity = 0
bird_gravity = 0.5
bird_jump = -10
bird_width = 40
bird_height = 40

# Pipes
pipe_width = 70
pipe_height = 300
pipe_x = screen_width
pipe_speed = 4
pipe_gap = 150
pipes = []

# Score
score = 0
font = pygame.font.Font(None, 36)

def draw_bird(x, y):
    pygame.draw.rect(screen, blue, (x, y, bird_width, bird_height))

def draw_pipe(x, height):
    pygame.draw.rect(screen, blue, (x, 0, pipe_width, height))
    pygame.draw.rect(screen, blue, (x, height + pipe_gap, pipe_width, screen_height - height - pipe_gap))

def game_over():
    text = font.render("Game Over", True, blue)
    screen.blit(text, (150, 250))
    pygame.display.update()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = bird_jump

    # Move o pássaro
    bird_y += bird_velocity
    bird_velocity += bird_gravity

    # Verifica colisões com o chão
    if bird_y >= screen_height - bird_height:
        bird_y = screen_height - bird_height
        bird_velocity = 0

    # Gera novos canos
    if len(pipes) == 0 or pipes[-1][0] < screen_width - 200:
        pipe_height = random.randint(50, screen_height - 200)
        pipes.append([screen_width, pipe_height])

    # Move os canos
    for pipe in pipes:
        pipe[0] -= pipe_speed

    # Remove os canos fora da tela
    if pipes and pipes[0][0] < -pipe_width:
        pipes.pop(0)

    # Verifica colisões com os canos
    for pipe in pipes:
        pipe_x, pipe_height = pipe
        if bird_x < pipe_x + pipe_width and bird_x + bird_width > pipe_x:
            if bird_y < pipe_height or bird_y + bird_height > pipe_height + pipe_gap:
                game_over()

    # Verifica se o pássaro passou por um cano
    if pipes and bird_x > pipes[0][0] + pipe_width:
        pipes.pop(0)
        score += 1

    # Limpa a tela
    screen.fill(white)

    # Desenha o pássaro
    draw_bird(bird_x, bird_y)

    # Desenha os canos
    for pipe in pipes:
        draw_pipe(pipe[0], pipe[1])

    # Desenha a pontuação
    score_text = font.render("Score: " + str(score), True, blue)
    screen.blit(score_text, (20, 20))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
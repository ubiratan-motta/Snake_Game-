import pygame
import random

from pygame.locals import *


def on_grid_random():
    x = random.randint(0, 40)
    y = random.randint(0, 40)
    return x * 10, y * 10


def colisao(c1, c2):
    return(c1[0] == c2[0]) and (c1[1] == c2[1])


UP = 0
RIGHT = 1
LEFT = 2
DOWN = 3


pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Cobra')

cobra = [(200, 200), (210, 200), (220, 200)]
cobra_cor = pygame.Surface((10, 10))
cobra_cor.fill((255, 255, 255))

maca_pos = on_grid_random()
maca = pygame.Surface((10, 10))
maca.fill((255, 0, 0))

direcao = LEFT

clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 18)
pontos = 0

game_over = False
while not game_over:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_UP and direcao != DOWN:
                direcao = UP
            if event.key == K_DOWN and direcao != UP:
                direcao = DOWN
            if event.key == K_LEFT and direcao != RIGHT:
                direcao = LEFT
            if event.key == K_RIGHT and direcao != LEFT:
                direcao = RIGHT

    if colisao(cobra[0], maca_pos):
        maca_pos = on_grid_random()
        cobra.append((0, 0))
        pontos = pontos + 1

    if cobra[0][0] == 400 or cobra[0][1] == 400 or cobra[0][0] < 0 or cobra[0][1] < 0:
        game_over = True
        break

    for i in range(1, len(cobra) - 1):
        if cobra[0][0] == cobra[i][0] and cobra[0][1] == cobra[i][1]:
            game_over = True

    if game_over:
        break

    for i in range(len(cobra) - 1, 0, -1):
        cobra[i] = (cobra[i - 1][0], cobra[i - 1][1])

    if direcao == UP:
        cobra[0] = (cobra[0][0], cobra[0][1] - 10)
    if direcao == DOWN:
        cobra[0] = (cobra[0][0], cobra[0][1] + 10)
    if direcao == RIGHT:
        cobra[0] = (cobra[0][0] + 10, cobra[0][1])
    if direcao == LEFT:
        cobra[0] = (cobra[0][0] - 10, cobra[0][1])

    screen.fill((0, 0, 0))
    screen.blit(maca, maca_pos)

    for x in range(0, 400, 10):
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 400))
    for y in range(0, 400, 10):
        pygame.draw.line(screen, (40, 40, 40), (0, y), (400, y))

    score_font = font.render('Score: %s' % pontos, True, (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (400 - 80, 10)
    screen.blit(score_font, score_rect)

    for pos in cobra:
        screen.blit(cobra_cor, pos)

    pygame.display.update()

while True:
    game_over_font = pygame.font.Font('freesansbold.ttf', 75)
    game_over_screen = game_over_font.render('Game Over', True, (255, 255, 255))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (400 / 2, 10)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

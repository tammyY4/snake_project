from src.const import k1_image, w_image, e_image, l_image, c_image, o_image, m_image, start_image, color_image

# Игра Змейка
# Подключение библиотеки PyGame
import pygame
from src.screen import screenMain
from src.func import quit_app, get_snake_color, get_snake_speed
from src.classh import Game

begin = True
start_game = False
color = False


def greetings():
    screenMain.fill((234, 11, 11))
    screenMain.blit(w_image, (11, 200))
    screenMain.blit(e_image, (119, 140))
    screenMain.blit(l_image, (169, 90))
    screenMain.blit(l_image, (259, 80))
    screenMain.blit(c_image, (340, 80))
    screenMain.blit(o_image, (440, 98))
    screenMain.blit(m_image, (508, 102))
    screenMain.blit(e_image, (617, 196))
    screenMain.blit(start_image, (260, 500))


while begin:
    greetings()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_app()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = pygame.mouse.get_pos()
                if (x >= 260 and x <= 370 and y >= 500 and y <= 550):
                    start_game = True
    while start_game:
        screenMain.fill((1, 1, 1))
        screenMain.blit(k1_image, (257, 400))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_app()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    snake_speed = get_snake_speed(x, y)
                    start_game = False
                    color = True
    while color:
        screenMain.fill((5, 5, 5))
        screenMain.blit(color_image, (257, 400))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_app()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    snake_color = get_snake_color(x, y)
                    c = Game(snake_speed, snake_color)
                    c.process()
quit_app()

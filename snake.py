# Игра Змейка
# Подключение библиотеки PyGame
import pygame
import time
import random

# Иницилизация PyGame
pygame.init()

# Создаем окно игры
high = 700  # высота (Oy)
widgh = 700  # ширина  (Ox)
screenMain = pygame.display.set_mode((widgh, high))
pygame.display.set_caption("My Snake")
k1_image = pygame.image.load("цифры.png")
w_image = pygame.image.load("w.png")
e_image = pygame.image.load("e.png")
l_image = pygame.image.load("l.png")
c_image = pygame.image.load("c.png")
o_image = pygame.image.load("o.png")
m_image = pygame.image.load("m.png")
start_image = pygame.image.load("start.jpg")
color_image = pygame.image.load("color.png")
begin = True
start_game = False
color = False
f2 = open('result.txt')
best_result = int(f2.readline()[::-1])
f2.close()


# Цикл игры
def game(snake_speed, color_of_snake):
    global best_result
    score = 0
    len_snake = 1
    game_continue = True  # выхода из цикла игры
    game_over = False
    game_restart = False
    color_continue = False
    x0 = widgh // 2
    y0 = high // 2  # начальные координаты головы
    snake_body = []
    snake_radius = 10
    # snake_speed = 30
    x0_change = 0
    y0_change = 0  # переменные, отвечающие за передвижение головы
    snake_body_move = [x0_change, y0_change]
    x1 = 346
    y1 = 350  # начальные координаты глаза1
    x1_change = 0
    y1_change = 0  # переменные, отвечающие за передвижение глаза1

    x2 = 354
    y2 = 350  # начальные координаты глаза2
    x2_change = 0
    y2_change = 0  # переменные, отвечающие за передвижение глаза2

    clock = pygame.time.Clock()
    k = random.randrange(1, 21)
    food_x = round(random.randrange(0, widgh - 2 * snake_radius) / snake_radius) * snake_radius
    food_y = round(random.randrange(0, high - 2 * snake_radius) / snake_radius) * snake_radius

    while game_continue:
        while game_over == True:
            while game_restart == True:
                screenMain.fill((0, 0, 0))
                print_gameover = pygame.font.Font(None, 70)
                result = print_gameover.render('Game over', True, (180, 0, 180))
                print_best_result = pygame.font.Font(None, 49)
                f1 = open('result.txt')
                k = f1.readline()[::-1]
                best_result_screen = print_best_result.render('Best Result: ' + k, True, (0, 128, 128))
                f1.close()
                print_score = pygame.font.Font(None, 49)
                score_screen = print_score.render('Your result: ' + str(score), True, (200, 200, 200))
                screenMain.blit(best_result_screen, (299, 10))
                screenMain.blit(score_screen, (0, 10))
                screenMain.blit(result, (237, 317))
                screenMain.blit(k1_image, (257, 400))

                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            x, y = pygame.mouse.get_pos()
                            if (x >= 232 and x <= 282 and y >= 350 and y <= 450):
                                snake_speed = 5
                                game_restart = False
                                color_continue = True
                            if (x > 282 and x <= 332 and y >= 350 and y <= 450):
                                snake_speed = 10
                                game_restart = False
                                color_continue = True
                            if (x > 332 and x <= 372 and y >= 350 and y <= 450):
                                snake_speed = 13
                                game_restart = False
                                color_continue = True
                            if (x > 382 and x <= 432 and y >= 350 and y <= 450):
                                snake_speed = 20
                                game_restart = False
                                color_continue = True
                            if (x > 432 and x <= 472 and y >= 350 and y <= 450):
                                snake_speed = 30
                                game_restart = False
                                color_continue = True
            while color_continue:
                screenMain.fill((5, 5, 5))
                screenMain.blit(color_image, (257, 400))

                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            x, y = pygame.mouse.get_pos()
                            if (x >= 232 and x <= 282 and y >= 350 and y <= 450):
                                game(snake_speed, (255, 0, 0))
                                color_continue = False
                                game_over = False
                            if (x > 282 and x <= 332 and y >= 350 and y <= 450):
                                game(snake_speed, (0, 128, 255))
                                color_continue = False
                                game_over = False
                            if (x > 332 and x <= 372 and y >= 350 and y <= 450):
                                game(snake_speed, (255, 255, 0))
                                color_continue = False
                                game_over = False
                            if (x > 382 and x <= 432 and y >= 350 and y <= 450):
                                game(snake_speed, (24, 3, 171))
                                color_continue = False
                                game_over = False
                            if (x > 432 and x <= 472 and y >= 350 and y <= 450):
                                game(snake_speed, (120, 54, 69))
                                color_continue = False
                                game_over = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_continue = False
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x0_change = -snake_radius
                    y0_change = 0
                    x1_change = -snake_radius
                    y1_change = 0
                    x2_change = -snake_radius
                    y2_change = 0
                elif event.key == pygame.K_RIGHT:
                    x0_change = snake_radius
                    y0_change = 0
                    x1_change = snake_radius
                    y1_change = 0
                    x2_change = snake_radius
                    y2_change = 0
                elif event.key == pygame.K_UP:
                    y0_change = -snake_radius
                    x0_change = 0
                    y1_change = -snake_radius
                    x1_change = 0
                    y2_change = -snake_radius
                    x2_change = 0
                elif event.key == pygame.K_DOWN:
                    y0_change = snake_radius
                    x0_change = 0

                    y1_change = snake_radius
                    x1_change = 0

                    y2_change = snake_radius
                    x2_change = 0
        if (x0 < 0 or y0 < 0 or x0 > 691 or y0 > 691):
            game_over = True
            game_restart = True

        x0 += x0_change
        y0 += y0_change
        x1 += x1_change
        y1 += y1_change
        x2 += x2_change
        y2 += y2_change

        screenMain.fill((67, 255, 68))
        if (k == 13 or k == 5 or k == 17):
            pygame.draw.circle(screenMain, (111, 11, 111), [food_x, food_y], snake_radius - 1)
        else:
            pygame.draw.circle(screenMain, (169, 11, 111), [food_x, food_y], snake_radius - 1)
        snake_new_part_of_body = []
        snake_new_part_of_body.append(x0)
        snake_new_part_of_body.append(y0)
        snake_body.append(snake_new_part_of_body)
        if len(snake_body) > len_snake:
            del snake_body[0]
        if (len(snake_body) > 1):
            for x in snake_body[:-1]:
                if x == snake_new_part_of_body:
                    game_over = True
                    game_restart = True

        for i in range(len(snake_body)):
            pygame.draw.circle(screenMain, color_of_snake, [snake_body[i][0], snake_body[i][1]], snake_radius)
        pygame.draw.circle(screenMain, (255, 255, 255), [x1, y1], 2)
        pygame.draw.circle(screenMain, (255, 255, 255), [x2, y2], 2)
        print_score = pygame.font.Font(None, 37)
        result = print_score.render(str(score), True, (180, 0, 180))
        screenMain.blit(result, (10, 1))

        pygame.display.update()
        if snake_body[0][0] == food_x and snake_body[0][1] == food_y:
            food_x = round(random.randrange(0, widgh - 2 * snake_radius) / snake_radius) * snake_radius
            food_y = round(random.randrange(0, high - 2 * snake_radius) / snake_radius) * snake_radius
            len_snake += 1
            if (k == 13 or k == 5):
                score += 2
            elif (k == 17):
                snake_speed -= 0.30
            else:
                score += 1
                snake_speed += 0.25
            k = random.randrange(0, 21)
            if score > best_result:
                best_result = score
                f = open('result.txt','w')
                f.write(str(best_result))
                f.close()

        clock.tick(snake_speed)
        # Выход из игры:
    pygame.quit()
    quit()


while begin:
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
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
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
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    if (x >= 232 and x <= 282 and y >= 350 and y <= 450):
                        snake_speed = 5
                        start_game = False
                        color = True
                    if (x > 282 and x <= 332 and y >= 350 and y <= 450):
                        snake_speed = 10
                        start_game = False
                        color = True
                    if (x > 332 and x <= 372 and y >= 350 and y <= 450):
                        snake_speed = 13
                        start_game = False
                        color = True
                    if (x > 382 and x <= 432 and y >= 350 and y <= 450):
                        snake_speed = 20
                        start_game = False
                        color = True
                    if (x > 432 and x <= 472 and y >= 350 and y <= 450):
                        snake_speed = 30
                        start_game = False
                        color = True
    while color:
        screenMain.fill((5, 5, 5))
        screenMain.blit(color_image, (257, 400))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    if (x >= 232 and x <= 282 and y >= 350 and y <= 450):
                        game(snake_speed, (255, 0, 0))
                        start_game = False
                        color = False
                        begin = False
                    if (x > 282 and x <= 332 and y >= 350 and y <= 450):
                        game(snake_speed, (0, 128, 255))
                        start_game = False
                        color = False
                        begin = False
                    if (x > 332 and x <= 372 and y >= 350 and y <= 450):
                        game(snake_speed, (255, 255, 0))
                        start_game = False
                        color = False
                        begin = False
                    if (x > 382 and x <= 432 and y >= 350 and y <= 450):
                        game(snake_speed, (24, 3, 171))
                        start_game = False
                        color = False
                        begin = False
                    if (x > 432 and x <= 472 and y >= 350 and y <= 450):
                        game(snake_speed, (120, 54, 69))
                        start_game = False
                        color = False
                        begin = False
pygame.quit()
quit()

import pygame
import random
from src.const import widgh, high, k1_image, color_image
from src.screen import screenMain
from src.func import quit_app, get_snake_color, get_snake_speed
class Game:
    def __init__(self, snake_speed, snake_color):
        with open('src/images/result.txt') as f2:
            self.best_result = int(f2.readline()[::-1])
        self.snake_speed = snake_speed
        self.snake_color = snake_color
        self.score = 0
        self.len_snake = 1
        self.game_continue = True  # выхода из цикла игры
        self.game_over = False
        self.game_restart = False
        self.color_continue = False
        self.x0 = widgh // 2
        self.y0 = high // 2  # начальные координаты головы
        self.snake_body = []
        self.snake_radius = 10
        self.x0_change = 0
        self.y0_change = 0  # переменные, отвечающие за передвижение головы
        self.snake_body_move = [self.x0_change, self.y0_change]
        self.x1 = 346
        self.y1 = 350  # начальные координаты глаза1
        self.x1_change = 0
        self.y1_change = 0  # переменные, отвечающие за передвижение глаза1

        self.x2 = 354
        self.y2 = 350  # начальные координаты глаза2
        self.x2_change = 0
        self.y2_change = 0  # переменные, отвечающие за передвижение глаза2

        self.clock = pygame.time.Clock()
        self.k = random.randrange(1, 21)
        self.food_x = round(random.randrange(0, widgh - 2 * self.snake_radius) / self.snake_radius) * self.snake_radius
        self.food_y = round(random.randrange(0, high - 2 * self.snake_radius) / self.snake_radius) * self.snake_radius

    def process(self):
        while self.game_continue:
            while self.game_over:
                while self.game_restart:
                    screenMain.fill((0, 0, 0))
                    print_gameover = pygame.font.Font(None, 70)
                    result = print_gameover.render('Game over', True, (180, 0, 180))
                    print_best_result = pygame.font.Font(None, 49)
                    f1 = open('src/images/result.txt')
                    k = f1.readline()[::-1]
                    best_result_screen = print_best_result.render('Best Result: ' + k, True, (0, 128, 128))
                    f1.close()
                    print_score = pygame.font.Font(None, 49)
                    score_screen = print_score.render('Your result: ' + str(self.score), True, (200, 200, 200))
                    screenMain.blit(best_result_screen, (299, 10))
                    screenMain.blit(score_screen, (0, 10))
                    screenMain.blit(result, (237, 317))
                    screenMain.blit(k1_image, (257, 400))

                    pygame.display.update()

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            quit_app()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                x, y = pygame.mouse.get_pos()
                                self.snake_speed = get_snake_speed(x, y)
                                self.game_restart = False
                                self.color_continue = True
                while self.color_continue:
                    screenMain.fill((5, 5, 5))
                    screenMain.blit(color_image, (257, 400))

                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            quit_app()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                x, y = pygame.mouse.get_pos()
                                self.snake_color = get_snake_color(x, y)
                                c1 = Game(self.snake_speed, self.snake_color)
                                c1.process()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_continue = False
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.x0_change = -self.snake_radius
                        self.y0_change = 0
                        self.x1_change = -self.snake_radius
                        self.y1_change = 0
                        self.x2_change = -self.snake_radius
                        self.y2_change = 0
                    elif event.key == pygame.K_RIGHT:
                        self.x0_change = self.snake_radius
                        self.y0_change = 0
                        self.x1_change = self.snake_radius
                        self.y1_change = 0
                        self.x2_change = self.snake_radius
                        self.y2_change = 0
                    elif event.key == pygame.K_UP:
                        self.y0_change = -self.snake_radius
                        self.x0_change = 0
                        self.y1_change = -self.snake_radius
                        self.x1_change = 0
                        self.y2_change = -self.snake_radius
                        self.x2_change = 0
                    elif event.key == pygame.K_DOWN:
                        self.y0_change = self.snake_radius
                        self.x0_change = 0

                        self.y1_change = self.snake_radius
                        self.x1_change = 0

                        self.y2_change = self.snake_radius
                        self.x2_change = 0
            if (self.x0 < self.snake_radius or self.y0 < self.snake_radius or self.x0 > widgh - self.snake_radius or self.y0 > high - self.snake_radius):
                self.game_over = True
                self.game_restart = True

            self.x0 += self.x0_change
            self.y0 += self.y0_change
            self.x1 += self.x1_change
            self.y1 += self.y1_change
            self.x2 += self.x2_change
            self.y2 += self.y2_change

            screenMain.fill((67, 255, 68))
            if (self.k == 13 or self.k == 5 or self.k == 17):
                pygame.draw.circle(screenMain, (111, 11, 111), [self.food_x, self.food_y], self.snake_radius - 1)
            else:
                pygame.draw.circle(screenMain, (169, 11, 111), [self.food_x, self.food_y], self.snake_radius - 1)
            snake_new_part_of_body = []
            snake_new_part_of_body.append(self.x0)
            snake_new_part_of_body.append(self.y0)
            self.snake_body.append(snake_new_part_of_body)
            if len(self.snake_body) > self.len_snake:
                del self.snake_body[0]
            if (len(self.snake_body) > 1):
                for x in self.snake_body[:-1]:
                    if x == snake_new_part_of_body:
                        self.game_over = True
                        self.game_restart = True

            for i in range(len(self.snake_body)):
                pygame.draw.circle(screenMain, self.snake_color, [self.snake_body[i][0], self.snake_body[i][1]], self.snake_radius)
            pygame.draw.circle(screenMain, (255, 255, 255), [self.x1, self.y1], 2)
            pygame.draw.circle(screenMain, (255, 255, 255), [self.x2, self.y2], 2)
            print_score = pygame.font.Font(None, 37)
            result = print_score.render(str(self.score), True, (180, 0, 180))
            screenMain.blit(result, (10, 1))

            pygame.display.update()
            if self.snake_body[0][0] == self.food_x and self.snake_body[0][1] == self.food_y:
                self.food_x = round(random.randrange(self.snake_radius, widgh - 2 * self.snake_radius) / self.snake_radius) * self.snake_radius
                self.food_y = round(random.randrange(self.snake_radius, high - 2 * self.snake_radius) / self.snake_radius) * self.snake_radius
                self.len_snake += 1
                if (self.k == 13 or self.k == 5):
                    self.score += 2
                elif (self.k == 17):
                    self.snake_speed -= 0.30
                else:
                    self.score += 1
                    self.snake_speed += 0.25
                self.k = random.randrange(0, 21)
                if self.score > self.best_result:
                    self.best_result = self.score
                    f = open('src/images/result.txt', 'w')
                    f.write(str(self.best_result))
                    f.close()

            self.clock.tick(self.snake_speed)
            # Выход из игры:
        pygame.quit()
        quit()

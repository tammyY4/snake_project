import pygame


def quit_app():
    pygame.quit()
    quit()

def get_snake_color(x: int, y: int):
    if (x >= 232 and x <= 282 and y >= 350 and y <= 450):
        return (255, 0, 0)
    if (x > 282 and x <= 332 and y >= 350 and y <= 450):
        return (0, 128, 255)
    if (x > 332 and x <= 372 and y >= 350 and y <= 450):
        return (255, 255, 0)
    if (x > 382 and x <= 432 and y >= 350 and y <= 450):
        return (24, 3, 171)
    if (x > 432 and x <= 472 and y >= 350 and y <= 450):
        return (120, 54, 69)


def get_snake_speed(x: int, y: int):
    if (x >= 232 and x <= 282 and y >= 350 and y <= 450):
        return 5
    if (x > 282 and x <= 332 and y >= 350 and y <= 450):
        return 10
    if (x > 332 and x <= 372 and y >= 350 and y <= 450):
        return 13
    if (x > 382 and x <= 432 and y >= 350 and y <= 450):
        return 20
    if (x > 432 and x <= 472 and y >= 350 and y <= 450):
        return 30

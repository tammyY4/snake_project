# Иницилизация PyGame
import pygame
from src.const import widgh, high

pygame.init()

screenMain = pygame.display.set_mode((widgh, high))
pygame.display.set_caption("My Snake")
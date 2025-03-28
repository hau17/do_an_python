import pygame

pygame.init()

# Màn hình
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
FPS = 60
TILE_SIZE = 40
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Font chữ
FONT = pygame.font.SysFont('Bauhaus 93', 70)
FONT_SCORE = pygame.font.SysFont('Bauhaus 93', 30)

# Game State
GAME_OVER = 0
MAIN_MENU = True
LEVEL = 3
MAX_LEVELS = 7
SCORE = 0
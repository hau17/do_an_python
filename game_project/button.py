import pygame
from pygame.locals import *

class Button():
    def __init__(self, x, y, image_filename):
        self.image = pygame.image.load(image_filename)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self, screen):
        screen.blit(self.image, self.rect)
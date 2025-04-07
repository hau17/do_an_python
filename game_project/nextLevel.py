import pygame
from pygame.locals import *
from settings import TILE_SIZE

class Nexlevel(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/img/next.png")
        self.image = pygame.transform.scale(self.image,(TILE_SIZE,TILE_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

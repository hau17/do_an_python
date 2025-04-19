import pygame
from pygame.locals import *
from settings import TILE_SIZE
class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/img/coin.png",)
        self.image = pygame.transform.scale(self.image, (TILE_SIZE-20, TILE_SIZE-20))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
import pygame
from pygame.locals import *

class Button():
    def __init__(self, x, y, image_filename):
        self.image = pygame.image.load(image_filename)
        self.image = pygame.transform.scale(self.image, (100, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # self.clicked = False
        self.status =False
    def draw(self, screen):
        self.status=False
        pos= pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1:
                self.status = True
                # self.clicked = True
            # if pygame.mouse.get_pressed()[0]==0:
            #     self.clicked = False
        screen.blit(self.image, self.rect)
        return self.status
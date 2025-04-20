import pygame
from pygame.locals import *
from settings import TILE_SIZE
import settings
from world import World, coin_group
class Player():
    def __init__(self, x, y, world, enemy_group,next_group):
        self.reset(x, y, world, enemy_group,next_group)
    def reset(self, x, y, world, enemy_group,next_group):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        self.world =world
        self.enemy_group= enemy_group
        self.next_group = next_group
        self.alive= True
        self.next_level = False
        for i in range(1,5):
            image_right = pygame.image.load(f'assets/img/guy{i}.png')
            image_right = pygame.transform.scale(image_right, (30, 70))
            image_left = pygame.transform.flip(image_right, True, False)
            self.images_right.append(image_right)
            self.images_left.append(image_left)
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y= y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        #van toc khi nhay
        self.vel_y = 0
        self.jumeped = False
        self.direction = 0
        # thuộc tính xác định có đang nhảy không
        self.in_air = True
    def update(self):
        global SCORE
        self.next_level = False
        if self.alive == True:
            dx,dy=0,0
            walk_cooldown = 20
            #lay su kien 
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] and self.jumeped==False and self.in_air == False:
                #đang ở dưới nhưng thật ra y đang max, nên âm là nhảy
                self.vel_y -= 15
                self.jumeped = True
            if  key[pygame.K_SPACE] ==False:
                self.jumeped = False
            if key[pygame.K_LEFT] or key[pygame.K_a]:
                self.direction = -1
                dx -= 5
                self.counter +=4
            if key[pygame.K_RIGHT] or key[pygame.K_d]:
                self.direction = 1
                dx += 5
                self.counter +=4

            #update animation
            
            if self.counter > walk_cooldown:
                self.counter = 0
                self.index +=1
                if (self.index >= len(self.images_right)):
                    self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]

            #them trong luc
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            dy+=self.vel_y
            
            self.in_air = True
            #kiem tra va cham
            for tile in self.world.tile_list:
                if tile[1].colliderect(self.rect.x, self.rect.y + 1, self.width, self.height):
                    self.in_air = False
                if tile[1].colliderect(self.rect.x ,self.rect.y + dy,self.width,self.height):
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0

                if tile[1].colliderect(self.rect.x +dx ,self.rect.y ,self.width,self.height):
                    dx = 0
            if pygame.sprite.spritecollide(self, self.enemy_group, False):
                self.alive = False
                self.image = pygame.transform.scale(pygame.image.load("assets/img/ghost.png"),(TILE_SIZE,TILE_SIZE))
            if pygame.sprite.spritecollide(self, self.next_group, False):
                self.next_level = True
            if pygame.sprite.spritecollide(self,coin_group,True):
                settings.SCORE+=1

            #update vi tri nhan vat
            self.rect.x += dx
            self.rect.y += dy

    def draw(self, screen):
        # ve ra man hinh
        screen.blit(self.image, self.rect)
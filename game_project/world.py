import pygame
#goi event nhanh hon
from pygame.locals import *
from settings import TILE_SIZE

from lava import Lava
from enemy import Enemy
from nextLevel import Nexlevel
from levels import *
enemy_group = pygame.sprite.Group()
next_group = pygame.sprite.Group()
class World():
    def __init__(self,data):
        self.tile_list=[]
        dat_img=pygame.image.load('assets/img/dirt.png')
        dat_img = pygame.transform.scale(dat_img, (TILE_SIZE, TILE_SIZE))
        row_count = 0
        for row in data:
            col_count =0
            for col in row:
                if col==1:
                    img_rect = dat_img.get_rect()
                    img_rect.x = col_count*TILE_SIZE
                    img_rect.y = row_count*TILE_SIZE
                    self.tile_list.append((dat_img, img_rect))
                if col==2:
                    lava= Lava(col_count*TILE_SIZE,row_count*TILE_SIZE)
                    enemy_group.add(lava)
                if col==3:
                    enemy= Enemy(col_count*TILE_SIZE,row_count*TILE_SIZE)
                    enemy_group.add(enemy)
                if col==4:
                    nextLevel = Nexlevel(col_count*TILE_SIZE,row_count*TILE_SIZE)
                    next_group.add(nextLevel)
                col_count+=1
            row_count+=1
    def draw(self, screen):
        for data in self.tile_list:
            screen.blit(data[0],data[1])
world_data = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
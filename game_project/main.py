import pygame
#goi event nhanh hon
from pygame.locals import *
# //fn bat dau tro choi
from settings import SCREEN_WIDTH, SCREEN_HEIGHT,FPS,TILE_SIZE
from player import Player
from world import World, world_data,enemy_group,next_group
from button import Button
from levels import level
pygame.init()
TILE_SIZE = TILE_SIZE
clock = pygame.time.Clock()
#hien thi cua so game
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
#ten cua so game
pygame.display.set_caption('Game wibu')
# def draw_grid():
# 	for line in range(0, 20):
# 		pygame.draw.line(screen, (255, 255, 255), (0, line * TILE_SIZE), (SCREEN_WIDTH, line * TILE_SIZE))
# 		pygame.draw.line(screen, (255, 255, 255), (line * TILE_SIZE, 0), (line * TILE_SIZE, SCREEN_HEIGHT))

#menu chơi hoặc thoát
menu =True
#level ban đầu
level_now = 0
level_group = pygame.sprite.Group()
#load_img
bg_img = pygame.image.load('assets/img/dark_bg.png')
bg_img = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

def load_level(cap):
    if cap < len(level):
        world = World(level[cap])
        return world
    else:
        return None
        
world = load_level(level_now)
player = Player(40, SCREEN_HEIGHT - 40- 70-100,world, enemy_group,next_group)
restart_button = Button((SCREEN_WIDTH //2) +200, SCREEN_HEIGHT //2, "assets/img/restart_btn.png")
start_button = Button((SCREEN_WIDTH //2 ) + 200, SCREEN_HEIGHT //2, "assets/img/start_btn.png")
exit_button = Button((SCREEN_WIDTH //2 ) -280 , SCREEN_HEIGHT //2, "assets/img/exit_btn.png")
#biến chạy game
run = True

while run:
    clock.tick(FPS)
    #set hinh anh giao dien
    screen.blit(bg_img, (0, 0))
    # draw_grid()
    if menu:
        if start_button.draw(screen):
            menu = False
        if exit_button.draw(screen):
            run = False
    else:
        world.draw(screen)
        enemy_group.update()
        enemy_group.draw(screen)
        next_group.draw(screen)

        player.update()
        player.draw(screen)
        if not player.alive:    
            pygame.display.update()
            if restart_button.draw(screen):
                enemy_group.empty()
                next_group.empty()
                level_now = 0
                world= load_level(level_now)
                if world:
                    player = Player(40, SCREEN_HEIGHT - 40- 70-100,world, enemy_group, next_group)
                else:
                    font = pygame.font.Font('assets/font/Pixellettersfull.ttf', 50)
                    text = font.render("YOU WIN", True, (255, 255, 255))
                    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                    screen.blit(text, text_rect)
                    pygame.display.update()
                    pygame.time.delay(2000)
                    run = False
            if exit_button.draw(screen):
                run = False
        if player.next_level:
            level_now += 1
            player.next_level = False  
            enemy_group.empty()
            next_group.empty()
            world = load_level(level_now)
            player = Player(40, SCREEN_HEIGHT - 40 - 70 - 100, world, enemy_group, next_group)
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
    pygame.display.update()
pygame.quit()

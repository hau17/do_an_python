import pygame
#goi event nhanh hon
from pygame.locals import *
# //fn bat dau tro choi
from settings import SCREEN_WIDTH, SCREEN_HEIGHT,FPS,TILE_SIZE
from player import Player
from world import World, world_data,hazard_group
from button import Button
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

#load_img
bg_img = pygame.image.load('assets/img/dark_bg.png')
bg_img = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

world = World(world_data)
player = Player(40, SCREEN_HEIGHT - 40- 70-100,world, hazard_group)
restart_button = Button(SCREEN_WIDTH //2, SCREEN_HEIGHT //2, "assets/img/restart_btn.png")
run = True
while run:
    clock.tick(FPS)
    #set hinh anh giao dien
    screen.blit(bg_img, (0, 0))
    # draw_grid()
    world.draw(screen)
    hazard_group.update()
    hazard_group.draw(screen)
    player.update()
    player.draw(screen)
    if not player.alive:
        # font = pygame.font.Font(None, 50)
        # text = font.render("Bạn đã chết! Nhấn ESC để thoát", True, (255, 0, 0))
        # screen.blit(text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2))
    
        pygame.display.update()
        # pygame.time.delay(2000)  # Đợi 2 giây rồi thoát
        # run = False
        restart_button.draw(screen)

    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
    pygame.display.update()
pygame.quit()
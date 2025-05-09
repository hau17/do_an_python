import pygame
#goi event nhanh hon
from pygame.locals import *
# //fn bat dau tro choi
from settings import SCREEN_WIDTH, SCREEN_HEIGHT,FPS,TILE_SIZE,FONT_SCORE, WHITE
import settings
from player import Player
from world import World, enemy_group,next_group, coin_group
from button import Button
from levels import level
pygame.init()
dddTILE_SIZE = TILE_SIZE
clock = pygame.time.Clock()
#hien thi cua so game
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
#ten cua so game
pygame.display.set_caption('Game wibu')
#menu chơi hoặc thoát
menu =True
#level ban đầu
level_now = 0
level_group = pygame.sprite.Group()
#load_img
bg_img = pygame.image.load('assets/img/dark_bg.png')
bg_img = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

def draw_text(text, x, y):
    img = FONT_SCORE.render(text, True,WHITE)
    screen.blit(img, (x, y))
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

# Initialize game_won flag
game_won = False

while run:
    clock.tick(FPS)
    screen.blit(bg_img, (0, 0))

    if menu:
        if start_button.draw(screen):
            menu = False
        if exit_button.draw(screen):
            run = False
    elif game_won:
        # Display win screen
        draw_text("YOU WIN", SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 50)
        draw_text("SCORE: " + str(settings.SCORE), SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2)
        if restart_button.draw(screen):
            enemy_group.empty()
            next_group.empty()
            coin_group.empty()
            level_now = 0
            world = load_level(level_now)
            player = Player(40, SCREEN_HEIGHT - 40 - 70 - 100, world, enemy_group, next_group)
            settings.SCORE = 0
            game_won = False  # Reset to start new game
        if exit_button.draw(screen):
            run = False
    else:
        # Normal gameplay
        world.draw(screen)
        coin_group.draw(screen)
        enemy_group.update()
        enemy_group.draw(screen)
        next_group.draw(screen)

        player.update()
        player.draw(screen)

        if not player.alive:
            draw_text("SCORE: " + str(settings.SCORE), SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2)
            if restart_button.draw(screen):
                enemy_group.empty()
                next_group.empty()
                coin_group.empty()
                level_now = 0
                world = load_level(level_now)
                player = Player(40, SCREEN_HEIGHT - 40 - 70 - 100, world, enemy_group, next_group)
                settings.SCORE = 0
            if exit_button.draw(screen):
                run = False
        elif player.next_level:
            level_now += 1
            player.next_level = False
            enemy_group.empty()
            next_group.empty()
            coin_group.empty()
            if level_now >= len(level):  # Win condition
                game_won = True  # Enter win state
            else:
                world = load_level(level_now)
                player = Player(40, SCREEN_HEIGHT - 40 - 70 - 100, world, enemy_group, next_group)
        else:
            draw_text("X" + str(settings.SCORE), 20, 20)

    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

    pygame.display.update()

pygame.quit()
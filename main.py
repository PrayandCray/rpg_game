import pygame
import sys

def player_animation():
    
    player.x += player_x_speed
    player.y += player_y_speed
    if player.left <= 0:
        player.left = 0
    if player.right >= screen_width:
        player.right = screen_width
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

pygame.init()
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('rpg_game')

bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)
player_x_speed = 0
player_y_speed = 0
player = pygame.Rect(screen_width / 2 - 50, screen_height / 2 - 50, 100, 100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_y_speed = -7
            if event.key == pygame.K_s:
                player_y_speed = 7
            if event.key == pygame.K_d:
                player_x_speed = 7
            if event.key == pygame.K_a:
                player_x_speed = -7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_y_speed = 0
            if event.key == pygame.K_s:
                player_y_speed = 0
            if event.key == pygame.K_d:
                player_x_speed = 0
            if event.key == pygame.K_a:
                player_x_speed = 0

    player_animation()

    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)

    pygame.display.flip()
    clock.tick(60)
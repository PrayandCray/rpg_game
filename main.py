import pygame
import sys
from player import *
from settings import *

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('rpg_game')

bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)
player = Player(screen_width / 2 - 50, screen_height / 2 - 50, 100, 100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    player.move(screen_width, screen_height)

    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    text = font.render(f'{player.world_x}, {player.world_y}', True, WHITE, bg_color)
    screen.blit(text, text.get_rect())

    pygame.display.flip()
    clock.tick(60)
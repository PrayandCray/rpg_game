import pygame
import sys


class Player():

    def __init__(self, x, y, width, height, speed=7):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed
        self.world_x = 0
        self.world_y = 0

    def move(self, screen_width, screen_height):
        
        keys=pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed
        
        self.rect.x = self.x
        self.rect.y = self.y
        
        if self.rect.left <= 0:
            self.rect.right = screen_width - 1
            self.world_x -= 1
        if self.rect.right >= screen_width:
            self.rect.left = 1
            self.world_x += 1
        if self.rect.top <= 0:
            self.rect.bottom = screen_height - 1
            self.world_y += 1
        if self.rect.bottom >= screen_height:
            self.world_y -= 1
            self.rect.top = 1
        self.x = self.rect.x
        self.y = self.rect.y
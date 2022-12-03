import pygame


from fireball import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rocket = pygame.image.load('graphics/rocket/rocket1.png').convert_alpha()
        self.rect = self.rocket.get_rect(center = (400, 200))
        self.image = self.rocket
        self.speed = 5
    
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.left >= 0:
            self.rect.x -= self.speed
        if keys[pygame.K_s] and self.rect.bottom <= 800:
            self.rect.y += self.speed
        if keys[pygame.K_w] and self.rect.top >= 0:
            self.rect.y -= self.speed
        if keys[pygame.K_d] and self.rect.right <= 500:
            self.rect.x += self.speed


    def update(self):
        self.player_input()

    def laser(self):
        return Laser(self.rect.centerx, self.rect.centery)
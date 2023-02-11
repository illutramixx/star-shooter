import random
import pygame
from pygame.math import Vector2
import math

class Asteroid(pygame.sprite.Sprite):
    MIN_SPEED = 1
    MAX_SPEED = 3


    def __init__(self):
        super().__init__()


        ast_big = pygame.image.load('graphics/asteroids/asteroid_big.png').convert_alpha()
        ast_medium = pygame.image.load('graphics/asteroids/asteroid_medium.png').convert_alpha()
        ast_small = pygame.image.load('graphics/asteroids/asteroid_small.png').convert_alpha()
        self.asteroids = [ast_big,ast_medium,ast_small]
        self.asteroids_index = random.randrange(2)

        self.x = random.randrange(500)
        self.y = random.randrange(500)
        self.image = self.asteroids[self.asteroids_index]
        self.rect = self.image.get_rect(center = (self.x, self.y))


        self.speed = random.randint(1, 3)
        self.angle = random.randrange(0, 360)


    def update(self):
        self.rect.x +=  self.speed * math.cos(self.angle)
        self.rect.y += self.speed  * math.sin(self.angle)
  


       
       
       
        

   

    def destroy(self):
       if self.counter > 100:
        self.kill()
        self.counter = 0
    


import random
import pygame
from pygame.math import Vector2

class Asteroid(pygame.sprite.Sprite):


    def __init__(self, index):
        super().__init__()


        ast_big = pygame.image.load('graphics/asteroids/asteroid_big.png').convert_alpha()
        ast_medium = pygame.image.load('graphics/asteroids/asteroid_medium.png').convert_alpha()
        ast_small = pygame.image.load('graphics/asteroids/asteroid_small.png').convert_alpha()
        self.asteroids = [ast_big,ast_medium,ast_small]
        self.asteroids_index = index



        self.image = self.asteroids[self.asteroids_index]
        self.rect = self.image.get_rect(center = (random.randrange(500), random.randrange(800)))
  

   # def update(self):
       
        #self.destroy()
        

    # def move(self):
    #     self.position = self.position + self.velocity
    
    # def collision(self, other):
    #     distance = self.position.distance_to(other.position)
    #     return distance < self.radius + other.radius

    def destroy(self):
       if self.counter > 100:
        self.kill()
        self.counter = 0
    


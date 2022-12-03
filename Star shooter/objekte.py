import pygame
from pygame.math import Vector2

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, index, pos, sprite, velo):
        super().__init__()


        ast_big = pygame.image.load('graphics/asteroids/asteroid_big.png').convert_alpha()
        ast_medium = pygame.image.load('graphics/asteroids/asteroid_medium.png').convert_alpha()
        ast_small = pygame.image.load('graphics/asteroids/asteroid_small.png').convert_alpha()
        self.asteroids = [ast_big,ast_medium,ast_small]
        self.asteroids_index = 0

        self.image = self.asteroids[self.asteroids_index]
        self.rect = self.image.get_rect(center = pos)

        self.position = Vector2(pos)
        self.sprite = sprite
        self.radius = sprite.get_width() / 2
        self.velovity = Vector2(velo)

   # def spawning(self):
        

    def draw(self, surface):
        blit_position = self.position - Vector2(self.radius)
        surface.blit(self.sprite, blit_position)

    def move(self):
        self.position = self.position + self.velocity
    
    def collision(self, other):
        distance = self.position.distance_to(other.position)
        return distance < self.radius + other.radius
    


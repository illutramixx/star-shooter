import pygame

class Astronaut(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/astronaut/astronaut.png').convert_alpha()
        self.rect = self.image.get_rect(center = (300,400))
       

    def rotate(self):
        old_rect = self.image.get_rect()
        new_image =  pygame.transform.rotate(self.image, 10)
        new_rect = old_rect.copy()
        new_rect.center = new_image.get_rect().center
        new_image = new_image.subsurface(new_rect).copy()
        self.image = new_image
        self.rect = new_rect



    def update(self):
        self.rect.y -= 0
        #self.rotate()
        if self.rect.y <= -100:
            self.kill()
    

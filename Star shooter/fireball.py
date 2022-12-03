import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.image = pygame.image.load('graphics/laser/laser2.png').convert_alpha()
        self.rect = self.image.get_rect(center = (x_pos,y_pos-6))
       

    def update(self):
        self.rect.y -= 10
        self.destroy()
        

    def destroy(self):
        if self.rect.y <= -100:
            self.kill()


from sys import exit
from pygame.math import Vector2
import math

import pygame

from spieler import Player
from astronaut import Astronaut
from objekte import Asteroid

running = False
pygame.init()
screen = pygame.display.set_mode((500, 800)) # weite, höhe
pygame.display.set_caption('Star Destroyer')
clock = pygame.time.Clock()

#test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

background_surf = pygame.image.load('graphics/background.png')
background_surf = pygame.transform.scale(background_surf, (500,800))
background_rect = background_surf.get_rect(center = (250, 400))
 #start screen
start_surf = pygame.image.load('graphics/start.png')
start_surf = pygame.transform.scale(start_surf, (500,800))
start_rect = start_surf.get_rect(center = (250, 400))
    
title_surf = pygame.image.load('graphics/title.png').convert_alpha()
title_surf = pygame.transform.scale(title_surf, (300,150))
title_rect = title_surf.get_rect(center = (250, 600))


rocket_surf = pygame.image.load('graphics/rocket/rocket2.png')
rocket_rect = rocket_surf.get_rect(center = (200, 400))
pygame.display.set_icon(pygame.image.load('graphics/icon.png'))

astro_surf = pygame.image.load('graphics/astronaut/astronaut.png')
astro_rect = astro_surf.get_rect(center = (300,300))

player = Player()
player_g = pygame.sprite.GroupSingle()
player_g.add(player)
life = 3

astronaut = pygame.sprite.Group()
astronaut.add(Astronaut())

asteroid_group = pygame.sprite.Group()
asteroid_group.add(Asteroid())

laser_group = pygame.sprite.Group()

radius = 150
angle = math.radians(45)
omega = 0.01 # angular velocity
center_rot_x = 250
center_rot_y = 300
rocket_angle = 0
rocket_calc = [radius, angle, omega, center_rot_x, center_rot_y, rocket_angle]


def collision_player_asteroid(life):  # Collision Between Player and Asteroid
    if pygame.sprite.spritecollide(player_g.sprite, asteroid_group, False):
        asteroid_group.empty()
        return life -1
    else: return life




def rocket_circle(rocket_calc):
    radius = rocket_calc[0]
    angle = rocket_calc[1]
    omega = rocket_calc[2]
    center_rot_x = rocket_calc[3]
    center_rot_y = rocket_calc[4]
    rocket_angle = rocket_calc[5]
    rocket_angle += 0.65

    x = center_rot_x + radius * math.cos(angle)
    y = center_rot_y -  radius * math.sin(angle)
    
    screen.blit(pygame.transform.rotozoom(rocket_surf, rocket_angle, 1), rocket_surf.get_rect(center = (x, y)))
    angle = angle + omega
    x = x + radius * omega * math.cos(angle + math.pi/2)
    y = y - radius * omega * math.sin(angle + math.pi/2)

    return [radius,angle, omega, center_rot_x, center_rot_y , rocket_angle]

#Lebensanzeige vom Spieler 

#heart_surf = pygame.image.load('graphics/heart.png')
def life_player():
    life_txt = 'graphics/heart' + str(life) + '.png'
    heart_surf = pygame.image.load(life_txt)
    heart_rect = start_surf.get_rect(center = (670, 1170))
    screen.blit(heart_surf, heart_rect)
    print('lol')




timer_interval = 1000 # 1sec
timer_event_id = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event_id, timer_interval)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 
        if running:
           # rocket_rect = rocket_surf.get_rect(center = (200, 400))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    laser_group.add(player.laser())
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == timer_event_id:
                #do something ->A spawn Asteroid
                asteroid_group.add(Asteroid())
                

        else: 
            #rocket_rect = rocket_surf.get_rect(center = (400, 200))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
                running = True
        

        
    if running:
        
        screen.blit(background_surf, background_rect)
        screen.blit(rocket_surf, rocket_rect)
        screen.blit(astro_surf, astro_rect)

        
        life_player()

        asteroid_group.draw(screen)
        player_g.draw(screen)
        laser_group.draw(screen)
        astronaut.draw(screen)

        player_g.update()
        laser_group.update()
        astronaut.update()
        asteroid_group.update()
       
        life = collision_player_asteroid(life)
        if(life <= 0): running = False
        
    else:
        screen.blit(start_surf, start_rect)
        screen.blit(title_surf, title_rect)
        rocket_calc = rocket_circle(rocket_calc)

    pygame.display.update()
    clock.tick(60) # loop nicht schnelles als 60*mal pro sec





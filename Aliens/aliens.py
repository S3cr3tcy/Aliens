import pygame
from redlaser import Red_Laser
import random

class Aliens(pygame.sprite.Sprite):
    def __init__(self,x,y,aliens_group):
        super().__init__()
        self.image=pygame.image.load("pictures_nanocillium_game/bacteria.png")
        self.image=pygame.transform.scale(self.image,(40,40))
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.velocity=1
        self.direction=1
        self.aliens_group=aliens_group
    def update(self,red_laser_group,aliens_group):
        self.rect.x=self.rect.x+(self.velocity*self.direction)
        alien_check=random.randint(1,1000)
        if alien_check>997 and len(red_laser_group)<20:
            Red_Laser(self.rect.centerx,self.rect.bottom,red_laser_group)
        if self.rect.x<=0 or self.rect.x>=600:
            for alien in aliens_group:
                alien.direction*=-1
                alien.rect.y+=1
        
import pygame
from redlaser import Red_Laser
import random

class Aliens(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=pygame.image.load("pictures_nanocillium_game/bacteria.png")
        self.image=pygame.transform.scale(self.image,(40,40))
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
    def shoot(self,shoot_check,red_laser_group):
        alien_check=random.randint(1,60)
        if alien_check == shoot_check:
            Red_Laser(self.rect.centerx,self.rect.bottom,red_laser_group)
import pygame
from greenlaser import Green_Laser
WIDTH=800
HEIGHT=600


class Spaceship(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("pictures_nanocillium_game/nanobot1.png")
        self.image=pygame.transform.scale(self.image,(50,50))
        self.rect=self.image.get_rect()
        self.rect.centerx=WIDTH//2 + 25
        self.rect.bottom=HEIGHT
    def move(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                self.rect.x+=50
            if event.key==pygame.K_LEFT:
                self.rect.x-=50
    def shoot(self,green_laser_group):
        Green_Laser(self.rect.x,self.rect.top,green_laser_group)
        


import pygame
from laser import Green_Laser
WIDTH=800
HEIGHT=600


class Spaceship(pygame.sprite.Sprite):

    def __init__(self):
        self.image=pygame.image.load("pictures_nanocillium_game/nanobot1.png")
        self.image=pygame.transform.scale(self.image,(100,100))
        self.rect=self.image.get_rect()
        self.rect.centerx=WIDTH//2
        self.rect.bottom=HEIGHT
    def move(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                self.rect.x+=20
            if event.key==pygame.K_LEFT:
                self.rect.x-=20
    def shoot(self):
        Green_Laser(self.rect.x,self.rect.y)


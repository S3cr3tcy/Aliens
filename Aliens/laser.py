import pygame

class Green_Laser(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.image=pygame.image.load("pictures_nanocillium_game/green_laser.png")
        self.rect=self.image.get_rect()
        self.rect.centerx=x
        self.rect.centery=y
    def update(self):
        self.rect.y-=10
        if self.rect.y<0:
            self.kill()
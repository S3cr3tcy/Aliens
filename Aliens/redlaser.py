import pygame

class Red_Laser(pygame.sprite.Sprite):
    def __init__(self,x,y,red_laser_group):
        super().__init__()
        self.image=pygame.image.load("pictures_nanocillium_game/red_laser.png")
        self.rect=self.image.get_rect()
        self.rect.centerx=x+20
        self.rect.centery=y
        red_laser_group.add(self)
    def update(self):
        self.rect.y+=1
        if self.rect.y>600:
            self.kill()
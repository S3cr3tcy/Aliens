import pygame
from spaceship import Spaceship
from aliens import Aliens
import random


pygame.init()

HEIGHT=600
WIDTH=800
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Aliens")

gameloop=True

nanobot=Spaceship()
nanobot_group=pygame.sprite.Group()
nanobot_group.add(nanobot)

green_laser_group=pygame.sprite.Group()

aliens_group=pygame.sprite.Group()

red_laser_group=pygame.sprite.Group()

for i in range(5):
    for o in range(12):
        x=o*50+100
        y=i*50
        alien=Aliens(x,y)
        aliens_group.add(alien)


while gameloop:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop=False
        nanobot.move(event)
        if event.type == pygame.KEYDOWN:
          if event.key==pygame.K_SPACE: 
              nanobot.shoot(green_laser_group)

    nanobot_group.draw(screen)
    green_laser_group.update()
    green_laser_group.draw(screen)
    
    shoot_check=random.randint(1,60)
    aliens_group.shoot(shoot_check,red_laser_group)
    aliens_group.draw(screen)
    red_laser_group.update()
    red_laser_group.draw(screen)
    pygame.display.flip()
pygame.quit()
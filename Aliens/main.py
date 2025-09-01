import pygame
from spaceship import Spaceship

pygame.init()

HEIGHT=600
WIDTH=800
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Aliens")

gameloop=True

nanobot=Spaceship()
nanobot_group=pygame.sprite.Group()
nanobot_group.add(nanobot)



while gameloop:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop=False
        nanobot.move(event)
        if event.type == pygame.KEYDOWN:
          if event.key==pygame.K_SPACE: 
              nanobot.shoot()
    nanobot.draw(screen)
    pygame.display.flip()
pygame.quit()
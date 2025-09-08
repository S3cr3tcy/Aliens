import pygame
from spaceship import Spaceship
from aliens import Aliens

pygame.init()

HEIGHT=600
WIDTH=800
FPS=60
clock=pygame.time.Clock()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Aliens")

font=pygame.font.SysFont("Arial",20)

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
        y=i*50+50
        alien=Aliens(x,y,aliens_group)
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
    
    aliens_group.update(red_laser_group,aliens_group)
    aliens_group.draw(screen)
    red_laser_group.update()
    red_laser_group.draw(screen)

    scoretext=font.render(f"Score: {nanobot.score}",True,"white")
    scorerect=scoretext.get_rect(centerx=WIDTH/2,top=20)
    screen.blit(scoretext,scorerect)

    lifetext=font.render(f"Lives: {nanobot.lives}",True,"white")
    liferect=lifetext.get_rect(centerx=WIDTH-50,top=20)
    screen.blit(lifetext,liferect)

    pygame.draw.line(screen,"white",(0,50),(WIDTH,50),4)
    pygame.draw.line(screen,"white",(0,HEIGHT-50),(WIDTH,HEIGHT-50),4)

    if pygame.sprite.groupcollide(aliens_group,green_laser_group,True,True):
        nanobot.score+=100
    if pygame.sprite.groupcollide(nanobot_group,red_laser_group,False,True):
        nanobot.lives-=1
        if nanobot.lives==0:
            gameloop=False

    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()
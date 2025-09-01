import pygame

pygame.init()

HEIGHT=600
WIDTH=800
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Paddle")

paddle_x=500
paddle_y=400
paddle_size_x=100
paddle_size_y=20
paddle_position=(paddle_x,paddle_y,paddle_size_x,paddle_size_y)


gameloop=True

class Paddle:
    
    def __init__(self):
        self.rect=pygame.Rect(paddle_position)

    def move(self,event):
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                self.rect.x+=20
            if event.key==pygame.K_LEFT:
                self.rect.x-=20

paddle=Paddle()

while gameloop:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameloop=False
        paddle.move(event)
    screen.fill("black")
    paddle=pygame.draw.rect(screen, "white", paddle_position)
    pygame.display.flip()
pygame.quit()
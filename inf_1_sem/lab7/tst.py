import pygame
import math
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 900))

steps_of_time_number = 2000

number_of_balls = 3

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]



def new_ball():
    global x, y, r, color
    x = randint(100,700)
    y = randint(100,500)
    r = randint(30,50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)



Vx=1
Vy=1
dt=1
    
    
def move():
    
    global x, y, Vx, Vy, dt
    
    if (x+r>=1200):
        Vx=-Vx
    if (x-r<=0):
        Vx=-Vx
    
    if (y+r>=900):
        Vy=-Vy
    if (y-r<=0):
        Vy=-Vy
    
    x=x+Vx*dt    
    y=y+Vy*dt


def inside():
    mx,my=pygame.mouse.get_pos()
    rtx=mx-x
    rty=my-y
    if math.sqrt(math.pow(rtx,2)+math.pow(rty,2))<=r:
        print('Great!')
        return True
    else:
        print('Oof...')
        return False

pygame.display.update()
clock = pygame.time.Clock()
finished = False



"pool = [ball for i in range (number_of_balls)]"


k=0


while not finished:
    clock.tick(FPS)
    
    new_ball()
    for i in range(steps_of_time_number):
        move()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    finished = True
            if event.type == pygame.QUIT:
                finished = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if inside()==True:
                    k=k+1
                    print("Your score is", k)
                    print()
                else:
                    print("Your score is still", k)
                    print()
        circle(screen, color, (x, y), r)
        pygame.display.update()
        screen.fill(BLACK)

pygame.quit()
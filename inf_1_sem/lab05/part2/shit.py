import pygame 
from random import randint

#color assign part
cr = (255, 0, 0)
cb = (0, 0, 255)
cy = (255, 255, 0)
cg = (0, 255, 0)
cm = (255, 0, 255)
cc = (0, 255, 255)
bl = (0, 0, 0)
wh = (255,255,255)

pl0 = [cr,cb,cy]
pl1 = [cg,cm,cc]

class shit:
    '''
    x - x position
    y - y position
    vx - x axis speed
    vy - y axis speed
    color - color of object
    type - type, if 0 - circle,1 - rect

    xmin - position of left object border
    xmxx - position of right object border
    ymin - position of top object border
    ymxx - position of buttom object border

    r = radius of circle or half of rect side

    R - r**2
    '''

    #intialize starting variables with help of random
    def __init__(self,x,y,vx,vy,r,W,H,skip,type):
        '''
        xm - maximum starting x possition
        ym - maximum starting y possition
        rm - maximum size of the object
        vm - maxim x,y speed of the object
        r = radius of circle or half of rect side
        '''
        #self.spawn = randint(20,300)
        self.spawn = 0
        self.W = W
        self.H = H
        #self.r = randint(r//3,r)
        #self.x = randint(xmin+2*self.r,xmax-2*self.r)
        #self.y = randint(ymin+2*self.r,ymax-2*self.r)
        #self.vx = randint(0,vx)
        #self.vy = randint(0,vy)
        #self.type = randint(0,1)

        self.skip = skip
        self.W = W
        self.H = H
        self.live = 0
        self.r = r
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.type = type

        if self.type == 0:
            self.color = pl0[randint(0,len(pl0)-1)]
            self.spawn = 100
        if self.type == 1:
            self.color = pl1[randint(0,len(pl1)-1)]
            self.spawn = 70

        if self.type == 2:
            self.color = pl1[randint(0,len(pl1)-1)]
            self.spawn = 150

            self.vx = vx/2
            self.vy = vy/2

        self.R = self.r**2

    #calculate some useful properties of an object
    def reass(self):
        '''
        xmin - position of left object border
        xmxx - position of right object border
        ymin - position of top object border
        ymxx - position of buttom object border
        r = radius of circle or half of rect side
        R - r**2
        '''
        self.xmax=self.x +self.r
        self.xmin=self.x - self.r
        self.ymax =self.y +self.r
        self.ymin = self.y-self.r
        self.live+=1

        if self.spawn < 30 and self.type == 0:
            return True
        else:
            return False



    def Draw(self,screen):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.r,0)



        
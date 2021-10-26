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

class target:
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
    def __init__(self,xmin,ymin,xmax,ymax,vx,vy,r,W,H):
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
        self.r = randint(r//3,r)
        self.x = randint(xmin+2*self.r,xmax-2*self.r)
        self.y = randint(ymin+2*self.r,ymax-2*self.r)
        self.vx = randint(0,vx)
        self.vy = randint(0,vy)
        self.type = randint(0,1)
        if self.type == 0:
            self.color = pl0[randint(0,len(pl0)-1)]
        if self.type == 1:
            self.color = pl1[randint(0,len(pl1)-1)]
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

    def Draw(self,screen):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.r,0)

    def Move(self):

        '''
        W,H - screen borders
        vm - maximum and minimum random speed
        '''
        W,H = self.W,self.H
        if self.xmin <= 0:
            self.vx =  - self.vx
        if self.xmax >= W:
            self.vx =  - self.vx
        if self.ymin <= 0:
            self.vy =  - self.vy
        if self.ymax >= H:
            self.vy =  - self.vy


        self.x = self.x+self.vx
        self.y = self.y+self.vy

        
    #calculate object next frame position



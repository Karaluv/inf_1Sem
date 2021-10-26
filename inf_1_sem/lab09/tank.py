import pygame 
from random import randint
import math

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

class tank:
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
    def __init__(self,x,y,vx,vy,r,W,H):
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
        self.r = r
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
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

    def Draw(self,screen,position,power):

        x0,y0 = self.x,self.y
        x,y = position

        power = power + 30

        l = ((x-x0)**2+(y-y0)**2)**0.5
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.r,0)
        #pygame.draw.line(screen,self.color,(x0,y0),((x-x0)/l*power+x0,(y-y0)/l*power+y0),15)

        self.draw_gun(screen,position,power+20)

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

    def draw_gun(self,screen,pos,power):
        an = math.atan2(-1*(pos[1]-self.y), (pos[0]-self.x)) 
        pygame.draw.polygon(screen, self.color, [(self.x + int(5*math.cos(an + 1.57)),self.y - int(5*math.sin(an + 1.57))), 
        (self.x + int(5*math.cos(an - 1.57)),self.y - int(5*math.sin(an - 1.57))), 
        (self.x + int(power*math.cos(an - 0.165)),self.y - int(power*math.sin(an - 0.165))), 
        (self.x + int(power*math.cos(an + 0.165)),self.y - int(power*math.sin(an + 0.165)))]) 
        #if self.f2_on: 
        self.color = (255,0,0)
        #else: 
        #self.color = (128,128,128)
        
    #calculate object next frame position




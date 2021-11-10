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
    def __init__(self,x,y,vx,vy,r,W,H,skip,type):
        '''
        xm - maximum starting x possition
        ym - maximum starting y possition
        rm - maximum size of the object
        vm - maxim x,y speed of the object
        r = radius of circle or half of rect side
        '''
        #self.spawn = randint(20,300)
        self.reload = 0
        self.skip = skip
        self.shell_type = 2
        self.da = 0
        self.spawn = 0
        self.power = 0 
        self.power_up = False
        self.W = W
        self.H = H
        self.r = r
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.type = type
        self.a = 0
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

        if self.reload>0:
            self.reload -= 1

    def Draw(self,screen: pygame.surface,power: int):

        '''
        power = power of the tank
        '''

        x0,y0 = self.x,self.y

        power = self.power + 30

        pygame.draw.circle(screen,self.color,(self.x,self.y),self.r,0)
        #pygame.draw.line(screen,self.color,(x0,y0),((x-x0)/l*power+x0,(y-y0)/l*power+y0),15)

        self.draw_gun(screen,power+20)

    def Move(self):

        '''
        W,H - screen borders
        vm - maximum and minimum random speed
        '''
        W,H = self.W,self.H

        if 20<(self.x+self.vx)<W-20:
            self.x = self.x+self.vx/self.skip

        self.a +=self.da/self.skip


    def draw_gun(self,screen,power):
        '''
        power = power of the tank
        '''

        an = self.a
        pygame.draw.polygon(screen, self.color, [(self.x + int(5*math.cos(an + 1.57)),self.y - int(5*math.sin(an + 1.57))), 
        (self.x + int(5*math.cos(an - 1.57)),self.y - int(5*math.sin(an - 1.57))), 
        (self.x + int(power*math.cos(an - 0.165)),self.y - int(power*math.sin(an - 0.165))), 
        (self.x + int(power*math.cos(an + 0.165)),self.y - int(power*math.sin(an + 0.165)))]) 
        #if self.f2_on: 
        self.color = (255,0,0)
        #else: 
        #self.color = (128,128,128)
        
    #calculate object next frame position




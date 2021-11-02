import pygame 
from random import randint
from shit import shit
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

class shell(shit):
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
    def __init__(self,x,y,vx,vy,r,W,H,skip,type,tankN):
        '''
        xm - maximum starting x possition
        ym - maximum starting y possition
        rm - maximum size of the object
        vm - maxim x,y speed of the object
        r = radius of circle or half of rect side
        '''
        #self.spawn = randint(20,300)
        self.tankN = tankN
        self.W = W
        self.H = H
        self.live = 0
        self.r = r
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.type = type
        self.skip = skip
        if self.type == 0:
            self.color = pl0[randint(0,len(pl0)-1)]
            self.spawn = 100*skip*2
        if self.type == 1:
            self.color = pl1[randint(0,len(pl1)-1)]
            self.spawn = 70*2*skip

        if self.type == 2:
            self.color = pl1[randint(0,len(pl1)-1)]
            self.spawn = 150*skip


        self.R = self.r**2

    #calculate some useful properties of an object

    def Move(self):

        '''
        W,H - screen borders
        vm - maximum and minimum random speed
        '''
        W,H = self.W,self.H
        k = 0.25

        l = ((self.x-W//2)**2+(self.y-H//2)**2)**0.5
        l = l/300

        if l>10:
            if self.type == 0 or self.type == 1:
                self.vx += 10/l*(-self.x+W//2)/self.skip/10
                self.vy += 10/l*(-self.y + H//2)/self.skip/10
            if self.type == 2:
                self.vx += 10/l*(self.x-W//2)/self.skip/10
                self.vy += 10/l*(self.y - H//2)/self.skip/10
        
        if self.xmin <= 0:
            self.vx =  - self.vx*k
            self.x = self.r
        if self.xmax >= W:
            self.vx =  - self.vx*k
            self.x = W - self.r
        if self.ymin <= 0:
            self.vy =  - self.vy*k
            self.y = self.r
        if self.ymax >= H:
            self.vy =  - self.vy*k
            self.y = H - self.r


        self.x = self.x+self.vx/self.skip
        self.y = self.y+self.vy/self.skip

        
    #calculate object next frame position


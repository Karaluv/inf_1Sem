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

class target(shit):

    def __init__(self,x,y,vx,vy,r,W,H,skip,type):
        super().__init__(x,y,vx,vy,r,W,H,skip,type)
        self.type = randint(0,1)



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

        l = (self.x-W//2)**2+(self.y-H//2)**2

        if self.type == 0 or self.type == 1:
            if l>10:
                self.vx += 100/l*(-self.x+W//2)/self.skip
                self.vy += 100/l*(-self.y + H//2)/self.skip



        self.x = self.x+self.vx/self.skip
        self.y = self.y+self.vy/self.skip



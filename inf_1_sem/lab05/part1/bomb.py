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

class bomb(shit):

    def __init__(self,x,y,vx,vy,r,W,H,skip):
        super().__init__(x,y,vx,vy,r,W,H,skip,0)
        self.color = (255,255,255)


    def Move(self):

        '''
        W,H - screen borders
        vm - maximum and minimum random speed
        '''
        x,y = self.x,self.y
        W,H = self.W,self.H
        if self.xmin <= 0:
            self.vx =  - self.vx
            return True
        if self.xmax >= W:
            self.vx =  - self.vx
            return True
        if self.ymin <= 0:
            self.vy =  - self.vy
            return True
        if self.ymax >= H:
            self.vy =  - self.vy
            return True

        if y>W-y:
            self.vy += 0.01/self.skip
        if y<W-y:
            self.vy += -0.01/self.skip



        self.x = self.x+self.vx/self.skip
        self.y = self.y+self.vy/self.skip




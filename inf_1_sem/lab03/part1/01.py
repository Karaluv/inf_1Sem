import pygame as pg
from pygame.draw import * 
import numpy as np
 
pg.init() 
 
FPS = 30 
screen = pg.display.set_mode((927, 769)) 
f1 = pg.Surface((927, 769))
f2 = pg.Surface((927, 769))
myfont = pg.font.SysFont('arial', 60)
textsurface = myfont.render('Python sucks!!!', False, (0, 0, 0))



bl = (0,0,0)
wh = (255,255,255,255)

f1.fill(wh)


ye = (255,212,42,255)
gr =(0,128,0,255)
ar =(255,102,0,255)
re = (255,42,42,255)
pu = (212,42,255,255)
br = (120,68,33,255)
go = (128,179,255,255)
se = (190,200,183,255)
sc = (233,198,175,255)

lg = (127,255,42,255)


def trig(f,x,y,l,a,cl):
     pg.draw.polygon(f,cl,([x,y],[int(x+l*np.cos(a)),int(y-l*np.sin(a))],[int(x+l*np.cos(a+1.047)),int(y - np.sin(a+1.047)*l)]))
     pg.draw.polygon(f,bl,([x,y],[int(x+l*np.cos(a)),int(y-l*np.sin(a))],[int(x+l*np.cos(a+1.047)),int(y - np.sin(a+1.047)*l)]),1)


def man(s,ck,cg,cm,cv):



    #body
    pg.draw.circle(s,cm,(447,769),246,0)

    pg.draw.polygon(s,ck,([669,558],[700,573],[854,124],[823,124]),0)
    pg.draw.polygon(s,ck,([202,574],[233,563],[103,116],[71,126]),0)

    pg.draw.ellipse(s,ck,(42,40,85,95),0)
    pg.draw.ellipse(s,ck,(790,36,87,110),0)
    pg.draw.ellipse(s,wh,(42,40,85,95),1)
    pg.draw.ellipse(s,wh,(790,36,87,110),1)


    pg.draw.polygon(s,cm,([174,578],[258,531],[316,600],[272,690],[185,676]),0)
    pg.draw.polygon(s,bl,([174,578],[258,531],[316,600],[272,690],[185,676]),1)

    pg.draw.polygon(s,cm,([585,607],[642,531],[724,568],[720,668],[636,692]),0)
    pg.draw.polygon(s,bl,([585,607],[642,531],[724,568],[720,668],[636,692]),1)

    #head
    pg.draw.ellipse(s,ck,(222,168,455,463),0)
    pg.draw.ellipse(s,cg,(327,316,99,87),0)
    pg.draw.ellipse(s,bl,(327,316,99,87),1)
    pg.draw.ellipse(s,bl,(360,350,28,28),0)

    pg.draw.ellipse(s,cg,(474,316,99,87),0)
    pg.draw.ellipse(s,bl,(474,316,99,87),1)
    pg.draw.ellipse(s,bl,(509,350,28,28),0)


    pg.draw.polygon(s,br,([433,416],[471,416],[452,450]),0)
    pg.draw.polygon(s,re,([324,467],[568,467],[454,545]),0)
    pg.draw.polygon(s,bl,([433,416],[471,416],[452,450]),1)
    pg.draw.polygon(s,bl,([324,467],[568,467],[454,545]),1)

    #volos
    L = 72

    trig(s,252,286,L,1.01,cv)
    trig(s,276,243,L,0.66,cv)
    trig(s,314,216,L,0.62,cv)
    trig(s,352,193,L,0.25,cv)
    trig(s,390,180,L,0.15,cv)
    trig(s,438,180,L,-0.125,cv)
    trig(s,489,185,L,0,cv)
    trig(s,538,183,L,-0.57,cv)
    trig(s,576,201,L,-0.74,cv)
    trig(s,611,230,L,-1,cv)

    return s


f1 = man(f1, sc,go,ar,pu)





screen.blit(f1,(0,0))

pg.draw.rect(screen,lg,(0,0,927,90),0)
pg.draw.rect(screen,bl,(0,0,927,90),1)
screen.blit(textsurface,(0,0))

pg.display.update() 
clock = pg.time.Clock() 
finished = False 
 
while not finished: 
    clock.tick(FPS) 
    for event in pg.event.get(): 
        if event.type == pg.QUIT: 
            finished = True 
 
pygame.quit()
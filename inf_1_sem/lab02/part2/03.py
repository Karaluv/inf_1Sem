import turtle
import numpy as np
import os
import sys


cords=[]
cords.append([(0,0),(0,2),(1,2),(1,0),(0,0),(1.2,0)])
cords.append([(1,0),(1,2),(0,1),(1.5,0)])
cords.append([(1,0),(0,0),(1,1),(1,2),(0,2),(1.2,0)])
cords.append([(0,0),(1,1),(0,1),(1,2),(0,2),(1.2,0)])
cords.append([(0,2),(0,1),(1,1),(1,2),(1,0),(1.2,0)])
cords.append([(0,0),(1,0),(1,1),(0,1),(0,2),(1,2),(1.2,0)])

cords.append([(1,2),(0,2),(0,0),(1,0),(1,1),(0,1),(0,0),(1.2,0)])
cords.append([(0,2),(1,2),(0,1),(0,0),(1.2,0)])
cords.append([(0,0),(1,0),(1,1),(0,1),(0,0),(0,2),(1,2),(1,1),(1.2,0)])
cords.append([(0,0),(1,1),(1,2),(0,2),(0,1),(1,1),(1.2,0)])

turtle.up()

turtle.speed(10)
turtle.goto(-300,0)

inp = open(os.path.join(sys.path[0],'input.txt'), 'r')
s = inp.read()
inp.close()

command = [int(d) for d in str(s)]


def getU(x,y,xf,yf):
    if xf == x:
        if yf > y:
            return 90
        if yf < y:
            return -90
    if yf == y:
        if xf > x:
            return 0
        if xf < x:
            return 180
    a = np.arctan((yf -y) / (xf-x))/np.pi*180 

    if yf - y <0 and xf -x < 0:
        a= a+180

    return a

def number(cr,l):

    x,y = -1,0


    a = 0

    

    for i in range(len(cr)):
        if i == 1:
            turtle.down()
        if i == len(cr)-1:
            turtle.up()
        a = getU(x,y,cr[i][0],cr[i][1]) 
        turtle.left(a)
        turtle.forward(np.sqrt( np.power(x-cr[i][0],2) +  np.power(y-cr[i][1],2) )*l)
        turtle.right(a)
        x,y = cr[i]

    
    








for j in command:
    number(cords[j],20)





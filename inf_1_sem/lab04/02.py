import turtle as tl
import numpy as np
import math


num = []
num.append([[0,0],[1,0],[1,2],[0,2],[0,0]])
num.append([[1,0],[1,2],[0,1]])
num.append([[1,0],[0,0],[1,1],[1,2],[0,2],[0,1]])
num.append([[0,0],[1,1],[0,1],[1,2],[0,2]])
num.append([[1,0],[1,2],[1,1],[0,1],[0,2]])

num.append([[1,0],[0,0],[0,1],[1,1],[1,2],[0,2]])

num.append([[1,2],[0,2],[0,0],[1,0],[1,1],[0,1]])

num.append([[0,0],[1,2],[0,2]])

num.append([[0,0],[1,0],[1,2],[0,2],[0,1],[1,1],[0,1],[0,0]])

num.append([[0,0],[1,0],[1,2],[0,2],[0,1],[1,1]])

L = 80

tl.speed(10)
tl.up()

tl.goto(-200,0)

def ug(xy0,xy1):
    return math.atan2(xy1[1]-xy0[1], xy1[0]-xy0[0]) / math.pi *180



def ch(cor,l):

    cor.append([1.5,0])
    cr1 = [0,0]

    for i in range(len(cor)):
        if i == 1:
            tl.down()
        if i == len(cor)-1:
            tl.up()

        cr0 = cr1
        cr1 = cor[i]

        a = ug(cr0,cr1)

        tl.left(a)
        tl.forward(  l*((cr0[0]-cr1[0])**2+(cr0[1]-cr1[1])**2)**0.5   )
        tl.right(a)


        
ch(num[1],L)
ch(num[4],L)
ch(num[1],L)
ch(num[7],L)
ch(num[0],L)
ch(num[0],L)
    
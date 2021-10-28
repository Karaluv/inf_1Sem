import random
from random import randint
import turtle
import numpy as np
import math


turtle.up()
turtle.speed(0)
turtle.goto(-300,200)
turtle.down()
turtle.goto(300,200)
turtle.goto(300,-200)
turtle.goto(-300,-200)
turtle.goto(-300,200)

number_of_turtles = 10
steps_of_time_number = 10000



combos  = []

for i in range(number_of_turtles):
    for j in range(i+1,number_of_turtles):
        combos.append((i,j))


pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.turtlesize(0.5,0.5,0.5)
    unit.penup()
    unit.speed(0)
    unit.goto(randint(-200, 200), randint(-200, 200))
    unit.vx = randint(-20,20)
    unit.vy = randint(-20,20)
    unit.Fx = 0
    unit.Fy = 0 
    unit.a = 0






k =10000
dt = 0.1


def rnd(t1,t2):

        x1,y1 = pool[t1].pos()
        x2,y2 = pool[t2].pos()

        l = np.power(np.power(x1-x2,2)+np.power(y1-y2,2),1.5)


        pool[t1].Fx +=  k * (x1-x2)/l
        pool[t2].Fx +=  k * (x2-x1)/l
        pool[t1].Fy +=  k * (y1-y2)/l
        pool[t2].Fy +=  k * (y2-y1)/l



def forces(chere):

    chere.vy += chere.Fy*dt
    chere.vx += chere.Fx*dt
    chere.a = math.atan2(chere.vy,chere.vx)/np.pi*180

    x,y =  chere.pos()

    if (x>200) and chere.vx>0:
        chere.vx = - chere.vx
    if (x<-200) and chere.vx<0:
        chere.vx = - chere.vx
    if (y>200) and chere.vy>0:
        chere.vy = - chere.vy
    if (y<-200) and chere.vy<0:
        chere.vy = - chere.vy
    
    v = np.sqrt(np.power(chere.vy,2)+np.power(chere.vx,2))
    chere.setheading(chere.a)
    chere.forward(v*dt)


    chere.Fy = 0
    chere.Fx = 0



for i in range(steps_of_time_number):

    for c in combos:
        rnd(c[0],c[1])
    for unit in pool:
        forces(unit)
    
        

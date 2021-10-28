import random 
import turtle


def rnd(l):
    a = random.random()*360
    l = random.random()*l
    return a,l

L=100
for i in range(100):
    am,lm = rnd(L)
    if am > 180:
        am = am -180
        turtle.left(am)
    else:
        turtle.right(am)
    
    turtle.forward(lm)
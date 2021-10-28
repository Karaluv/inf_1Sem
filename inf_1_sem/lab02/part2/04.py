import turtle
import numpy as np


turtle.shape("circle")

v =20
a = 80

a = a*np.pi/180

ax = 0
ay = -1
ky=-0.01
vx = v * np.cos(a)
vy = v * np.sin(a)
dt = 0.1

x = 0
y = 0

turtle.goto(300,0)
turtle.goto(-300,0)

x=-300

for i in range(10000):
    vx += ax*dt
    x += vx*dt
    y += vy*dt
    vy += ay*dt+ky*vy*dt
    if y<=0:
        vy = - vy
    turtle.goto(x,y)


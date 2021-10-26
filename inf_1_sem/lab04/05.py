import turtle as tl
import numpy as np

tl.shape('circle')
vx = 20
vy = 40
g = 9.8
x = -300
y = 0
dt = 0.1
k = 0.08
tl.goto(500,0)
tl.goto(-300,0)
for i in range(800):
	x += vx*dt
	y += (vy*dt - g*dt*dt/2)
	vy -= g*dt
	tl.goto(x,y)
	vx = vx*(1-k*dt)
	vy = vy*(1-k*dt)
	if(y < 0):
		vy = (-1)*vy
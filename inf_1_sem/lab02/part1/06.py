import turtle

turtle.shape('turtle')

turtle.speed(10)

a = 50

rng = 3



for r in range(rng):

    
    turtle.forward(a)
    turtle.stamp()
    turtle.right(180)

    turtle.forward(a)

    turtle.right(180+360/rng)



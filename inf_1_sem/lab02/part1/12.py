import turtle


turtle.shape('turtle')

turtle.speed(10)



def circle(r):
    for i in range (0,180,5):

        turtle.forward(r)  

        turtle.right(5)  


turtle.up()
turtle.forward(-300)
turtle.left(90)
turtle.down()

for i in range(10):

    circle(10)
    circle(2)






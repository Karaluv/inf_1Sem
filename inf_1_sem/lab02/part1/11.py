import turtle


turtle.shape('turtle')

turtle.speed(10)



def circle(r):
    for i in range (0,360,5):

        turtle.forward(r)  

        turtle.right(5)  


    

turtle.left(90)

for i in range(10):

    turtle.left(180)
    circle(4+i/2)





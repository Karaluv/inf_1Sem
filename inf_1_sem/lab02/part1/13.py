import turtle


turtle.shape('turtle')

turtle.speed(10)



def circle(r,d):
    for i in range (0,360//d,5):

        turtle.forward(r)  

        turtle.right(5)  


turtle.up()
turtle.forward(-114)
turtle.left(90)
turtle.down()



turtle.fillcolor("yellow")
turtle.down()
turtle.begin_fill()
circle(10,1)
turtle.end_fill()
turtle.up()
turtle.goto(-40-23,72)

turtle.fillcolor("blue")
turtle.down()
turtle.begin_fill()
circle(2,1)
turtle.end_fill()
turtle.up()

turtle.goto(40-23,72)

turtle.fillcolor("blue")
turtle.down()
turtle.begin_fill()
circle(2,1)
turtle.end_fill()
turtle.up()


turtle.color("black")
turtle.width(10)
turtle.goto(0,0)
turtle.right(180)
turtle.down()
turtle.forward(20)
turtle.up()


turtle.color("red")
turtle.goto(80,-10)
turtle.down()
circle(7,2)
turtle.up()



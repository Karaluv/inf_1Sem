import turtle


turtle.shape('turtle')

turtle.speed(10)



def ugol(n,l):
    a = 180-180 * (n-2)/n

    turtle.left(a/2)

    for j in range(n):
       
        turtle.forward(l)
        turtle.left(a)

    turtle.left(-a - (180-a)/2)


    



for i in range(3,10):


    ugol(i,100+i*5)

    turtle.up()
    turtle.forward(5)
    turtle.left(90)
    turtle.down()




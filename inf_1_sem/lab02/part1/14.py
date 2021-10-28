import turtle

turtle.shape('turtle')


n=11


def star(N):


    for i in range(N):
 

            turtle.forward(100)
 

            turtle.right(180 - 180/N)

star(n)


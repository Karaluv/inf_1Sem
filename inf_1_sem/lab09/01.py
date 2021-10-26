import pygame
from random import randint
import os
import sys
from target import target
from shell import shell
from tank import tank



# load score function
def load():
    global Hscore
    with open(os.path.join(sys.path[0],"score.txt"), 'r') as f:
        Hscore = [line.rstrip('\n') for line in f]

# save score function
def save(data):
    '''
    data - score array
    '''
    with open(os.path.join(sys.path[0],"score.txt"), 'w') as f:
        for s in data:
            f.write(str(s) + '\n')

# 1-d list to n-d list
def to_matrix(l, n):
    '''
    l - input list
    n - output number of dimentions
    '''
    return [l[i:i+n] for i in range(0, len(l), n)]

#def prints score in table like way 
def printscore(matrix):
    '''
    matrix - input 2d array from names and scores
    '''
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print ('\n'.join(table))

# print - load part
load()
printscore(to_matrix(Hscore,5))

#input name and stuff for high score

name = input('Your name: ')
Number_of_objects = int(input('Number of targets at single time: '))
Size = int(input('Maximum size of the objects: '))
Speed = int(input('Maximum speed of the objects: '))

#init part
pygame.init()
FPS = 60
screen = pygame.display.set_mode((1200, 800))

#color assign part
cr = (255, 0, 0)
cb = (0, 0, 255)
cy = (255, 255, 0)
cg = (0, 255, 0)
cm = (255, 0, 255)
cc = (0, 255, 255)
bl = (0, 0, 0)
wh = (255,255,255)

pl0 = [cr,cb,cy]
pl1 = [cg,cm,cc]

#set width and high
W = 1200
H = 800

#set start score
score = 0
number_of_rounds = 0

#set array of targets
targets = []
shells = []
Tank = 1

#init part of drawing text with score
pygame.font.init() 
myfont = pygame.font.SysFont('Comic Sans MS', 40)


#initialize all objects on screen
def init(L):
    '''
    Speed - maximum object speed
    Size - maximum object size
    L - number of objects
    W,H - screen borders
    '''
    global W,H
    for i in range(L):
        targets.append(target(W//2,0,W,H,5,5,40,W,H))
        targets[i].reass()
    global Tank 
    Tank = tank(100,600,0,0,20,W,H)
    Tank.reass()

#initialize new ball after the death previous
def new_shell(x,y,vx,vy):
    '''
    Speed - maximum object speed
    W,H - screen borders
    Size - maximum object size
    '''
    global W,H
    shellf = shell.shell(x,y,vx,vy,10,W,H)
    shellf.reass()
    return shellf


#initialize new ball after the death previous
def new_target(xmin,ymin,xmax,ymax,vx,vy,r):
    '''
    Speed - maximum object speed
    W,H - screen borders
    Size - maximum object size
    '''
    global W,H
    targetf = target(xmin,ymin,xmax,ymax,vx,vy,r,W,H)
    targetf.reass()
    return targetf


#redraw and compute next position of all screen objects and draw score
def update(position,power):
    '''
    balls - list of all creen objects
    W,H - screen borders
    score - players score
    '''

    textsurface = myfont.render('Your score: '+str(score), False, (0, 0, 0),wh)

    colision()

    death_list = find()


    for i in range(len(shells)):
        if shells[i].spawn == 0:
            death_list.append((-1,i))
        else:
            shells[i].spawn -=1
            shells[i].reass()
            shells[i].Move()
            shells[i].Draw(screen)
        
    for i in range(len(targets)):
        targets[i].reass()
        targets[i].Move()
        targets[i].Draw(screen)

    kill(death_list)
    Tank.Draw(screen,position,power)
    screen.blit(textsurface,(20,20))
   


#function of killing of an object and adding score and reving
def kill(death_list):
    for p in death_list:
        if p[0]!=-1:
            del targets[p[0]]
            print_stat()
            global Speed
            global Size
            targets.append(new_target(W//2,0,W,H,Speed,Speed,Size))
        if p[1]!=-1:
            del shells[p[1]]
#function finds if player has clicked at the object or no and gets that object index
def find():
    pairs = create_pairs(targets,shells)
    death = []
    global score
    for p in pairs:

        if abs(targets[p[0]].x - shells[p[1]].x)<(targets[p[0]].r + shells[p[1]].r):
            if abs(targets[p[0]].y - shells[p[1]].y)<(targets[p[0]].r + shells[p[1]].r):
                if (targets[p[0]].x - shells[p[1]].x)**2 + (targets[p[0]].y - shells[p[1]].y)**2<(targets[p[0]].r + shells[p[1]].r)**2:
                    death.append(p)
                    score +=30
                    print(score)
    return death
#finds all posible pairs
def create_pairs(arr1,arr2):

    pairs = []

    for i in range(len(arr1)):
        for j in range(i,len(arr2)):
            pairs.append((i,j))
    return pairs

#finds if balls collide
def colision():

    pairs = create_pairs(shells,shells)

    for p in pairs:

        if abs(shells[p[0]].x - shells[p[1]].x)<(shells[p[0]].r + shells[p[1]].r):
            if abs(shells[p[0]].y - shells[p[1]].y)<(shells[p[0]].r + shells[p[1]].r):
                if (shells[p[0]].x - shells[p[1]].x)**2 + (shells[p[0]].y - shells[p[1]].y)**2<(shells[p[0]].r + shells[p[1]].r)**2:
                    shells[p[0]].vx = - shells[p[0]].vx
                    shells[p[0]].vy = - shells[p[0]].vy
                    shells[p[1]].vx = - shells[p[1]].vx
                    shells[p[1]].vy = - shells[p[1]].vy


#exit function
def exit(Hscore):
    Hscore.append(name)
    Hscore.append(score)
    Hscore.append(Number_of_objects)
    Hscore.append(Size)
    Hscore.append(Speed)
    save(Hscore)

#function which starts on click and launch all other functions 
def shoot(event,power):
    global number_of_rounds
    number_of_rounds +=1
    x,y = event

    k = power+10

    x0,y0 = Tank.x,Tank.y

    l = ((x-x0)**2+(y-y0)**2)**0.5

    shells.append(shell(x0,y0,(x-x0)*k/l,(y-y0)*k/l,10,W,H))
    shells[-1].reass()


def print_stat():
    global number_of_rounds
    print("u killed with "+str(number_of_rounds)+" shoots")
    number_of_rounds = 0



#init stuff
pygame.display.update()
clock = pygame.time.Clock()
finished = False
#start function
init(Number_of_objects)

power = 0

#main loop
while not finished:
    clock.tick(FPS)
    if 33>power >0:
        power +=1

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                #exit(Hscore)
                finished = True
        if event.type == pygame.QUIT:
            #quit and save part
            #exit(Hscore)
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #mouse event part
            if power<33:
                power+=1
        elif event.type == pygame.MOUSEBUTTONUP:
            if power != 0:
                shoot(event.pos,power)
            power = 0
    #draw part

    update(pygame.mouse.get_pos(),power)
    pygame.display.update()
    screen.fill(bl)
    


pygame.quit()


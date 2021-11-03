import pygame
from random import randint
import os
import sys
from target import target
from shell import shell
from tank import tank
from bomb import bomb
import math

def exit(Hscore):
    Hscore.append(name)
    Hscore.append('Score first tank: '+str(score[0])+'; Score second tank: '+str(score[1]))
    Hscore.append(Number_of_objects)
    Hscore.append(Size)
    Hscore.append(Speed)
    save(Hscore)

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


skip = 10


FPSR = FPS * skip

frame = 0
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
number_of_rounds = 0

#set array of targets
targets = []
shells = []
tanks = []
bombs = []

score = [0,0]
#init part of drawing text with score
pygame.font.init() 
myfont = pygame.font.SysFont('Comic Sans MS', 40)

#function that defines variables durin game restart
def start():

    #set start score
    global targets,shells,tanks,bombs,t0,t1,score,number_of_rounds,name,Number_of_objects,Size,Speed
    
    screen.fill(bl)
    pygame.display.update()
    number_of_rounds = 0

    #set array of targets
    targets = []
    shells = []
    tanks = []
    bombs = []


    score = [0,0]

    name = input('Your name: ')
    Number_of_objects = int(input('Number of targets at single time: '))
    Size = int(input('Maximum size of the objects: '))
    Speed = int(input('Maximum speed of the objects: '))

    init(Number_of_objects,2)



#initialize all objects on screen
def init(L_target,L_tank):
    '''
    Speed - maximum object speed
    Size - maximum object size
    L - number of objects
    W,H - screen borders
    '''
    global W,H,skip
    global Size,Speed
    for i in range(L_target):
        targets.append(new_target(0,0,W,H,randint(0,Speed),randint(0,Speed),Size))

    tanks.append(tank(20,H-20,0,0,20,W,H,skip,0))
    tanks[-1].reass()

    tanks.append(tank(W-20,20,0,0,20,W,H,skip,1))
    tanks[-1].reass()


#initialize new ball after the death previous
def new_shell(x,y,vx,vy):
    '''
    Speed - maximum object speed
    W,H - screen borders
    Size - maximum object size
    '''
    global W,H,skip
    shellf = shell.shell(x,y,vx,vy,10,W,H,skip)
    shellf.reass()
    return shellf


#initialize new target after the death previous
def new_target(xmin,ymin,xmax,ymax,vx,vy,r):
    '''
    Speed - maximum object speed
    W,H - screen borders
    Size - maximum object size
    '''
    global W,H,skip
    r = randint(r//3,r)
    x = randint(xmin+r,xmax-r)
    y = randint(ymin+r,ymax-r)
    type = randint(0,1)
    targetf = target(x,y,vx,vy,r,W,H,skip,type)
    targetf.reass()
    return targetf


#redraw and compute next position of all screen objects and draw score
def update(drawing):
    '''
    balls - list of all creen objects
    W,H - screen borders
    score - players score
    '''

    textsurface = myfont.render('Score first tank: '+str(score[0])+'; Score second tank: '+str(score[1]), False, (0, 0, 0),wh)

    death_list = []


    for i in range(len(shells)):
        if shells[i]:
            if shells[i].spawn == 0:
                death_list.append((-1,i))
            else:
                shells[i].spawn -=1
                if shells[i].reass():
                
                    for j in range(5):
                        shells.append(shell(shells[i].x,shells[i].y,randint(0,10)/10*shells[i].vx,randint(0,10)/10*shells[i].vx,10,W,H,skip,1,shells[i].tankN))
                    death_list.append((-1,shells[i]))
                else:
                    shells[i].Move()
                    shells[i].Draw(screen)
        
    for i in range(len(targets)):
        if targets[i]:
            targets[i].reass()
            targets[i].Move()
            if drawing:
                targets[i].Draw(screen)

    for i in range(len(bombs)):
        bombs[i].reass()
        if bombs[i].Move():
            death_list.append((bombs[i],0))
        if drawing:
            bombs[i].Draw(screen)

    colision()

    death_list = death_list+find()

    kill(death_list)
    tanks[0].reass()
    tanks[0].Move()
    if drawing:
        tanks[0].Draw(screen,tanks[0].power)
    tanks[1].reass()
    tanks[1].Move()
    if drawing:
        tanks[1].Draw(screen,tanks[1].power)

    screen.blit(textsurface,(20,20))
   


#function of killing of an object and adding score and reving
def kill(death_list):
    sh = False
    global W,H
    global t0,t1,skip
    tankN=-1
    for p in death_list:
        for t in p:
            if type(t) == target:
                sh =False
                
                try:
                    
                    targets.remove(t)
                except ValueError:
                    pass # or scream: thing not in some_list!
                except AttributeError:
                    call_security("")

                print_stat()
                global Speed
                global Size
                targets.append(new_target(W//2,0,W,H,Speed,Speed,Size))
                if not tankN == -1:
                    score[tankN] += 1
                tankN = -1
            if type(t) == shell:
                sh = True
                if t.live > 3*skip:
                    tankN = t.tankN
                    shells.remove(t)
                    sh = False

            if type(t) == tank:
                if not sh:
                    if t == tanks[1]:
                        score[0]+=10
                    if t == tanks[0]:
                        score[1]+=10
                    sh = False
            if type(t) == bomb:
                sh = False
                bombs.remove(t)
                if not tankN == -1:
                    score[tankN] += 1
                tankN = -1

#function finds if player has clicked at the object or no and gets that object index
def find():
    pairs = create_pairs(shells,targets)
    pairs = pairs +create_pairs(shells,tanks)
    pairs = pairs +create_pairs(targets,tanks)
    pairs = pairs +create_pairs(bombs,tanks)
    pairs = pairs +create_pairs(shells,bombs)
    death = []
    global score
    for p in pairs:

        if abs(p[0].x - p[1].x)<(p[0].r + p[1].r):
            if abs(p[0].y - p[1].y)<(p[0].r + p[1].r):
                if (p[0].x - p[1].x)**2 + (p[0].y - p[1].y)**2<(p[0].r + p[1].r)**2:
                    death.append(p)
                   

    return death
#finds all posible pairs
def create_pairs(arr1,arr2):

    pairs = []
    
    for i in range(len(arr1)):
        for j in range(i,len(arr2)):
            if arr1[i] and arr2[j]:
                pairs.append((arr1[i],arr2[j]))
    return pairs

#finds if balls collide
def colision():

    pairs = create_pairs(shells,shells)
    pairs = pairs +create_pairs(targets,targets)


    for p in pairs:
        if abs(p[0].x - p[1].x)<(p[0].r + p[1].r):
            if abs(p[0].y - p[1].y)<(p[0].r + p[1].r):
                if (p[0].x - p[1].x)**2 + (p[0].y - p[1].y)**2<(p[0].r + p[1].r)**2:
                    if not p[0].type == 1 and not type(p) == shells :
                        p[0].vx = - p[0].vx
                        p[0].vy = - p[0].vy
                    if not p[1].type == 1 and not type(p) == shells :
                        p[1].vx = - p[1].vx
                        p[1].vy = - p[1].vy


#exit function
def spawn_bomb(pos):
    bombs.append(bomb(pos[0],pos[1],0,0,15,W,H,1))

#function which starts on click and launch all other functions 
def shoot(tank):
    global number_of_rounds
    if tank.reload ==0:
        number_of_rounds +=1
 

        k = tank.power+10

        x0,y0 = tank.x,tank.y


        find = False
    
        for i in range(len(shells)):
            if not shells[i]:
                shells[i] = shell(x0,y0,math.cos(tank.a)*k,-math.sin(tank.a)*k,10,W,H,skip,tank.shell_type,tanks.index(tank))
                shells[i].reass()
                find = True
                break
        if not find:
            shells.append(shell(x0,y0,math.cos(tank.a)*k,-math.sin(tank.a)*k,10,W,H,skip,tank.shell_type,tanks.index(tank)))
            shells[-1].reass()
        tank.reload = skip*60


def print_stat():
    global number_of_rounds



#init stuff
pygame.display.update()
clock = pygame.time.Clock()
finished = False
#start function
init(Number_of_objects,1)

power = 0

#main loop
while not finished:

    clock.tick(FPSR)

    frame += 1
    

    if tanks[0].power_up:
        if tanks[0].power<33:
            tanks[0].power+=1/skip

    if tanks[1].power_up:
        if tanks[1].power<33:
            tanks[1].power+=1/skip

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                #exit(Hscore)
                finished = True
            if event.key == pygame.K_w:
                tanks[0].da =0.05
            if event.key == pygame.K_s:
                tanks[0].da =-0.05

            if event.key == pygame.K_LSHIFT :
                #mouse event part
                if tanks[0].power<33:
                    tanks[0].power+=1
                    tanks[0].power_up = True
            if event.key == pygame.K_d:
                tanks[0].vx = 5
            if event.key == pygame.K_a:
                tanks[0].vx = -5



            if event.key == pygame.K_DOWN:
                tanks[1].da =0.05
            if event.key == pygame.K_UP:
                tanks[1].da =-0.05

            if event.key == pygame.K_RSHIFT :
                #mouse event part
                if tanks[1].power<33:
                    tanks[1].power+=1
                    tanks[1].power_up = True
            if event.key == pygame.K_RIGHT:
                tanks[1].vx = 5
            if event.key == pygame.K_LEFT:
                tanks[1].vx = -5

            if event.key == pygame.K_0:
                tanks[0].shell_type = 0
            if event.key == pygame.K_1:
                tanks[0].shell_type = 2
            if event.key == pygame.K_KP0:
                tanks[1].shell_type = 0
            if event.key == pygame.K_KP1:
                tanks[1].shell_type = 2

            if event.key == pygame.K_SPACE:
                spawn_bomb(pygame.mouse.get_pos())
            if event.key == pygame.K_r:
                exit(Hscore)
                start()

        if event.type == pygame.QUIT:
            #quit and save part
            #exit(Hscore)
            finished = True
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_d:
                tanks[0].vx = 0
            if event.key == pygame.K_a:
                tanks[0].vx = 0

            if event.key == pygame.K_w:
                tanks[0].da =0
            if event.key == pygame.K_s:
                tanks[0].da =0

            if event.key == pygame.K_LSHIFT :
                if tanks[0].power != 0:
                    if tanks[0].power_up:
                        shoot(tanks[0])
                        tanks[0].power = 0
                tanks[0].power_up = False


            if event.key == pygame.K_LEFT:
                tanks[1].vx = 0
            if event.key == pygame.K_RIGHT:
                tanks[1].vx = 0

            if event.key == pygame.K_DOWN:
                tanks[1].da =0
            if event.key == pygame.K_UP:
                tanks[1].da =0

            if event.key == pygame.K_RSHIFT :
                if tanks[1].power != 0:
                    if tanks[1].power_up:
                        shoot(tanks[1])
                        tanks[1].power = 0
                tanks[1].power_up = False


        #if event.type == pygame.
    #draw part
    drawing = False
    if frame == skip:
        drawing = True
        frame = 1
    update(drawing)
    if drawing:
        pygame.display.update()
        screen.fill(bl)
   #save score
exit(Hscore)

pygame.quit()


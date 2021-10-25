import pygame
from random import randint
import os
import sys
from pygame.locals import Color
try:
    import pafy
    import vlc
except:
    print("pip install pafy and pip install python-vlc and install vlc media player on your pc pls!!!")
from pygame import display




kadr = 0
max_kadr = 999-153


try:
    url = "https://www.youtube.com/watch?v=B4eSmhr4-2Q"
    #url = "hhh"
    video = pafy.new(url)
    best = video.getbest()
    playurl = best.url
    
    Instance = vlc.Instance()
    player = Instance.media_player_new()
    Media = Instance.media_new(playurl)
    player.set_media(Media)
    player.audio_set_volume(90)
    player.play()
    play = False
except:
    play = True
    print("vlc is needed, or url is dead auto play is of, presaved track is played")


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




if play:
    soundObj = pygame.mixer.Sound(os.path.join(sys.path[0],'gachi\\music.mp3'))
    soundObj.play()

FPS = 60

thickarrow_strings = (               #sized 24x24
  " xxxxxxxxx              ",
  " xx......xx             ",
  "    xx.....xx           ",
  "       xxxx             ",
  "         xxxxx          ",
  "       xx..x..xx        ",
  "      xx...x...xx       ",
  "      xx...x...xx       ",
  "      xxxx..xxxxx       ",
  "      xx.......xx       ",
  "      xx.......xx       ",
  "      xx.......xxx      ",
  "       xx........xx     ",
  "       xx........xx     ",
  "       xx........xx     ",
  "       xx........xx     ",
  "       xx........xx     ",
  "      xx..........xx    ",
  "  xxxx............xxxx  ",
  "xx.........xx.........xx",
  "xx.........xx.........xx",
  "xx.........xx.........xx",
  "  xx....xx   xx.....xx  ",
  "    xxxx        xxx     ")

cursor, mask = pygame.cursors.compile(thickarrow_strings, "X", ".")
cursor_sizer = ((24, 24), (7, 11), cursor, mask)
pygame.mouse.set_cursor(*cursor_sizer)

infoObject = pygame.display.Info()

screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h),pygame.FULLSCREEN)





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
W = infoObject.current_w
H = infoObject.current_h



#set start score
score = 0

#set array of targets
balls = []

#init part of drawing text with score
pygame.font.init() 
myfont = pygame.font.SysFont('Comic Sans MS', 40)

#class ball - class of flighing objects
class ball:
    '''
    x - x position
    y - y position
    vx - x axis speed
    vy - y axis speed
    color - color of object
    type - type, if 0 - circle,1 - rect

    xmin - position of left object border
    xmxx - position of right object border
    ymin - position of top object border
    ymxx - position of buttom object border

    r = radius of circle or half of rect side

    R - r**2
    '''

    #intialize starting variables with help of random
    def __init__(self,xm,ym,vm,rm):
        '''
        xm - maximum starting x possition
        ym - maximum starting y possition
        rm - maximum size of the object
        vm - maxim x,y speed of the object
        r = radius of circle or half of rect side
        '''
        global DrawF,TragectoryF
        #self.spawn = randint(20,300)
        self.spawn = 0
        self.r = randint(int(rm/3),rm)
        self.x = randint(0,xm)
        self.y = randint(0,ym)
        self.vx = randint(-vm,vm)
        self.vy = randint(-vm,vm)
        self.type = randint(0,1)

        if self.type == 0:
            self.color = pl0[randint(0,len(pl0)-1)]
            self.texture = t0[randint(0,len(t0)-1)]
        if self.type == 1:
            self.color = pl1[randint(0,len(pl1)-1)]
            self.texture = t1[randint(0,len(t1)-1)]

        self.texture = pygame.transform.scale(self.texture,(self.r*2,self.r*2))

        self.mask = pygame.mask.from_surface(self.texture)

        self.R = self.r**2

        self.draw = DrawF[self.type]
        self.tragectory = TragectoryF[self.type]

    #calculate some useful properties of an object
    def reass(self):
        '''
        xmin - position of left object border
        xmxx - position of right object border
        ymin - position of top object border
        ymxx - position of buttom object border
        r = radius of circle or half of rect side
        R - r**2
        '''
        self.xmax=self.x +self.r
        self.xmin=self.x - self.r
        self.ymax =self.y +self.r
        self.ymin = self.y-self.r
        self.rect = self.texture.get_rect(center=(self.x, self.y))


        
    #calculate object next frame position
def tragectory1(self,vm,W,H):
    '''
    W,H - screen borders
    vm - maximum and minimum random speed
    '''
    if self.xmin <= 0:
        self.vx =  randint(0,vm)
        self.vy =  randint(-vm,vm)
    if self.xmax >= W:
        self.vx =  randint(-vm,0)
        self.vy =  randint(-vm,vm)
    if self.ymin <= 0:
        self.vy =  randint(0,vm)
        self.vx =  randint(-vm,vm)
    if self.ymax >= H:
        self.vy =  randint(-vm,0)
        self.vx =  randint(-vm,vm)

    self.x = self.vx + self.x
    self.y = self.vy + self.y

def tragectory2(self,g,W,H):
    '''
    W,H - screen borders
    g - y axiliration
    '''
    g = int(g) 
    if self.xmin <= 0:
        self.vx =  abs(self.vx)
        self.x = 0+self.r*2
    if self.xmax >= W:
        self.vx =  -abs(self.vx)
        self.x = W-self.r*2
    if self.ymin <= 0:
        self.vy =  abs(self.vy)
        self.y = 0+self.r*2
    if self.ymax >= H:
        self.vy =  -abs(self.vy)
        self.y = H-self.r*2

    self.vy = self.vy + g

    self.x = self.vx + self.x
    self.y = self.vy + self.y

TragectoryF = [tragectory1,tragectory2]

#draw object function
def draw1(self):
    '''
    type - type of an object
    '''
    screen.blit(self.texture,(self.xmin,self.ymin))


def draw2(self):
    '''
    type - type of an object
    '''
    #pygame.draw.rect(screen,self.color,(self.xmin,self.ymin,2*self.r,2*self.r),0)
    screen.blit(self.texture,(self.xmin,self.ymin))

DrawF = [draw1,draw2]

#initialize all objects on screen
def init(L):
    '''
    Speed - maximum object speed
    Size - maximum object size
    L - number of objects
    W,H - screen borders
    '''
    for i in range(L):
        balls.append(ball(W,H,Speed,Size))
        balls[i].reass()

#initialize new ball after the death previous
def new_ball():
    '''
    Speed - maximum object speed
    W,H - screen borders
    Size - maximum object size
    '''
    global W,H,Size,Speed
    ballf = ball(W,H,Speed,Size)
    ballf.reass()
    return ballf


#redraw and compute next position of all screen objects and draw score
def update():
    '''
    balls - list of all creen objects
    W,H - screen borders
    score - players score
    '''
    global balls,W,H,score

    textsurface = myfont.render('FIST THEM ALL '+str(score), False, wh,(0,0,0,255))

    colision()

    l =len(balls)

    for i in range(l):
        if balls[i].spawn > 0:
            balls[i].spawn -= 1
        else:
            balls[i].reass()
            balls[i].tragectory(balls[i],2,W,H)
            balls[i].draw(balls[i])
        
    screen.blit(textsurface,(20,20))
   
#function of killing of an object and adding score and reving
def kill(apa):
    '''
    apa - list of indexes of dead objects
    score - score
    '''
    global score

    for i in apa:
        if balls[i].spawn == 0:
            if balls[i].type == 1:
                score = score+30

            if balls[i].type == 0:
                score = score + 60

            balls[i] = new_ball()

    print(score)

#function finds if player has clicked at the object or no and gets that object index
def find(event):
    '''
    event - position of the mouse
    '''
    x,y = event

    aps = list(range(len(balls)))
    apx = []
    apy =[]
    apa = []
    #checks x cordintes
    for i in aps:
        if balls[i].xmin < x:
            if balls[i].xmax > x:
                apx.append(i)
    #checks y cordinates 
    for i in apx:
        if balls[i].ymin < y:
            if balls[i].ymax > y:
                apy.append(i)
    # checks distance from center for circles and applies changes for rects
    for i in apy:
        pos_in_mask = x - balls[i].xmin, y - balls[i].ymin
        touching = balls[i].rect.collidepoint(*event) and balls[i].mask.get_at(pos_in_mask)
        if touching:
            apa.append(i)
    #returns list of the dead objects
    if apa:
        soundObj = pygame.mixer.Sound(os.path.join(sys.path[0],'gachi\\aaa.mp3'))
        soundObj.play()
    else:
        soundObj = pygame.mixer.Sound(os.path.join(sys.path[0],'gachi\\sorry.mp3'))
        soundObj.play()
    return apa

#finds all posible pairs
def create_pairs():

    pairs = []

    for i in range(len(balls)):
        for j in range(i,len(balls)):
            pairs.append((i,j))
    return pairs

#finds if balls collide
def colision():

    pairs = create_pairs()

    for p in pairs:

        if abs(balls[p[0]].x - balls[p[1]].x)<(balls[p[0]].r + balls[p[1]].r):
            if abs(balls[p[0]].y - balls[p[1]].y)<(balls[p[0]].r + balls[p[1]].r):
                if (balls[p[0]].x - balls[p[1]].x)**2 + (balls[p[0]].y - balls[p[1]].y)**2<(balls[p[0]].r + balls[p[1]].r)**2:
                    balls[p[0]].vx = - balls[p[0]].vx
                    balls[p[0]].vy = - balls[p[0]].vy
                    balls[p[1]].vx = - balls[p[1]].vx
                    balls[p[1]].vy = - balls[p[1]].vy


#exit function
def exit(Hscore):
    Hscore.append(name)
    Hscore.append(score)
    Hscore.append(Number_of_objects)
    Hscore.append(Size)
    Hscore.append(Speed)
    save(Hscore)

#function which starts on click and launch all other functions 
def click(event):
    '''
    event - mouse position
    '''
    death_list = find(event)
    if death_list:
        kill(death_list)

#init stuff
pygame.display.update()
clock = pygame.time.Clock()
finished = False

#kop = pygame.image.load(os.path.join(sys.path[0], 'kop.png')).convert_alpha()
#ech = pygame.image.load(os.path.join(sys.path[0], 'ech.png')).convert_alpha()
#nuh = pygame.image.load(os.path.join(sys.path[0], 'nuh.png')).convert_alpha()
#loh = pygame.image.load(os.path.join(sys.path[0], 'loh.png')).convert_alpha()
#kar = pygame.image.load(os.path.join(sys.path[0], 'kar.png')).convert_alpha()

#shiz = pygame.image.load(os.path.join(sys.path[0], 'shiz.png')).convert_alpha()
#nol = pygame.image.load(os.path.join(sys.path[0], 'nol.png')).convert_alpha()
#hz = pygame.image.load(os.path.join(sys.path[0], 'hz.png')).convert_alpha()

#t0 = [kop,ech,nuh,loh,kar]
#t1 = [shiz,nol,hz]

bil=[]
def loadB():
    for i in range(0,620-291):
        bil.append(pygame.image.load(os.path.join(sys.path[0],"Billy\\00"+str(i+291)+'.jpg')).convert_alpha())
        bil[i] = pygame.transform.scale(bil[i],(infoObject.current_w, infoObject.current_h))
loadB()
k =[]
def loadK():
    for i in range(0,999-153):
        k.append(pygame.image.load(os.path.join(sys.path[0],"kadr\\00"+str(i+153)+'.jpg')).convert_alpha())
        k[i] = pygame.transform.scale(k[i],(infoObject.current_w, infoObject.current_h))

loadK()
t=[]
def loadG():
    for i in range(1,32):
        t.append(pygame.image.load(os.path.join(sys.path[0],"gachi\\"+str(i)+'.png')).convert_alpha())
loadG()


t0 = t[0:15]
t1 = t[16:30]
#start function






soundObj = pygame.mixer.Sound(os.path.join(sys.path[0],'gachi\\intro.mp3'))
soundObj.play()


init(Number_of_objects)


#main loop
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                finished = True
        if event.type == pygame.QUIT:
            #quit and save part
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #mouse event part
            click(event.pos)
    #draw part
    
    screen.blit(k[int(kadr) ],(0,0))
    kadr = kadr +0.5
    if kadr >= max_kadr-1:
        exit(Hscore)
        finished = True
    update()
    pygame.display.flip()
    screen.fill(bl)
 
try:
    player.stop()
except:
    print("vlc")
finished = False
kadr = 0
max_kadr = 620 - 291

soundObj = pygame.mixer.Sound(os.path.join(sys.path[0],'gachi\\on.mp3'))
soundObj.play()

text = myfont.render(name+" fucked "+str(score)+" slaves", True, wh,bl)

text_rect = text.get_rect(center=(int(W/2), int(H/2)))
text.set_colorkey(bl)


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                finished = True
    screen.blit(bil[int(kadr) ],(0,0))
    screen.blit(text, text_rect)
    kadr = kadr +0.5
    if kadr >= max_kadr-1:
        finished = True
    pygame.display.flip()

pygame.quit()

from pygame import *
from math import *
from random import *
import subprocess


size=width,height=1440,720
screen=display.set_mode(size)
RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
init()
mono = font.SysFont("Monospace",50)
def floweyFont(text,height,lower=50,upper=1370):
    fx = lower
    fy = height
    count = 0
    inc = 0
    for char in text:
        if char == "\n" or fx > upper:
            fy+=50
            fx = lower
        else:
            if char == "," or char == "." or char == "!": 
                inc = 400
            else:
                inc = 0
            char = mono.render(char,True,WHITE)
            screen.blit(char,(fx,fy))
            display.flip()
            fx+=25
            time.wait(65+inc)
        
    time.wait(1500)

game_over = False
sprites = [image.load("%i.png" % k) for k in range(4)]
for i in range(4):
    sprites[i] = transform.scale(sprites[i],(50,62))
GUY = [100,90]
POS = [100,130]
X = 0
Y = 1
di = [False for i in range(4)]
#screen.blit(image.load("l1.png"),(0,0))
yy = image.load("l1.png")
Z = image.load("l1.png")
screen.blit(image.load("realOne.png"),(0,0))
scroll = image.load("scroll_left.png")
scroll = transform.scale(scroll,(50,62))
x = screen.copy()
scrolls = [[365,90],[484,669],[559,345-scroll.get_rect().height+30],[805,504]]
DONE = set()
for s in scrolls:
    s[1] += 10
m = -1
def mask(screen,GUY,w):
    
    offx = GUY[X] - 50
    offy = GUY[Y] - 65
    try:
        m = -1
        if GUY[X] > 1090 and GUY[Y] > 245:
            viewRect = Rect(1235+5-200,430+5-260,200,260)
        elif GUY[X] > 1090:
            viewRect = Rect(1235+5-200,offy,200,260)
        elif GUY[Y] > 245:
            viewRect = Rect(offx,430+5-260,200,260)
        else:
            viewRect = Rect(offx,offy,200,260)
        viewScreen = x.subsurface(viewRect).copy()
        newView = transform.scale(viewScreen,(width,height))
        player = Rect(POS[X]+10,POS[Y]+10,40,42)

        viewBack = yy.subsurface(viewRect).copy()
        Z.blit(transform.scale(viewBack,(width,height)),(0,0))
        
        
        screen.blit(transform.scale(viewScreen,(width,height)),(0,0))
        screen.blit(sprites[w],(POS[X],POS[Y]))
        COUNT = -1
        for s in scrolls:
            COUNT += 1
            if s[0]-GUY[X] < 50 and abs(s[1]-GUY[Y]) < 201:
                if GUY[Y] <= 180:
                    screen.blit(scroll,(POS[X]+int((s[0]-GUY[X])*7.2),s[1]-int((GUY[Y]-s[1])*720/260)))
                    scrollRect = Rect(POS[X]+int((s[0]-GUY[X])*7.2)+10,s[1]-int((GUY[Y]-s[1])*720/260)+10,30,42)
                    m = COUNT
                elif s[1]-130 > 0:
                    screen.blit(scroll,(POS[X]+int((s[0]-GUY[X])*7.2),s[1]-130))
                    m = COUNT
                    scrollRect = Rect(POS[X]+int((s[0]-GUY[X])*7.2)+10,s[1]-130+10,30,42)
        if m >= 0:
            if scrollRect.colliderect(player) and di[m] == False:
                subprocess.call("One%i.py" % m,shell = True)
                DONE.add(m)
                #print(m)
                di[m] = True
                
        
        if len(DONE) == 4 and GUY[X] > 2080:
            game_over = True
            screen.fill(BLACK)
            floweyFont("That's Level 1!",300)
            display.flip()
            time.wait(2000)
            quit()
                
        #draw.rect(screen,BLUE,player,5)
    except:
        pass
    

mask(screen,GUY,0)
display.flip()
def movePlayer(GUY):
    keys = key.get_pressed()
    #player = Rect(100,130,50,62)
    if keys[K_RIGHT] and GUY[X] < 1260+1040:
        GUY[X] += 3
        if GUY[X] > 1090:
            POS[X] = GUY[X]-1090+100
        else:
            POS[X] = 100
        if Z.get_at((POS[X]+40,POS[Y]+10)) == WHITE and Z.get_at((POS[X]+40,POS[Y]+52)) == WHITE:
            #print(GUY[X],GUY[Y])
            mask(screen,GUY,3)
        else:
            GUY[X] -= 3 
    
    if keys[K_LEFT] and GUY[X] > 96:
        GUY[X] -= 3
        if GUY[X] > 1090:
            POS[X] = GUY[X]-1090+100
        else:
            POS[X] = 100
        if Z.get_at((POS[X]+10,POS[Y]+10)) == WHITE and Z.get_at((POS[X]+10,POS[Y]+52)) == WHITE:
            #print(GUY[X],GUY[Y])
            mask(screen,GUY,2)
        else:
            GUY[X] += 3
        
    if keys[K_UP] and GUY[Y] > 86:
        GUY[Y] -= 3
        if GUY[Y] > 245:
            POS[Y]= GUY[Y]-245+130
        else:
            POS[Y] = 130
        if Z.get_at((POS[X]+10,POS[Y]+10)) == WHITE and Z.get_at((POS[X]+40,POS[Y]+10)) == WHITE:
            #print(GUY[X],GUY[Y])
            mask(screen,GUY,1)
        else:
            GUY[Y] += 3
        
    if keys[K_DOWN] and GUY[Y] < 750:
        GUY[Y] += 3
        if GUY[Y] > 245:
            POS[Y]= GUY[Y]-245+130
        else:
            POS[Y] = 130
        if Z.get_at((POS[X]+10,POS[Y]+52)) == WHITE and Z.get_at((POS[X]+40,POS[Y]+52)) == WHITE:
            #print(GUY[X],GUY[Y])
            mask(screen,GUY,0)
        else:
            GUY[Y] -= 3

 
    
myClock = time.Clock()
running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
    if not game_over:
        mx,my=mouse.get_pos()
        mb = mouse.get_pressed()
        movePlayer(GUY)
        display.flip()
        
    else:
        running = False
    myClock.tick(120)
quit()

from pygame import *
from math import *
from random import *
from tkinter import *
from tkinter.filedialog import *


size=width,height=1440,720
screen=display.set_mode(size)
RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)


MAP = Rect(50,50,1185,380) #MAP
draw.rect(screen,GREEN,MAP)

tiles = [Rect(60,70,20,30),Rect(80,70,20,30)]
cx = 80
cy = 70
pdir = -1
cdir = -1

while cx < 1180:
    if pdir == 1 or pdir == 2:
        cdir = 0
    elif pdir == 0:
        cdir = randint(1,2)
    else:
        cdir = 0
    
    if cdir == 0:
        
        x = randint(2,3)
        for i in range(x):
            if cx < 1200:
                tiles.append(Rect(cx+20,cy,20,30))
                cx += 20
    elif cdir == 1:
        y = randint(2,3)
        for i in range(y):
            if cy < 390:
                tiles.append(Rect(cx,cy+30,20,30))
                cy += 30
    elif cdir == 2:
        y = randint(2,3)
        for i in range(y):
            if cy > 130:
                tiles.append(Rect(cx,cy-30,20,30))
                cy -= 30
                    
        
    pdir = cdir
print(cx)
    
for i in tiles:
    draw.rect(screen,WHITE,i)

sprites = [image.load("%i.png" % k) for k in range(4)]
for i in range(4):
    sprites[i] = transform.scale(sprites[i],(50,62))
GUY = [100,90]
POS = [100,130]
X = 0
Y = 1
x = screen.copy()
try:
    fname = asksaveasfilename(defaultextension=".png")
    if fname != "":
        image.save(x,fname)
except:
    pass
def mask(screen,GUY,w):
    
    offx = GUY[X] - 50
    offy = GUY[Y] - 65
    try:
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
        player = Rect(POS[X],POS[Y],50,62)

        screen.blit(transform.scale(viewScreen,(width,height)),(0,0))
        screen.blit(sprites[w],(POS[X],POS[Y]))
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
        print(GUY[X])
        if GUY[X] > 1090:
            POS[X] = GUY[X]-1090+100
        else:
            POS[X] = 100
        if screen.get_at((POS[X]+50,POS[Y])) == WHITE and screen.get_at((POS[X]+50,POS[Y]+62)) == WHITE:
            mask(screen,GUY,3)
        else:
            GUY[X] -= 3 
    
    if keys[K_LEFT] and GUY[X] > 96:
        GUY[X] -= 3
        if GUY[X] > 1090:
            POS[X] = GUY[X]-1090+100
        else:
            POS[X] = 100
        if screen.get_at((POS[X],POS[Y])) == WHITE and screen.get_at((POS[X],POS[Y]+62)) == WHITE:
            mask(screen,GUY,2)
        else:
            GUY[X] += 3
        
    if keys[K_UP] and GUY[Y] > 86:
        GUY[Y] -= 3
        if GUY[Y] > 245:
            POS[Y]= GUY[Y]-245+130
        else:
            POS[Y] = 130
        if screen.get_at((POS[X],POS[Y])) == WHITE and screen.get_at((POS[X]+50,POS[Y])) == WHITE:
            mask(screen,GUY,1)
        else:
            GUY[Y] += 3
        
    if keys[K_DOWN] and GUY[Y] < 750:
        GUY[Y] += 3
        if GUY[Y] > 245:
            POS[Y]= GUY[Y]-245+130
        else:
            POS[Y] = 130
        if screen.get_at((POS[X],POS[Y]+62)) == WHITE and screen.get_at((POS[X]+50,POS[Y]+62)) == WHITE:
            mask(screen,GUY,0)
        else:
            GUY[Y] -= 3
            

    
myClock = time.Clock()
running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
    mx,my=mouse.get_pos()
    mb = mouse.get_pressed()
    movePlayer(GUY)
    display.flip()
    myClock.tick(120)
quit()

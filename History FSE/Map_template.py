from pygame import *
from math import *
from random import *


size=width,height=1440,720
screen=display.set_mode(size)
RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)

#screen.fill(WHITE)
MAP = Rect(50,50,1185,380) #MAP
draw.rect(screen,GREEN,MAP)

sprites = [image.load("%i.png" % k) for k in range(4)]
for i in range(4):
    sprites[i] = transform.scale(sprites[i],(50,62))
GUY = [95,95]
POS = [100,130]
X = 0
Y = 1
x = screen.copy()
def drawScene(screen,GUY,w):
    print(GUY[X],GUY[Y])
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
        screen.blit(transform.scale(viewScreen,(width,height)),(0,0))
        
        screen.blit(sprites[w],(POS[X],POS[Y]))
    except:
        pass
    

drawScene(screen,GUY,0)
display.flip()
def movePlayer(GUY):
    #print(mouse.get_pos())
    keys = key.get_pressed()
    if keys[K_RIGHT] and GUY[X] < 1260+1040:
        GUY[0] += 5
        if GUY[X] > 1090:
            POS[X] = GUY[X]-1090+100
        else:
            POS[X] = 100
        drawScene(screen,GUY,3)
          
    if keys[K_LEFT] and GUY[X] > 96:
        GUY[0] -= 5
        if GUY[X] > 1090:
            POS[X] = GUY[X]-1090+100
        else:
            POS[X] = 100
        drawScene(screen,GUY,2)
        
    if keys[K_UP] and GUY[Y] > 96:
        GUY[1] -= 5
        if GUY[Y] > 245:
            POS[Y]= GUY[Y]-245+130
        else:
            POS[Y] = 130
        drawScene(screen,GUY,1)
        
    if keys[K_DOWN] and GUY[Y] < 730:
        GUY[1] += 5
        if GUY[Y] > 245:
            POS[Y]= GUY[Y]-245+130
        else:
            POS[Y] = 130
        drawScene(screen,GUY,0)

running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
    mx,my=mouse.get_pos()
    mb = mouse.get_pressed()
    movePlayer(GUY)
    display.flip()

quit()


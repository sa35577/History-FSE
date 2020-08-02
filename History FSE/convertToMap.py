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




sprites = [image.load("%i.png" % k) for k in range(4)]
for i in range(4):
    sprites[i] = transform.scale(sprites[i],(50,62))
GUY = [100,90]
POS = [100,130]
X = 0
Y = 1
x = image.load("l1.png")
#print(x.get_rect().width)

#print(screen.get_at((65,75)))
screen.blit(x,(0,0))
grass = image.load("grass.png")
back = image.load("background1.png")
#back = transform.scale(back,(1185,380))
#print(screen.get_at((65,75)))
a = 65
b = 75
display.flip()
grass = transform.scale(grass,(20,30))
screen.blit(grass,(60,70))
tiles = [[60,70]]
y = screen.copy()
##screen.blit(back,(50,50))
while True:
    x = 0
    try:
        if y.get_at((a+20,b)) == WHITE:
            tiles.append([a+15,b-5])
            y.blit(grass,(a+15,b-5))
            a += 20
            x = 1
            print(1)
    except:
        pass
    try:
        if y.get_at((a,b+30)) == WHITE and x == 0:
            tiles.append([a-5,b+25])
            y.blit(grass,(a-5,b+25))
            b += 30
            x = 1
            print(2)
    except:
        pass
    if 1 > 0:
        if screen.get_at((a,b-30)) == WHITE and x == 0: 
            y.blit(grass,(a-5,b-35))
            tiles.append([a-5,b-35])
            b -= 30
            x = 1
            print(3)
            
    if x == 0:
        break
    display.flip()
screen.blit(back,(50,50))
for t in tiles:
    screen.blit(grass,(t[0],t[1]))
display.flip()
        
image.save(screen,"realOne.png")


    

running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
    mx,my=mouse.get_pos()
    mb = mouse.get_pressed()
    
    display.flip()
quit()

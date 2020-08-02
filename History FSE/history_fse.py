from pygame import *
from math import *
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
mono2 = font.SysFont("Monospace",40)

##txt files
intro = open("intro.txt")
intro1 = intro.read()

stage = "start"
left = image.load("left.png")
right = image.load("right.png")

sprites = [image.load("%i.png" % k) for k in range(4)]
for i in range(4):
    sprites[i] = transform.scale(sprites[i],(50,62))


levelOne = image.load("l1.png")


#CENTER - 720,360
#PIC WIDTH - 2500PX
#PIC BACK - 255,255,0 (YELLOW)

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

class start:
    def __init__(self,name,posx,posy,ide):
        self.name = name
        self.posx = posx
        self.posy = posy
        self.ide = ide
        self.rectangle = Rect(posx,posy,300,100)
        for i in range(255):
            draw.rect(screen,(0,i,0),(self.rectangle))
            
            if name != "1982-Present":
                screen.blit(mono.render(name,True,(0,0,i)),(posx+20,posy+20))
            else:
                screen.blit(mono2.render(name,True,(0,0,i)),(posx+10,posy+20))
            display.flip()

def collided(obj):
    if obj.rectangle.collidepoint(mx,my) and mb[0] == 1:
        draw.rect(screen,RED,(obj.posx-7,obj.posy-7,314,114),7)
        x = obj.ide
        screen.fill(BLACK)
    elif obj.rectangle.collidepoint(mx,my):
        draw.rect(screen,BLUE,(obj.posx-7,obj.posy-7,314,114),7)
        x = "0"
    else:
        draw.rect(screen,BLACK,(obj.posx-7,obj.posy-7,314,114),7)
        x = "0"
    return x



first = True


running=True
while running:
    for evt in event.get():
        if evt.type==QUIT and stage == "start":
            running=False
        elif  evt.type == QUIT:
            stage = "start"
            screen.fill(BLACK)
            first = True

    mx,my=mouse.get_pos()
    mb = mouse.get_pressed()
    if stage == "start":
        if first:
            floweyFont("History FSE",320,595)
            floweyFont("Sat Arora",400,620)
            sec1 = start("1914-1929",720-200-200-100,360-200-100,"sec1")
            sec2 = start("1929-1945",720-200-200-100,360+200,"sec2")
            sec3 = start("1945-1982",720+200,360-200-100,"sec3")
            sec4 = start("1982-Present",720+200,360+200,"sec4")
            sections = [sec1,sec2,sec3,sec4]
            first = False
        for sec in sections:
            val = collided(sec)
            if val != "0":
                stage = val
                screen.fill(BLACK)
                first = True
    elif stage == "sec1":
        
        if first:
            screen.blit(left,(100,600))
            screen.blit(right,(1250,600))
            first = False
            floweyFont(intro1,50)    
        sec1L = Rect(100,600,50,50)
        sec1R = Rect(1250,600,50,50)
        if sec1L.collidepoint(mx,my) and mb[0] == 1:
            stage = "start"
            screen.fill(BLACK)
            first = True
        elif sec1R.collidepoint(mx,my) and mb[0] == 1:
            subprocess.call("TileMap1a.py",shell=True)
    elif stage == "sec2":
        subprocess.call("TileMap2a.py",shell=True)
        first = True
        stage = "start"
        screen.fill(BLACK)
    elif stage == "sec3":
        subprocess.call("TileMap3a.py",shell=True)
        first = True
        stage = "start"
        screen.fill(BLACK)
    elif stage == "sec4":
        subprocess.call("TileMap4a.py",shell=True)
        first = True
        stage = "start"
        screen.fill(BLACK)

        
    
    display.flip()
intro.close()
quit()

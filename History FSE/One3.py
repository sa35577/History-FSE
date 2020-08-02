from pygame import *

size=width,height=1440,720
screen=display.set_mode(size)
RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
init()

mono = font.SysFont("Monospace",20)
paper = image.load("paper.jpg")
#screen.blit(paper,(0,0))
screen.blit(transform.scale(paper,(2100,1400)),(-300,-300))
para = open("One3.txt")
paragraph = para.read()
def floweyFont(text,height,lower=50,upper=1370):
    fx = lower
    fy = height
    count = 0
    inc = 0
    for char in text:
        if char == "\n" or fx > upper:
            fy+=30
            fx = lower
        else:
            if char == "," or char == "." or char == "!": 
                inc = 400
            else:
                inc = 0
            char = mono.render(char,True,BLACK)
            screen.blit(char,(fx,fy))
            display.flip()
            fx+=10
            #time.wait(65+inc)
        
    #time.wait(1500)

floweyFont(paragraph,50)
display.flip()
para.close()
running = True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
    mx,my=mouse.get_pos()
    mb = mouse.get_pressed()
quit()


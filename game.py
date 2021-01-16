from pygame import *
from Boy import *
from Girl import *
from BoyAI import *
from GirlAI import *

screen = display.set_mode((800,800))


running = True
myClock = time.Clock()

boy = Boy(300,300, [[0 for x in range(3)] for y in range(4)])

while running:
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
        
    boy.moveBoy(boy)
    boy.drawBoy()
    #boy.drawHitbox()
    boy.update()
    myClock.tick(50)
    
quit()

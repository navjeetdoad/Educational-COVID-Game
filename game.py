from pygame import *
from Boy import *
from Girl import *
from BoyAI import *
from GirlAI import *

screen = display.set_mode((800,800))
font.init()

# --- Loading Assets ----------------
background = image.load("Assets/background.png")
titleFont = font.SysFont("Comic Sans MS", 60)
buttonFont = font.SysFont("Comic Sans MS", 48)
# -----------------------------------
def introScreen():
    screen.blit(background, (-5,0))
    titleText = "COVID-19 Education"
    buttonText = "Click here to start!"
    
    title = titleFont.render(titleText, True, (0,0,0))
    button = buttonFont.render(buttonText, True, (0,0,0))

    screen.blit(title, (200,200))
    screen.blit(button, (250, 700))
    
    display.flip()

running = True
myClock = time.Clock()

boy = Boy(300,300, [[0 for x in range(3)] for y in range(4)])

while running:
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False

    introScreen()
    
    #boy.moveBoy(boy)
    #boy.drawBoy()
    #boy.drawHitbox()
    #boy.update()
    myClock.tick(50)
    
quit()

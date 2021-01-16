from pygame import *

screen = display.set_mode((800,600))

def moveCharacter():

    global move, frame
    keys = key.get_pressed()

    
    newMove = -1        
    if keys[K_RIGHT]:
        newMove = RIGHT
        character[0] += 3
    elif keys[K_DOWN]:
        newMove = DOWN
        character[1] += 3
    elif keys[K_UP]:
        newMove = UP
        character[1] -= 3
    elif keys[K_LEFT]:
        newMove = LEFT
        character[0] -= 3
    else:
        frame = 0

    if move == newMove:     # 0 is a standing pose, so we want to skip over it when we are moving
        frame = frame + 0.30 # adding 0.2 allows us to slow down the animation
        if frame >= len(pics[move]):
            frame = 1
    elif newMove != -1:     # a move was selected
        move = newMove      # make that our current move
        frame = 1

def makeMove(name,start,end):
    move = []
    for i in range(start,end+1):
        move.append(image.load("%s/%s%d.png" % (name,name,i)))
        
    return move


def drawScene():
    screen.fill((200,222,255))
    pic = pics[move][int(frame)]
    screen.blit(pic,(character[0]-pic.get_width()//2,character[1]-pic.get_height()//2))            
    display.flip()


RIGHT = 0 # These are just the indices of the moves
DOWN = 1  
UP = 2
LEFT = 3

pics = [] #2d list
pics.append(makeMove("RIGHT",0,2))      # RIGHT
pics.append(makeMove("DOWN",0,2))     # DOWN
pics.append(makeMove("UP",0,2))    # UP
pics.append(makeMove("LEFT",0,2))    # LEFT

frame = 0     # current frame within the move
move = 0      # current move being performed (right, down, up, left)

character=[300,300]

running = True
myClock = time.Clock()

while running:
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
        
    moveCharacter()          
    drawScene()
    myClock.tick(50)
    
quit()

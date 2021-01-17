from pygame import *
import pygame

screen = display.set_mode((950, 800))
font.init()

# --- Loading Assets ----------------
leftHand = image.load("Assets/handLeft.png")
rightHand = image.load("Assets/handRight.png")
tap = image.load("Assets/waterTap.png")
titleFont = font.SysFont("Comic Sans MS", 60)


# -----------------------------------
def introScreen():
    screen.fill((255, 255, 255))
    titleText = "PAUSED"
    title = titleFont.render(titleText, True, (0, 0, 0))

    screen.blit(title, (200, 200))
    screen.blit(tap, (0, 0))
    screen.blit(leftHand, (150, 350))
    screen.blit(rightHand, (480, 350))

    display.flip()


# boy = Boy(300,300, [[0 for x in range(3)] for y in range(4)])

pygame.init()
running = True
clock = pygame.time.Clock()

while running:
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False

    clock.tick(50)
    introScreen()

quit()
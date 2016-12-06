import pygame
pygame.init()

gameDisplay= pygame.display.set_mode((800, 600))

xcoor = 0 #the leader of the group of blocks
ycoor = 550

jump = False
fall = False
gameExit = False

while not gameExit:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not fall:
                    jump = True

    if jump:
        ycoor += 5
        if ycoor >= 500:
            ycoor = 500
            jump = False
            fall = True

    if fall:
        ycoor -= 5
        if ycoor <= 0:
            ycoor = 0
            fall = False

    pygame.draw.rect(gameDisplay, (164, 66, 244),[xcoor,ycoor,50,50])
pygame.quit() #unintiliazes pygames
quit()

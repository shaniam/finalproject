from models import ourMusic, sprites
import pygame
import os
import time

pygame.init() #short for initialize does return a tuple of successful intilizaton
colors={"black":(0,0,0), "white": (255, 255, 255), "red": (255, 0, 0), "green": (0, 255, 0), "purple": (164, 66, 244), "pink" :(252, 25, 123)}
gameDisplay= pygame.display.set_mode((800, 600))

bg=pygame.image.load('clouds_converted.jpg')
moore=pygame.image.load("baemoore_converted.png")
jump = False
fall = False

cube = pygame.image.load("cube.png")
player=sprites(moore, 50, 544)

ob = sprites(cube, 2125, 580)
ob1 = sprites(cube, 2125, 580)
ob2 = sprites(cube, 2125, 580)
ob3 = sprites(cube, 2125, 580)
ob4 = sprites(cube, 2125, 580)
ob5 = sprites(cube, 2125, 580)
ob6 = sprites(cube, 2125, 580)
ob7 = sprites(cube, 2125, 580)
ob8 = sprites(cube, 2125, 580)
ob9 = sprites(cube, 2125, 580)
ob10 = sprites(cube, 2125, 580)
ob11 = sprites(cube, 2125, 580)
ob12 = sprites(cube, 2125, 580)
ob13 = sprites(cube, 2125, 580)
ob14 = sprites(cube, 2125, 580)
ob15 = sprites(cube, 2125, 580)
ob16 = sprites(cube, 2125, 580)
ob17 = sprites(cube, 2125, 580)
ob18 = sprites(cube, 2125, 580)
ob19 = sprites(cube, 2125, 580)
ob20 = sprites(cube, 2125, 580)
ob21 = sprites(cube, 2125, 580)
ob22 = sprites(cube, 2125, 580)
ob23 = sprites(cube, 2125, 580)
ob24 = sprites(cube, 2125, 580)
ob25 = sprites(cube, 2125, 580)
ob26 = sprites(cube, 2125, 580)
ob27 = sprites(cube, 2125, 580)
ob28 = sprites(cube, 2125, 580)
ob29 = sprites(cube, 2125, 580)
ob30 = sprites(cube, 2125, 580)
ob31 = sprites(cube, 2125, 580)
ob32 = sprites(cube, 2125, 580)
ob33 = sprites(cube, 2125, 580)
ob34 = sprites(cube, 2125, 580)
ob35 = sprites(cube, 2125, 580)
ob36 = sprites(cube, 2125, 580)
ob37 = sprites(cube, 2125, 580)
ob38 = sprites(cube, 2125, 580)
ob39 = sprites(cube, 2125, 580)
ob40 = sprites(cube, 2125, 580)
ob41 = sprites(cube, 2125, 580)
ob42 = sprites(cube, 2125, 580)
ob43 = sprites(cube, 2125, 580)
ob44 = sprites(cube, 2125, 580)
ob45 = sprites(cube, 2125, 580)
ob46 = sprites(cube, 2125, 580)
ob47 = sprites(cube, 2125, 580)
ob48 = sprites(cube, 2125, 580)
ob49 = sprites(cube, 2125, 580)
ob50 = sprites(cube, 2125, 580)
ob51 = sprites(cube, 2125, 580)
ob52 = sprites(cube, 2125, 580)
ob53 = sprites(cube, 2125, 580)
ob54 = sprites(cube, 2125, 580)
ob55 = sprites(cube, 2125, 580)
ob56 = sprites(cube, 2125, 580)
ob57 = sprites(cube, 2125, 580)
ob58 = sprites(cube, 2125, 580)
ob59 = sprites(cube, 2125, 580)
ob60 = sprites(cube, 2125, 580)
ob61 = sprites(cube, 2125, 580)
ob62 = sprites(cube, 2125, 580)
ob63 = sprites(cube, 2125, 580)
ob64 = sprites(cube, 2125, 580)
ob65 = sprites(cube, 2125, 580)
ob66 = sprites(cube, 2125, 580)
ob67 = sprites(cube, 2125, 580)
ob68 = sprites(cube, 2125, 580)
ob69 = sprites(cube, 2125, 580)
ob70 = sprites(cube, 2125, 580)
ob71 = sprites(cube, 2125, 580)
ob72 = sprites(cube, 2125, 580)
ob73 = sprites(cube, 2125, 580)
ob74 = sprites(cube, 2125, 580)
ob75 = sprites(cube, 2125, 580)
ob76 = sprites(cube, 2125, 580)
ob77 = sprites(cube, 2125, 580)
ob78 = sprites(cube, 2125, 580)
ob79 = sprites(cube, 2125, 580)
ob80 = sprites(cube, 2125, 580)
ob81 = sprites(cube, 2125, 580)
ob82 = sprites(cube, 2125, 580)
ob83 = sprites(cube, 2125, 580)
ob84 = sprites(cube, 2125, 580)
ob85 = sprites(cube, 2125, 580)
ob86 = sprites(cube, 2125, 580)
ob87 = sprites(cube, 2125, 580)
ob88 = sprites(cube, 2125, 580)
ob89 = sprites(cube, 2125, 580)
ob90 = sprites(cube, 2125, 580)
ob91 = sprites(cube, 2125, 580)
ob92 = sprites(cube, 2125, 580)
ob93 = sprites(cube, 2125, 580)
ob94 = sprites(cube, 2125, 580)
ob95 = sprites(cube, 2125, 580)
ob96 = sprites(cube, 2125, 580)
ob97 = sprites(cube, 2125, 580)
ob98 = sprites(cube, 2125, 580)
ob99 = sprites(cube, 2125, 580)
ob100 = sprites(cube, 2125, 580)
ob101 = sprites(cube, 2125, 580)
ob102 = sprites(cube, 2125, 580)
ob103 = sprites(cube, 2125, 580)
ob104 = sprites(cube, 2125, 580)
ob105 = sprites(cube, 2125, 580)
ob106 = sprites(cube, 2125, 580)
ob107 = sprites(cube, 2125, 580)
ob108 = sprites(cube, 2125, 580)
ob109 = sprites(cube, 2125, 580)
ob110 = sprites(cube, 2125, 580)
ob111 = sprites(cube, 2125, 580)
ob112 = sprites(cube, 2125, 580)
ob113 = sprites(cube, 2125, 580)
ob114 = sprites(cube, 2125, 580)
ob115 = sprites(cube, 2125, 580)
ob116 = sprites(cube, 2125, 580)
ob117 = sprites(cube, 2125, 580)
ob118 = sprites(cube, 2125, 580)
ob119 = sprites(cube, 2125, 580)
ob120 = sprites(cube, 2125, 580)
ob121 = sprites(cube, 2125, 580)
ob122 = sprites(cube, 2125, 580)
ob123 = sprites(cube, 2125, 580)
ob124 = sprites(cube, 2125, 580)
ob125 = sprites(cube, 2125, 580)
ob126 = sprites(cube, 2125, 580)
ob127 = sprites(cube, 2125, 580)
ob128 = sprites(cube, 2125, 580)
ob129 = sprites(cube, 2125, 580)
ob130 = sprites(cube, 2125, 580)
ob131 = sprites(cube, 2125, 580)
ob132 = sprites(cube, 2125, 580)
ob133 = sprites(cube, 2125, 580)





pygame.display.set_caption("lets play!")
theSong=ourMusic("m83.ogg")
theSong.musicUpload()
theSong.musicPlay()
gameExit = False
clock = pygame.time.Clock()



spritesgroup=pygame.sprite.Group()
spritesgroup.add(ob, ob1, ob2, ob3, ob4, ob5, ob6, ob7, ob8, ob9, ob10,
                 ob11, ob12, ob13, ob14, ob15, ob16, ob17, ob18, ob19, ob20,
                 ob21, ob22, ob23, ob24, ob25, ob26, ob27, ob28, ob29, ob30,
                 ob31, ob32, ob33, ob34, ob35, ob36, ob37, ob38, ob39, ob40,
                 ob41, ob42, ob43, ob44, ob45, ob46, ob47, ob48, ob49, ob50,
                 ob51, ob52, ob53, ob54, ob55, ob56, ob57, ob58, ob59, ob60,
                 ob61, ob62, ob63, ob64, ob65, ob66, ob67, ob68, ob69, ob70,
                 ob71, ob72, ob73, ob74, ob75, ob76, ob77, ob78, ob79, ob80,
                 ob81, ob82, ob83, ob84, ob85, ob86, ob87, ob88, ob89, ob90,
                 ob91, ob92, ob93, ob94, ob95, ob96, ob97, ob98, ob99, ob100,
                 ob101, ob102, ob103, ob104, ob105, ob106, ob107, ob108, ob109, ob110,
                 ob111, ob112, ob113, ob114, ob115, ob116, ob117, ob118, ob119, ob120,
                 ob121, ob122, ob123, ob124, ob125, ob126, ob127, ob128, ob129, ob130,
                 ob131, ob132, ob133)

score=600

while not gameExit:
    clock.tick(40)
    timer = pygame.time.get_ticks()
    #print(timer)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameExit=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not fall:
                    jump = True
            if event.key == pygame.K_ESCAPE:
                gameExit= True
    if jump:
        player.rect.y -= 16
        if player.rect.y <= 410:
            ycoor = 500
            jump = False
            fall = True

    if fall:
        player.rect.y += 16
        if player.rect.y >= 544:
            ycoor = 0
            fall = False
    pygame.display.update()
    gameDisplay.blit(bg,[0,0])
    time.sleep(.05)
    player.pos()
    ob.pos()
    ob.left(7)
    ob1.pos()
    ob2.pos()
    ob3.pos()
    ob4.pos()
    ob5.pos()
    ob6.pos()
    ob7.pos()
    ob8.pos()
    ob9.pos()
    ob10.pos()
    ob11.pos()
    ob12.pos()
    ob13.pos()
    ob14.pos()
    ob15.pos()
    ob16.pos()
    ob17.pos()
    ob18.pos()
    ob19.pos()
    ob20.pos()
    ob21.pos()
    ob22.pos()
    ob23.pos()
    ob24.pos()
    ob25.pos()
    ob26.pos()
    ob27.pos()
    ob28.pos()
    ob29.pos()
    ob30.pos()
    ob31.pos()
    ob32.pos()
    ob33.pos()
    ob34.pos()
    ob35.pos()
    ob36.pos()
    ob37.pos()
    ob38.pos()
    ob39.pos()
    ob40.pos()
    ob41.pos()
    ob42.pos()
    ob43.pos()
    ob44.pos()
    ob45.pos()
    ob46.pos()
    ob47.pos()
    ob48.pos()
    ob49.pos()
    ob50.pos()
    ob51.pos()
    ob52.pos()
    ob53.pos()
    ob54.pos()
    ob55.pos()
    ob56.pos()
    ob57.pos()
    ob58.pos()
    ob59.pos()
    ob60.pos()
    ob61.pos()
    ob62.pos()
    ob63.pos()
    ob64.pos()
    ob65.pos()
    ob66.pos()
    ob67.pos()
    ob68.pos()
    ob69.pos()
    ob70.pos()
    ob71.pos()
    ob72.pos()
    ob73.pos()
    ob74.pos()
    ob76.pos()
    ob77.pos()
    ob78.pos()
    ob79.pos()
    ob80.pos()
    ob81.pos()
    ob82.pos()
    ob83.pos()
    ob84.pos()
    ob85.pos()
    ob86.pos()
    ob87.pos()
    ob89.pos()
    ob90.pos()
    ob91.pos()
    ob92.pos()
    ob93.pos()
    ob94.pos()
    ob95.pos()
    ob96.pos()
    ob97.pos()
    ob98.pos()
    ob99.pos()
    ob100.pos()
    ob101.pos()
    ob102.pos()
    ob103.pos()
    ob104.pos()
    ob105.pos()
    ob106.pos()
    ob107.pos()
    ob108.pos()
    ob109.pos()
    ob110.pos()
    ob111.pos()
    ob112.pos()
    ob113.pos()
    ob114.pos()
    ob115.pos()
    ob116.pos()
    ob117.pos()
    ob118.pos()
    ob119.pos()
    ob120.pos()
    ob121.pos()
    ob122.pos()
    ob123.pos()
    ob124.pos()
    ob125.pos()
    ob126.pos()
    ob127.pos()
    ob128.pos()
    ob129.pos()
    ob130.pos()
    ob131.pos()
    ob132.pos()
    ob133.pos()


    if(timer > 1200):
        ob1.left(7)
    if(timer > 2800):
        ob2.left(7)
    if(timer > 4000):
        ob3.left(7)
    if(timer > 5200):
        ob4.left(7)
    if(timer > 6400):
        ob5.left(7)
    if(timer > 7600):
        ob6.left(7)
    if(timer > 8800):
        ob7.left(7)
    if(timer > 10000):
        ob8.left(7)
    if(timer > 11200):
        ob9.left(7)
    if(timer > 12400):
        ob10.left(7)
    if(timer > 13600):
        ob11.left(7)
    if(timer > 14800):
        ob12.left(7)
    if(timer > 16000):
        ob13.left(7)
    if(timer > 17200):
        ob14.left(7)
    if(timer > 18400):
        ob15.left(7)
    if(timer > 20800):
        ob16.left(7)
    if(timer > 22000):
        ob17.left(7)
    if(timer > 23200):
        ob18.left(7)
    if(timer > 24400):
        ob19.left(7)
    if(timer > 25600):
        ob20.left(7)
    if(timer > 29200):
        ob21.left(7)
    if(timer > 30400):
        ob22.left(7)
    if(timer > 31600):
        ob23.left(7)
    if(timer > 32800):
        ob24.left(7)
    if(timer > 34000):
        ob25.left(7)
    if(timer > 35200):
        ob26.left(7)
    if(timer > 36400):
        ob27.left(7)
    if(timer > 37600):
        ob28.left(7)
    if(timer > 38800):
        ob29.left(7)
    if(timer > 41200):
        ob30.left(7)
    if(timer > 44800):
        ob31.left(7)
    if(timer > 46000):
        ob32.left(7)
    if(timer > 47200):
        ob33.left(7)
    if(timer > 48400):
        ob34.left(7)
    if(timer > 50800):
        ob35.left(7)
    if(timer > 53200):
        ob36.left(7)
    if(timer > 54400):
        ob37.left(7)
    if(timer > 55600):
        ob38.left(7)
    if(timer > 59200):
        ob39.left(7)
    if(timer > 60400):
        ob40.left(7)
    if(timer > 61600):
        ob41.left(7)
    if(timer > 62800):
        ob42.left(7)
    if(timer > 65200):
        ob43.left(7)
    if(timer > 66400):
        ob44.left(7)
    if(timer > 70000):
        ob45.left(7)
    if(timer > 71200):
        ob46.left(7)
    if(timer > 72400):
        ob47.left(7)
    if(timer > 74800):
        ob48.left(7)
    if(timer > 76000):
        ob49.left(7)
    if(timer > 77200):
        ob50.left(7)
    if(timer > 79400):
        ob51.left(7)
    if(timer > 80800):
        ob52.left(7)
    if(timer > 84400):
        ob53.left(7)
    if(timer > 85600):
        ob54.left(7)
    if(timer > 86800):
        ob55.left(7)
    if(timer > 88000):
        ob56.left(7)
    if(timer > 89200):
        ob57.left(7)
    if(timer > 90400):
        ob58.left(7)
    if(timer > 94000):
        ob59.left(7)
    if(timer > 95200):
        ob60.left(7)
    if(timer > 96400):
        ob61.left(7)
    if(timer > 98600):
        ob62.left(7)
    if(timer > 102200):
        ob63.left(7)
    if(timer > 103400):
        ob64.left(7)
    if(timer > 104600):
        ob65.left(7)
    if(timer > 105800):
        ob66.left(7)
    if(timer > 108200):
        ob67.left(7)
    if(timer > 109400):
        ob68.left(7)
    if(timer > 111800):
        ob69.left(7)
    if(timer > 113000):
        ob70.left(7)
    if(timer > 114200):
        ob71.left(7)
    if(timer > 115400):
        ob72.left(7)
    if(timer > 119000):
        ob73.left(7)
    if(timer > 120200):
        ob74.left(7)
    if(timer > 121400):
        ob75.left(7)
    if(timer > 122600):
        ob76.left(7)
    if(timer > 123800):
        ob77.left(7)
    if(timer > 125000):
        ob78.left(7)
    if(timer > 128600):
        ob79.left(7)
    if(timer > 131000):
        ob80.left(7)
    if(timer > 133400):
        ob81.left(7)
    if(timer > 134600):
        ob82.left(7)
    if(timer > 135800):
        ob83.left(7)
    if(timer > 137000):
        ob84.left(7)
    if(timer > 138200):
        ob85.left(7)
    if(timer > 139400):
        ob86.left(7)
    if(timer > 140600):
        ob87.left(7)
    if(timer > 144200):
        ob88.left(7)
    if(timer > 145400):
        ob89.left(7)
    if(timer > 146600):
        ob90.left(7)
    if(timer > 147800):
        ob91.left(7)
    if(timer > 150200):
        ob92.left(7)
    if(timer > 151400):
        ob93.left(7)
    if(timer > 152600):
        ob94.left(7)
    if(timer > 153800):
        ob95.left(7)
    if(timer > 156000):
        ob96.left(7)
    if(timer > 159600):
        ob97.left(7)
    if(timer > 160800):
        ob98.left(7)
    if(timer > 162000):
        ob99.left(7)
    if(timer > 163200):
        ob100.left(7)
    if(timer > 164400):
        ob101.left(7)
    if(timer > 165600):
        ob102.left(7)
    if(timer > 168000):
        ob103.left(7)
    if(timer > 170400):
        ob104.left(7)
    if(timer > 171600):
        ob105.left(7)
    if(timer > 172800):
        ob106.left(7)
    if(timer > 174000):
        ob107.left(7)
    if(timer > 177600):
        ob108.left(7)
    if(timer > 178800):
        ob109.left(7)
    if(timer > 180000):
        ob110.left(7)
    if(timer > 181200):
        ob111.left(7)
    if(timer > 182400):
        ob112.left(7)
    if(timer > 183600):
        ob113.left(7)
    if(timer > 184800):
        ob114.left(7)
    if(timer > 186000):
        ob115.left(7)
    if(timer > 188400):
        ob116.left(7)
    if(timer > 192000):
        ob117.left(7)
    if(timer > 193200):
        ob118.left(7)
    if(timer > 194400):
        ob119.left(7)
    if(timer > 196600):
        ob120.left(7)
    if(timer > 198800):
        ob121.left(7)
    if(timer > 200000):
        ob122.left(7)
    if(timer > 201200):
        ob123.left(7)
    if(timer > 202400):
        ob124.left(7)
    if(timer > 203600):
        ob125.left(7)
    if(timer > 204800):
        ob126.left(7)
    if(timer > 206000):
        ob127.left(7)
    if(timer > 207200):
        ob128.left(7)
    if(timer > 208400):
        ob129.left(7)
    if(timer > 209600):
        ob130.left(7)
    if(timer > 210800):
        ob131.left(7)
    if(timer > 212000):
        ob132.left(7)
    if(timer > 213200):
        ob133.left(7)


    blocks_hit_list = pygame.sprite.spritecollide(player, spritesgroup, True)
    print(blocks_hit_list)
    if (blocks_hit_list!=[]):
        score-=10
        print(score)

pygame.quit() #unintiliazes pygames
quit() #this will exit out of python

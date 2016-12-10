from models import ourMusic, sprites
import pygame
import os
import time

pygame.init() #short for initialize does return a tuple of successful intilizaton
colors={"black":(0,0,0), "white": (255, 255, 255), "red": (255, 0, 0), "green": (0, 255, 0), "purple": (164, 66, 244), "pink" :(252, 25, 123)}
gameDisplay= pygame.display.set_mode((800, 600))

bg=pygame.image.load('clouds_converted.jpg')
moore=pygame.image.load("baemoore_converted.png")
myfont = pygame.font.SysFont("Extrude.ttf", 30)
myfonter =pygame.font.SysFont("AldotheApache",60)
jump = False
fall = False


cube = pygame.image.load("cube.png")
pointob=sprites(cube, -10, 580) #the cube it will hit
pointob.pos()
player=sprites(moore, 50, 544)

score=0
y=str(score)
scorething=open("hometownscores.txt", "r")
scoresentence=scorething.readline()
b=scoresentence.strip()
b=int(b)
scorething.close()


ob = sprites(cube, 10000, 580)
ob1 = sprites(cube, 10000, 580)
ob2 = sprites(cube, 10000, 580)
ob3 = sprites(cube, 10000, 580)
ob4 = sprites(cube, 10000, 580)
ob5 = sprites(cube, 10000, 580)
ob6 = sprites(cube, 10000, 580)
ob7 = sprites(cube, 10000, 580)
ob8 = sprites(cube, 10000, 580)
ob9 = sprites(cube, 10000, 580)
ob10 = sprites(cube, 10000, 580)
ob11 = sprites(cube, 10000, 580)
ob12 = sprites(cube, 10000, 580)
ob13 = sprites(cube, 10000, 580)
ob14 = sprites(cube, 10000, 580)
ob15 = sprites(cube, 10000, 580)
ob16 = sprites(cube, 10000, 580)
ob17 = sprites(cube, 10000, 580)
ob18 = sprites(cube, 10000, 580)
ob19 = sprites(cube, 10000, 580)
ob20 = sprites(cube, 10000, 580)
ob21 = sprites(cube, 10000, 580)
ob22 = sprites(cube, 10000, 580)
ob23 = sprites(cube, 10000, 580)
ob24 = sprites(cube, 10000, 580)
ob25 = sprites(cube, 10000, 580)
ob26 = sprites(cube, 10000, 580)
ob27 = sprites(cube, 10000, 580)
ob28 = sprites(cube, 10000, 580)
ob29 = sprites(cube, 10000, 580)
ob30 = sprites(cube, 10000, 580)
ob31 = sprites(cube, 10000, 580)
ob32 = sprites(cube, 10000, 580)
ob33 = sprites(cube, 10000, 580)
ob34 = sprites(cube, 10000, 580)
ob35 = sprites(cube, 10000, 580)
ob36 = sprites(cube, 10000, 580)
ob37 = sprites(cube, 10000, 580)
ob38 = sprites(cube, 10000, 580)
ob39 = sprites(cube, 10000, 580)
ob40 = sprites(cube, 10000, 580)
ob41 = sprites(cube, 10000, 580)
ob42 = sprites(cube, 10000, 580)
ob43 = sprites(cube, 10000, 580)
ob44 = sprites(cube, 10000, 580)
ob45 = sprites(cube, 10000, 580)
ob46 = sprites(cube, 10000, 580)
ob47 = sprites(cube, 10000, 580)
ob48 = sprites(cube, 10000, 580)
ob49 = sprites(cube, 10000, 580)
ob50 = sprites(cube, 10000, 580)
ob51 = sprites(cube, 10000, 580)
ob52 = sprites(cube, 10000, 580)
ob53 = sprites(cube, 10000, 580)
ob54 = sprites(cube, 10000, 580)
ob55 = sprites(cube, 10000, 580)
ob56 = sprites(cube, 10000, 580)
ob57 = sprites(cube, 10000, 580)
ob58 = sprites(cube, 10000, 580)
ob59 = sprites(cube, 10000, 580)
ob60 = sprites(cube, 10000, 580)
ob61 = sprites(cube, 10000, 580)
ob62 = sprites(cube, 10000, 580)
ob63 = sprites(cube, 10000, 580)
ob64 = sprites(cube, 10000, 580)
ob65 = sprites(cube, 10000, 580)
ob66 = sprites(cube, 10000, 580)
ob67 = sprites(cube, 10000, 580)
ob68 = sprites(cube, 10000, 580)
ob69 = sprites(cube, 10000, 580)
ob70 = sprites(cube, 10000, 580)
ob71 = sprites(cube, 10000, 580)
ob72 = sprites(cube, 10000, 580)
ob73 = sprites(cube, 10000, 580)
ob74 = sprites(cube, 10000, 580)
ob75 = sprites(cube, 10000, 580)
ob76 = sprites(cube, 10000, 580)
ob77 = sprites(cube, 10000, 580)
ob78 = sprites(cube, 10000, 580)
ob79 = sprites(cube, 10000, 580)
ob80 = sprites(cube, 10000, 580)
ob81 = sprites(cube, 10000, 580)
ob82 = sprites(cube, 10000, 580)
ob83 = sprites(cube, 10000, 580)
ob84 = sprites(cube, 10000, 580)
ob85 = sprites(cube, 10000, 580)
ob86 = sprites(cube, 10000, 580)
ob87 = sprites(cube, 10000, 580)
ob88 = sprites(cube, 10000, 580)
ob89 = sprites(cube, 10000, 580)
ob90 = sprites(cube, 10000, 580)
ob91 = sprites(cube, 10000, 580)
ob92 = sprites(cube, 10000, 580)
ob93 = sprites(cube, 10000, 580)
ob94 = sprites(cube, 10000, 580)
ob95 = sprites(cube, 10000, 580)
ob96 = sprites(cube, 10000, 580)
ob97 = sprites(cube, 10000, 580)
ob98 = sprites(cube, 10000, 580)
ob99 = sprites(cube, 10000, 580)
ob100 = sprites(cube, 10000, 580)
ob101 = sprites(cube, 10000, 580)
ob102 = sprites(cube, 10000, 580)
ob103 = sprites(cube, 10000, 580)
ob104 = sprites(cube, 10000, 580)
ob105 = sprites(cube, 10000, 580)
ob106 = sprites(cube, 10000, 580)
ob107 = sprites(cube, 10000, 580)
ob108 = sprites(cube, 10000, 580)
ob109 = sprites(cube, 10000, 580)
ob110 = sprites(cube, 10000, 580)
ob111 = sprites(cube, 10000, 580)
ob112 = sprites(cube, 10000, 580)
ob113 = sprites(cube, 10000, 580)
ob114 = sprites(cube, 10000, 580)
ob115 = sprites(cube, 10000, 580)
ob116 = sprites(cube, 10000, 580)
ob117 = sprites(cube, 10000, 580)
ob118 = sprites(cube, 10000, 580)
ob119 = sprites(cube, 10000, 580)
ob120 = sprites(cube, 10000, 580)
ob121 = sprites(cube, 10000, 580)
ob122 = sprites(cube, 10000, 580)
ob123 = sprites(cube, 10000, 580)
ob124 = sprites(cube, 10000, 580)
ob125 = sprites(cube, 10000, 580)
ob126 = sprites(cube, 10000, 580)
ob127 = sprites(cube, 10000, 580)
ob128 = sprites(cube, 10000, 580)
ob129 = sprites(cube, 10000, 580)
ob130 = sprites(cube, 10000, 580)
ob131 = sprites(cube, 10000, 580)
ob132 = sprites(cube, 10000, 580)
ob133 = sprites(cube, 10000, 580)
ob134 = sprites(cube, 10000, 580)
ob135 = sprites(cube, 10000, 580)
ob136 = sprites(cube, 10000, 580)
ob137 = sprites(cube, 10000, 580)
ob138 = sprites(cube, 10000, 580)
ob139 = sprites(cube, 10000, 580)
ob140 = sprites(cube, 10000, 580)
ob141 = sprites(cube, 10000, 580)
ob142 = sprites(cube, 10000, 580)
ob143 = sprites(cube, 10000, 580)
ob144 = sprites(cube, 10000, 580)
ob145 = sprites(cube, 10000, 580)
ob146 = sprites(cube, 10000, 580)
ob147 = sprites(cube, 10000, 580)
ob148 = sprites(cube, 10000, 580)
ob149 = sprites(cube, 10000, 580)
ob150 = sprites(cube, 10000, 580)
ob151 = sprites(cube, 10000, 580)
ob152 = sprites(cube, 10000, 580)
ob153 = sprites(cube, 10000, 580)
ob154 = sprites(cube, 10000, 580)
ob155 = sprites(cube, 10000, 580)
ob156 = sprites(cube, 10000, 580)
ob157 = sprites(cube, 10000, 580)
ob158 = sprites(cube, 10000, 580)
ob159 = sprites(cube, 10000, 580)
ob160 = sprites(cube, 10000, 580)
ob161 = sprites(cube, 10000, 580)
ob162 = sprites(cube, 10000, 580)
ob163 = sprites(cube, 10000, 580)
ob164 = sprites(cube, 10000, 580)
ob165 = sprites(cube, 10000, 580)
ob166 = sprites(cube, 10000, 580)
ob167 = sprites(cube, 10000, 580)
ob168 = sprites(cube, 10000, 580)
ob169 = sprites(cube, 10000, 580)
ob170 = sprites(cube, 10000, 580)
ob171 = sprites(cube, 10000, 580)
ob172 = sprites(cube, 10000, 580)
ob173 = sprites(cube, 10000, 580)
ob174 = sprites(cube, 10000, 580)
ob175 = sprites(cube, 10000, 580)
ob176 = sprites(cube, 10000, 580)
ob177 = sprites(cube, 10000, 580)
ob178 = sprites(cube, 10000, 580)
ob179 = sprites(cube, 10000, 580)
ob180 = sprites(cube, 10000, 580)
ob181 = sprites(cube, 10000, 580)
ob182 = sprites(cube, 10000, 580)
ob183 = sprites(cube, 10000, 580)
ob184 = sprites(cube, 10000, 580)
ob185 = sprites(cube, 10000, 580)
ob186 = sprites(cube, 10000, 580)
ob187 = sprites(cube, 10000, 580)
ob188 = sprites(cube, 10000, 580)
ob189 = sprites(cube, 10000, 580)
ob190 = sprites(cube, 10000, 580)
ob191 = sprites(cube, 10000, 580)
ob192 = sprites(cube, 10000, 580)
ob193 = sprites(cube, 10000, 580)
ob194 = sprites(cube, 10000, 580)
ob195 = sprites(cube, 10000, 580)
ob196 = sprites(cube, 10000, 580)
ob197 = sprites(cube, 10000, 580)
ob198 = sprites(cube, 10000, 580)
ob199 = sprites(cube, 10000, 580)
ob200 = sprites(cube, 10000, 580)
ob201 = sprites(cube, 10000, 580)
ob202 = sprites(cube, 10000, 580)
ob203 = sprites(cube, 10000, 580)
ob204 = sprites(cube, 10000, 580)
ob205 = sprites(cube, 10000, 580)
ob206 = sprites(cube, 10000, 580)
ob207 = sprites(cube, 10000, 580)
ob208 = sprites(cube, 10000, 580)
ob209 = sprites(cube, 10000, 580)
ob210 = sprites(cube, 10000, 580)
ob211 = sprites(cube, 10000, 580)
ob212 = sprites(cube, 10000, 580)
ob213 = sprites(cube, 10000, 580)
ob214 = sprites(cube, 10000, 580)
ob215 = sprites(cube, 10000, 580)
ob216 = sprites(cube, 10000, 580)
ob217 = sprites(cube, 10000, 580)
ob218 = sprites(cube, 10000, 580)
ob219 = sprites(cube, 10000, 580)
ob220 = sprites(cube, 10000, 580)
ob221 = sprites(cube, 10000, 580)
ob222 = sprites(cube, 10000, 580)
ob223 = sprites(cube, 10000, 580)
ob224 = sprites(cube, 10000, 580)
ob225 = sprites(cube, 10000, 580)
ob226 = sprites(cube, 10000, 580)

pygame.display.set_caption("lets play!")
theSong=ourMusic("hometown.ogg")
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
                 ob131, ob132, ob133, ob134, ob135, ob136, ob137, ob138, ob139, ob140,
                 ob141, ob142, ob143, ob144, ob145, ob146, ob147, ob148, ob149, ob150,
                 ob151, ob152, ob153, ob154, ob155, ob156, ob157, ob158, ob159, ob160,
                 ob161, ob162, ob163, ob164, ob165, ob166, ob167, ob168, ob169, ob170,
                 ob171, ob172, ob173, ob174, ob175, ob176, ob177, ob178, ob179, ob180,
                 ob181, ob182, ob183, ob184, ob185, ob186, ob187, ob188, ob189, ob190,
                 ob191, ob192, ob193, ob194, ob195, ob196, ob197, ob198, ob199, ob200,
                 ob201, ob202, ob203, ob204, ob205, ob206, ob207, ob208, ob209, ob210,
                 ob211, ob212, ob213, ob214, ob215, ob216, ob217, ob218, ob219, ob220,
                 ob221, ob222, ob223, ob224, ob225, ob226)#, ob227, ob228, ob229, ob230)

score=0
y=str(score)

while not gameExit:
    clock.tick(40)
    timer = pygame.time.get_ticks()
    print(timer)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameExit=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not fall:
                    print("************************HELLO************************")
                    print("************************HELLO************************")
                    print("************************HELLO************************")
                    print("************************HELLO************************")
                    print("************************HELLO************************")
                    print("************************HELLO************************")
                    print("************************HELLO************************")
                    print("************************HELLO************************")
                    print("************************HELLO************************")
                    print("************************HELLO************************")
                    jump = True
            if event.key == pygame.K_RETURN:
                gameExit= True
    if jump:
        player.rect.y -= 60
        if player.rect.y <= 410:
            ycoor = 500
            jump = False
            fall = True

    if fall:
        player.rect.y += 60
        if player.rect.y >= 544:
            ycoor = 0
            fall = False
    pygame.display.update()
    gameDisplay.blit(bg,[0,0])
    time.sleep(.05)
    player.pos()
    spritesgroup.draw(gameDisplay)
    ob.left(40)
    if(timer > 1700):
        ob1.left(40)
    if(timer > 2700):
        ob2.left(40)
    if(timer > 3700):
        ob3.left(40)
    if(timer > 4700):
        ob4.left(40)
    if(timer > 5700):
        ob5.left(40)
    if(timer > 6700):
        ob6.left(40)
    if(timer > 7700):
        ob7.left(40)
    if(timer > 8700):
        ob8.left(40)
    if(timer > 9700):
        ob9.left(40)
    if(timer > 10700):
        ob10.left(40)
    if(timer > 11700):
        ob11.left(40)
    if(timer > 12700):
        ob12.left(40)
    if(timer > 13700):
        ob13.left(40)
    if(timer > 14700):
        ob14.left(40)
    if(timer > 15700):
        ob15.left(40)
    if(timer > 16700):
        ob16.left(40)
    if(timer > 17700):
        ob17.left(40)
    if(timer > 18700):
        ob18.left(40)
    if(timer > 19700):
        ob19.left(40)
    if(timer > 20700):
        ob20.left(40)
    if(timer > 21700):
        ob21.left(40)
    if(timer > 22700):
        ob22.left(40)
    if(timer > 23700):
        ob23.left(40)
    if(timer > 25200):
        ob24.left(40)
    if(timer > 26200):
        ob25.left(40)
    if(timer > 27200):
        ob26.left(40)
    if(timer > 28200):
        ob27.left(40)
    if(timer > 29200):
        ob28.left(40)
    if(timer > 30200):
        ob29.left(40)
    if(timer > 31200):
        ob30.left(40)
    if(timer > 32200):
        ob31.left(40)
    if(timer > 33200):
        ob32.left(40)
    if(timer > 34200):
        ob33.left(40)
    if(timer > 35200):
        ob34.left(40)
    if(timer > 36200):
        ob35.left(40)
    if(timer > 37200):
        ob36.left(40)
    if(timer > 40700):
        ob37.left(40)
    if(timer > 41200):
        ob38.left(40)
    if(timer > 41700):
        ob39.left(40)
    if(timer > 42200):
        ob40.left(40)
    if(timer > 42700):
        ob41.left(40)
    if(timer > 43200):
        ob42.left(40)
    if(timer > 43700):
        ob43.left(40)
    if(timer > 44200):
        ob44.left(40)
    if(timer > 44700):
        ob45.left(40)
    if(timer > 45200):
        ob46.left(40)
    if(timer > 45700):
        ob47.left(40)
    if(timer > 46200):
        ob48.left(40)
    if(timer > 46700):
        ob49.left(40)
    if(timer > 47200):
        ob50.left(40)
    if(timer > 47700):
        ob51.left(40)
    if(timer > 48200):
        ob52.left(40)
    if(timer > 48700):
        ob53.left(40)
    if(timer > 49200):
        ob54.left(40)
    if(timer > 49700):
        ob55.left(40)
    if(timer > 50200):
        ob56.left(40)
    if(timer > 50700):
        ob57.left(40)
    if(timer > 51200):
        ob58.left(40)
    if(timer > 51700):
        ob59.left(40)
    if(timer > 52200):
        ob60.left(40)
    if(timer > 52700):
        ob61.left(40)
    if(timer > 53200):
        ob62.left(40)
    if(timer > 53700):
        ob63.left(40)
    if(timer > 54200):
        ob64.left(40)
    if(timer > 54700):
        ob65.left(40)
    if(timer > 55200):
        ob66.left(40)
    if(timer > 55700):
        ob67.left(40)
    if(timer > 56200):
        ob68.left(40)
    if(timer > 57200):
        ob69.left(40)
    if(timer > 58200):
        ob70.left(40)
    if(timer > 59200):
        ob71.left(40)
    if(timer > 60200):
        ob72.left(40)
    if(timer > 61200):
        ob73.left(40)
    if(timer > 62200):
        ob74.left(40)
    if(timer > 63200):
        ob75.left(40)
    if(timer > 64200):
        ob76.left(40)
    if(timer > 65200):
        ob77.left(40)
    if(timer > 66200):
        ob78.left(40)
    if(timer > 67200):
        ob79.left(40)
    if(timer > 68200):
        ob80.left(40)
    if(timer > 69200):
        ob81.left(40)
    if(timer > 70200):
        ob82.left(40)
    if(timer > 71200):
        ob83.left(40)
    if(timer > 72200):
        ob84.left(40)
    if(timer > 73200):
        ob85.left(40)
    if(timer > 74200):
        ob86.left(40)
    if(timer > 75200):
        ob87.left(40)
    if(timer > 76200):
        ob88.left(40)
    if(timer > 77200):
        ob89.left(40)
    if(timer > 78200):
        ob90.left(40)
    if(timer > 79200):
        ob91.left(40)
    if(timer > 80200):
        ob92.left(40)
    if(timer > 81200):
        ob93.left(40)
    if(timer > 82200):
        ob94.left(40)
    if(timer > 83200):
        ob95.left(40)
    if(timer > 84200):
        ob96.left(40)
    if(timer > 85200):
        ob97.left(40)
    if(timer > 86200):
        ob98.left(40)
    if(timer > 87200):
        ob99.left(40)
    if(timer > 88200):
        ob100.left(40)
    if(timer > 89200):
        ob101.left(40)
    if(timer > 90200):
        ob102.left(40)
    if(timer > 91200):
        ob103.left(40)
    if(timer > 92200):
        ob104.left(40)
    if(timer > 93200):
        ob105.left(40)
    if(timer > 94200):
        ob106.left(40)
    if(timer > 95200):
        ob107.left(40)
    if(timer > 96200):
        ob108.left(40)
    if(timer > 97200):
        ob109.left(40)
    if(timer > 98200):
        ob110.left(40)
    if(timer > 99200):
        ob111.left(40)
    if(timer > 100200):
        ob112.left(40)
    if(timer > 101200):
        ob113.left(40)
    if(timer > 102200):
        ob114.left(40)
    if(timer > 104700):
        ob115.left(40)
    if(timer > 105200):
        ob116.left(40)
    if(timer > 105700):
        ob117.left(40)
    if(timer > 106200):
        ob118.left(40)
    if(timer > 106700):
        ob119.left(40)
    if(timer > 107200):
        ob120.left(40)
    if(timer > 107700):
        ob121.left(40)
    if(timer > 108200):
        ob122.left(40)
    if(timer > 108700):
        ob123.left(40)
    if(timer > 109200):
        ob124.left(40)
    if(timer > 109700):
        ob125.left(40)
    if(timer > 110200):
        ob126.left(40)
    if(timer > 110700):
        ob127.left(40)
    if(timer > 111200):
        ob128.left(40)
    if(timer > 111700):
        ob129.left(40)
    if(timer > 112200):
        ob130.left(40)
    if(timer > 112700):
        ob131.left(40)
    if(timer > 113200):
        ob132.left(40)
    if(timer > 113700):
        ob133.left(40)
    if(timer > 114200):
        ob134.left(40)
    if(timer > 114700):
        ob135.left(40)
    if(timer > 115200):
        ob136.left(40)
    if(timer > 115700):
        ob137.left(40)
    if(timer > 116200):
        ob138.left(40)
    if(timer > 116700):
        ob139.left(40)
    if(timer > 117200):
        ob140.left(40)
    if(timer > 117700):
        ob141.left(40)
    if(timer > 118200):
        ob142.left(40)
    if(timer > 118700):
        ob143.left(40)
    if(timer > 119200):
        ob144.left(40)
    if(timer > 119700):
        ob145.left(40)
    if(timer > 122100):
        ob146.left(40)
    if(timer > 122600):
        ob147.left(40)
    if(timer > 124100):
        ob148.left(40)
    if(timer > 124600):
        ob149.left(40)
    if(timer > 126100):
        ob150.left(40)
    if(timer > 126600):
        ob151.left(40)
    if(timer > 128100):
        ob152.left(40)
    if(timer > 128600):
        ob153.left(40)
    if(timer > 130100):
        ob154.left(40)
    if(timer > 130600):
        ob155.left(40)
    if(timer > 132100):
        ob156.left(40)
    if(timer > 132600):
        ob157.left(40)
    if(timer > 134100):
        ob158.left(40)
    if(timer > 134600):
        ob159.left(40)
    if(timer > 136100):
        ob160.left(40)
    if(timer > 136600):
        ob161.left(40)
    if(timer > 138100):
        ob162.left(40)
    if(timer > 138600):
        ob163.left(40)
    if(timer > 139600):
        ob164.left(40)
    if(timer > 140100):
        ob165.left(40)
    if(timer > 141600):
        ob166.left(40)
    if(timer > 142100):
        ob167.left(40)
    if(timer > 143600):
        ob168.left(40)
    if(timer > 144100):
        ob169.left(40)
    if(timer > 145600):
        ob170.left(40)
    if(timer > 146100):
        ob171.left(40)
    if(timer > 147600):
        ob172.left(40)
    if(timer > 148100):
        ob173.left(40)
    if(timer > 148600):
        ob174.left(40)
    if(timer > 150100):
        ob175.left(40)
    if(timer > 150600):
        ob176.left(40)
    if(timer > 152100):
        ob177.left(40)
    if(timer > 152600):
        ob178.left(40)
    if(timer > 169350):
        ob179.left(40)
    if(timer > 170350):
        ob180.left(40)
    if(timer > 171350):
        ob181.left(40)
    if(timer > 172350):
        ob182.left(40)
    if(timer > 173350):
        ob183.left(40)
    if(timer > 174350):
        ob184.left(40)
    if(timer > 175350):
        ob185.left(40)
    if(timer > 176350):
        ob186.left(40)
    if(timer > 177350):
        ob187.left(40)
    if(timer > 178350):
        ob188.left(40)
    if(timer > 179350):
        ob189.left(40)
    if(timer > 180350):
        ob190.left(40)
    if(timer > 181350):
        ob191.left(40)
    if(timer > 182350):
        ob192.left(40)
    if(timer > 183350):
        ob193.left(40)
    if(timer > 184350):
        ob194.left(40)
    if(timer > 185350):
        ob195.left(40)
    if(timer > 186350):
        ob196.left(40)
    if(timer > 187350):
        ob197.left(40)
    if(timer > 188350):
        ob198.left(40)
    if(timer > 189350):
        ob199.left(40)
    if(timer > 190350):
        ob200.left(40)
    if(timer > 191350):
        ob201.left(40)
    if(timer > 192350):
        ob202.left(40)
    if(timer > 192350):
        ob203.left(40)
    if(timer > 193350):
        ob204.left(40)
    if(timer > 194350):
        ob205.left(40)
    if(timer > 195350):
        ob206.left(40)
    if(timer > 196350):
        ob207.left(40)
    if(timer > 197350):
        ob208.left(40)
    if(timer > 198350):
        ob209.left(40)
    if(timer > 199350):
        ob210.left(40)
    if(timer > 200350):
        ob211.left(40)
    if(timer > 201350):
        ob212.left(40)
    if(timer > 202350):
        ob213.left(40)
    if(timer > 203350):
        ob214.left(40)
    if(timer > 204350):
        ob215.left(40)
    if(timer > 205350):
        ob216.left(40)
    if(timer > 206350):
        ob217.left(40)
    if(timer > 207350):
        ob218.left(40)
    if(timer > 208350):
        ob219.left(40)
    if(timer > 209350):
        ob220.left(40)
    if(timer > 210350):
        ob221.left(40)





    blocks_hit_list = pygame.sprite.spritecollide(pointob, spritesgroup, True)
    player_hit_list =  pygame.sprite.spritecollide(player, spritesgroup, True)

    pygame.sprite.spritecollide(player, spritesgroup, True)
    if (blocks_hit_list!=[]):
        score+=10
        y=str(score)
        #print(score)
        #print(y)
    if (player_hit_list !=[]):
        score-=5
        y=str(score)
    score1=myfont.render(y, 1, (156,254,149))
    gameDisplay.blit(score1,(300, 50))


    label = myfont.render("YOUR CURRENT SCORE IS:", 1, (160,243,252))
    gameDisplay.blit(label, (300, 0))
    if (timer > 500) and (timer<5000):
        firstinstruct=myfonter.render("TWENTY ONE PILOTS - HOMETOWN ", 1, (156,254,149))
        gameDisplay.blit(firstinstruct, (50, 400))
    if (timer > 5100) and (timer<13100):
        firstinstruct=myfonter.render("PRESS SPACE TO JUMP OVER THE BLOCKS", 1, (156,254,149))
        gameDisplay.blit(firstinstruct, (50, 400))
    if (timer > 13200) and (timer<14200):
        firstinstruct=myfonter.render("READY!", 1, (156,254,149))
        gameDisplay.blit(firstinstruct, (50, 400))
    if (timer>14250 and timer<15200):
        firstinstruct=myfonter.render(" SET! ", 1, (156,254,149))
        gameDisplay.blit(firstinstruct, (50, 400))
    if (timer>15250 and timer<16200):
        firstinstruct=myfonter.render(" GO! ", 1, (156,254,149))
        gameDisplay.blit(firstinstruct, (50, 400))


    if int(y)>int(b):
        b=y
    if (timer>226500 and timer<236500):
        if b==y:
            first=myfont.render("NEW HIGH SCORE!", 1, (156,254,149))
            gameDisplay.blit(first, (50, 400))
            scorefile=open("hometownscores.txt", "w")
            b=str(b)
            scorefile.write(b)
            scorefile.close()
        else:
            b=str(b)
            highscores=("ALL TIME HIGH SCORE IS " + b)
            first=myfont.render(highscores, 1, (156,254,149))
            gameDisplay.blit(first, (50, 400))
            scorefile=open("hometownscores.txt", "w")
            scorefile.write(b)
            scorefile.close()
    if (timer > 237000):
        first=myfont.render("PRESS RETURN TO EXIT TO THE MAIN SCREEN", 1, (156,254,149))
        gameDisplay.blit(first, (50, 400))

pygame.quit() #unintiliazes pygames
with open("menu.py") as f:
    code = compile(f.read(), "menu.py", 'exec')
    exec(code)

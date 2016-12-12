from models import ourMusic, sprites
import pygame
import os
import time

class hometownController:
    def __init__(self):
        pygame.init() #short for initialize does return a tuple of successful intilizaton
        self.colors={"black":(0,0,0), "white": (255, 255, 255), "red": (255, 0, 0), "green": (0, 255, 0), "purple": (164, 66, 244), "pink" :(252, 25, 123), "blue":(144,229,213)}
        self.gameDisplay= pygame.display.set_mode((800, 600))

        self.bg=pygame.image.load('clouds_converted.jpg')
        self.moore=pygame.image.load("baemoore_converted.png")
        self.myfont = pygame.font.SysFont("Extrude", 30)
        self.myfonter =pygame.font.SysFont("AldotheApache",45)
        self.jump = False
        self.fall = False


        self.cube = pygame.image.load("cube.png")
        self.pointo=sprites(self.cube, -10, 580) #the self.cube it will hit
        self.pointo.pos()
        self.player=sprites(self.moore, 50, 544)

        self.ob = sprites(self.cube, 10000, 580)
        self.ob1 = sprites(self.cube, 10000, 580)
        self.ob2 = sprites(self.cube, 10000, 580)
        self.ob3 = sprites(self.cube, 10000, 580)
        self.ob4 = sprites(self.cube, 10000, 580)
        self.ob5 = sprites(self.cube, 10000, 580)
        self.ob6 = sprites(self.cube, 10000, 580)
        self.ob7 = sprites(self.cube, 10000, 580)
        self.ob8 = sprites(self.cube, 10000, 580)
        self.ob9 = sprites(self.cube, 10000, 580)
        self.ob10 = sprites(self.cube, 10000, 580)
        self.ob11 = sprites(self.cube, 10000, 580)
        self.ob12 = sprites(self.cube, 10000, 580)
        self.ob13 = sprites(self.cube, 10000, 580)
        self.ob14 = sprites(self.cube, 10000, 580)
        self.ob15 = sprites(self.cube, 10000, 580)
        self.ob16 = sprites(self.cube, 10000, 580)
        self.ob17 = sprites(self.cube, 10000, 580)
        self.ob18 = sprites(self.cube, 10000, 580)
        self.ob19 = sprites(self.cube, 10000, 580)
        self.ob20 = sprites(self.cube, 10000, 580)
        self.ob21 = sprites(self.cube, 10000, 580)
        self.ob22 = sprites(self.cube, 10000, 580)
        self.ob23 = sprites(self.cube, 10000, 580)
        self.ob24 = sprites(self.cube, 10000, 580)
        self.ob25 = sprites(self.cube, 10000, 580)
        self.ob26 = sprites(self.cube, 10000, 580)
        self.ob27 = sprites(self.cube, 10000, 580)
        self.ob28 = sprites(self.cube, 10000, 580)
        self.ob29 = sprites(self.cube, 10000, 580)
        self.ob30 = sprites(self.cube, 10000, 580)
        self.ob31 = sprites(self.cube, 10000, 580)
        self.ob32 = sprites(self.cube, 10000, 580)
        self.ob33 = sprites(self.cube, 10000, 580)
        self.ob34 = sprites(self.cube, 10000, 580)
        self.ob35 = sprites(self.cube, 10000, 580)
        self.ob36 = sprites(self.cube, 10000, 580)
        self.ob37 = sprites(self.cube, 10000, 580)
        self.ob38 = sprites(self.cube, 10000, 580)
        self.ob39 = sprites(self.cube, 10000, 580)
        self.ob40 = sprites(self.cube, 10000, 580)
        self.ob41 = sprites(self.cube, 10000, 580)
        self.ob42 = sprites(self.cube, 10000, 580)
        self.ob43 = sprites(self.cube, 10000, 580)
        self.ob44 = sprites(self.cube, 10000, 580)
        self.ob45 = sprites(self.cube, 10000, 580)
        self.ob46 = sprites(self.cube, 10000, 580)
        self.ob47 = sprites(self.cube, 10000, 580)
        self.ob48 = sprites(self.cube, 10000, 580)
        self.ob49 = sprites(self.cube, 10000, 580)
        self.ob50 = sprites(self.cube, 10000, 580)
        self.ob51 = sprites(self.cube, 10000, 580)
        self.ob52 = sprites(self.cube, 10000, 580)
        self.ob53 = sprites(self.cube, 10000, 580)
        self.ob54 = sprites(self.cube, 10000, 580)
        self.ob55 = sprites(self.cube, 10000, 580)
        self.ob56 = sprites(self.cube, 10000, 580)
        self.ob57 = sprites(self.cube, 10000, 580)
        self.ob58 = sprites(self.cube, 10000, 580)
        self.ob59 = sprites(self.cube, 10000, 580)
        self.ob60 = sprites(self.cube, 10000, 580)
        self.ob61 = sprites(self.cube, 10000, 580)
        self.ob62 = sprites(self.cube, 10000, 580)
        self.ob63 = sprites(self.cube, 10000, 580)
        self.ob64 = sprites(self.cube, 10000, 580)
        self.ob65 = sprites(self.cube, 10000, 580)
        self.ob66 = sprites(self.cube, 10000, 580)
        self.ob67 = sprites(self.cube, 10000, 580)
        self.ob68 = sprites(self.cube, 10000, 580)
        self.ob69 = sprites(self.cube, 10000, 580)
        self.ob70 = sprites(self.cube, 10000, 580)
        self.ob71 = sprites(self.cube, 10000, 580)
        self.ob72 = sprites(self.cube, 10000, 580)
        self.ob73 = sprites(self.cube, 10000, 580)
        self.ob74 = sprites(self.cube, 10000, 580)
        self.ob75 = sprites(self.cube, 10000, 580)
        self.ob76 = sprites(self.cube, 10000, 580)
        self.ob77 = sprites(self.cube, 10000, 580)
        self.ob78 = sprites(self.cube, 10000, 580)
        self.ob79 = sprites(self.cube, 10000, 580)
        self.ob80 = sprites(self.cube, 10000, 580)
        self.ob81 = sprites(self.cube, 10000, 580)
        self.ob82 = sprites(self.cube, 10000, 580)
        self.ob83 = sprites(self.cube, 10000, 580)
        self.ob84 = sprites(self.cube, 10000, 580)
        self.ob85 = sprites(self.cube, 10000, 580)
        self.ob86 = sprites(self.cube, 10000, 580)
        self.ob87 = sprites(self.cube, 10000, 580)
        self.ob88 = sprites(self.cube, 10000, 580)
        self.ob89 = sprites(self.cube, 10000, 580)
        self.ob90 = sprites(self.cube, 10000, 580)
        self.ob91 = sprites(self.cube, 10000, 580)
        self.ob92 = sprites(self.cube, 10000, 580)
        self.ob93 = sprites(self.cube, 10000, 580)
        self.ob94 = sprites(self.cube, 10000, 580)
        self.ob95 = sprites(self.cube, 10000, 580)
        self.ob96 = sprites(self.cube, 10000, 580)
        self.ob97 = sprites(self.cube, 10000, 580)
        self.ob98 = sprites(self.cube, 10000, 580)
        self.ob99 = sprites(self.cube, 10000, 580)
        self.ob100 = sprites(self.cube, 10000, 580)
        self.ob101 = sprites(self.cube, 10000, 580)
        self.ob102 = sprites(self.cube, 10000, 580)
        self.ob103 = sprites(self.cube, 10000, 580)
        self.ob104 = sprites(self.cube, 10000, 580)
        self.ob105 = sprites(self.cube, 10000, 580)
        self.ob106 = sprites(self.cube, 10000, 580)
        self.ob107 = sprites(self.cube, 10000, 580)
        self.ob108 = sprites(self.cube, 10000, 580)
        self.ob109 = sprites(self.cube, 10000, 580)
        self.ob110 = sprites(self.cube, 10000, 580)
        self.ob111 = sprites(self.cube, 10000, 580)
        self.ob112 = sprites(self.cube, 10000, 580)
        self.ob113 = sprites(self.cube, 10000, 580)
        self.ob114 = sprites(self.cube, 10000, 580)
        self.ob115 = sprites(self.cube, 10000, 580)
        self.ob116 = sprites(self.cube, 10000, 580)
        self.ob117 = sprites(self.cube, 10000, 580)
        self.ob118 = sprites(self.cube, 10000, 580)
        self.ob119 = sprites(self.cube, 10000, 580)
        self.ob120 = sprites(self.cube, 10000, 580)
        self.ob121 = sprites(self.cube, 10000, 580)
        self.ob122 = sprites(self.cube, 10000, 580)
        self.ob123 = sprites(self.cube, 10000, 580)
        self.ob124 = sprites(self.cube, 10000, 580)
        self.ob125 = sprites(self.cube, 10000, 580)
        self.ob126 = sprites(self.cube, 10000, 580)
        self.ob127 = sprites(self.cube, 10000, 580)
        self.ob128 = sprites(self.cube, 10000, 580)
        self.ob129 = sprites(self.cube, 10000, 580)
        self.ob130 = sprites(self.cube, 10000, 580)
        self.ob131 = sprites(self.cube, 10000, 580)
        self.ob132 = sprites(self.cube, 10000, 580)
        self.ob133 = sprites(self.cube, 10000, 580)
        self.ob134 = sprites(self.cube, 10000, 580)
        self.ob135 = sprites(self.cube, 10000, 580)
        self.ob136 = sprites(self.cube, 10000, 580)
        self.ob137 = sprites(self.cube, 10000, 580)
        self.ob138 = sprites(self.cube, 10000, 580)
        self.ob139 = sprites(self.cube, 10000, 580)
        self.ob140 = sprites(self.cube, 10000, 580)
        self.ob141 = sprites(self.cube, 10000, 580)
        self.ob142 = sprites(self.cube, 10000, 580)
        self.ob143 = sprites(self.cube, 10000, 580)
        self.ob144 = sprites(self.cube, 10000, 580)
        self.ob145 = sprites(self.cube, 10000, 580)
        self.ob146 = sprites(self.cube, 10000, 580)
        self.ob147 = sprites(self.cube, 10000, 580)
        self.ob148 = sprites(self.cube, 10000, 580)
        self.ob149 = sprites(self.cube, 10000, 580)
        self.ob150 = sprites(self.cube, 10000, 580)
        self.ob151 = sprites(self.cube, 10000, 580)
        self.ob152 = sprites(self.cube, 10000, 580)
        self.ob153 = sprites(self.cube, 10000, 580)
        self.ob154 = sprites(self.cube, 10000, 580)
        self.ob155 = sprites(self.cube, 10000, 580)
        self.ob156 = sprites(self.cube, 10000, 580)
        self.ob157 = sprites(self.cube, 10000, 580)
        self.ob158 = sprites(self.cube, 10000, 580)
        self.ob159 = sprites(self.cube, 10000, 580)
        self.ob160 = sprites(self.cube, 10000, 580)
        self.ob161 = sprites(self.cube, 10000, 580)
        self.ob162 = sprites(self.cube, 10000, 580)
        self.ob163 = sprites(self.cube, 10000, 580)
        self.ob164 = sprites(self.cube, 10000, 580)
        self.ob165 = sprites(self.cube, 10000, 580)
        self.ob166 = sprites(self.cube, 10000, 580)
        self.ob167 = sprites(self.cube, 10000, 580)
        self.ob168 = sprites(self.cube, 10000, 580)
        self.ob169 = sprites(self.cube, 10000, 580)
        self.ob170 = sprites(self.cube, 10000, 580)
        self.ob171 = sprites(self.cube, 10000, 580)
        self.ob172 = sprites(self.cube, 10000, 580)
        self.ob173 = sprites(self.cube, 10000, 580)
        self.ob174 = sprites(self.cube, 10000, 580)
        self.ob175 = sprites(self.cube, 10000, 580)
        self.ob176 = sprites(self.cube, 10000, 580)
        self.ob177 = sprites(self.cube, 10000, 580)
        self.ob178 = sprites(self.cube, 10000, 580)
        self.ob179 = sprites(self.cube, 10000, 580)
        self.ob180 = sprites(self.cube, 10000, 580)
        self.ob181 = sprites(self.cube, 10000, 580)
        self.ob182 = sprites(self.cube, 10000, 580)
        self.ob183 = sprites(self.cube, 10000, 580)
        self.ob184 = sprites(self.cube, 10000, 580)
        self.ob185 = sprites(self.cube, 10000, 580)
        self.ob186 = sprites(self.cube, 10000, 580)
        self.ob187 = sprites(self.cube, 10000, 580)
        self.ob188 = sprites(self.cube, 10000, 580)
        self.ob189 = sprites(self.cube, 10000, 580)
        self.ob190 = sprites(self.cube, 10000, 580)
        self.ob191 = sprites(self.cube, 10000, 580)
        self.ob192 = sprites(self.cube, 10000, 580)
        self.ob193 = sprites(self.cube, 10000, 580)
        self.ob194 = sprites(self.cube, 10000, 580)
        self.ob195 = sprites(self.cube, 10000, 580)
        self.ob196 = sprites(self.cube, 10000, 580)
        self.ob197 = sprites(self.cube, 10000, 580)
        self.ob198 = sprites(self.cube, 10000, 580)
        self.ob199 = sprites(self.cube, 10000, 580)
        self.ob200 = sprites(self.cube, 10000, 580)
        self.ob201 = sprites(self.cube, 10000, 580)
        self.ob202 = sprites(self.cube, 10000, 580)
        self.ob203 = sprites(self.cube, 10000, 580)
        self.ob204 = sprites(self.cube, 10000, 580)
        self.ob205 = sprites(self.cube, 10000, 580)
        self.ob206 = sprites(self.cube, 10000, 580)
        self.ob207 = sprites(self.cube, 10000, 580)
        self.ob208 = sprites(self.cube, 10000, 580)
        self.ob209 = sprites(self.cube, 10000, 580)
        self.ob210 = sprites(self.cube, 10000, 580)
        self.ob211 = sprites(self.cube, 10000, 580)
        self.ob212 = sprites(self.cube, 10000, 580)
        self.ob213 = sprites(self.cube, 10000, 580)
        self.ob214 = sprites(self.cube, 10000, 580)
        self.ob215 = sprites(self.cube, 10000, 580)
        self.ob216 = sprites(self.cube, 10000, 580)
        self.ob217 = sprites(self.cube, 10000, 580)
        self.ob218 = sprites(self.cube, 10000, 580)
        self.ob219 = sprites(self.cube, 10000, 580)
        self.ob220 = sprites(self.cube, 10000, 580)
        self.ob221 = sprites(self.cube, 10000, 580)
        self.ob222 = sprites(self.cube, 10000, 580)
        self.ob223 = sprites(self.cube, 10000, 580)
        self.ob224 = sprites(self.cube, 10000, 580)
        self.ob225 = sprites(self.cube, 10000, 580)
        self.ob226 = sprites(self.cube, 10000, 580)




        pygame.display.set_caption("lets play!")
        self.theSong=ourMusic("hometown.ogg")
        self.theSong.musicUpload()
        self.theSong.musicPlay()
        self.gameExit = False
        self.clock = pygame.time.Clock()



        self.spritesgroup=pygame.sprite.Group()
        self.spritesgroup.add(self.ob, self.ob1, self.ob2, self.ob3, self.ob4, self.ob5, self.ob6, self.ob7, self.ob8, self.ob9, self.ob10,
                         self.ob11, self.ob12, self.ob13, self.ob14, self.ob15, self.ob16, self.ob17, self.ob18, self.ob19, self.ob20,
                         self.ob21, self.ob22, self.ob23, self.ob24, self.ob25, self.ob26, self.ob27, self.ob28, self.ob29, self.ob30,
                         self.ob31, self.ob32, self.ob33, self.ob34, self.ob35, self.ob36, self.ob37, self.ob38, self.ob39, self.ob40,
                         self.ob41, self.ob42, self.ob43, self.ob44, self.ob45, self.ob46, self.ob47, self.ob48, self.ob49, self.ob50,
                         self.ob51, self.ob52, self.ob53, self.ob54, self.ob55, self.ob56, self.ob57, self.ob58, self.ob59, self.ob60,
                         self.ob61, self.ob62, self.ob63, self.ob64, self.ob65, self.ob66, self.ob67, self.ob68, self.ob69, self.ob70,
                         self.ob71, self.ob72, self.ob73, self.ob74, self.ob75, self.ob76, self.ob77, self.ob78, self.ob79, self.ob80,
                         self.ob81, self.ob82, self.ob83, self.ob84, self.ob85, self.ob86, self.ob87, self.ob88, self.ob89, self.ob90,
                         self.ob91, self.ob92, self.ob93, self.ob94, self.ob95, self.ob96, self.ob97, self.ob98, self.ob99, self.ob100,
                         self.ob101, self.ob102, self.ob103, self.ob104, self.ob105, self.ob106, self.ob107, self.ob108, self.ob109, self.ob110,
                         self.ob111, self.ob112, self.ob113, self.ob114, self.ob115, self.ob116, self.ob117, self.ob118, self.ob119, self.ob120,
                         self.ob121, self.ob122, self.ob123, self.ob124, self.ob125, self.ob126, self.ob127, self.ob128, self.ob129, self.ob130,
                         self.ob131, self.ob132, self.ob133, self.ob134, self.ob135, self.ob136, self.ob137, self.ob138, self.ob139, self.ob140,
                         self.ob141, self.ob142, self.ob143, self.ob144, self.ob145, self.ob146, self.ob147, self.ob148, self.ob149, self.ob150,
                         self.ob150, self.ob151, self.ob152, self.ob153, self.ob154, self.ob155, self.ob156, self.ob157, self.ob158, self.ob159, self.ob160,
                         self.ob161, self.ob162, self.ob163, self.ob164, self.ob165, self.ob166, self.ob167, self.ob168, self.ob169, self.ob170,
                         self.ob171, self.ob172, self.ob173, self.ob174, self.ob175, self.ob176, self.ob177, self.ob178, self.ob179, self.ob180,
                         self.ob181, self.ob182, self.ob183, self.ob184, self.ob185, self.ob186, self.ob187, self.ob188, self.ob189, self.ob190,
                         self.ob191, self.ob192, self.ob193, self.ob194, self.ob195, self.ob196, self.ob197, self.ob198, self.ob199, self.ob200,
                         self.ob201, self.ob202, self.ob203, self.ob204, self.ob205, self.ob206, self.ob207, self.ob208, self.ob209, self.ob210,
                         self.ob211, self.ob212, self.ob213, self.ob214, self.ob215, self.ob216, self.ob217, self.ob218, self.ob219, self.ob220,
                         self.ob221, self.ob222, self.ob223, self.ob224, self.ob225, self.ob226)

        self.score=0
        self.y=str(self.score)

        self.scorething=open("hometownscores.txt", "r")
        self.scoresentence=self.scorething.readline()
        self.b=self.scoresentence.strip()
        self.b=int(self.b)
        self.scorething.close()


        while not self.gameExit:
            self.clock.tick(40)
            self.timer = pygame.time.get_ticks()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.gameExit=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if not self.fall:
                            self.jump = True
                    if event.key == pygame.K_RETURN:
                            self.gameExit= True
            if self.jump:
                self.player.rect.y -= 60
                if self.player.rect.y <= 410:
                    ycoor = 500
                    self.jump = False
                    self.fall = True

            if self.fall:
                self.player.rect.y += 60
                if self.player.rect.y >= 544:
                    ycoor = 0
                    self.fall = False
            pygame.display.update()
            self.gameDisplay.blit(self.bg,[0,0])
            #gameDisplay.fill(colors["pink"])
            time.sleep(.05)
            self.player.pos()
            self.spritesgroup.draw(self.gameDisplay)
            self.ob.left(40)
            if(self.timer > 1700):
                self.ob1.left(40)
            if(self.timer > 2700):
                self.ob2.left(40)
            if(self.timer > 3700):
                self.ob3.left(40)
            if(self.timer > 4700):
                self.ob4.left(40)
            if(self.timer > 5700):
                self.ob5.left(40)
            if(self.timer > 6700):
                self.ob6.left(40)
            if(self.timer > 7700):
                self.ob7.left(40)
            if(self.timer > 8700):
                self.ob8.left(40)
            if(self.timer > 9700):
                self.ob9.left(40)
            if(self.timer > 10700):
                self.ob10.left(40)
            if(self.timer > 11700):
                self.ob11.left(40)
            if(self.timer > 12700):
                self.ob12.left(40)
            if(self.timer > 13700):
                self.ob13.left(40)
            if(self.timer > 14700):
                self.ob14.left(40)
            if(self.timer > 15700):
                self.ob15.left(40)
            if(self.timer > 16700):
                self.ob16.left(40)
            if(self.timer > 17700):
                self.ob17.left(40)
            if(self.timer > 18700):
                self.ob18.left(40)
            if(self.timer > 19700):
                self.ob19.left(40)
            if(self.timer > 20700):
                self.ob20.left(40)
            if(self.timer > 21700):
                self.ob21.left(40)
            if(self.timer > 22700):
                self.ob22.left(40)
            if(self.timer > 23700):
                self.ob23.left(40)
            if(self.timer > 25200):
                self.ob24.left(40)
            if(self.timer > 26200):
                self.ob25.left(40)
            if(self.timer > 27200):
                self.ob26.left(40)
            if(self.timer > 28200):
                self.ob27.left(40)
            if(self.timer > 29200):
                self.ob28.left(40)
            if(self.timer > 30200):
                self.ob29.left(40)
            if(self.timer > 31200):
                self.ob30.left(40)
            if(self.timer > 32200):
                self.ob31.left(40)
            if(self.timer > 33200):
                self.ob32.left(40)
            if(self.timer > 34200):
                self.ob33.left(40)
            if(self.timer > 35200):
                self.ob34.left(40)
            if(self.timer > 36200):
                self.ob35.left(40)
            if(self.timer > 37200):
                self.ob36.left(40)
            if(self.timer > 40700):
                self.ob37.left(40)
            if(self.timer > 41200):
                self.ob38.left(40)
            if(self.timer > 41700):
                self.ob39.left(40)
            if(self.timer > 42200):
                self.ob40.left(40)
            if(self.timer > 42700):
                self.ob41.left(40)
            if(self.timer > 43200):
                self.ob42.left(40)
            if(self.timer > 43700):
                self.ob43.left(40)
            if(self.timer > 44200):
                self.ob44.left(40)
            if(self.timer > 44700):
                self.ob45.left(40)
            if(self.timer > 45200):
                self.ob46.left(40)
            if(self.timer > 45700):
                self.ob47.left(40)
            if(self.timer > 46200):
                self.ob48.left(40)
            if(self.timer > 46700):
                self.ob49.left(40)
            if(self.timer > 47200):
                self.ob50.left(40)
            if(self.timer > 47700):
                self.ob51.left(40)
            if(self.timer > 48200):
                self.ob52.left(40)
            if(self.timer > 48700):
                self.ob53.left(40)
            if(self.timer > 49200):
                self.ob54.left(40)
            if(self.timer > 49700):
                self.ob55.left(40)
            if(self.timer > 50200):
                self.ob56.left(40)
            if(self.timer > 50700):
                self.ob57.left(40)
            if(self.timer > 51200):
                self.ob58.left(40)
            if(self.timer > 51700):
                self.ob59.left(40)
            if(self.timer > 52200):
                self.ob60.left(40)
            if(self.timer > 52700):
                self.ob61.left(40)
            if(self.timer > 53200):
                self.ob62.left(40)
            if(self.timer > 53700):
                self.ob63.left(40)
            if(self.timer > 54200):
                self.ob64.left(40)
            if(self.timer > 54700):
                self.ob65.left(40)
            if(self.timer > 55200):
                self.ob66.left(40)
            if(self.timer > 55700):
                self.ob67.left(40)
            if(self.timer > 56200):
                self.ob68.left(40)
            if(self.timer > 57200):
                self.ob69.left(40)
            if(self.timer > 58200):
                self.ob70.left(40)
            if(self.timer > 59200):
                self.ob71.left(40)
            if(self.timer > 60200):
                self.ob72.left(40)
            if(self.timer > 61200):
                self.ob73.left(40)
            if(self.timer > 62200):
                self.ob74.left(40)
            if(self.timer > 63200):
                self.ob75.left(40)
            if(self.timer > 64200):
                self.ob76.left(40)
            if(self.timer > 65200):
                self.ob77.left(40)
            if(self.timer > 66200):
                self.ob78.left(40)
            if(self.timer > 67200):
                self.ob79.left(40)
            if(self.timer > 68200):
                self.ob80.left(40)
            if(self.timer > 69200):
                self.ob81.left(40)
            if(self.timer > 70200):
                self.ob82.left(40)
            if(self.timer > 71200):
                self.ob83.left(40)
            if(self.timer > 72200):
                self.ob84.left(40)
            if(self.timer > 73200):
                self.ob85.left(40)
            if(self.timer > 74200):
                self.ob86.left(40)
            if(self.timer > 75200):
                self.ob87.left(40)
            if(self.timer > 76200):
                self.ob88.left(40)
            if(self.timer > 77200):
                self.ob89.left(40)
            if(self.timer > 78200):
                self.ob90.left(40)
            if(self.timer > 79200):
                self.ob91.left(40)
            if(self.timer > 80200):
                self.ob92.left(40)
            if(self.timer > 81200):
                self.ob93.left(40)
            if(self.timer > 82200):
                self.ob94.left(40)
            if(self.timer > 83200):
                self.ob95.left(40)
            if(self.timer > 84200):
                self.ob96.left(40)
            if(self.timer > 85200):
                self.ob97.left(40)
            if(self.timer > 86200):
                self.ob98.left(40)
            if(self.timer > 87200):
                self.ob99.left(40)
            if(self.timer > 88200):
                self.ob100.left(40)
            if(self.timer > 89200):
                self.ob101.left(40)
            if(self.timer > 90200):
                self.ob102.left(40)
            if(self.timer > 91200):
                self.ob103.left(40)
            if(self.timer > 92200):
                self.ob104.left(40)
            if(self.timer > 93200):
                self.ob105.left(40)
            if(self.timer > 94200):
                self.ob106.left(40)
            if(self.timer > 95200):
                self.ob107.left(40)
            if(self.timer > 96200):
                self.ob108.left(40)
            if(self.timer > 97200):
                self.ob109.left(40)
            if(self.timer > 98200):
                self.ob110.left(40)
            if(self.timer > 99200):
                self.ob111.left(40)
            if(self.timer > 100200):
                self.ob112.left(40)
            if(self.timer > 101200):
                self.ob113.left(40)
            if(self.timer > 102200):
                self.ob114.left(40)
            if(self.timer > 104700):
                self.ob115.left(40)
            if(self.timer > 105200):
                self.ob116.left(40)
            if(self.timer > 105700):
                self.ob117.left(40)
            if(self.timer > 106200):
                self.ob118.left(40)
            if(self.timer > 106700):
                self.ob119.left(40)
            if(self.timer > 107200):
                self.ob120.left(40)
            if(self.timer > 107700):
                self.ob121.left(40)
            if(self.timer > 108200):
                self.ob122.left(40)
            if(self.timer > 108700):
                self.ob123.left(40)
            if(self.timer > 109200):
                self.ob124.left(40)
            if(self.timer > 109700):
                self.ob125.left(40)
            if(self.timer > 110200):
                self.ob126.left(40)
            if(self.timer > 110700):
                self.ob127.left(40)
            if(self.timer > 111200):
                self.ob128.left(40)
            if(self.timer > 111700):
                self.ob129.left(40)
            if(self.timer > 112200):
                self.ob130.left(40)
            if(self.timer > 112700):
                self.ob131.left(40)
            if(self.timer > 113200):
                self.ob132.left(40)
            if(self.timer > 113700):
                self.ob133.left(40)
            if(self.timer > 114200):
                self.ob134.left(40)
            if(self.timer > 114700):
                self.ob135.left(40)
            if(self.timer > 115200):
                self.ob136.left(40)
            if(self.timer > 115700):
                self.ob137.left(40)
            if(self.timer > 116200):
                self.ob138.left(40)
            if(self.timer > 116700):
                self.ob139.left(40)
            if(self.timer > 117200):
                self.ob140.left(40)
            if(self.timer > 117700):
                self.ob141.left(40)
            if(self.timer > 118200):
                self.ob142.left(40)
            if(self.timer > 118700):
                self.ob143.left(40)
            if(self.timer > 119200):
                self.ob144.left(40)
            if(self.timer > 119700):
                self.ob145.left(40)
            if(self.timer > 122100):
                self.ob146.left(40)
            if(self.timer > 122600):
                self.ob147.left(40)
            if(self.timer > 124100):
                self.ob148.left(40)
            if(self.timer > 124600):
                self.ob149.left(40)
            if(self.timer > 126100):
                self.ob150.left(40)
            if(self.timer > 126600):
                self.ob151.left(40)
            if(self.timer > 128100):
                self.ob152.left(40)
            if(self.timer > 128600):
                self.ob153.left(40)
            if(self.timer > 130100):
                self.ob154.left(40)
            if(self.timer > 130600):
                self.ob155.left(40)
            if(self.timer > 132100):
                self.ob156.left(40)
            if(self.timer > 132600):
                self.ob157.left(40)
            if(self.timer > 134100):
                self.ob158.left(40)
            if(self.timer > 134600):
                self.ob159.left(40)
            if(self.timer > 136100):
                self.ob160.left(40)
            if(self.timer > 136600):
                self.ob161.left(40)
            if(self.timer > 138100):
                self.ob162.left(40)
            if(self.timer > 138600):
                self.ob163.left(40)
            if(self.timer > 139600):
                self.ob164.left(40)
            if(self.timer > 140100):
                self.ob165.left(40)
            if(self.timer > 141600):
                self.ob166.left(40)
            if(self.timer > 142100):
                self.ob167.left(40)
            if(self.timer > 143600):
                self.ob168.left(40)
            if(self.timer > 144100):
                self.ob169.left(40)
            if(self.timer > 145600):
                self.ob170.left(40)
            if(self.timer > 146100):
                self.ob171.left(40)
            if(self.timer > 147600):
                self.ob172.left(40)
            if(self.timer > 148100):
                self.ob173.left(40)
            if(self.timer > 148600):
                self.ob174.left(40)
            if(self.timer > 150100):
                self.ob175.left(40)
            if(self.timer > 150600):
                self.ob176.left(40)
            if(self.timer > 152100):
                self.ob177.left(40)
            if(self.timer > 152600):
                self.ob178.left(40)
            if(self.timer > 169350):
                self.ob179.left(40)
            if(self.timer > 170350):
                self.ob180.left(40)
            if(self.timer > 171350):
                self.ob181.left(40)
            if(self.timer > 172350):
                self.ob182.left(40)
            if(self.timer > 173350):
                self.ob183.left(40)
            if(self.timer > 174350):
                self.ob184.left(40)
            if(self.timer > 175350):
                self.ob185.left(40)
            if(self.timer > 176350):
                self.ob186.left(40)
            if(self.timer > 177350):
                self.ob187.left(40)
            if(self.timer > 178350):
                self.ob188.left(40)
            if(self.timer > 179350):
                self.ob189.left(40)
            if(self.timer > 180350):
                self.ob190.left(40)
            if(self.timer > 181350):
                self.ob191.left(40)
            if(self.timer > 182350):
                self.ob192.left(40)
            if(self.timer > 183350):
                self.ob193.left(40)
            if(self.timer > 184350):
                self.ob194.left(40)
            if(self.timer > 185350):
                self.ob195.left(40)
            if(self.timer > 186350):
                self.ob196.left(40)
            if(self.timer > 187350):
                self.ob197.left(40)
            if(self.timer > 188350):
                self.ob198.left(40)
            if(self.timer > 189350):
                self.ob199.left(40)
            if(self.timer > 190350):
                self.ob200.left(40)
            if(self.timer > 191350):
                self.ob201.left(40)
            if(self.timer > 192350):
                self.ob202.left(40)
            if(self.timer > 192350):
                self.ob203.left(40)
            if(self.timer > 193350):
                self.ob204.left(40)
            if(self.timer > 194350):
                self.ob205.left(40)
            if(self.timer > 195350):
                self.ob206.left(40)
            if(self.timer > 196350):
                self.ob207.left(40)
            if(self.timer > 197350):
                self.ob208.left(40)
            if(self.timer > 198350):
                self.ob209.left(40)
            if(self.timer > 199350):
                self.ob210.left(40)
            if(self.timer > 200350):
                self.ob211.left(40)
            if(self.timer > 201350):
                self.ob212.left(40)
            if(self.timer > 202350):
                self.ob213.left(40)
            if(self.timer > 203350):
                self.ob214.left(40)
            if(self.timer > 204350):
                self.ob215.left(40)
            if(self.timer > 205350):
                self.ob216.left(40)
            if(self.timer > 206350):
                self.ob217.left(40)
            if(self.timer > 207350):
                self.ob218.left(40)
            if(self.timer > 208350):
                self.ob219.left(40)
            if(self.timer > 209350):
                self.ob220.left(40)
            if(self.timer > 210350):
                self.ob221.left(40)


            self.blocks_hit_list = pygame.sprite.spritecollide(self.pointo, self.spritesgroup, True)
            self.player_hit_list =  pygame.sprite.spritecollide(self.player, self.spritesgroup, True)

            pygame.sprite.spritecollide(self.player, self.spritesgroup, True)
            if (self.blocks_hit_list!=[]):
                self.score+=10
                self.y=str(self.score)
            if (self.player_hit_list !=[]):
                self.score-=5
                self.y=str(self.score)
            self.score1=self.myfont.render(self.y, 1, (156,254,149))
            self.gameDisplay.blit(self.score1,(600, 50))
            self.label = self.myfont.render("YOUR CURRENT SCORE IS:", 1, (160,243,252))
            self.gameDisplay.blit(self.label, (300, 50))
            if (self.timer > 500) and (self.timer<5000):
                self.firstinstruct=self.myfonter.render("TWENTY ONE PILOTS - HOMETOWN ", 1, (156,254,149))
                self.gameDisplay.blit(self.firstinstruct, (125, 300))
            if (self.timer > 5100) and (self.timer<13100):
                self.firstinstruct=self.myfonter.render("PRESS SPACE TO JUMP OVER THE BLOCKS", 1, (156,254,149))
                self.gameDisplay.blit(self.firstinstruct, (50, 300))
            if (self.timer > 13200) and (self.timer<14200):
                self.firstinstruct=self.myfonter.render("READY!", 1, (156,254,149))
                self.gameDisplay.blit(self.firstinstruct, (350, 300))
            if (self.timer>14250 and self.timer<15200):
                self.firstinstruct=self.myfonter.render(" SET! ", 1, (156,254,149))
                self.gameDisplay.blit(self.firstinstruct, (350, 300))
            if (self.timer>15250 and self.timer<16200):
                self.firstinstruct=self.myfonter.render(" GO! ", 1, (156,254,149))
                self.gameDisplay.blit(self.firstinstruct, (350, 300))
            if int(self.y)>int(self.b):
                self.b=self.y
            if (self.timer>226000 and self.timer<236000):
                if self.b==self.y:
                    self.first=self.myfont.render("NEW HIGH SCORE!", 1, (156,254,149))
                    self.gameDisplay.blit(self.first, (50, 400))
                    self.scorefile=open("hometownscores.txt", "w")
                    self.b=str(self.b)
                    self.scorefile.write(self.b)
                    self.scorefile.close()
                else:
                    self.b=str(self.b)
                    self.highscores=("ALL TIME HIGH SCORE IS " + self.b)
                    self.first=self.myfont.render(self.highscores, 1, (156,254,149))
                    self.gameDisplay.blit(self.first, (50, 400))
                    self.scorefile=open("hometownscores.txt", "w")
                    self.scorefile.write(self.b)
                    self.scorefile.close()
            if(self.timer >236000):
                    self.first=self.myfont.render("PRESS RETURN TO EXIT PROGRAM", 1, (156,254,149))
                    self.gameDisplay.blit(self.first, (50, 400))


        pygame.quit() #unintiliazes pygames
        quit()
def main():
    hometownController()
main()

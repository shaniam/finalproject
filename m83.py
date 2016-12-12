from models import ourMusic, sprites
import pygame
import os
import time

class mController:
    def __init__(self):
        pygame.init() #short for initialize does return a tuple of successful intilizaton
        colors={"black":(0,0,0), "white": (255, 255, 255), "red": (255, 0, 0), "green": (0, 255, 0), "purple": (164, 66, 244), "pink" :(252, 25, 123)}
        self.gameDisplay= pygame.display.set_mode((800, 600))

        self.bg=pygame.image.load('clouds_converted.jpg')
        self.moore=pygame.image.load("baemoore_converted.png")
        self.myfont = pygame.font.SysFont("Extrude", 30)
        self.myfonter =pygame.font.SysFont("AldotheApache",45)

        self.jump = False
        self.fall = False


        pygame.display.set_caption("lets play!")
        self.thesong=ourMusic("m83.ogg")
        self.thesong.musicUpload()
        self.thesong.musicPlay()
        self.gameExit = False
        self.clock = pygame.time.Clock()

        self.score=0
        self.y=str(self.score)
        self.scorething=open("m83scores.txt", "r")
        self.scoresentence=self.scorething.readline()
        self.b=self.scoresentence.strip()
        self.b=int(self.b)
        self.scorething.close()


        self.cube = pygame.image.load("cube.png")
        self.layer=sprites(self.moore, 50, 544)

        self.pointo=sprites(self.cube, -10, 580) #the cube it will hit
        self.pointo.pos()
        self.player=sprites(self.moore, 50, 544)

        self.ob = sprites(self.cube, 2125, 580)
        self.ob1 = sprites(self.cube, 2125, 580)
        self.ob2 = sprites(self.cube, 2125, 580)
        self.ob3 = sprites(self.cube, 2125, 580)
        self.ob4 = sprites(self.cube, 2125, 580)
        self.ob5 = sprites(self.cube, 2125, 580)
        self.ob6 = sprites(self.cube, 2125, 580)
        self.ob7 = sprites(self.cube, 2125, 580)
        self.ob8 = sprites(self.cube, 2125, 580)
        self.ob9 = sprites(self.cube, 2125, 580)
        self.ob10 = sprites(self.cube, 2125, 580)
        self.ob11 = sprites(self.cube, 2125, 580)
        self.ob12 = sprites(self.cube, 2125, 580)
        self.ob13 = sprites(self.cube, 2125, 580)
        self.ob14 = sprites(self.cube, 2125, 580)
        self.ob15 = sprites(self.cube, 2125, 580)
        self.ob16 = sprites(self.cube, 2125, 580)
        self.ob17 = sprites(self.cube, 2125, 580)
        self.ob18 = sprites(self.cube, 2125, 580)
        self.ob19 = sprites(self.cube, 2125, 580)
        self.ob20 = sprites(self.cube, 2125, 580)
        self.ob21 = sprites(self.cube, 2125, 580)
        self.ob22 = sprites(self.cube, 2125, 580)
        self.ob23 = sprites(self.cube, 2125, 580)
        self.ob24 = sprites(self.cube, 2125, 580)
        self.ob25 = sprites(self.cube, 2125, 580)
        self.ob26 = sprites(self.cube, 2125, 580)
        self.ob27 = sprites(self.cube, 2125, 580)
        self.ob28 = sprites(self.cube, 2125, 580)
        self.ob29 = sprites(self.cube, 2125, 580)
        self.ob30 = sprites(self.cube, 2125, 580)
        self.ob31 = sprites(self.cube, 2125, 580)
        self.ob32 = sprites(self.cube, 2125, 580)
        self.ob33 = sprites(self.cube, 2125, 580)
        self.ob34 = sprites(self.cube, 2125, 580)
        self.ob35 = sprites(self.cube, 2125, 580)
        self.ob36 = sprites(self.cube, 2125, 580)
        self.ob37 = sprites(self.cube, 2125, 580)
        self.ob38 = sprites(self.cube, 2125, 580)
        self.ob39 = sprites(self.cube, 2125, 580)
        self.ob40 = sprites(self.cube, 2125, 580)
        self.ob41 = sprites(self.cube, 2125, 580)
        self.ob42 = sprites(self.cube, 2125, 580)
        self.ob43 = sprites(self.cube, 2125, 580)
        self.ob44 = sprites(self.cube, 2125, 580)
        self.ob45 = sprites(self.cube, 2125, 580)
        self.ob46 = sprites(self.cube, 2125, 580)
        self.ob47 = sprites(self.cube, 2125, 580)
        self.ob48 = sprites(self.cube, 2125, 580)
        self.ob49 = sprites(self.cube, 2125, 580)
        self.ob50 = sprites(self.cube, 2125, 580)
        self.ob51 = sprites(self.cube, 2125, 580)
        self.ob52 = sprites(self.cube, 2125, 580)
        self.ob53 = sprites(self.cube, 2125, 580)
        self.ob54 = sprites(self.cube, 2125, 580)
        self.ob55 = sprites(self.cube, 2125, 580)
        self.ob56 = sprites(self.cube, 2125, 580)
        self.ob57 = sprites(self.cube, 2125, 580)
        self.ob58 = sprites(self.cube, 2125, 580)
        self.ob59 = sprites(self.cube, 2125, 580)
        self.ob60 = sprites(self.cube, 2125, 580)
        self.ob61 = sprites(self.cube, 2125, 580)
        self.ob62 = sprites(self.cube, 2125, 580)
        self.ob63 = sprites(self.cube, 2125, 580)
        self.ob64 = sprites(self.cube, 2125, 580)
        self.ob65 = sprites(self.cube, 2125, 580)
        self.ob66 = sprites(self.cube, 2125, 580)
        self.ob67 = sprites(self.cube, 2125, 580)
        self.ob68 = sprites(self.cube, 2125, 580)
        self.ob69 = sprites(self.cube, 2125, 580)
        self.ob70 = sprites(self.cube, 2125, 580)
        self.ob71 = sprites(self.cube, 2125, 580)
        self.ob72 = sprites(self.cube, 2125, 580)
        self.ob73 = sprites(self.cube, 2125, 580)
        self.ob74 = sprites(self.cube, 2125, 580)
        self.ob75 = sprites(self.cube, 2125, 580)
        self.ob76 = sprites(self.cube, 2125, 580)
        self.ob77 = sprites(self.cube, 2125, 580)
        self.ob78 = sprites(self.cube, 2125, 580)
        self.ob79 = sprites(self.cube, 2125, 580)
        self.ob80 = sprites(self.cube, 2125, 580)
        self.ob81 = sprites(self.cube, 2125, 580)
        self.ob82 = sprites(self.cube, 2125, 580)
        self.ob83 = sprites(self.cube, 2125, 580)
        self.ob84 = sprites(self.cube, 2125, 580)
        self.ob85 = sprites(self.cube, 2125, 580)
        self.ob86 = sprites(self.cube, 2125, 580)
        self.ob87 = sprites(self.cube, 2125, 580)
        self.ob88 = sprites(self.cube, 2125, 580)
        self.ob89 = sprites(self.cube, 2125, 580)
        self.ob90 = sprites(self.cube, 2125, 580)
        self.ob91 = sprites(self.cube, 2125, 580)
        self.ob92 = sprites(self.cube, 2125, 580)
        self.ob93 = sprites(self.cube, 2125, 580)
        self.ob94 = sprites(self.cube, 2125, 580)
        self.ob95 = sprites(self.cube, 2125, 580)
        self.ob96 = sprites(self.cube, 2125, 580)
        self.ob97 = sprites(self.cube, 2125, 580)
        self.ob98 = sprites(self.cube, 2125, 580)
        self.ob99 = sprites(self.cube, 2125, 580)
        self.ob100 = sprites(self.cube, 2125, 580)
        self.ob101 = sprites(self.cube, 2125, 580)
        self.ob102 = sprites(self.cube, 2125, 580)
        self.ob103 = sprites(self.cube, 2125, 580)
        self.ob104 = sprites(self.cube, 2125, 580)
        self.ob105 = sprites(self.cube, 2125, 580)
        self.ob106 = sprites(self.cube, 2125, 580)
        self.ob107 = sprites(self.cube, 2125, 580)
        self.ob108 = sprites(self.cube, 2125, 580)
        self.ob109 = sprites(self.cube, 2125, 580)
        self.ob110 = sprites(self.cube, 2125, 580)
        self.ob111 = sprites(self.cube, 2125, 580)
        self.ob112 = sprites(self.cube, 2125, 580)
        self.ob113 = sprites(self.cube, 2125, 580)
        self.ob114 = sprites(self.cube, 2125, 580)
        self.ob115 = sprites(self.cube, 2125, 580)
        self.ob116 = sprites(self.cube, 2125, 580)
        self.ob117 = sprites(self.cube, 2125, 580)
        self.ob118 = sprites(self.cube, 2125, 580)
        self.ob119 = sprites(self.cube, 2125, 580)
        self.ob120 = sprites(self.cube, 2125, 580)
        self.ob121 = sprites(self.cube, 2125, 580)
        self.ob122 = sprites(self.cube, 2125, 580)
        self.ob123 = sprites(self.cube, 2125, 580)
        self.ob124 = sprites(self.cube, 2125, 580)
        self.ob125 = sprites(self.cube, 2125, 580)
        self.ob126 = sprites(self.cube, 2125, 580)
        self.ob127 = sprites(self.cube, 2125, 580)
        self.ob128 = sprites(self.cube, 2125, 580)
        self.ob129 = sprites(self.cube, 2125, 580)
        self.ob130 = sprites(self.cube, 2125, 580)
        self.ob131 = sprites(self.cube, 2125, 580)
        self.ob132 = sprites(self.cube, 2125, 580)
        self.ob133 = sprites(self.cube, 2125, 580)

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
                         self.ob131, self.ob132, self.ob133)

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
                self.player.rect.y -= 16
                if self.player.rect.y <= 410:
                    self.ycoor = 500
                    self.jump = False
                    self.fall = True

            if self.fall:
                self.player.rect.y += 16
                if self.player.rect.y >= 544:
                    self.ycoor = 0
                    self.fall = False

            pygame.display.update()
            self.gameDisplay.blit(self.bg,[0,0])
            time.sleep(.05)
            self.player.pos()
            self.spritesgroup.draw(self.gameDisplay)
            self.ob.left(7)


            if(self.timer > 1200):
                self.ob1.left(7)
            if(self.timer > 2800):
                self.ob2.left(7)
            if(self.timer > 4000):
                self.ob3.left(7)
            if(self.timer > 5200):
                self.ob4.left(7)
            if(self.timer > 6400):
                self.ob5.left(7)
            if(self.timer > 7600):
                self.ob6.left(7)
            if(self.timer > 8800):
                self.ob7.left(7)
            if(self.timer > 10000):
                self.ob8.left(7)
            if(self.timer > 11200):
                self.ob9.left(7)
            if(self.timer > 12400):
                self.ob10.left(7)
            if(self.timer > 13600):
                self.ob11.left(7)
            if(self.timer > 14800):
                self.ob12.left(7)
            if(self.timer > 16000):
                self.ob13.left(7)
            if(self.timer > 17200):
                self.ob14.left(7)
            if(self.timer > 18400):
                self.ob15.left(7)
            if(self.timer > 20800):
                self.ob16.left(7)
            if(self.timer > 22000):
                self.ob17.left(7)
            if(self.timer > 23200):
                self.ob18.left(7)
            if(self.timer > 24400):
                self.ob19.left(7)
            if(self.timer > 25600):
                self.ob20.left(7)
            if(self.timer > 29200):
                self.ob21.left(7)
            if(self.timer > 30400):
                self.ob22.left(7)
            if(self.timer > 31600):
                self.ob23.left(7)
            if(self.timer > 32800):
                self.ob24.left(7)
            if(self.timer > 34000):
                self.ob25.left(7)
            if(self.timer > 35200):
                self.ob26.left(7)
            if(self.timer > 36400):
                self.ob27.left(7)
            if(self.timer > 37600):
                self.ob28.left(7)
            if(self.timer > 38800):
                self.ob29.left(7)
            if(self.timer > 41200):
                self.ob30.left(7)
            if(self.timer > 44800):
                self.ob31.left(7)
            if(self.timer > 46000):
                self.ob32.left(7)
            if(self.timer > 47200):
                self.ob33.left(7)
            if(self.timer > 48400):
                self.ob34.left(7)
            if(self.timer > 50800):
                self.ob35.left(7)
            if(self.timer > 53200):
                self.ob36.left(7)
            if(self.timer > 54400):
                self.ob37.left(7)
            if(self.timer > 55600):
                self.ob38.left(7)
            if(self.timer > 59200):
                self.ob39.left(7)
            if(self.timer > 60400):
                self.ob40.left(7)
            if(self.timer > 61600):
                self.ob41.left(7)
            if(self.timer > 62800):
                self.ob42.left(7)
            if(self.timer > 65200):
                self.ob43.left(7)
            if(self.timer > 66400):
                self.ob44.left(7)
            if(self.timer > 70000):
                self.ob45.left(7)
            if(self.timer > 71200):
                self.ob46.left(7)
            if(self.timer > 72400):
                self.ob47.left(7)
            if(self.timer > 74800):
                self.ob48.left(7)
            if(self.timer > 76000):
                self.ob49.left(7)
            if(self.timer > 77200):
                self.ob50.left(7)
            if(self.timer > 79400):
                self.ob51.left(7)
            if(self.timer > 80800):
                self.ob52.left(7)
            if(self.timer > 84400):
                self.ob53.left(7)
            if(self.timer > 85600):
                self.ob54.left(7)
            if(self.timer > 86800):
                self.ob55.left(7)
            if(self.timer > 88000):
                self.ob56.left(7)
            if(self.timer > 89200):
                self.ob57.left(7)
            if(self.timer > 90400):
                self.ob58.left(7)
            if(self.timer > 94000):
                self.ob59.left(7)
            if(self.timer > 95200):
                self.ob60.left(7)
            if(self.timer > 96400):
                self.ob61.left(7)
            if(self.timer > 98600):
                self.ob62.left(7)
            if(self.timer > 102200):
                self.ob63.left(7)
            if(self.timer > 103400):
                self.ob64.left(7)
            if(self.timer > 104600):
                self.ob65.left(7)
            if(self.timer > 105800):
                self.ob66.left(7)
            if(self.timer > 108200):
                self.ob67.left(7)
            if(self.timer > 109400):
                self.ob68.left(7)
            if(self.timer > 111800):
                self.ob69.left(7)
            if(self.timer > 113000):
                self.ob70.left(7)
            if(self.timer > 114200):
                self.ob71.left(7)
            if(self.timer > 115400):
                self.ob72.left(7)
            if(self.timer > 119000):
                self.ob73.left(7)
            if(self.timer > 120200):
                self.ob74.left(7)
            if(self.timer > 121400):
                self.ob75.left(7)
            if(self.timer > 122600):
                self.ob76.left(7)
            if(self.timer > 123800):
                self.ob77.left(7)
            if(self.timer > 125000):
                self.ob78.left(7)
            if(self.timer > 128600):
                self.ob79.left(7)
            if(self.timer > 131000):
                self.ob80.left(7)
            if(self.timer > 133400):
                self.ob81.left(7)
            if(self.timer > 134600):
                self.ob82.left(7)
            if(self.timer > 135800):
                self.ob83.left(7)
            if(self.timer > 137000):
                self.ob84.left(7)
            if(self.timer > 138200):
                self.ob85.left(7)
            if(self.timer > 139400):
                self.ob86.left(7)
            if(self.timer > 140600):
                self.ob87.left(7)
            if(self.timer > 144200):
                self.ob88.left(7)
            if(self.timer > 145400):
                self.ob89.left(7)
            if(self.timer > 146600):
                self.ob90.left(7)
            if(self.timer > 147800):
                self.ob91.left(7)
            if(self.timer > 150200):
                self.ob92.left(7)
            if(self.timer > 151400):
                self.ob93.left(7)
            if(self.timer > 152600):
                self.ob94.left(7)
            if(self.timer > 153800):
                self.ob95.left(7)
            if(self.timer > 156000):
                self.ob96.left(7)
            if(self.timer > 159600):
                self.ob97.left(7)
            if(self.timer > 160800):
                self.ob98.left(7)
            if(self.timer > 162000):
                self.ob99.left(7)
            if(self.timer > 163200):
                self.ob100.left(7)
            if(self.timer > 164400):
                self.ob101.left(7)
            if(self.timer > 165600):
                self.ob102.left(7)
            if(self.timer > 168000):
                self.ob103.left(7)
            if(self.timer > 170400):
                self.ob104.left(7)
            if(self.timer > 171600):
                self.ob105.left(7)
            if(self.timer > 172800):
                self.ob106.left(7)
            if(self.timer > 174000):
                self.ob107.left(7)
            if(self.timer > 177600):
                self.ob108.left(7)
            if(self.timer > 178800):
                self.ob109.left(7)
            if(self.timer > 180000):
                self.ob110.left(7)
            if(self.timer > 181200):
                self.ob111.left(7)
            if(self.timer > 182400):
                self.ob112.left(7)
            if(self.timer > 183600):
                self.ob113.left(7)
            if(self.timer > 184800):
                self.ob114.left(7)
            if(self.timer > 186000):
                self.ob115.left(7)
            if(self.timer > 188400):
                self.ob116.left(7)
            if(self.timer > 192000):
                self.ob117.left(7)
            if(self.timer > 193200):
                self.ob118.left(7)
            if(self.timer > 194400):
                self.ob119.left(7)
            if(self.timer > 196600):
                self.ob120.left(7)
            if(self.timer > 198800):
                self.ob121.left(7)
            if(self.timer > 200000):
                self.ob122.left(7)
            if(self.timer > 201200):
                self.ob123.left(7)
            if(self.timer > 202400):
                self.ob124.left(7)
            if(self.timer > 203600):
                self.ob125.left(7)
            if(self.timer > 204800):
                self.ob126.left(7)
            if(self.timer > 206000):
                self.ob127.left(7)
            if(self.timer > 207200):
                self.ob128.left(7)
            if(self.timer > 208400):
                self.ob129.left(7)
            if(self.timer > 209600):
                self.ob130.left(7)
            if(self.timer > 210800):
                self.ob131.left(7)
            if(self.timer > 212000):
                self.ob132.left(7)
            if(self.timer > 213200):
                self.ob133.left(7)
            if (self.timer > 500) and (self.timer<5000):
                self.firstinstruct=self.myfonter.render("M83 - MIDNIGHT CITY ", 1, (156,254,149))
                self.gameDisplay.blit(self.firstinstruct, (275, 300))
            if (self.timer > 5100) and (self.timer<15100):
                self.firstinstruct=self.myfonter.render("PRESS SPACE TO JUMP OVER THE BLOCKS", 1, (156,254,149))
                self.gameDisplay.blit(self.firstinstruct, (50, 300))
            if (self.timer > 15200) and (self.timer<16200):
                self.firstinstruct=self.myfonter.render("READY!", 1, (156,254,149))
                self.gameDisplay.blit(self.firstinstruct, (350, 300))
            if (self.timer>16250 and self.timer<17200):
                self.firstinstruct=self.myfonter.render(" SET! ", 1, (156,254,149))
                self.gameDisplay.blit(self.firstinstruct, (350, 300))
            if (self.timer>17250 and self.timer<18200):
                self.firstinstruct=self.myfonter.render(" GO! ", 1, (156,254,149))
                self.gameDisplay.blit(self.firstinstruct, (350, 300))


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
            if int(self.y)>int(self.b):
                self.b=self.y
            if (self.timer>232000 and self.timer<237000):
                if self.b==self.y:
                    self.first=self.myfont.render("NEW HIGH SCORE!", 1, (156,254,149))
                    self.gameDisplay.blit(self.first, (50, 400))
                    self.scorefile=open("m83scores.txt", "w")
                    self.b=str(self.b)
                    self.scorefile.write(self.b)
                    self.scorefile.close()
                else:
                    self.b=str(self.b)
                    self.highscores=("ALL TIME HIGH SCORE IS " + self.b)
                    self.first=self.myfont.render(self.highscores, 1, (156,254,149))
                    self.gameDisplay.blit(self.first, (50, 400))
                    self.scorefile=open("m83scores.txt", "w")
                    self.scorefile.write(self.b)
                    self.scorefile.close()
            if(self.timer >237100):
                    self.first=self.myfont.render("PRESS RETURN TO EXIT PROGRAM", 1, (156,254,149))
                    self.gameDisplay.blit(self.first, (50, 400))

        pygame.quit() #unintiliazes pygames
        quit()

def main():
    mController()
main()

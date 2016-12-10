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
scorething=open("christmasscores.txt", "r")
scoresentence=scorething.readline()
b=scoresentence.strip()
b=int(b)
scorething.close()

ob = sprites(cube, 4400, 580)
ob1 = sprites(cube, 4400, 580)
ob2 = sprites(cube, 4400, 580)
ob3 = sprites(cube, 4400, 580)
ob4 = sprites(cube, 4400, 580)
ob5 = sprites(cube, 4400, 580)
ob6 = sprites(cube, 4400, 580)
ob7 = sprites(cube, 4400, 580)
ob8 = sprites(cube, 4400, 580)
ob9 = sprites(cube, 4400, 580)
ob10 = sprites(cube, 4400, 580)
ob11 = sprites(cube, 4400, 580)
ob12 = sprites(cube, 4400, 580)
ob13 = sprites(cube, 4400, 580)
ob14 = sprites(cube, 4400, 580)
ob15 = sprites(cube, 4400, 580)
ob16 = sprites(cube, 4400, 580)
ob17 = sprites(cube, 4400, 580)
ob18 = sprites(cube, 4400, 580)
ob19 = sprites(cube, 4400, 580)
ob20 = sprites(cube, 4400, 580)
ob21 = sprites(cube, 4400, 580)
ob22 = sprites(cube, 4400, 580)
ob23 = sprites(cube, 4400, 580)
ob24 = sprites(cube, 4400, 580)
ob25 = sprites(cube, 4400, 580)
ob26 = sprites(cube, 4400, 580)
ob27 = sprites(cube, 4400, 580)
ob28 = sprites(cube, 4400, 580)
ob29 = sprites(cube, 4400, 580)
ob30 = sprites(cube, 4400, 580)
ob31 = sprites(cube, 4400, 580)
ob32 = sprites(cube, 4400, 580)
ob33 = sprites(cube, 4400, 580)
ob34 = sprites(cube, 4400, 580)
ob35 = sprites(cube, 4400, 580)
ob36 = sprites(cube, 4400, 580)
ob37 = sprites(cube, 4400, 580)
ob38 = sprites(cube, 4400, 580)
ob39 = sprites(cube, 4400, 580)
ob40 = sprites(cube, 4400, 580)
ob41 = sprites(cube, 4400, 580)
ob42 = sprites(cube, 4400, 580)
ob43 = sprites(cube, 4400, 580)
ob44 = sprites(cube, 4400, 580)
ob45 = sprites(cube, 4400, 580)
ob46 = sprites(cube, 4400, 580)
ob47 = sprites(cube, 4400, 580)
ob48 = sprites(cube, 4400, 580)
ob49 = sprites(cube, 4400, 580)
ob50 = sprites(cube, 4400, 580)
ob51 = sprites(cube, 4400, 580)
ob52 = sprites(cube, 4400, 580)
ob53 = sprites(cube, 4400, 580)
ob54 = sprites(cube, 4400, 580)
ob55 = sprites(cube, 4400, 580)
ob56 = sprites(cube, 4400, 580)
ob57 = sprites(cube, 4400, 580)
ob58 = sprites(cube, 4400, 580)
ob59 = sprites(cube, 4400, 580)
ob60 = sprites(cube, 4400, 580)
ob61 = sprites(cube, 4400, 580)
ob62 = sprites(cube, 4400, 580)
ob63 = sprites(cube, 4400, 580)
ob64 = sprites(cube, 4400, 580)
ob65 = sprites(cube, 4400, 580)
ob66 = sprites(cube, 4400, 580)
ob67 = sprites(cube, 4400, 580)
ob68 = sprites(cube, 4400, 580)
ob69 = sprites(cube, 4400, 580)
ob70 = sprites(cube, 4400, 580)
ob71 = sprites(cube, 4400, 580)
ob72 = sprites(cube, 4400, 580)
ob73 = sprites(cube, 4400, 580)
ob74 = sprites(cube, 4400, 580)
ob75 = sprites(cube, 4400, 580)
ob76 = sprites(cube, 4400, 580)
ob77 = sprites(cube, 4400, 580)
ob78 = sprites(cube, 4400, 580)
ob79 = sprites(cube, 4400, 580)
ob80 = sprites(cube, 4400, 580)
ob81 = sprites(cube, 4400, 580)
ob82 = sprites(cube, 4400, 580)
ob83 = sprites(cube, 4400, 580)
ob84 = sprites(cube, 4400, 580)
ob85 = sprites(cube, 4400, 580)
ob86 = sprites(cube, 4400, 580)
ob87 = sprites(cube, 4400, 580)
ob88 = sprites(cube, 4400, 580)
ob89 = sprites(cube, 4400, 580)
ob90 = sprites(cube, 4400, 580)
ob91 = sprites(cube, 4400, 580)
ob92 = sprites(cube, 4400, 580)
ob93 = sprites(cube, 4400, 580)
ob94 = sprites(cube, 4400, 580)
ob95 = sprites(cube, 4400, 580)
ob96 = sprites(cube, 4400, 580)
ob97 = sprites(cube, 4400, 580)
ob98 = sprites(cube, 4400, 580)
ob99 = sprites(cube, 4400, 580)
ob100 = sprites(cube, 4400, 580)
ob101 = sprites(cube, 4400, 580)
ob102 = sprites(cube, 4400, 580)
ob103 = sprites(cube, 4400, 580)
ob104 = sprites(cube, 4400, 580)
ob105 = sprites(cube, 4400, 580)
ob106 = sprites(cube, 4400, 580)
ob107 = sprites(cube, 4400, 580)
ob108 = sprites(cube, 4400, 580)
ob109 = sprites(cube, 4400, 580)
ob110 = sprites(cube, 4400, 580)
ob111 = sprites(cube, 4400, 580)
ob112 = sprites(cube, 4400, 580)
ob113 = sprites(cube, 4400, 580)
ob114 = sprites(cube, 4400, 580)
ob115 = sprites(cube, 4400, 580)
ob116 = sprites(cube, 4400, 580)
ob117 = sprites(cube, 4400, 580)
ob118 = sprites(cube, 4400, 580)
ob119 = sprites(cube, 4400, 580)
ob120 = sprites(cube, 4400, 580)
ob121 = sprites(cube, 4400, 580)
ob122 = sprites(cube, 4400, 580)
ob123 = sprites(cube, 4400, 580)
ob124 = sprites(cube, 4400, 580)
ob125 = sprites(cube, 4400, 580)
ob126 = sprites(cube, 4400, 580)
ob127 = sprites(cube, 4400, 580)
ob128 = sprites(cube, 4400, 580)
ob129 = sprites(cube, 4400, 580)
ob130 = sprites(cube, 4400, 580)
ob131 = sprites(cube, 4400, 580)
ob132 = sprites(cube, 4400, 580)
ob133 = sprites(cube, 4400, 580)
ob134 = sprites(cube, 4400, 580)
ob135 = sprites(cube, 4400, 580)
ob136 = sprites(cube, 4400, 580)
ob137 = sprites(cube, 4400, 580)
ob138 = sprites(cube, 4400, 580)
ob139 = sprites(cube, 4400, 580)
ob140 = sprites(cube, 4400, 580)
ob141 = sprites(cube, 4400, 580)
ob142 = sprites(cube, 4400, 580)
ob143 = sprites(cube, 4400, 580)
ob144 = sprites(cube, 4400, 580)
ob145 = sprites(cube, 4400, 580)
ob146 = sprites(cube, 4400, 580)
ob147 = sprites(cube, 4400, 580)
ob148 = sprites(cube, 4400, 580)
ob149 = sprites(cube, 4400, 580)
ob150 = sprites(cube, 4400, 580)
ob151 = sprites(cube, 4400, 580)
ob152 = sprites(cube, 4400, 580)
ob153 = sprites(cube, 4400, 580)
ob154 = sprites(cube, 4400, 580)
ob155 = sprites(cube, 4400, 580)
ob156 = sprites(cube, 4400, 580)
ob157 = sprites(cube, 4400, 580)
ob158 = sprites(cube, 4400, 580)
ob159 = sprites(cube, 4400, 580)
ob160 = sprites(cube, 4400, 580)
ob161 = sprites(cube, 4400, 580)
ob162 = sprites(cube, 4400, 580)
ob163 = sprites(cube, 4400, 580)
ob164 = sprites(cube, 4400, 580)
ob165 = sprites(cube, 4400, 580)
ob166 = sprites(cube, 4400, 580)
ob167 = sprites(cube, 4400, 580)
ob168 = sprites(cube, 4400, 580)
ob169 = sprites(cube, 4400, 580)
ob170 = sprites(cube, 4400, 580)
ob171 = sprites(cube, 4400, 580)
ob172 = sprites(cube, 4400, 580)
ob173 = sprites(cube, 4400, 580)
ob174 = sprites(cube, 4400, 580)
ob175 = sprites(cube, 4400, 580)
ob176 = sprites(cube, 4400, 580)
ob177 = sprites(cube, 4400, 580)
ob178 = sprites(cube, 4400, 580)
ob179 = sprites(cube, 4400, 580)
ob180 = sprites(cube, 4400, 580)
ob181 = sprites(cube, 4400, 580)
ob182 = sprites(cube, 4400, 580)
ob183 = sprites(cube, 4400, 580)
ob184 = sprites(cube, 4400, 580)
ob185 = sprites(cube, 4400, 580)
ob186 = sprites(cube, 4400, 580)
ob187 = sprites(cube, 4400, 580)
ob188 = sprites(cube, 4400, 580)
ob189 = sprites(cube, 4400, 580)
ob190 = sprites(cube, 4400, 580)
ob191 = sprites(cube, 4400, 580)
ob192 = sprites(cube, 4400, 580)
ob193 = sprites(cube, 4400, 580)
ob194 = sprites(cube, 4400, 580)
ob195 = sprites(cube, 4400, 580)
ob196 = sprites(cube, 4400, 580)
ob197 = sprites(cube, 4400, 580)
ob198 = sprites(cube, 4400, 580)
ob199 = sprites(cube, 4400, 580)
ob200 = sprites(cube, 4400, 580)
ob201 = sprites(cube, 4400, 580)
ob202 = sprites(cube, 4400, 580)
ob203 = sprites(cube, 4400, 580)
ob204 = sprites(cube, 4400, 580)
ob205 = sprites(cube, 4400, 580)
ob206 = sprites(cube, 4400, 580)
ob207 = sprites(cube, 4400, 580)
ob208 = sprites(cube, 4400, 580)
ob209 = sprites(cube, 4400, 580)
ob210 = sprites(cube, 4400, 580)
ob211 = sprites(cube, 4400, 580)
ob212 = sprites(cube, 4400, 580)
ob213 = sprites(cube, 4400, 580)
ob214 = sprites(cube, 4400, 580)
ob215 = sprites(cube, 4400, 580)
ob216 = sprites(cube, 4400, 580)
ob217 = sprites(cube, 4400, 580)
ob218 = sprites(cube, 4400, 580)
ob219 = sprites(cube, 4400, 580)
ob220 = sprites(cube, 4400, 580)
ob221 = sprites(cube, 4400, 580)
ob222 = sprites(cube, 4400, 580)
ob223 = sprites(cube, 4400, 580)
ob224 = sprites(cube, 4400, 580)
ob225 = sprites(cube, 4400, 580)
ob226 = sprites(cube, 4400, 580)
ob227 = sprites(cube, 4400, 580)
ob228 = sprites(cube, 4400, 580)
ob229 = sprites(cube, 4400, 580)
ob230 = sprites(cube, 4400, 580)
ob231 = sprites(cube, 4400, 580)
ob232 = sprites(cube, 4400, 580)
ob233 = sprites(cube, 4400, 580)
ob234 = sprites(cube, 4400, 580)
ob235 = sprites(cube, 4400, 580)
ob236 = sprites(cube, 4400, 580)
ob237 = sprites(cube, 4400, 580)
ob238 = sprites(cube, 4400, 580)
ob239 = sprites(cube, 4400, 580)
ob240 = sprites(cube, 4400, 580)
ob241 = sprites(cube, 4400, 580)
ob242 = sprites(cube, 4400, 580)
ob243 = sprites(cube, 4400, 580)
ob244 = sprites(cube, 4400, 580)
ob245 = sprites(cube, 4400, 580)
ob246 = sprites(cube, 4400, 580)
ob247 = sprites(cube, 4400, 580)
ob248 = sprites(cube, 4400, 580)
ob249 = sprites(cube, 4400, 580)
ob250 = sprites(cube, 4400, 580)
ob251 = sprites(cube, 4400, 580)
ob252 = sprites(cube, 4400, 580)
ob253 = sprites(cube, 4400, 580)
ob254 = sprites(cube, 4400, 580)
ob255 = sprites(cube, 4400, 580)
ob256 = sprites(cube, 4400, 580)
ob257 = sprites(cube, 4400, 580)
ob258 = sprites(cube, 4400, 580)
ob259 = sprites(cube, 4400, 580)
ob260 = sprites(cube, 4400, 580)
ob261 = sprites(cube, 4400, 580)
ob262 = sprites(cube, 4400, 580)
ob263 = sprites(cube, 4400, 580)
ob264 = sprites(cube, 4400, 580)
ob265 = sprites(cube, 4400, 580)
ob266 = sprites(cube, 4400, 580)
ob267 = sprites(cube, 4400, 580)
ob268 = sprites(cube, 4400, 580)
ob269 = sprites(cube, 4400, 580)
ob270 = sprites(cube, 4400, 580)
ob271 = sprites(cube, 4400, 580)
ob272 = sprites(cube, 4400, 580)
ob273 = sprites(cube, 4400, 580)
ob274 = sprites(cube, 4400, 580)
ob275 = sprites(cube, 4400, 580)
ob276 = sprites(cube, 4400, 580)
ob277 = sprites(cube, 4400, 580)
ob278 = sprites(cube, 4400, 580)
ob279 = sprites(cube, 4400, 580)
ob280 = sprites(cube, 4400, 580)
ob281 = sprites(cube, 4400, 580)
ob282 = sprites(cube, 4400, 580)
ob283 = sprites(cube, 4400, 580)
ob284 = sprites(cube, 4400, 580)
ob285 = sprites(cube, 4400, 580)
ob286 = sprites(cube, 4400, 580)
ob287 = sprites(cube, 4400, 580)
ob288 = sprites(cube, 4400, 580)
ob289 = sprites(cube, 4400, 580)
ob290 = sprites(cube, 4400, 580)
ob291 = sprites(cube, 4400, 580)
ob292 = sprites(cube, 4400, 580)
ob293 = sprites(cube, 4400, 580)
ob294 = sprites(cube, 4400, 580)
ob295 = sprites(cube, 4400, 580)
ob296 = sprites(cube, 4400, 580)
ob297 = sprites(cube, 4400, 580)
ob298 = sprites(cube, 4400, 580)
ob299 = sprites(cube, 4400, 580)
ob300 = sprites(cube, 4400, 580)
ob301 = sprites(cube, 4400, 580)
ob302 = sprites(cube, 4400, 580)
ob303 = sprites(cube, 4400, 580)
ob304 = sprites(cube, 4400, 580)
ob305 = sprites(cube, 4400, 580)
ob306 = sprites(cube, 4400, 580)
ob307 = sprites(cube, 4400, 580)
ob308 = sprites(cube, 4400, 580)
ob309 = sprites(cube, 4400, 580)
ob310 = sprites(cube, 4400, 580)
ob311 = sprites(cube, 4400, 580)
ob312 = sprites(cube, 4400, 580)
ob313 = sprites(cube, 4400, 580)
ob314 = sprites(cube, 4400, 580)
ob315 = sprites(cube, 4400, 580)
ob316 = sprites(cube, 4400, 580)
ob317 = sprites(cube, 4400, 580)
ob318 = sprites(cube, 4400, 580)
ob319 = sprites(cube, 4400, 580)
ob320 = sprites(cube, 4400, 580)
ob321 = sprites(cube, 4400, 580)
ob322 = sprites(cube, 4400, 580)
ob323 = sprites(cube, 4400, 580)
ob324 = sprites(cube, 4400, 580)
ob325 = sprites(cube, 4400, 580)
ob326 = sprites(cube, 4400, 580)
ob327 = sprites(cube, 4400, 580)
ob328 = sprites(cube, 4400, 580)
ob329 = sprites(cube, 4400, 580)
ob330 = sprites(cube, 4400, 580)
ob331 = sprites(cube, 4400, 580)
ob332 = sprites(cube, 4400, 580)
ob333 = sprites(cube, 4400, 580)
ob334 = sprites(cube, 4400, 580)
ob335 = sprites(cube, 4400, 580)
ob336 = sprites(cube, 4400, 580)
ob337 = sprites(cube, 4400, 580)
ob338 = sprites(cube, 4400, 580)
ob339 = sprites(cube, 4400, 580)
ob340 = sprites(cube, 4400, 580)
ob341 = sprites(cube, 4400, 580)
ob342 = sprites(cube, 4400, 580)
ob343 = sprites(cube, 4400, 580)
ob344 = sprites(cube, 4400, 580)
ob345 = sprites(cube, 4400, 580)
ob346 = sprites(cube, 4400, 580)
ob347 = sprites(cube, 4400, 580)
ob348 = sprites(cube, 4400, 580)
ob349 = sprites(cube, 4400, 580)


pygame.display.set_caption("lets play!")
theSong=ourMusic("christmas.ogg")
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
                ob221, ob222, ob223, ob224, ob225, ob226, ob227, ob228, ob229, ob230,
                ob231, ob232, ob233, ob234, ob235, ob236, ob237, ob238, ob239, ob240,
                ob241, ob242, ob243, ob244, ob245, ob246, ob247, ob248, ob249, ob250,
                ob251, ob252, ob253, ob254)
spritesgroup1=pygame.sprite.Group()
spritesgroup1.add(ob255, ob256, ob257, ob258, ob259, ob260, ob261, ob262, ob263, ob264,
                ob265, ob266, ob267, ob268, ob269, ob270, ob271, ob272, ob273, ob274,
                ob275, ob276, ob277, ob278, ob279, ob280, ob281, ob282, ob283, ob284,
                ob285, ob286, ob287, ob288, ob289, ob290, ob291, ob292, ob293, ob294,
                ob295, ob296, ob297, ob298, ob299, ob300, ob301, ob302, ob303, ob304,
                ob305, ob306, ob307, ob308, ob309, ob310, ob311, ob312, ob313, ob314,
                ob315, ob316, ob317, ob318, ob319, ob320, ob321, ob322, ob323, ob324,
                ob325, ob326, ob327, ob328, ob329, ob330, ob331, ob332, ob333, ob334,
                ob335, ob336, ob337, ob338, ob339, ob340, ob341, ob342, ob343, ob344,
                ob345, ob346, ob347, ob348, ob349)

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
        player.rect.y -= 65
        if player.rect.y <= 410:
            ycoor = 500
            jump = False
            fall = True

    if fall:
        player.rect.y += 65
        if player.rect.y >= 544:
            ycoor = 0
            fall = False
    pygame.display.update()
    gameDisplay.blit(bg,[0,0])
    time.sleep(.05)
    player.pos()
    spritesgroup.draw(gameDisplay)
    spritesgroup1.draw(gameDisplay)
    ob.left(40)
    if(timer > 5800):
        ob1.left(40)
    if(timer > 10500):
        ob2.left(40)
    if(timer > 14300):
        ob3.left(40)
    if(timer > 18300):
        ob4.left(40)
    if(timer > 21400):
        ob5.left(40)
    if(timer > 22600):
        ob6.left(40)
    if(timer > 25200):
        ob7.left(40)
    if(timer > 26400):
        ob8.left(40)
    if(timer > 28800):
        ob9.left(40)
    if(timer > 33000):
        ob10.left(40)
    if(timer > 35600):
        ob11.left(40)
    if(timer > 44600):
        ob12.left(40)
    if(timer > 45000): #1
        ob13.left(40)
    if(timer > 45400): #2
        ob14.left(40)
    if(timer > 45800): #3
        ob15.left(40)
    if(timer > 46200): #4
        ob16.left(40)
    if(timer > 46600): #5
        ob17.left(40)
    if(timer > 47000): #6
        ob18.left(40)
    if(timer > 47400): #7
        ob19.left(40)
    if(timer > 47800): #8
        ob20.left(40)
    if(timer > 48200): #9
        ob21.left(40)
    if(timer > 48600): #10
        ob22.left(40)
    if(timer > 49000): #11
        ob23.left(40)
    if(timer > 49400): #12
        ob24.left(40)
    if(timer > 49800): #13
        ob25.left(40)
    if(timer > 50200):
        ob26.left(40)
    if(timer > 50600):
        ob27.left(40)
    if(timer > 51000):
        ob28.left(40)
    if(timer > 52000):
        ob29.left(40)
    if(timer > 52830):
        ob30.left(40)
    if(timer > 53660):
        ob31.left(40)
    if(timer > 54490):
        ob32.left(40)
    if(timer > 55320):
        ob33.left(40)
    if(timer > 56150):
        ob34.left(40)
    if(timer > 56980):
        ob35.left(40)
    if(timer > 57810):
        ob36.left(40)
    if(timer > 58640):
        ob37.left(40)
    if(timer > 59470):
        ob38.left(40)
    if(timer > 60300):
        ob39.left(40)
    if(timer > 61130):
        ob40.left(40)
    if(timer > 61960):
        ob41.left(40)
    if(timer > 62790):
        ob42.left(40)
    if(timer > 63620):
        ob43.left(40)
    if(timer > 64450):
        ob44.left(40)
    if(timer > 65280):
        ob45.left(40)
    if(timer > 66110):
        ob46.left(40)
    if(timer > 66940):
        ob47.left(40)
    if(timer > 67770):
        ob48.left(40)
    if(timer > 68600):
        ob49.left(40)
    if(timer > 69430):
        ob50.left(40)
    if(timer > 70260):
        ob51.left(40)
    if(timer > 71090):
        ob52.left(40)
    if(timer > 71920):
        ob53.left(40)
    if(timer > 72750):
        ob54.left(40)
    if(timer > 73580):
        ob55.left(40)
    if(timer > 74410):
        ob56.left(40)
    if(timer > 75240):
        ob57.left(40)
    if(timer > 76070):
        ob58.left(40)
    if(timer > 76900):
        ob59.left(40)
    if(timer > 77730):
        ob60.left(40)
    if(timer > 78560):
        ob61.left(40)
    if(timer > 79390):
        ob62.left(40)
    if(timer > 80220):
        ob63.left(40)
    if(timer > 81050):
        ob64.left(40)
    if(timer > 81880):
        ob65.left(40)
    if(timer > 82710):
        ob66.left(40)
    if(timer > 83540):
        ob67.left(40)
    if(timer > 84370):
        ob68.left(40)
    if(timer > 85200):
        ob69.left(40)
    if(timer > 86030):
        ob70.left(40)
    if(timer > 86860):
        ob71.left(40)
    if(timer > 87690):
        ob72.left(40)
    if(timer > 88520):
        ob73.left(40)
    if(timer > 89350):
        ob74.left(40)
    if(timer > 90180):
        ob75.left(40)
    if(timer > 91010):
        ob76.left(40)
    if(timer > 91840):
        ob77.left(40)
    if(timer > 92670):
        ob78.left(40)
    if(timer > 93500):
        ob79.left(40)
    if(timer > 94330):
        ob80.left(40)
    if(timer > 95160):
        ob81.left(40)
    if(timer > 95990):
        ob82.left(40)
    if(timer > 96820):
        ob83.left(40)
    if(timer > 97220):
        ob84.left(40)
    if(timer > 97620):
        ob85.left(40)
    if(timer > 98020):
        ob86.left(40)
    if(timer > 98420):
        ob87.left(40)
    if(timer > 98820):
        ob88.left(40)
    if(timer > 99220):
        ob89.left(40)
    if(timer > 99620):
        ob90.left(40)
    if(timer > 100020):
        ob91.left(40)
    if(timer > 100420):
        ob92.left(40)
    if(timer > 100820):
        ob93.left(40)
    if(timer > 101220):
        ob94.left(40)
    if(timer > 101620):
        ob95.left(40)
    if(timer > 102020):
        ob96.left(40)
    if(timer > 102420):
        ob97.left(40)
    if(timer > 102820):
        ob98.left(40)
    if(timer > 103220):
        ob99.left(40)
    if(timer > 103620):
        ob100.left(40)
    if(timer > 104020):
        ob101.left(40)
    if(timer > 104420):
        ob102.left(40)
    if(timer > 104820):
        ob103.left(40)
    if(timer > 105650):
        ob104.left(40)
    if(timer > 106480):
        ob105.left(40)
    if(timer > 107310):
        ob106.left(40)
    if(timer > 108140):
        ob107.left(40)
    if(timer > 108970):
        ob108.left(40)
    if(timer > 109800):
        ob109.left(40)
    if(timer > 110630):
        ob110.left(40)
    if(timer > 111460):
        ob111.left(40)
    if(timer > 112290):
        ob112.left(40)
    if(timer > 113120):
        ob113.left(40)
    if(timer > 113950):
        ob114.left(40)
    if(timer > 114780):
        ob115.left(40)
    if(timer > 115610):
        ob116.left(40)
    if(timer > 116440):
        ob117.left(40)
    if(timer > 117270):
        ob118.left(40)
    if(timer > 118100):
        ob119.left(40)
    if(timer > 118930):
        ob120.left(40)
    if(timer > 119760):
        ob121.left(40)
    if(timer > 120590):
        ob122.left(40)
    if(timer > 121420):
        ob123.left(40)
    if(timer > 122250):
        ob124.left(40)
    if(timer > 123080):
        ob125.left(40)
    if(timer > 123910):
        ob126.left(40)
    if(timer > 124740):
        ob127.left(40)
    if(timer > 125570):
        ob128.left(40)
    if(timer > 126400):
        ob129.left(40)
    if(timer > 127230):
        ob130.left(40)
    if(timer > 128060):
        ob131.left(40)
    if(timer > 128460):
        ob132.left(40)
    if(timer > 128860):
        ob133.left(40)
    if(timer > 129260):
        ob134.left(40)
    if(timer > 129660):
        ob135.left(40)
    if(timer > 130060):
        ob136.left(40)
    if(timer > 130460):
        ob137.left(40)
    if(timer > 130860):
        ob138.left(40)
    if(timer > 131260):
        ob139.left(40)
    if(timer > 131660):
        ob140.left(40)
    if(timer > 132060):
        ob141.left(40)
    if(timer > 132460):
        ob142.left(40)
    if(timer > 132860):
        ob143.left(40)
    if(timer > 133260):
        ob144.left(40)
    if(timer > 133660):
        ob145.left(40)
    if(timer > 134490):
        ob146.left(40)
    if(timer > 135320):
        ob147.left(40)
    if(timer > 136150):
        ob148.left(40)
    if(timer > 136980):
        ob149.left(40)
    if(timer > 137810):
        ob150.left(40)
    if(timer > 138640):
        ob151.left(40)
    if(timer > 139470):
        ob152.left(40)
    if(timer > 140300):
        ob153.left(40)
    if(timer > 141130):
        ob154.left(40)
    if(timer > 141960):
        ob155.left(40)
    if(timer > 142790):
        ob156.left(40)
    if(timer > 143620):
        ob157.left(40)
    if(timer > 144450):
        ob158.left(40)
    if(timer > 145280):
        ob159.left(40)
    if(timer > 145280):
        ob160.left(40)
    if(timer > 145280):
        ob161.left(40)
    if(timer > 145280):
        ob162.left(40)
    if(timer > 145280):
        ob163.left(40)
    if(timer > 145280):
        ob164.left(40)
    if(timer > 145280):
        ob165.left(40)
    if(timer > 145280):
        ob167.left(40)
    if(timer > 145280):
        ob168.left(40)
    if(timer > 145280):
        ob169.left(40)
    if(timer > 145280):
        ob170.left(40)
    if(timer > 145280):
        ob171.left(40)
    if(timer > 145280):
        ob172.left(40)
    if(timer > 145280):
        ob173.left(40)
    if(timer > 145280):
        ob174.left(40)
    if(timer > 145280):
        ob175.left(40)
    if(timer > 145280):
        ob176.left(40)
    if(timer > 145280):
        ob177.left(40)
    if(timer > 145280):
        ob178.left(40)
    if(timer > 145280):
        ob179.left(40)
    if(timer > 145280):
        ob180.left(40)
    if(timer > 145280):
        ob181.left(40)
    if(timer > 145280):
        ob182.left(40)
    if(timer > 145280):
        ob183.left(40)
    if(timer > 145280):
        ob184.left(40)
    if(timer > 145280):
        ob185.left(40)
    if(timer > 145280):
        ob186.left(40)
    if(timer > 145280):
        ob187.left(40)
    if(timer > 145280):
        ob188.left(40)
    if(timer > 145280):
        ob189.left(40)
    if(timer > 146110):
        ob190.left(40)
    if(timer > 146940):
        ob191.left(40)
    if(timer > 147770):
        ob192.left(40)
    if(timer > 148600):
        ob193.left(40)
    if(timer > 149430):
        ob194.left(40)
    if(timer > 150260):
        ob195.left(40)
    if(timer > 151090):
        ob196.left(40)
    if(timer > 151920):
        ob197.left(40)
    if(timer > 152320):
        ob198.left(40)
    if(timer > 152720):
        ob199.left(40)
    if(timer > 153120):
        ob200.left(40)
    if(timer > 153520):
        ob201.left(40)
    if(timer > 153920):
        ob202.left(40)
    if(timer > 154320):
        ob203.left(40)
    if(timer > 154720):
        ob204.left(40)
    if(timer > 155120):
        ob205.left(40)
    if(timer > 155520):
        ob206.left(40)
    if(timer > 155920):
        ob207.left(40)
    if(timer > 156320):
        ob208.left(40)
    if(timer > 156720):
        ob209.left(40)
    if(timer > 157120):
        ob210.left(40)
    if(timer > 157520):
        ob211.left(40)
    if(timer > 158350):
        ob212.left(40)
    if(timer > 159180):
        ob213.left(40)
    if(timer > 160010):
        ob214.left(40)
    if(timer > 160840):
        ob215.left(40)
    if(timer > 161670):
        ob216.left(40)
    if(timer > 162500):
        ob217.left(40)
    if(timer > 163330):
        ob218.left(40)
    if(timer > 164160):
        ob219.left(40)
    if(timer > 164990):
        ob220.left(40)
    if(timer > 165820):
        ob221.left(40)
    if(timer > 166650):
        ob222.left(40)
    if(timer > 167480):
        ob223.left(40)
    if(timer > 168310):
        ob224.left(40)
    if(timer > 169140):
        ob225.left(40)
    if(timer > 169970):
        ob226.left(40)
    if(timer > 170800):
        ob227.left(40)
    if(timer > 171200):
        ob228.left(40)
    if(timer > 171600):
        ob229.left(40)
    if(timer > 172000):
        ob230.left(40)
    if(timer > 172400):
        ob231.left(40)
    if(timer > 172800):
        ob232.left(40)
    if(timer > 173200):
        ob233.left(40)
    if(timer > 173600):
        ob234.left(40)
    if(timer > 174000):
        ob235.left(40)
    if(timer > 174400):
        ob236.left(40)
    if(timer > 174800):
        ob237.left(40)
    if(timer > 175200):
        ob238.left(40)
    if(timer > 175600):
        ob239.left(40)
    if(timer > 176000):
        ob240.left(40)
    if(timer > 176400):
        ob241.left(40)
    if(timer > 176800):
        ob242.left(40)
    if(timer > 177200):
        ob243.left(40)
    if(timer > 177600):
        ob244.left(40)
    if(timer > 178000):
        ob245.left(40)
    if(timer > 178400):
        ob246.left(40)
    if(timer > 178800):
        ob247.left(40)
    if(timer > 179200):
        ob248.left(40)
    if(timer > 179600):
        ob249.left(40)
    if(timer > 180000):
        ob250.left(40)
    if(timer > 180400):
        ob251.left(40)
    if(timer > 180800):
        ob252.left(40)
    if(timer > 181200):
        ob253.left(40)
    if(timer > 181600):
        ob254.left(40)
    if(timer > 182000):
        ob255.left(40)
    if(timer > 182400):
        ob256.left(40)
    if(timer > 182800):
        ob257.left(40)
    if(timer > 183200):
        ob258.left(40)
    if(timer > 183600):
        ob259.left(40)
    if(timer > 184000):
        ob260.left(40)
    if(timer > 184400):
        ob261.left(40)
    if(timer > 184800):
        ob262.left(40)
    if(timer > 185200):
        ob263.left(40)
    if(timer > 185600):
        ob264.left(40)
    if(timer > 186000):
        ob265.left(40)
    if(timer > 186400):
        ob266.left(40)
    if(timer > 186800):
        ob267.left(40)
    if(timer > 187200):
        ob268.left(40)
    if(timer > 187600):
        ob269.left(40)
    if(timer > 188000):
        ob270.left(40)
    if(timer > 188400):
        ob271.left(40)
    if(timer > 188800):
        ob272.left(40)
    if(timer > 189200):
        ob273.left(40)
    if(timer > 189600):
        ob274.left(40)
    if(timer > 190000):
        ob275.left(40)
    if(timer > 190400):
        ob276.left(40)
    if(timer > 190800):
        ob277.left(40)
    if(timer > 191200):
        ob278.left(40)
    if(timer > 191600):
        ob279.left(40)
    if(timer > 192000):
        ob280.left(40)
    if(timer > 192400):
        ob281.left(40)
    if(timer > 192800):
        ob282.left(40)
    if(timer > 193200):
        ob283.left(40)
    if(timer > 193600):
        ob284.left(40)
    if(timer > 194000):
        ob285.left(40)
    if(timer > 194400):
        ob286.left(40)
    if(timer > 194800):
        ob287.left(40)
    if(timer > 195200):
        ob288.left(40)
    if(timer > 195600):
        ob289.left(40)
    if(timer > 196000):
        ob290.left(40)
    if(timer > 196400):
        ob291.left(40)
    if(timer > 196800):
        ob292.left(40)
    if(timer > 197200):
        ob293.left(40)
    if(timer > 197600):
        ob294.left(40)
    if(timer > 198000):
        ob295.left(40)
    if(timer > 198400):
        ob296.left(40)
    if(timer > 198800):
        ob297.left(40)
    if(timer > 199200):
        ob298.left(40)
    if(timer > 199600):
        ob299.left(40)
    if(timer > 200000):
        ob300.left(40)
    if(timer > 200400):
        ob301.left(40)
    if(timer > 200800):
        ob302.left(40)
    if(timer > 201200):
        ob303.left(40)
    if(timer > 201600):
        ob304.left(40)
    if(timer > 202000):
        ob305.left(40)
    if(timer > 202400):
        ob306.left(40)
    if(timer > 202800):
        ob307.left(40)
    if(timer > 203200):
        ob308.left(40)
    if(timer > 203600):
        ob309.left(40)
    if(timer > 204000):
        ob310.left(40)
    if(timer > 204400):
        ob311.left(40)
    if(timer > 204800):
        ob312.left(40)
    if(timer > 205200):
        ob313.left(40)
    if(timer > 205600):
        ob314.left(40)
    if(timer > 206000):
        ob315.left(40)
    if(timer > 206400):
        ob316.left(40)
    if(timer > 206800):
        ob317.left(40)
    if(timer > 207200):
        ob318.left(40)
    if(timer > 207600):
        ob319.left(40)
    if(timer > 208000):
        ob320.left(40)
    if(timer > 208400):
        ob321.left(40)
    if(timer > 208800):
        ob322.left(40)
    if(timer > 209200):
        ob323.left(40)
    if(timer > 209600):
        ob324.left(40)
    if(timer > 210000):
        ob325.left(40)
    if(timer > 210400):
        ob326.left(40)
    if(timer > 210800):
        ob327.left(40)
    if(timer > 211200):
        ob328.left(40)
    if(timer > 211600):
        ob329.left(40)
    if(timer > 212000):
        ob330.left(40)
    if(timer > 212400):
        ob331.left(40)
    if(timer > 212800):
        ob332.left(40)
    if(timer > 213200):
        ob333.left(40)
    if(timer > 213600):
        ob334.left(40)
    if(timer > 214000):
        ob335.left(40)
    if(timer > 214400):
        ob336.left(40)
    if(timer > 214800):
        ob337.left(40)
    if(timer > 215200):
        ob338.left(40)
    if(timer > 215600):
        ob339.left(40)
    if(timer > 216000):
        ob340.left(40)
    if(timer > 216400):
        ob341.left(40)
    if(timer > 216800):
        ob342.left(40)
    if(timer > 217200):
        ob343.left(40)
    if(timer > 217600):
        ob344.left(40)
    if(timer > 218000):
        ob345.left(40)
    if(timer > 218400):
        ob346.left(40)
    if(timer > 218800):
        ob347.left(40)
    if(timer > 219200):
        ob348.left(40)
    if(timer > 219600):
        ob349.left(40)



    blocks_hit_list = pygame.sprite.spritecollide(pointob, spritesgroup, True)
    player_hit_list =  pygame.sprite.spritecollide(player, spritesgroup, True)
    blocks_hit_list1 = pygame.sprite.spritecollide(pointob, spritesgroup1, True)
    player_hit_list1 =  pygame.sprite.spritecollide(player, spritesgroup1, True)
    pygame.sprite.spritecollide(player, spritesgroup, True)
    if (blocks_hit_list != [] or blocks_hit_list1 != []):
        score+=10
        y=str(score)
    if (player_hit_list != [] or player_hit_list1 != []):
        score-=5
        y=str(score)
    score1=myfont.render(y, 1, (156,254,149))
    gameDisplay.blit(score1,(300, 50))
    label = myfont.render("YOUR CURRENT SCORE IS:", 1, (160,243,252))
    gameDisplay.blit(label, (300, 0))
    if (timer > 500) and (timer<4000):
        firstinstruct=myfonter.render("MARIAH CAREY - ALL I WANT FOR CHRISTMAS IS YOU ", 1, (156,254,149))
        gameDisplay.blit(firstinstruct, (50, 400))
    if (timer > 4100) and (timer<5100):
        firstinstruct=myfonter.render("READY!", 1, (156,254,149))
        gameDisplay.blit(firstinstruct, (50, 400))
    if (timer>5200 and timer<6200):
        firstinstruct=myfonter.render(" SET! ", 1, (156,254,149))
        gameDisplay.blit(firstinstruct, (50, 400))
    if (timer>6300 and timer<7300):
        firstinstruct=myfonter.render(" GO! ", 1, (156,254,149))
        gameDisplay.blit(firstinstruct, (50, 400))

    if int(y)>int(b):
        b=y
    if (timer>230000 and timer<240000):
        if b==y:
            first=myfont.render("NEW HIGH SCORE!", 1, (156,254,149))
            gameDisplay.blit(first, (50, 400))
            scorefile=open("christmasscores.txt", "w")
            b=str(b)
            scorefile.write(b)
            scorefile.close()
        else:
            b=str(b)
            highscores=("ALL TIME HIGH SCORE IS " + b)
            first=myfont.render(highscores, 1, (156,254,149))
            gameDisplay.blit(first, (50, 400))
            scorefile=open("christmasscores.txt", "w")
            scorefile.write(b)
            scorefile.close()
    if (timer > 241000):
            first=myfont.render("PRESS RETURN TO EXIT TO THE MAIN SCREEN", 1, (156,254,149))
            gameDisplay.blit(first, (50, 400))

pygame.quit() #unintiliazes pygames
with open("menu.py") as f:
    code = compile(f.read(), "menu.py", 'exec')
    exec(code)

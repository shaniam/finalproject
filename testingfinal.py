from direct.showbase.ShowBase import ShowBase
from panda3d.core import TextNode, PandaNode, NodePath, GeomNode, LineSegs
from direct.gui.OnscreenText import OnscreenText
from direct.actor.Actor import Actor
from models import ourMusic, sprites
import random
import sys
import os
import math

class selfMenu(ShowBase):
    def __init__(self):
        """Creates initial window"""
        # Set up the window, camera, etc.
        ShowBase.__init__(self)
        # Set the background color to black
        self.win.setClearColor((0, 0, 0, 1))
        #Loads the world
        self.newScreen()

    def setKey(self, key, value):
        """Binds moving actions to keys"""
        self.keyMap[key] = value

    def move(self, task):
        """Moves actor around and gets camera to follow"""

        #Time since the last frame was called
        dt = globalClock.getDt()

        # If a move-key is pressed, move moore in the specified direction.
        if self.keyMap["left"]:
            self.moore.setH(self.moore.getH() + 300 * dt)
        if self.keyMap["right"]:
            self.moore.setH(self.moore.getH() - 300 * dt)
        if self.keyMap["forward"]:
            self.moore.setY(self.moore, -25 * dt)

        # If Moore is moving, loop the run animation.
        # If he is standing still, stop the animation.

        if self.keyMap["forward"] or self.keyMap["left"] or self.keyMap["right"]:
            if self.isMoving is False:
                self.moore.loop("run")
                self.isMoving = True
        else:
            if self.isMoving:
                self.moore.stop()
                self.moore.pose("walk", 5)
                self.isMoving = False

        # If the camera is too far from Moore, move it closer.
        # If the camera is too close to Moore, move it farther.
        # Camera set far away so that it does not dip under the model

        camvec = self.moore.getPos() - self.camera.getPos()
        camdist = camvec.length()
        camvec.normalize()
        if camdist > 28.0:
            self.camera.setPos(self.camera.getPos() + camvec * (camdist - 28))
            camdist = 28.0
        if camdist < 3.0:
            self.camera.setPos(self.camera.getPos() - camvec * (3 - camdist))
            camdist = 3.0

        self.camera.lookAt(self.floater)


        # Makes lines that Moore can collide with to trigger an event
        self.collisionevent('castle',-5,-80,10)
        self.collisionevent('house',-70,-10,20)
        self.collisionevent('tepee',-10,115, 10)
        self.collisionevent('halloffame',55,-10,10)
        self.collisionevent('fifthline',-200,180,320)
        self.collisionevent('sixthline',120,-188,368)
        self.collisionevent('seventhline',-200,-188,320)
        self.collisionevent('eighthline',-200,-188,368)

        return task.cont

    def collisionevent(self,name,startx,starty,iterations):
        """Triggers an event upon a collision"""
        xnames=["castle","tepee","fifthline","seventhline"]
        ynames=["house","halloffame","sixthline","eighthline"]
        levelnames=['castle','house','tepee','halloffame']
        outsidenames=['fifthline','sixthline','seventhline','eighthline']
        self.name=LineSegs(name)
        self.name.moveTo(startx,starty,0)
        x=startx
        y=starty
        for i in range(iterations):
            self.name.drawTo(x,y,0)
            if name in xnames:
                x+=1
            if name in ynames:
                y+=1
        self.name.create()
        vertexlist=self.name.getVertices()

        coorlist=[]

        for i in range(len(vertexlist)):
            coorlist.append([vertexlist[i][0],vertexlist[i][1]])


        moorecoor= [int(self.moore.getX()),int(self.moore.getY())]

        if (moorecoor in coorlist):
            if name in levelnames:
                base.graphicsEngine.removeWindow(self.win)
                self.secondWindow(name)

            if name in outsidenames:
                self.moore.setPos(0,0,0)

    def secondWindow(self,name):
        #secondwindowcode, after level code based on level
        if name=='castle':
            self.music.stop()
            self.test = Controller()

        if name=='house':
            self.music.stop()
            with open("hometown.py") as f:
                code = compile(f.read(), "hometown.py", 'exec')
                exec(code)

        if name=='tepee':
            self.music.stop()
            with open("m83.py") as f:
                code = compile(f.read(), "m83.py", 'exec')
                exec(code)

        if name=='halloffame':
            print("")

    def startMusic(self):
        """Starts and stops music"""
        if self.music:
            self.music.stop()
            self.music = None
        else:
            self.music = self.loader.loadMusic("phase/gunsforhands.ogg")
            self.music.play()


    def newScreen(self):
        """Creates screen with world model and actors"""

        #Loads world model
        self.world = loader.loadModel("phase/trialworld.bam")
        self.world.reparentTo(render)
        #Loads the font
        self.font = loader.loadFont("phase/LemonMilk.ttf")


        self.keyMap = {
            "left": 0, "right": 0, "forward": 0, "cam-left": 0, "cam-right": 0}
        #Loads actor and animations
        mooreStartPos = (0,0,0)
        self.moore = Actor("phase/ralph",
                           {"run": "phase/ralph-run",
                            "walk": "phase/ralph-walk"})
        self.moore.reparentTo(render)
        self.moore.setScale(.2)
        self.moore.setPos(mooreStartPos)
        # Loads a floater above Moore's head to point the camera at
        self.floater = NodePath(PandaNode("floater"))
        self.floater.reparentTo(self.moore)

        #Controls for moving actor around
        self.accept("a", self.setKey, ["left", True])
        self.accept("d", self.setKey, ["right", True])
        self.accept("w", self.setKey, ["forward", True])
        self.accept("a-up", self.setKey, ["left", False])
        self.accept("d-up", self.setKey, ["right", False])
        self.accept("w-up", self.setKey, ["forward", False])

        taskMgr.add(self.move, "moveTask")

        self.isMoving = False

        # Set up the camera
        # Disables the mouse from moving the scren
        self.disableMouse()
        self.camera.setPos(self.moore.getX(), self.moore.getY()+10, self.moore.getZ()+2)

        # Loads the music file
        self.music = self.loader.loadMusic("phase/gunsforhands.ogg")
        # Plays the music
        self.music.play()
        # Starts/stops music
        self.accept("m-up", self.startMusic)
        # Creates a title
        self.title = self.addTitle("Moore's World: The Best World", self.font)
        # Creates the instructions
        self.inst1 = self.addInstructions(0.06, "ESC: Quit", self.font)
        self.inst5 = self.addInstructions(0.12, "M: Enable/Disable Music", self.font)
        self.inst2 = self.addInstructions(0.18, "CONTROLS: W/A/D", self.font)
        self.inst5 = self.addInstructions(0.24, "TEPEE: EASY", self.font)
        self.inst5 = self.addInstructions(0.30, "HOUSE: MEDIUM", self.font)
        self.inst5 = self.addInstructions(0.36, "CASTLE: HARD", self.font)
        # Exits the program
        self.accept("escape", sys.exit)


    def addInstructions(self, pos, msg, font):
        """Posts instructions on screen"""
        return OnscreenText(text=msg, style=1, font=font, fg=(1, 1, 1, 1), scale=.05,
                            shadow=(0, 0, 0, 1), parent=base.a2dTopLeft,
                            pos=(0.08, -pos - 0.04), align=TextNode.ALeft)

    def addTitle(self, text, font):
        """Posts title on screen"""
        return OnscreenText(text=text, style=1, font=font, fg=(1, 1, 1, 1), scale=.07,
                            parent=base.a2dBottomRight, align=TextNode.ARight,
                            pos=(-0.1, 0.09), shadow=(0, 0, 0, 1))

def main():
    """Runs program"""
    demo = selfMenu()
    demo.run()

main()

class Controller:
    def __init__(self):
        pygame.init() #short for initialize does return a tuple of successful intilizaton
        self.colors={"black":(0,0,0), "white": (255, 255, 255), "red": (255, 0, 0), "green": (0, 255, 0), "purple": (164, 66, 244), "pink" :(252, 25, 123)}
        self.gameDisplay= pygame.display.set_mode((800, 600))

        self.bg=pygame.image.load('clouds_converted.jpg')
        self.moore=pygame.image.load("baemoore_converted.png")
        self.myfont = pygame.font.SysFont("Extrude.ttf", 30)
        self.myfonter =pygame.font.SysFont("AldotheApache.ttf",60)
        self.jump = False
        self.fall = False


        self.cube = pygame.image.load("cube.png")
        self.pointo=sprites(self.cube, -10, 580) #the cube it will hit
        self.pointo.pos()
        self.player=sprites(self.moore, 50, 544)

        self.score=0
        self.y=str(self.score)
        self.scorething=open("christmasscores.txt", "r")
        self.scoresentence=self.scorething.readline()
        self.b=self.scoresentence.strip()
        self.b=int(self.b)
        self.scorething.close()

        self.ob = sprites(self.cube, 4400, 580)
        self.ob1 = sprites(self.cube, 4400, 580)
        self.ob2 = sprites(self.cube, 4400, 580)
        self.ob3 = sprites(self.cube, 4400, 580)
        self.ob4 = sprites(self.cube, 4400, 580)
        self.ob5 = sprites(self.cube, 4400, 580)
        self.ob6 = sprites(self.cube, 4400, 580)
        self.ob7 = sprites(self.cube, 4400, 580)
        self.ob8 = sprites(self.cube, 4400, 580)
        self.ob9 = sprites(self.cube, 4400, 580)
        self.ob10 = sprites(self.cube, 4400, 580)
        self.ob11 = sprites(self.cube, 4400, 580)
        self.ob12 = sprites(self.cube, 4400, 580)
        self.ob13 = sprites(self.cube, 4400, 580)
        self.ob14 = sprites(self.cube, 4400, 580)
        self.ob15 = sprites(self.cube, 4400, 580)
        self.ob16 = sprites(self.cube, 4400, 580)
        self.ob17 = sprites(self.cube, 4400, 580)
        self.ob18 = sprites(self.cube, 4400, 580)
        self.ob19 = sprites(self.cube, 4400, 580)
        self.ob20 = sprites(self.cube, 4400, 580)
        self.ob21 = sprites(self.cube, 4400, 580)
        self.ob22 = sprites(self.cube, 4400, 580)
        self.ob23 = sprites(self.cube, 4400, 580)
        self.ob24 = sprites(self.cube, 4400, 580)
        self.ob25 = sprites(self.cube, 4400, 580)
        self.ob26 = sprites(self.cube, 4400, 580)
        self.ob27 = sprites(self.cube, 4400, 580)
        self.ob28 = sprites(self.cube, 4400, 580)
        self.ob29 = sprites(self.cube, 4400, 580)
        self.ob30 = sprites(self.cube, 4400, 580)
        self.ob31 = sprites(self.cube, 4400, 580)
        self.ob32 = sprites(self.cube, 4400, 580)
        self.ob33 = sprites(self.cube, 4400, 580)
        self.ob34 = sprites(self.cube, 4400, 580)
        self.ob35 = sprites(self.cube, 4400, 580)
        self.ob36 = sprites(self.cube, 4400, 580)
        self.ob37 = sprites(self.cube, 4400, 580)
        self.ob38 = sprites(self.cube, 4400, 580)
        self.ob39 = sprites(self.cube, 4400, 580)
        self.ob40 = sprites(self.cube, 4400, 580)
        self.ob41 = sprites(self.cube, 4400, 580)
        self.ob42 = sprites(self.cube, 4400, 580)
        self.ob43 = sprites(self.cube, 4400, 580)
        self.ob44 = sprites(self.cube, 4400, 580)
        self.ob45 = sprites(self.cube, 4400, 580)
        self.ob46 = sprites(self.cube, 4400, 580)
        self.ob47 = sprites(self.cube, 4400, 580)
        self.ob48 = sprites(self.cube, 4400, 580)
        self.ob49 = sprites(self.cube, 4400, 580)
        self.ob50 = sprites(self.cube, 4400, 580)
        self.ob51 = sprites(self.cube, 4400, 580)
        self.ob52 = sprites(self.cube, 4400, 580)
        self.ob53 = sprites(self.cube, 4400, 580)
        self.ob54 = sprites(self.cube, 4400, 580)
        self.ob55 = sprites(self.cube, 4400, 580)
        self.ob56 = sprites(self.cube, 4400, 580)
        self.ob57 = sprites(self.cube, 4400, 580)
        self.ob58 = sprites(self.cube, 4400, 580)
        self.ob59 = sprites(self.cube, 4400, 580)
        self.ob60 = sprites(self.cube, 4400, 580)
        self.ob61 = sprites(self.cube, 4400, 580)
        self.ob62 = sprites(self.cube, 4400, 580)
        self.ob63 = sprites(self.cube, 4400, 580)
        self.ob64 = sprites(self.cube, 4400, 580)
        self.ob65 = sprites(self.cube, 4400, 580)
        self.ob66 = sprites(self.cube, 4400, 580)
        self.ob67 = sprites(self.cube, 4400, 580)
        self.ob68 = sprites(self.cube, 4400, 580)
        self.ob69 = sprites(self.cube, 4400, 580)
        self.ob70 = sprites(self.cube, 4400, 580)
        self.ob71 = sprites(self.cube, 4400, 580)
        self.ob72 = sprites(self.cube, 4400, 580)
        self.ob73 = sprites(self.cube, 4400, 580)
        self.ob74 = sprites(self.cube, 4400, 580)
        self.ob75 = sprites(self.cube, 4400, 580)
        self.ob76 = sprites(self.cube, 4400, 580)
        self.ob77 = sprites(self.cube, 4400, 580)
        self.ob78 = sprites(self.cube, 4400, 580)
        self.ob79 = sprites(self.cube, 4400, 580)
        self.ob80 = sprites(self.cube, 4400, 580)
        self.ob81 = sprites(self.cube, 4400, 580)
        self.ob82 = sprites(self.cube, 4400, 580)
        self.ob83 = sprites(self.cube, 4400, 580)
        self.ob84 = sprites(self.cube, 4400, 580)
        self.ob85 = sprites(self.cube, 4400, 580)
        self.ob86 = sprites(self.cube, 4400, 580)
        self.ob87 = sprites(self.cube, 4400, 580)
        self.ob88 = sprites(self.cube, 4400, 580)
        self.ob89 = sprites(self.cube, 4400, 580)
        self.ob90 = sprites(self.cube, 4400, 580)
        self.ob91 = sprites(self.cube, 4400, 580)
        self.ob92 = sprites(self.cube, 4400, 580)
        self.ob93 = sprites(self.cube, 4400, 580)
        self.ob94 = sprites(self.cube, 4400, 580)
        self.ob95 = sprites(self.cube, 4400, 580)
        self.ob96 = sprites(self.cube, 4400, 580)
        self.ob97 = sprites(self.cube, 4400, 580)
        self.ob98 = sprites(self.cube, 4400, 580)
        self.ob99 = sprites(self.cube, 4400, 580)
        self.ob100 = sprites(self.cube, 4400, 580)
        self.ob101 = sprites(self.cube, 4400, 580)
        self.ob102 = sprites(self.cube, 4400, 580)
        self.ob103 = sprites(self.cube, 4400, 580)
        self.ob104 = sprites(self.cube, 4400, 580)
        self.ob105 = sprites(self.cube, 4400, 580)
        self.ob106 = sprites(self.cube, 4400, 580)
        self.ob107 = sprites(self.cube, 4400, 580)
        self.ob108 = sprites(self.cube, 4400, 580)
        self.ob109 = sprites(self.cube, 4400, 580)
        self.ob110 = sprites(self.cube, 4400, 580)
        self.ob111 = sprites(self.cube, 4400, 580)
        self.ob112 = sprites(self.cube, 4400, 580)
        self.ob113 = sprites(self.cube, 4400, 580)
        self.ob114 = sprites(self.cube, 4400, 580)
        self.ob115 = sprites(self.cube, 4400, 580)
        self.ob116 = sprites(self.cube, 4400, 580)
        self.ob117 = sprites(self.cube, 4400, 580)
        self.ob118 = sprites(self.cube, 4400, 580)
        self.ob119 = sprites(self.cube, 4400, 580)
        self.ob120 = sprites(self.cube, 4400, 580)
        self.ob121 = sprites(self.cube, 4400, 580)
        self.ob122 = sprites(self.cube, 4400, 580)
        self.ob123 = sprites(self.cube, 4400, 580)
        self.ob124 = sprites(self.cube, 4400, 580)
        self.ob125 = sprites(self.cube, 4400, 580)
        self.ob126 = sprites(self.cube, 4400, 580)
        self.ob127 = sprites(self.cube, 4400, 580)
        self.ob128 = sprites(self.cube, 4400, 580)
        self.ob129 = sprites(self.cube, 4400, 580)
        self.ob130 = sprites(self.cube, 4400, 580)
        self.ob131 = sprites(self.cube, 4400, 580)
        self.ob132 = sprites(self.cube, 4400, 580)
        self.ob133 = sprites(self.cube, 4400, 580)
        self.ob134 = sprites(self.cube, 4400, 580)
        self.ob135 = sprites(self.cube, 4400, 580)
        self.ob136 = sprites(self.cube, 4400, 580)
        self.ob137 = sprites(self.cube, 4400, 580)
        self.ob138 = sprites(self.cube, 4400, 580)
        self.ob139 = sprites(self.cube, 4400, 580)
        self.ob140 = sprites(self.cube, 4400, 580)
        self.ob141 = sprites(self.cube, 4400, 580)
        self.ob142 = sprites(self.cube, 4400, 580)
        self.ob143 = sprites(self.cube, 4400, 580)
        self.ob144 = sprites(self.cube, 4400, 580)
        self.ob145 = sprites(self.cube, 4400, 580)
        self.ob146 = sprites(self.cube, 4400, 580)
        self.ob147 = sprites(self.cube, 4400, 580)
        self.ob148 = sprites(self.cube, 4400, 580)
        self.ob149 = sprites(self.cube, 4400, 580)
        self.ob150 = sprites(self.cube, 4400, 580)
        self.ob151 = sprites(self.cube, 4400, 580)
        self.ob152 = sprites(self.cube, 4400, 580)
        self.ob153 = sprites(self.cube, 4400, 580)
        self.ob154 = sprites(self.cube, 4400, 580)
        self.ob155 = sprites(self.cube, 4400, 580)
        self.ob156 = sprites(self.cube, 4400, 580)
        self.ob157 = sprites(self.cube, 4400, 580)
        self.ob158 = sprites(self.cube, 4400, 580)
        self.ob159 = sprites(self.cube, 4400, 580)
        self.ob160 = sprites(self.cube, 4400, 580)
        self.ob161 = sprites(self.cube, 4400, 580)
        self.ob162 = sprites(self.cube, 4400, 580)
        self.ob163 = sprites(self.cube, 4400, 580)
        self.ob164 = sprites(self.cube, 4400, 580)
        self.ob165 = sprites(self.cube, 4400, 580)
        self.ob166 = sprites(self.cube, 4400, 580)
        self.ob167 = sprites(self.cube, 4400, 580)
        self.ob168 = sprites(self.cube, 4400, 580)
        self.ob169 = sprites(self.cube, 4400, 580)
        self.ob170 = sprites(self.cube, 4400, 580)
        self.ob171 = sprites(self.cube, 4400, 580)
        self.ob172 = sprites(self.cube, 4400, 580)
        self.ob173 = sprites(self.cube, 4400, 580)
        self.ob174 = sprites(self.cube, 4400, 580)
        self.ob175 = sprites(self.cube, 4400, 580)
        self.ob176 = sprites(self.cube, 4400, 580)
        self.ob177 = sprites(self.cube, 4400, 580)
        self.ob178 = sprites(self.cube, 4400, 580)
        self.ob179 = sprites(self.cube, 4400, 580)
        self.ob180 = sprites(self.cube, 4400, 580)
        self.ob181 = sprites(self.cube, 4400, 580)
        self.ob182 = sprites(self.cube, 4400, 580)
        self.ob183 = sprites(self.cube, 4400, 580)
        self.ob184 = sprites(self.cube, 4400, 580)
        self.ob185 = sprites(self.cube, 4400, 580)
        self.ob186 = sprites(self.cube, 4400, 580)
        self.ob187 = sprites(self.cube, 4400, 580)
        self.ob188 = sprites(self.cube, 4400, 580)
        self.ob189 = sprites(self.cube, 4400, 580)
        self.ob190 = sprites(self.cube, 4400, 580)
        self.ob191 = sprites(self.cube, 4400, 580)
        self.ob192 = sprites(self.cube, 4400, 580)
        self.ob193 = sprites(self.cube, 4400, 580)
        self.ob194 = sprites(self.cube, 4400, 580)
        self.ob195 = sprites(self.cube, 4400, 580)
        self.ob196 = sprites(self.cube, 4400, 580)
        self.ob197 = sprites(self.cube, 4400, 580)
        self.ob198 = sprites(self.cube, 4400, 580)
        self.ob199 = sprites(self.cube, 4400, 580)
        self.ob200 = sprites(self.cube, 4400, 580)
        self.ob201 = sprites(self.cube, 4400, 580)
        self.ob202 = sprites(self.cube, 4400, 580)
        self.ob203 = sprites(self.cube, 4400, 580)
        self.ob204 = sprites(self.cube, 4400, 580)
        self.ob205 = sprites(self.cube, 4400, 580)
        self.ob206 = sprites(self.cube, 4400, 580)
        self.ob207 = sprites(self.cube, 4400, 580)
        self.ob208 = sprites(self.cube, 4400, 580)
        self.ob209 = sprites(self.cube, 4400, 580)
        self.ob210 = sprites(self.cube, 4400, 580)
        self.ob211 = sprites(self.cube, 4400, 580)
        self.ob212 = sprites(self.cube, 4400, 580)
        self.ob213 = sprites(self.cube, 4400, 580)
        self.ob214 = sprites(self.cube, 4400, 580)
        self.ob215 = sprites(self.cube, 4400, 580)
        self.ob216 = sprites(self.cube, 4400, 580)
        self.ob217 = sprites(self.cube, 4400, 580)
        self.ob218 = sprites(self.cube, 4400, 580)
        self.ob219 = sprites(self.cube, 4400, 580)
        self.ob220 = sprites(self.cube, 4400, 580)
        self.ob221 = sprites(self.cube, 4400, 580)
        self.ob222 = sprites(self.cube, 4400, 580)
        self.ob223 = sprites(self.cube, 4400, 580)
        self.ob224 = sprites(self.cube, 4400, 580)
        self.ob225 = sprites(self.cube, 4400, 580)
        self.ob226 = sprites(self.cube, 4400, 580)
        self.ob227 = sprites(self.cube, 4400, 580)
        self.ob228 = sprites(self.cube, 4400, 580)
        self.ob229 = sprites(self.cube, 4400, 580)
        self.ob230 = sprites(self.cube, 4400, 580)
        self.ob231 = sprites(self.cube, 4400, 580)
        self.ob232 = sprites(self.cube, 4400, 580)
        self.ob233 = sprites(self.cube, 4400, 580)
        self.ob234 = sprites(self.cube, 4400, 580)
        self.ob235 = sprites(self.cube, 4400, 580)
        self.ob236 = sprites(self.cube, 4400, 580)
        self.ob237 = sprites(self.cube, 4400, 580)
        self.ob238 = sprites(self.cube, 4400, 580)
        self.ob239 = sprites(self.cube, 4400, 580)
        self.ob240 = sprites(self.cube, 4400, 580)
        self.ob241 = sprites(self.cube, 4400, 580)
        self.ob242 = sprites(self.cube, 4400, 580)
        self.ob243 = sprites(self.cube, 4400, 580)
        self.ob244 = sprites(self.cube, 4400, 580)
        self.ob245 = sprites(self.cube, 4400, 580)
        self.ob246 = sprites(self.cube, 4400, 580)
        self.ob247 = sprites(self.cube, 4400, 580)
        self.ob248 = sprites(self.cube, 4400, 580)
        self.ob249 = sprites(self.cube, 4400, 580)
        self.ob250 = sprites(self.cube, 4400, 580)
        self.ob251 = sprites(self.cube, 4400, 580)
        self.ob252 = sprites(self.cube, 4400, 580)
        self.ob253 = sprites(self.cube, 4400, 580)
        self.ob254 = sprites(self.cube, 4400, 580)
        self.ob255 = sprites(self.cube, 4400, 580)
        self.ob256 = sprites(self.cube, 4400, 580)
        self.ob257 = sprites(self.cube, 4400, 580)
        self.ob258 = sprites(self.cube, 4400, 580)
        self.ob259 = sprites(self.cube, 4400, 580)
        self.ob260 = sprites(self.cube, 4400, 580)
        self.ob261 = sprites(self.cube, 4400, 580)
        self.ob262 = sprites(self.cube, 4400, 580)
        self.ob263 = sprites(self.cube, 4400, 580)
        self.ob264 = sprites(self.cube, 4400, 580)
        self.ob265 = sprites(self.cube, 4400, 580)
        self.ob266 = sprites(self.cube, 4400, 580)
        self.ob267 = sprites(self.cube, 4400, 580)
        self.ob268 = sprites(self.cube, 4400, 580)
        self.ob269 = sprites(self.cube, 4400, 580)
        self.ob270 = sprites(self.cube, 4400, 580)
        self.ob271 = sprites(self.cube, 4400, 580)
        self.ob272 = sprites(self.cube, 4400, 580)
        self.ob273 = sprites(self.cube, 4400, 580)
        self.ob274 = sprites(self.cube, 4400, 580)
        self.ob275 = sprites(self.cube, 4400, 580)
        self.ob276 = sprites(self.cube, 4400, 580)
        self.ob277 = sprites(self.cube, 4400, 580)
        self.ob278 = sprites(self.cube, 4400, 580)
        self.ob279 = sprites(self.cube, 4400, 580)
        self.ob280 = sprites(self.cube, 4400, 580)
        self.ob281 = sprites(self.cube, 4400, 580)
        self.ob282 = sprites(self.cube, 4400, 580)
        self.ob283 = sprites(self.cube, 4400, 580)
        self.ob284 = sprites(self.cube, 4400, 580)
        self.ob285 = sprites(self.cube, 4400, 580)
        self.ob286 = sprites(self.cube, 4400, 580)
        self.ob287 = sprites(self.cube, 4400, 580)
        self.ob288 = sprites(self.cube, 4400, 580)
        self.ob289 = sprites(self.cube, 4400, 580)
        self.ob290 = sprites(self.cube, 4400, 580)
        self.ob291 = sprites(self.cube, 4400, 580)
        self.ob292 = sprites(self.cube, 4400, 580)
        self.ob293 = sprites(self.cube, 4400, 580)
        self.ob294 = sprites(self.cube, 4400, 580)
        self.ob295 = sprites(self.cube, 4400, 580)
        self.ob296 = sprites(self.cube, 4400, 580)
        self.ob297 = sprites(self.cube, 4400, 580)
        self.ob298 = sprites(self.cube, 4400, 580)
        self.ob299 = sprites(self.cube, 4400, 580)
        self.ob300 = sprites(self.cube, 4400, 580)
        self.ob301 = sprites(self.cube, 4400, 580)
        self.ob302 = sprites(self.cube, 4400, 580)
        self.ob303 = sprites(self.cube, 4400, 580)
        self.ob304 = sprites(self.cube, 4400, 580)
        self.ob305 = sprites(self.cube, 4400, 580)
        self.ob306 = sprites(self.cube, 4400, 580)
        self.ob307 = sprites(self.cube, 4400, 580)
        self.ob308 = sprites(self.cube, 4400, 580)
        self.ob309 = sprites(self.cube, 4400, 580)
        self.ob310 = sprites(self.cube, 4400, 580)
        self.ob311 = sprites(self.cube, 4400, 580)
        self.ob312 = sprites(self.cube, 4400, 580)
        self.ob313 = sprites(self.cube, 4400, 580)
        self.ob314 = sprites(self.cube, 4400, 580)
        self.ob315 = sprites(self.cube, 4400, 580)
        self.ob316 = sprites(self.cube, 4400, 580)
        self.ob317 = sprites(self.cube, 4400, 580)
        self.ob318 = sprites(self.cube, 4400, 580)
        self.ob319 = sprites(self.cube, 4400, 580)
        self.ob320 = sprites(self.cube, 4400, 580)
        self.ob321 = sprites(self.cube, 4400, 580)
        self.ob322 = sprites(self.cube, 4400, 580)
        self.ob323 = sprites(self.cube, 4400, 580)
        self.ob324 = sprites(self.cube, 4400, 580)
        self.ob325 = sprites(self.cube, 4400, 580)
        self.ob326 = sprites(self.cube, 4400, 580)
        self.ob327 = sprites(self.cube, 4400, 580)
        self.ob328 = sprites(self.cube, 4400, 580)
        self.ob329 = sprites(self.cube, 4400, 580)
        self.ob330 = sprites(self.cube, 4400, 580)
        self.ob331 = sprites(self.cube, 4400, 580)
        self.ob332 = sprites(self.cube, 4400, 580)
        self.ob333 = sprites(self.cube, 4400, 580)
        self.ob334 = sprites(self.cube, 4400, 580)
        self.ob335 = sprites(self.cube, 4400, 580)
        self.ob336 = sprites(self.cube, 4400, 580)
        self.ob337 = sprites(self.cube, 4400, 580)
        self.ob338 = sprites(self.cube, 4400, 580)
        self.ob339 = sprites(self.cube, 4400, 580)
        self.ob340 = sprites(self.cube, 4400, 580)
        self.ob341 = sprites(self.cube, 4400, 580)
        self.ob342 = sprites(self.cube, 4400, 580)
        self.ob343 = sprites(self.cube, 4400, 580)
        self.ob344 = sprites(self.cube, 4400, 580)
        self.ob345 = sprites(self.cube, 4400, 580)
        self.ob346 = sprites(self.cube, 4400, 580)
        self.ob347 = sprites(self.cube, 4400, 580)
        self.ob348 = sprites(self.cube, 4400, 580)
        self.ob349 = sprites(self.cube, 4400, 580)


        pygame.display.set_caption("lets play!")
        self.theSong=ourMusic("christmas.ogg")
        self.theSong.musicUpload()
        self.theSong.musicPlay()
        self.gameExit = False
        self.clock = pygame.time.Clock()



        self.spritesGroup=pygame.sprite.Group()
        self.spritesGroup.add(self.ob, self.ob1, self.ob2, self.ob3, self.ob4, self.ob5, self.ob6, self.ob7, self.ob8, self.ob9, self.ob10,
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
                        self.ob151, self.ob152, self.ob153, self.ob154, self.ob155, self.ob156, self.ob157, self.ob158, self.ob159, self.ob160,
                        self.ob161, self.ob162, self.ob163, self.ob164, self.ob165, self.ob166, self.ob167, self.ob168, self.ob169, self.ob170,
                        self.ob171, self.ob172, self.ob173, self.ob174, self.ob175, self.ob176, self.ob177, self.ob178, self.ob179, self.ob180,
                        self.ob181, self.ob182, self.ob183, self.ob184, self.ob185, self.ob186, self.ob187, self.ob188, self.ob189, self.ob190,
                        self.ob191, self.ob192, self.ob193, self.ob194, self.ob195, self.ob196, self.ob197, self.ob198, self.ob199, self.ob200,
                        self.ob201, self.ob202, self.ob203, self.ob204, self.ob205, self.ob206, self.ob207, self.ob208, self.ob209, self.ob210,
                        self.ob211, self.ob212, self.ob213, self.ob214, self.ob215, self.ob216, self.ob217, self.ob218, self.ob219, self.ob220,
                        self.ob221, self.ob222, self.ob223, self.ob224, self.ob225, self.ob226, self.ob227, self.ob228, self.ob229, self.ob230,
                        self.ob231, self.ob232, self.ob233, self.ob234, self.ob235, self.ob236, self.ob237, self.ob238, self.ob239, self.ob240,
                        self.ob241, self.ob242, self.ob243, self.ob244, self.ob245, self.ob246, self.ob247, self.ob248, self.ob249, self.ob250,
                        self.ob251, self.ob252, self.ob253, self.ob254)
        self.spritesGroup1=pygame.sprite.Group()
        self.spritesGroup1.add(self.ob255, self.ob256, self.ob257, self.ob258, self.ob259, self.ob260, self.ob261, self.ob262, self.ob263, self.ob264,
                        self.ob265, self.ob266, self.ob267, self.ob268, self.ob269, self.ob270, self.ob271, self.ob272, self.ob273, self.ob274,
                        self.ob275, self.ob276, self.ob277, self.ob278, self.ob279, self.ob280, self.ob281, self.ob282, self.ob283, self.ob284,
                        self.ob285, self.ob286, self.ob287, self.ob288, self.ob289, self.ob290, self.ob291, self.ob292, self.ob293, self.ob294,
                        self.ob295, self.ob296, self.ob297, self.ob298, self.ob299, self.ob300, self.ob301, self.ob302, self.ob303, self.ob304,
                        self.ob305, self.ob306, self.ob307, self.ob308, self.ob309, self.ob310, self.ob311, self.ob312, self.ob313, self.ob314,
                        self.ob315, self.ob316, self.ob317, self.ob318, self.ob319, self.ob320, self.ob321, self.ob322, self.ob323, self.ob324,
                        self.ob325, self.ob326, self.ob327, self.ob328, self.ob329, self.ob330, self.ob331, self.ob332, self.ob333, self.ob334,
                        self.ob335, self.ob336, self.ob337, self.ob338, self.ob339, self.ob340, self.ob341, self.ob342, self.ob343, self.ob344,
                        self.ob345, self.ob346, self.ob347, self.ob348, self.ob349)

        self.score=0
        self.y=str(self.score)

        while not self.gameExit:
            self.clock.tick(40)
            self.timer = pygame.time.get_ticks()
            print(self.timer)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.gameExit=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if not self.fall:
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
                            self.jump = True
                    if event.key == pygame.K_RETURN:
                        self.gameExit= True
            if self.jump:
                self.player.rect.y -= 65
                if self.player.rect.y <= 410:
                    ycoor = 500
                    self.jump = False
                    self.fall = True

            if self.fall:
                self.player.rect.y += 65
                if self.player.rect.y >= 544:
                    ycoor = 0
                    self.fall = False
            self.gameDisplay.blit(self.bg,[0,0])
            time.sleep(.05)
            self.player.pos()
            self.spritesGroup.draw(self.gameDisplay)
            self.spritesGroup1.draw(self.gameDisplay)
            self.ob.left(40)
            if(self.timer > 5800):
                self.ob1.left(40)
            if(self.timer > 10500):
                self.ob2.left(40)
            if(self.timer > 14300):
                self.ob3.left(40)
            if(self.timer > 18300):
                self.ob4.left(40)
            if(self.timer > 21400):
                self.ob5.left(40)
            if(self.timer > 22600):
                self.ob6.left(40)
            if(self.timer > 25200):
                self.ob7.left(40)
            if(self.timer > 26400):
                self.ob8.left(40)
            if(self.timer > 28800):
                self.ob9.left(40)
            if(self.timer > 33000):
                self.ob10.left(40)
            if(self.timer > 35600):
                self.ob11.left(40)
            if(self.timer > 44600):
                self.ob12.left(40)
            if(self.timer > 45000): #1
                self.ob13.left(40)
            if(self.timer > 45400): #2
                self.ob14.left(40)
            if(self.timer > 45800): #3
                self.ob15.left(40)
            if(self.timer > 46200): #4
                self.ob16.left(40)
            if(self.timer > 46600): #5
                self.ob17.left(40)
            if(self.timer > 47000): #6
                self.ob18.left(40)
            if(self.timer > 47400): #7
                self.ob19.left(40)
            if(self.timer > 47800): #8
                self.ob20.left(40)
            if(self.timer > 48200): #9
                self.ob21.left(40)
            if(self.timer > 48600): #10
                self.ob22.left(40)
            if(self.timer > 49000): #11
                self.ob23.left(40)
            if(self.timer > 49400): #12
                self.ob24.left(40)
            if(self.timer > 49800): #13
                self.ob25.left(40)
            if(self.timer > 50200):
                self.ob26.left(40)
            if(self.timer > 50600):
                self.ob27.left(40)
            if(self.timer > 51000):
                self.ob28.left(40)
            if(self.timer > 52000):
                self.ob29.left(40)
            if(self.timer > 52830):
                self.ob30.left(40)
            if(self.timer > 53660):
                self.ob31.left(40)
            if(self.timer > 54490):
                self.ob32.left(40)
            if(self.timer > 55320):
                self.ob33.left(40)
            if(self.timer > 56150):
                self.ob34.left(40)
            if(self.timer > 56980):
                self.ob35.left(40)
            if(self.timer > 57810):
                self.ob36.left(40)
            if(self.timer > 58640):
                self.ob37.left(40)
            if(self.timer > 59470):
                self.ob38.left(40)
            if(self.timer > 60300):
                self.ob39.left(40)
            if(self.timer > 61130):
                self.ob40.left(40)
            if(self.timer > 61960):
                self.ob41.left(40)
            if(self.timer > 62790):
                self.ob42.left(40)
            if(self.timer > 63620):
                self.ob43.left(40)
            if(self.timer > 64450):
                self.ob44.left(40)
            if(self.timer > 65280):
                self.ob45.left(40)
            if(self.timer > 66110):
                self.ob46.left(40)
            if(self.timer > 66940):
                self.ob47.left(40)
            if(self.timer > 67770):
                self.ob48.left(40)
            if(self.timer > 68600):
                self.ob49.left(40)
            if(self.timer > 69430):
                self.ob50.left(40)
            if(self.timer > 70260):
                self.ob51.left(40)
            if(self.timer > 71090):
                self.ob52.left(40)
            if(self.timer > 71920):
                self.ob53.left(40)
            if(self.timer > 72750):
                self.ob54.left(40)
            if(self.timer > 73580):
                self.ob55.left(40)
            if(self.timer > 74410):
                self.ob56.left(40)
            if(self.timer > 75240):
                self.ob57.left(40)
            if(self.timer > 76070):
                self.ob58.left(40)
            if(self.timer > 76900):
                self.ob59.left(40)
            if(self.timer > 77730):
                self.ob60.left(40)
            if(self.timer > 78560):
                self.ob61.left(40)
            if(self.timer > 79390):
                self.ob62.left(40)
            if(self.timer > 80220):
                self.ob63.left(40)
            if(self.timer > 81050):
                self.ob64.left(40)
            if(self.timer > 81880):
                self.ob65.left(40)
            if(self.timer > 82710):
                self.ob66.left(40)
            if(self.timer > 83540):
                self.ob67.left(40)
            if(self.timer > 84370):
                self.ob68.left(40)
            if(self.timer > 85200):
                self.ob69.left(40)
            if(self.timer > 86030):
                self.ob70.left(40)
            if(self.timer > 86860):
                self.ob71.left(40)
            if(self.timer > 87690):
                self.ob72.left(40)
            if(self.timer > 88520):
                self.ob73.left(40)
            if(self.timer > 89350):
                self.ob74.left(40)
            if(self.timer > 90180):
                self.ob75.left(40)
            if(self.timer > 91010):
                self.ob76.left(40)
            if(self.timer > 91840):
                self.ob77.left(40)
            if(self.timer > 92670):
                self.ob78.left(40)
            if(self.timer > 93500):
                self.ob79.left(40)
            if(self.timer > 94330):
                self.ob80.left(40)
            if(self.timer > 95160):
                self.ob81.left(40)
            if(self.timer > 95990):
                self.ob82.left(40)
            if(self.timer > 96820):
                self.ob83.left(40)
            if(self.timer > 97220):
                self.ob84.left(40)
            if(self.timer > 97620):
                self.ob85.left(40)
            if(self.timer > 98020):
                self.ob86.left(40)
            if(self.timer > 98420):
                self.ob87.left(40)
            if(self.timer > 98820):
                self.ob88.left(40)
            if(self.timer > 99220):
                self.ob89.left(40)
            if(self.timer > 99620):
                self.ob90.left(40)
            if(self.timer > 100020):
                self.ob91.left(40)
            if(self.timer > 100420):
                self.ob92.left(40)
            if(self.timer > 100820):
                self.ob93.left(40)
            if(self.timer > 101220):
                self.ob94.left(40)
            if(self.timer > 101620):
                self.ob95.left(40)
            if(self.timer > 102020):
                self.ob96.left(40)
            if(self.timer > 102420):
                self.ob97.left(40)
            if(self.timer > 102820):
                self.ob98.left(40)
            if(self.timer > 103220):
                self.ob99.left(40)
            if(self.timer > 103620):
                self.ob100.left(40)
            if(self.timer > 104020):
                self.ob101.left(40)
            if(self.timer > 104420):
                self.ob102.left(40)
            if(self.timer > 104820):
                self.ob103.left(40)
            if(self.timer > 105650):
                self.ob104.left(40)
            if(self.timer > 106480):
                self.ob105.left(40)
            if(self.timer > 107310):
                self.ob106.left(40)
            if(self.timer > 108140):
                self.ob107.left(40)
            if(self.timer > 108970):
                self.ob108.left(40)
            if(self.timer > 109800):
                self.ob109.left(40)
            if(self.timer > 110630):
                self.ob110.left(40)
            if(self.timer > 111460):
                self.ob111.left(40)
            if(self.timer > 112290):
                self.ob112.left(40)
            if(self.timer > 113120):
                self.ob113.left(40)
            if(self.timer > 113950):
                self.ob114.left(40)
            if(self.timer > 114780):
                self.ob115.left(40)
            if(self.timer > 115610):
                self.ob116.left(40)
            if(self.timer > 116440):
                self.ob117.left(40)
            if(self.timer > 117270):
                self.ob118.left(40)
            if(self.timer > 118100):
                self.ob119.left(40)
            if(self.timer > 118930):
                self.ob120.left(40)
            if(self.timer > 119760):
                self.ob121.left(40)
            if(self.timer > 120590):
                self.ob122.left(40)
            if(self.timer > 121420):
                self.ob123.left(40)
            if(self.timer > 122250):
                self.ob124.left(40)
            if(self.timer > 123080):
                self.ob125.left(40)
            if(self.timer > 123910):
                self.ob126.left(40)
            if(self.timer > 124740):
                self.ob127.left(40)
            if(self.timer > 125570):
                self.ob128.left(40)
            if(self.timer > 126400):
                self.ob129.left(40)
            if(self.timer > 127230):
                self.ob130.left(40)
            if(self.timer > 128060):
                self.ob131.left(40)
            if(self.timer > 128460):
                self.ob132.left(40)
            if(self.timer > 128860):
                self.ob133.left(40)
            if(self.timer > 129260):
                self.ob134.left(40)
            if(self.timer > 129660):
                self.ob135.left(40)
            if(self.timer > 130060):
                self.ob136.left(40)
            if(self.timer > 130460):
                self.ob137.left(40)
            if(self.timer > 130860):
                self.ob138.left(40)
            if(self.timer > 131260):
                self.ob139.left(40)
            if(self.timer > 131660):
                self.ob140.left(40)
            if(self.timer > 132060):
                self.ob141.left(40)
            if(self.timer > 132460):
                self.ob142.left(40)
            if(self.timer > 132860):
                self.ob143.left(40)
            if(self.timer > 133260):
                self.ob144.left(40)
            if(self.timer > 133660):
                self.ob145.left(40)
            if(self.timer > 134490):
                self.ob146.left(40)
            if(self.timer > 135320):
                self.ob147.left(40)
            if(self.timer > 136150):
                self.ob148.left(40)
            if(self.timer > 136980):
                self.ob149.left(40)
            if(self.timer > 137810):
                self.ob150.left(40)
            if(self.timer > 138640):
                self.ob151.left(40)
            if(self.timer > 139470):
                self.ob152.left(40)
            if(self.timer > 140300):
                self.ob153.left(40)
            if(self.timer > 141130):
                self.ob154.left(40)
            if(self.timer > 141960):
                self.ob155.left(40)
            if(self.timer > 142790):
                self.ob156.left(40)
            if(self.timer > 143620):
                self.ob157.left(40)
            if(self.timer > 144450):
                self.ob158.left(40)
            if(self.timer > 145280):
                self.ob159.left(40)
            if(self.timer > 145280):
                self.ob160.left(40)
            if(self.timer > 145280):
                self.ob161.left(40)
            if(self.timer > 145280):
                self.ob162.left(40)
            if(self.timer > 145280):
                self.ob163.left(40)
            if(self.timer > 145280):
                self.ob164.left(40)
            if(self.timer > 145280):
                self.ob165.left(40)
            if(self.timer > 145280):
                self.ob167.left(40)
            if(self.timer > 145280):
                self.ob168.left(40)
            if(self.timer > 145280):
                self.ob169.left(40)
            if(self.timer > 145280):
                self.ob170.left(40)
            if(self.timer > 145280):
                self.ob171.left(40)
            if(self.timer > 145280):
                self.ob172.left(40)
            if(self.timer > 145280):
                self.ob173.left(40)
            if(self.timer > 145280):
                self.ob174.left(40)
            if(self.timer > 145280):
                self.ob175.left(40)
            if(self.timer > 145280):
                self.ob176.left(40)
            if(self.timer > 145280):
                self.ob177.left(40)
            if(self.timer > 145280):
                self.ob178.left(40)
            if(self.timer > 145280):
                self.ob179.left(40)
            if(self.timer > 145280):
                self.ob180.left(40)
            if(self.timer > 145280):
                self.ob181.left(40)
            if(self.timer > 145280):
                self.ob182.left(40)
            if(self.timer > 145280):
                self.ob183.left(40)
            if(self.timer > 145280):
                self.ob184.left(40)
            if(self.timer > 145280):
                self.ob185.left(40)
            if(self.timer > 145280):
                self.ob186.left(40)
            if(self.timer > 145280):
                self.ob187.left(40)
            if(self.timer > 145280):
                self.ob188.left(40)
            if(self.timer > 145280):
                self.ob189.left(40)
            if(self.timer > 146110):
                self.ob190.left(40)
            if(self.timer > 146940):
                self.ob191.left(40)
            if(self.timer > 147770):
                self.ob192.left(40)
            if(self.timer > 148600):
                self.ob193.left(40)
            if(self.timer > 149430):
                self.ob194.left(40)
            if(self.timer > 150260):
                self.ob195.left(40)
            if(self.timer > 151090):
                self.ob196.left(40)
            if(self.timer > 151920):
                self.ob197.left(40)
            if(self.timer > 152320):
                self.ob198.left(40)
            if(self.timer > 152720):
                self.ob199.left(40)
            if(self.timer > 153120):
                self.ob200.left(40)
            if(self.timer > 153520):
                self.ob201.left(40)
            if(self.timer > 153920):
                self.ob202.left(40)
            if(self.timer > 154320):
                self.ob203.left(40)
            if(self.timer > 154720):
                self.ob204.left(40)
            if(self.timer > 155120):
                self.ob205.left(40)
            if(self.timer > 155520):
                self.ob206.left(40)
            if(self.timer > 155920):
                self.ob207.left(40)
            if(self.timer > 156320):
                self.ob208.left(40)
            if(self.timer > 156720):
                self.ob209.left(40)
            if(self.timer > 157120):
                self.ob210.left(40)
            if(self.timer > 157520):
                self.ob211.left(40)
            if(self.timer > 158350):
                self.ob212.left(40)
            if(self.timer > 159180):
                self.ob213.left(40)
            if(self.timer > 160010):
                self.ob214.left(40)
            if(self.timer > 160840):
                self.ob215.left(40)
            if(self.timer > 161670):
                self.ob216.left(40)
            if(self.timer > 162500):
                self.ob217.left(40)
            if(self.timer > 163330):
                self.ob218.left(40)
            if(self.timer > 164160):
                self.ob219.left(40)
            if(self.timer > 164990):
                self.ob220.left(40)
            if(self.timer > 165820):
                self.ob221.left(40)
            if(self.timer > 166650):
                self.ob222.left(40)
            if(self.timer > 167480):
                self.ob223.left(40)
            if(self.timer > 168310):
                self.ob224.left(40)
            if(self.timer > 169140):
                self.ob225.left(40)
            if(self.timer > 169970):
                self.ob226.left(40)
            if(self.timer > 170800):
                self.ob227.left(40)
            if(self.timer > 171200):
                self.ob228.left(40)
            if(self.timer > 171600):
                self.ob229.left(40)
            if(self.timer > 172000):
                self.ob230.left(40)
            if(self.timer > 172400):
                self.ob231.left(40)
            if(self.timer > 172800):
                self.ob232.left(40)
            if(self.timer > 173200):
                self.ob233.left(40)
            if(self.timer > 173600):
                self.ob234.left(40)
            if(self.timer > 174000):
                self.ob235.left(40)
            if(self.timer > 174400):
                self.ob236.left(40)
            if(self.timer > 174800):
                self.ob237.left(40)
            if(self.timer > 175200):
                self.ob238.left(40)
            if(self.timer > 175600):
                self.ob239.left(40)
            if(self.timer > 176000):
                self.ob240.left(40)
            if(self.timer > 176400):
                self.ob241.left(40)
            if(self.timer > 176800):
                self.ob242.left(40)
            if(self.timer > 177200):
                self.ob243.left(40)
            if(self.timer > 177600):
                self.ob244.left(40)
            if(self.timer > 178000):
                self.ob245.left(40)
            if(self.timer > 178400):
                self.ob246.left(40)
            if(self.timer > 178800):
                self.ob247.left(40)
            if(self.timer > 179200):
                self.ob248.left(40)
            if(self.timer > 179600):
                self.ob249.left(40)
            if(self.timer > 180000):
                self.ob250.left(40)
            if(self.timer > 180400):
                self.ob251.left(40)
            if(self.timer > 180800):
                self.ob252.left(40)
            if(self.timer > 181200):
                self.ob253.left(40)
            if(self.timer > 181600):
                self.ob254.left(40)
            if(self.timer > 182000):
                self.ob255.left(40)
            if(self.timer > 182400):
                self.ob256.left(40)
            if(self.timer > 182800):
                self.ob257.left(40)
            if(self.timer > 183200):
                self.ob258.left(40)
            if(self.timer > 183600):
                self.ob259.left(40)
            if(self.timer > 184000):
                self.ob260.left(40)
            if(self.timer > 184400):
                self.ob261.left(40)
            if(self.timer > 184800):
                self.ob262.left(40)
            if(self.timer > 185200):
                self.ob263.left(40)
            if(self.timer > 185600):
                self.ob264.left(40)
            if(self.timer > 186000):
                self.ob265.left(40)
            if(self.timer > 186400):
                self.ob266.left(40)
            if(self.timer > 186800):
                self.ob267.left(40)
            if(self.timer > 187200):
                self.ob268.left(40)
            if(self.timer > 187600):
                self.ob269.left(40)
            if(self.timer > 188000):
                self.ob270.left(40)
            if(self.timer > 188400):
                self.ob271.left(40)
            if(self.timer > 188800):
                self.ob272.left(40)
            if(self.timer > 189200):
                self.ob273.left(40)
            if(self.timer > 189600):
                self.ob274.left(40)
            if(self.timer > 190000):
                self.ob275.left(40)
            if(self.timer > 190400):
                self.ob276.left(40)
            if(self.timer > 190800):
                self.ob277.left(40)
            if(self.timer > 191200):
                self.ob278.left(40)
            if(self.timer > 191600):
                self.ob279.left(40)
            if(self.timer > 192000):
                self.ob280.left(40)
            if(self.timer > 192400):
                self.ob281.left(40)
            if(self.timer > 192800):
                self.ob282.left(40)
            if(self.timer > 193200):
                self.ob283.left(40)
            if(self.timer > 193600):
                self.ob284.left(40)
            if(self.timer > 194000):
                self.ob285.left(40)
            if(self.timer > 194400):
                self.ob286.left(40)
            if(self.timer > 194800):
                self.ob287.left(40)
            if(self.timer > 195200):
                self.ob288.left(40)
            if(self.timer > 195600):
                self.ob289.left(40)
            if(self.timer > 196000):
                self.ob290.left(40)
            if(self.timer > 196400):
                self.ob291.left(40)
            if(self.timer > 196800):
                self.ob292.left(40)
            if(self.timer > 197200):
                self.ob293.left(40)
            if(self.timer > 197600):
                self.ob294.left(40)
            if(self.timer > 198000):
                self.ob295.left(40)
            if(self.timer > 198400):
                self.ob296.left(40)
            if(self.timer > 198800):
                self.ob297.left(40)
            if(self.timer > 199200):
                self.ob298.left(40)
            if(self.timer > 199600):
                self.ob299.left(40)
            if(self.timer > 200000):
                self.ob300.left(40)
            if(self.timer > 200400):
                self.ob301.left(40)
            if(self.timer > 200800):
                self.ob302.left(40)
            if(self.timer > 201200):
                self.ob303.left(40)
            if(self.timer > 201600):
                self.ob304.left(40)
            if(self.timer > 202000):
                self.ob305.left(40)
            if(self.timer > 202400):
                self.ob306.left(40)
            if(self.timer > 202800):
                self.ob307.left(40)
            if(self.timer > 203200):
                self.ob308.left(40)
            if(self.timer > 203600):
                self.ob309.left(40)
            if(self.timer > 204000):
                self.ob310.left(40)
            if(self.timer > 204400):
                self.ob311.left(40)
            if(self.timer > 204800):
                self.ob312.left(40)
            if(self.timer > 205200):
                self.ob313.left(40)
            if(self.timer > 205600):
                self.ob314.left(40)
            if(self.timer > 206000):
                self.ob315.left(40)
            if(self.timer > 206400):
                self.ob316.left(40)
            if(self.timer > 206800):
                self.ob317.left(40)
            if(self.timer > 207200):
                self.ob318.left(40)
            if(self.timer > 207600):
                self.ob319.left(40)
            if(self.timer > 208000):
                self.ob320.left(40)
            if(self.timer > 208400):
                self.ob321.left(40)
            if(self.timer > 208800):
                self.ob322.left(40)
            if(self.timer > 209200):
                self.ob323.left(40)
            if(self.timer > 209600):
                self.ob324.left(40)
            if(self.timer > 210000):
                self.ob325.left(40)
            if(self.timer > 210400):
                self.ob326.left(40)
            if(self.timer > 210800):
                self.ob327.left(40)
            if(self.timer > 211200):
                self.ob328.left(40)
            if(self.timer > 211600):
                self.ob329.left(40)
            if(self.timer > 212000):
                self.ob330.left(40)
            if(self.timer > 212400):
                self.ob331.left(40)
            if(self.timer > 212800):
                self.ob332.left(40)
            if(self.timer > 213200):
                self.ob333.left(40)
            if(self.timer > 213600):
                self.ob334.left(40)
            if(self.timer > 214000):
                self.ob335.left(40)
            if(self.timer > 214400):
                self.ob336.left(40)
            if(self.timer > 214800):
                self.ob337.left(40)
            if(self.timer > 215200):
                self.ob338.left(40)
            if(self.timer > 215600):
                self.ob339.left(40)
            if(self.timer > 216000):
                self.ob340.left(40)
            if(self.timer > 216400):
                self.ob341.left(40)
            if(self.timer > 216800):
                self.ob342.left(40)
            if(self.timer > 217200):
                self.ob343.left(40)
            if(self.timer > 217600):
                self.ob344.left(40)
            if(self.timer > 218000):
                self.ob345.left(40)
            if(self.timer > 218400):
                self.ob346.left(40)
            if(self.timer > 218800):
                self.ob347.left(40)
            if(self.timer > 219200):
                self.ob348.left(40)
            if(self.timer > 219600):
                self.ob349.left(40)



            self.blocks_hit_list = pygame.sprite.spritecollide(self.pointo, self.spritesGroup, True)
            self.player_blocks_hit_list =  pygame.sprite.spritecollide(self.player, self.spritesGroup, True)
            self.blocks_hit_list1 = pygame.sprite.spritecollide(self.pointo, self.spritesGroup1, True)
            self.player_blocks_hit_list1 =  pygame.sprite.spritecollide(self.player, self.spritesGroup1, True)
            pygame.sprite.spritecollide(self.player, self.spritesGroup, True)
            if (self.blocks_hit_list != [] or self.blocks_hit_list1 != []):
                self.score+=10
                self.y=str(self.score)
            if (self.player_blocks_hit_list != [] or self.player_blocks_hit_list1 != []):
                self.score-=5
                self.y=str(self.score)
            self.score1=self.myfont.render(self.y, 1, (156,254,149))
            self.gameDisplay.blit(self.score1,(300, 50))
            self.label = self.myfont.render("YOUR CURRENT SCORE IS:", 1, (160,243,252))
            self.gameDisplay.blit(self.label, (300, 0))
            if (self.timer > 500) and (self.timer<4000):
                self.firstinstruct=self.myfonter.render("MARIAH CAREY - ALL I WANT FOR CHRISTMAS IS YOU ", 1, (156,254,149))
                self.gameDisplay.blit(self.firstinstruct, (50, 400))
            if (self.timer > 4100) and (self.timer<5100):
                self.firstinstruct=self.myfonter.render("READY!", 1, (156,254,149))
                self.gameDisplay.blit(self.firstinstruct, (50, 400))
            if (self.timer>5200 and self.timer<6200):
                self.firstinstruct=self.myfonter.render(" SET! ", 1, (156,254,149))
                self.gameDisplay.blit(self.firstinstruct, (50, 400))
            if (self.timer>6300 and self.timer<7300):
                self.firstinstruct=self.myfonter.render(" GO! ", 1, (156,254,149))
                self.gameDisplay.blit(self.firstinstruct, (50, 400))

            if int(self.y)>int(self.b):
                self.b=self.y
            if (self.timer>230000 and self.timer<240000):
                if self.b==self.y:
                    self.first=self.myfont.render("NEW HIGH SCORE!", 1, (156,254,149))
                    self.gameDisplay.blit(self.first, (50, 400))
                    self.scorefile=open("christmasscores.txt", "w")
                    self.b=str(self.b)
                    self.scorefile.write(self.b)
                    self.scorefile.close()
                else:
                    self.b=str(self.b)
                    self.highscores=("ALL TIME HIGH SCORE IS " + self.b)
                    self.first=self.myfont.render(self.highscores, 1, (156,254,149))
                    self.gameDisplay.blit(self.first, (50, 400))
                    self.scorefile=open("christmasscores.txt", "w")
                    self.scorefile.write(self.b)
                    self.scorefile.close()
            if (self.timer > 241000):
                    self.first=self.myfont.render("PRESS RETURN TO EXIT TO THE MAIN SCREEN", 1, (156,254,149))
                    self.gameDisplay.blit(self.first, (50, 400))

            pygame.display.update()

        pygame.quit()

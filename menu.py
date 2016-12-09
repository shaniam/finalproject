from direct.showbase.ShowBase import ShowBase
from panda3d.core import TextNode, PandaNode, NodePath, GeomNode, LineSegs
from direct.gui.OnscreenText import OnscreenText
from direct.actor.Actor import Actor
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
        self.collisionEvent('castle',-5,-80,10)
        self.collisionEvent('house',-70,-10,20)
        self.collisionEvent('tepee',-10,115, 10)
        self.collisionEvent('halloffame',55,-10,10)
        self.collisionEvent('fifthline',-200,180,320)
        self.collisionEvent('sixthline',120,-188,368)
        self.collisionEvent('seventhline',-200,-188,320)
        self.collisionEvent('eighthline',-200,-188,368)

        return task.cont

    def collisionEvent(self,name,startx,starty,iterations):
        """Triggers an event upon a collision"""
        xNames=["castle","tepee","fifthline","seventhline"]
        yNames=["house","halloffame","sixthline","eighthline"]
        levelNames=['castle','house','tepee','halloffame']
        outsideNames=['fifthline','sixthline','seventhline','eighthline']
        self.name=LineSegs(name)
        self.name.moveTo(startx,starty,0)
        x=startx
        y=starty
        for i in range(iterations):
            self.name.drawTo(x,y,0)
            if name in xNames:
                x+=1
            if name in yNames:
                y+=1
        self.name.create()
        vertexList=self.name.getVertices()

        coorList=[]

        for i in range(len(vertexList)):
            coorList.append([vertexList[i][0],vertexList[i][1]])


        mooreCoor= [int(self.moore.getX()),int(self.moore.getY())]

        if (mooreCoor in coorList):
            if name in levelNames:
                base.graphicsEngine.removeWindow(self.win)
                self.secondWindow(name)

            if name in outsideNames:
                self.moore.setPos(0,0,0)

    def secondWindow(self,name):
        #secondwindowcode, after level code based on level
        if name=='castle':
             #pygame code level one
            self.music.stop()
            with open("christmas.py") as f:
                code = compile(f.read(), "christmas.py", 'exec')
                exec(code) #pygame code level one

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
            print("") #pygame code level four

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
        self.environ = loader.loadModel("phase/trialworld.bam")
        self.environ.reparentTo(render)
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

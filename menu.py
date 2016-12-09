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
        #Loads the font
        font = self.loader.loadFont("phase/Chunkfive.ttf")
        #Sets start to none
        self.start= None
        #Displays text on a screen
        self.x = OnscreenText(text="Press Space to Start", style=1, fg=(1, 1, 1, 1), scale=.27, font=font, pos=(0,0), mayChange=True, align=TextNode.ACenter)
        self.acceptOnce("space", self.removeText)

    #moore
    def setKey(self, key, value):
        """Binds moving actions to keys"""
        self.keyMap[key] = value

    #moore
    def move(self, task):
        """Moves actor around and gets camera to follow"""


        dt = globalClock.getDt()

        # If a move-key is pressed, move moore in the specified direction.

        if self.keyMap["left"]:
            self.moore.setH(self.moore.getH() + 300 * dt)
        if self.keyMap["right"]:
            self.moore.setH(self.moore.getH() - 300 * dt)
        if self.keyMap["forward"]:
            self.moore.setY(self.moore, -25 * dt)

        # If moore is moving, loop the run animation.
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

        # If the camera is too far from moore, move it closer.
        # If the camera is too close to moore, move it farther.

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
        #print(coorlist)


        moorecoor= [int(self.moore.getX()),int(self.moore.getY())]
        #print(moorecoor)
        if (moorecoor in coorlist):
            if name in levelnames:
                base.graphicsEngine.removeWindow(self.win)
                self.secondWindow(name)

            if name in outsidenames:
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


        self.keyMap = {
            "left": 0, "right": 0, "forward": 0, "cam-left": 0, "cam-right": 0}
        #Loads actor and actions
        mooreStartPos = (0,0,0)
        self.moore = Actor("phase/ralph",
                           {"run": "phase/ralph-run",
                            "walk": "phase/ralph-walk"})
        self.moore.reparentTo(render)
        self.moore.setScale(.2)
        self.moore.setPos(mooreStartPos)
        #creates a "floating" above actor's head for camera to point at
        self.floater = NodePath(PandaNode("floater"))
        self.floater.reparentTo(self.moore)

        #Controls for moving actor around
        self.accept("arrow_left", self.setKey, ["left", True])
        self.accept("arrow_right", self.setKey, ["right", True])
        self.accept("arrow_up", self.setKey, ["forward", True])
        self.accept("arrow_left-up", self.setKey, ["left", False])
        self.accept("arrow_right-up", self.setKey, ["right", False])
        self.accept("arrow_up-up", self.setKey, ["forward", False])

        taskMgr.add(self.move, "moveTask")

        self.isMoving = False

        # Set up the camera
        self.disableMouse()
        self.camera.setPos(self.moore.getX(), self.moore.getY()+10, self.moore.getZ()+2)


        self.music = self.loader.loadMusic("phase/gunsforhands.ogg")
        self.music.play()
        self.accept("m-up", self.startMusic)
        # Add the Title
        self.title = self.addTitle("Moore's World: The Best World")
        # Post the instructions
        self.inst1 = self.addInstructions(0.06, "[ESC]: Quit")
        self.inst2 = self.addInstructions(0.12, "[Left Arrow]: Rotate Moore Left")
        self.inst3 = self.addInstructions(0.18, "[Right Arrow]: Rotate Moore Right")
        self.inst4 = self.addInstructions(0.24, "[Up Arrow]: Run Moore Forward")
        self.inst5 = self.addInstructions(0.30, "[M]: Enable/Disable Music")
        self.accept("escape", sys.exit)

    def removeText(self):
        """Deletes press space to start screen and loads new screen with world model"""
        self.newScreen()
        self.x.destroy()

    def addInstructions(self, pos, msg):
        """Posts instructions on screen"""
        return OnscreenText(text=msg, style=1, fg=(1, 1, 1, 1), scale=.05,
                            shadow=(0, 0, 0, 1), parent=base.a2dTopLeft,
                            pos=(0.08, -pos - 0.04), align=TextNode.ALeft)

    def addTitle(self, text):
        """Posts title on screen"""
        return OnscreenText(text=text, style=1, fg=(1, 1, 1, 1), scale=.07,
                            parent=base.a2dBottomRight, align=TextNode.ARight,
                            pos=(-0.1, 0.09), shadow=(0, 0, 0, 1))

def main():
    """Runs program"""
    demo = selfMenu()
    demo.run()

main()

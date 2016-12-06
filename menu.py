
from direct.showbase.ShowBase import ShowBase
from panda3d.core import TextNode, PandaNode, NodePath
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

    #RALPH
    def setKey(self, key, value):
        """Binds moving actions to keys"""
        self.keyMap[key] = value

    #RALPH
    def move(self, task):
        """Moves actor around and gets camera to follow"""


        dt = globalClock.getDt()

        # If a move-key is pressed, move ralph in the specified direction.

        if self.keyMap["left"]:
            self.ralph.setH(self.ralph.getH() + 300 * dt)
        if self.keyMap["right"]:
            self.ralph.setH(self.ralph.getH() - 300 * dt)
        if self.keyMap["forward"]:
            self.ralph.setY(self.ralph, -25 * dt)

        # If ralph is moving, loop the run animation.
        # If he is standing still, stop the animation.

        if self.keyMap["forward"] or self.keyMap["left"] or self.keyMap["right"]:
            if self.isMoving is False:
                self.ralph.loop("run")
                self.isMoving = True
        else:
            if self.isMoving:
                self.ralph.stop()
                self.ralph.pose("walk", 5)
                self.isMoving = False

        # If the camera is too far from ralph, move it closer.
        # If the camera is too close to ralph, move it farther.

        camvec = self.ralph.getPos() - self.camera.getPos()
        camdist = camvec.length()
        camvec.normalize()
        if camdist > 10.0:
            self.camera.setPos(self.camera.getPos() + camvec * (camdist - 10))
            camdist = 10.0
        if camdist < 5.0:
            self.camera.setPos(self.camera.getPos() - camvec * (5 - camdist))
            camdist = 5.0



        self.camera.lookAt(self.floater)

        return task.cont


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
        self.environ = loader.loadModel("phase/trialworld3.egg")
        self.environ.reparentTo(render)


        self.keyMap = {
            "left": 0, "right": 0, "forward": 0, "cam-left": 0, "cam-right": 0}
        #Loads actor and actions
        ralphStartPos = (0,0,.05)
        self.ralph = Actor("phase/ralph",
                           {"run": "phase/ralph-run",
                            "walk": "phase/ralph-walk"})
        self.ralph.reparentTo(render)
        self.ralph.setScale(.2)
        self.ralph.setPos(ralphStartPos)
        #creates a "floating" above actor's head for camera to point at
        self.floater = NodePath(PandaNode("floater"))
        self.floater.reparentTo(self.ralph)

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
        self.camera.setPos(self.ralph.getX()+100, self.ralph.getY()+200, self.ralph.getZ()+100)


        self.music = self.loader.loadMusic("phase/gunsforhands.ogg")
        self.music.play()
        self.accept("m-up", self.startMusic)
        # Add the Title
        self.title = self.addTitle("Title: The description will be here")
        # Post the instructions
        self.inst1 = self.addInstructions(0.06, "[ESC]: Quit")
        self.inst2 = self.addInstructions(0.12, "[Left Arrow]: Rotate Ralph Left")
        self.inst3 = self.addInstructions(0.18, "[Right Arrow]: Rotate Ralph Right")
        self.inst4 = self.addInstructions(0.24, "[Up Arrow]: Run self Forward")
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

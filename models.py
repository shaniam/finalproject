import pygame
import os
import time
#import panda3d
gameDisplay= pygame.display.set_mode((800, 600))

class ourMusic: #our music class
    """this is our music class, pass any song as your parameter"""
    def __init__(self, song):
        self.song=song #this is the song
    def musicUpload(self):
        """loads the song passed"""
        pygame.mixer.music.load(self.song)
    def musicPlay(self):
        """plays the song passed"""
        pygame.mixer.music.play(loops=-1, start=0.0) #assignes loops and plays music
class sprites(pygame.sprite.Sprite):
    """this is our sprites class, takes image and cooridnates as the parameters"""
    def __init__(self, image, xcoor, ycoor):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x=xcoor
        self.rect.y=ycoor
        self.rect.topleft = self.rect.x, self.rect.y
    def pos(self):
        """this displays the sprite an inititial position"""
        gameDisplay.blit(self.image, [self.rect.x, self.rect.y])
    def left(self, num):
        """moves the sprite a given distance"""
        dist = num
        self.rect.x = self.rect.x - dist

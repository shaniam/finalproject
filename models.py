import pygame
import os
import time
#import panda3d
gameDisplay= pygame.display.set_mode((800, 600))

class ourMusic: #our music class
    def __init__(self, song):
        self.song=song #sthis is the song
    def musicUpload(self):
        pygame.mixer.music.load(self.song)
    def musicPlay(self):
        pygame.mixer.music.play(loops=-1, start=0.0) #assignes loops and plays music
class sprites(pygame.sprite.Sprite):
    def __init__(self, image, xcoor, ycoor):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x=xcoor
        self.rect.y=ycoor
        self.rect.topleft = self.rect.x, self.rect.y
    def pos(self):
        gameDisplay.blit(self.image, [self.rect.x, self.rect.y])
    def left(self, num):
        dist = num
        self.rect.x = self.rect.x - dist

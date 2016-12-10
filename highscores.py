import pygame
class highscoreController:
    def __init__(self):
        pygame.init()
        self.gameExit=False
        self.gameDisplay= pygame.display.set_mode((800, 600))
        self.bg=pygame.image.load('scorebackground.jpg')

        self.m83scores=open("m83scores.txt", "r")
        self.m83scoresentence=self.m83scores.readline()
        self.m83score=self.m83scoresentence.strip()
        self.m83score=str(self.m83score)
        self.m83scores.close()

        self.myfont = pygame.font.SysFont("moon_flower.ttf", 40)
        self.gameDisplay.blit(self.bg,[0,0])
        self.hometownscores=open("hometownscores.txt", "r")
        self.hometownscoresentence=self.hometownscores.readline()
        self.hometownscore=self.hometownscoresentence.strip()
        self.hometownscore=str(self.hometownscore)
        self.hometownscores.close()

        self.xmasscores=open("christmasscores.txt", "r")
        self.xmasscoresentence=self.xmasscores.readline()
        self.xmasscore=self.xmasscoresentence.strip()
        self.xmasscore=str(self.xmasscore)
        self.xmasscores.close()

        self.myfont = pygame.font.SysFont("moon_flower.ttf", 40)
        self.gameDisplay.blit(self.bg,[0,0])
        while not self.gameExit:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.gameExit=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.gameExit= True
            self.gameDisplay.blit(self.bg,[0,0])
            self.m83scoreline=self.myfont.render(self.m83score, 1, (100, 123, 177))
            self.hometownscoreline=self.myfont.render(self.hometownscore, 1, (100, 123, 177))
            self.xmasscoreline=self.myfont.render(self.xmasscore, 1, (100, 123, 177))
            self.gameDisplay.blit(self.m83scoreline, (370,225))
            self.gameDisplay.blit(self.hometownscoreline, (365, 355))
            self.gameDisplay.blit(self.xmasscoreline, (365, 490))


            pygame.display.update()
        pygame.quit()
        quit()
def main():
    highscoreController()
main()

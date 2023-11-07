import pygame as pg
import random
from pygame.sprite import AbstractGroup

class Interactible(pg.sprite.Sprite):

    def __init__(self, width, height, position : pg.Vector2) -> None:
        super().__init__()

        self.image = pg.Surface([width,height])
        self.position = position
        self.rect = pg.Rect(position.x, position.y, width, height)

        self.isActive = False
        self.progress = 0
        self.currentKey = pg.K_0
        self.progressPerSuccess = 25


    def startInteraction(self):
        print("Début de l'interaction")
        self.isActive = True
        self.currentKey = self.choseRandomKey()
        self.showKey(self.currentKey)
    
    def stopInteraction(self):
        print("Fin de l'interaction")
        self.isActive = False

    def update(self):
        if(not self.isActive):
            return
        if(self.progress > 100):#TaskManager.currentTask.size
            print("End of interaction")
            self.isActive = False
    

        if pg.key.get_pressed()[self.currentKey]:
            self.currentKey = self.choseRandomKey()
            self.showKey(self.currentKey)
            self.progress += self.progressPerSuccess


    def choseRandomKey(self) -> int:
        return random.choice([pg.K_a, pg.K_b, pg.K_c, pg.K_d])

    def showKey(self, keyValue):
        print("Appuyez sur : ", pg.key.name(keyValue))





if __name__ == "__main__":
    pg.init
    pg.font.init()
    pg.display.set_caption("survie")
    screen = pg.display.set_mode((1920,1080))
    clock = pg.time.Clock()
    dt = 0

    pc = Interactible(width=1, height=1, position=pg.Vector2(0, 0))
    pc.startInteraction()
    while(True):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

        pc.update()
        dt = clock.tick(60)
        pg.display.flip()

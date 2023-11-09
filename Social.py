import pygame as pg
import random
import Parameters

class Social(pg.sprite.Sprite):
    def __init__(self, gameManager, width, height, position : pg.Vector2, parameters:Parameters.Parameters) -> None:
        super().__init__()

        self.gameManager = gameManager
        self.social = self.gameManager.socialBar

        self.image = pg.Surface([width,height])
        self.position = position
        self.rect = pg.Rect(position.x, position.y, width, height)

        self.isActive = False
        self.pos = [0.0]
        self.zoneLength = parameters.parameters["socialZoneLength"]
        self.speed = parameters.parameters["socialSpeed"]
        self.progress = parameters.parameters["socialBarProgressPerSuccess"]
        self.timeBeforeNextBar = random.uniform(3000 * self.speed, 50000 * self.speed)
        self.timeAfterError = parameters.parameters["socialTimeAfterError"]
        self.timeBeforeNextTry = 0
    
    def startInteraction(self):
        print("Début de l'interaction")
        self.isActive = True
    
    def stopInteraction(self):
        print("Fin de l'interaction")
        self.isActive = False
    
    def update(self, dt):
        if not self.isActive:
            return
        if self.timeBeforeNextTry > 0:
            self.timeBeforeNextTry -= dt
            return
        
        if self.isActive:
            for item in self.pos:
                pg.draw.rect(screen, ("green"), (500, item, 100, 15))
        
        self.timeBeforeNextBar -= dt
        if self.timeBeforeNextBar <= 0:
            self.pos.append(0.0)
            self.timeBeforeNextBar = random.uniform(3000 * self.speed, 50000 * self.speed)

        for i in range(0, len(self.pos)):
            if i < len(self.pos):
                self.pos[i] += self.speed * dt
                if self.pos[i] > 100:
                    self.pos.pop(i)

        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            for i in range(0, len(self.pos)):
                if i < len(self.pos):
                    if 85 - self.zoneLength/2 < self.pos[i] < 85 + self.zoneLength/2:
                        self.pos.pop(i)
                        self.social.addProgress(self.progress)
                    else:
                        self.timeBeforeNextTry = self.timeAfterError
                
        print(self.pos)





if __name__ == "__main__":
    import GameManager

    pg.init
    pg.font.init()
    pg.display.set_caption("survie")
    screen = pg.display.set_mode((1920,1080))
    clock = pg.time.Clock()
    dt = 0

    social = Social(gameManager=GameManager.GameManager(screen), width=1, height=1, position=pg.Vector2(0, 0))
    social.startInteraction()
    while(social.isActive):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

        
        dt = clock.tick(60)
        social.update(dt)
        pg.display.flip()


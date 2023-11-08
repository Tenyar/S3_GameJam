import pygame as pg
import Parameters

class Lit(pg.sprite.Sprite):
    def __init__(self, gameManager, width, height, position : pg.Vector2, parameters:Parameters.Parameters) -> None:
        super().__init__()

        self.gameManager = gameManager
        self.sleep = self.gameManager.sleepBar

        self.image = pg.Surface([width,height])
        self.position = position
        self.rect = pg.Rect(position.x, position.y, width, height)

        self.isActive = False
        self.pos = 0
        self.speed = 0.1
        self.speedDifference = 3
        self.progress = 0.02
        self.zonePos = 50
        self.zoneLength = 10

    def startInteraction(self):
        print("Début de l'interaction")
        self.isActive = True
    
    def stopInteraction(self):
        print("Fin de l'interaction")
        self.isActive = False
        self.pos=0
    
    def update(self, dt):
        if not self.isActive:
            return

        self.pos -= self.speed * dt
        if(self.pos < 0):
            self.pos = 0
        elif(self.pos > 100):
            self.pos = 100

        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            self.pos += self.speed * self.speedDifference * dt
            if self.zonePos - self.zoneLength/2 < self.pos < self.zonePos + self.zoneLength/2:
                self.sleep.addProgress(self.progress*dt)
        print(self.pos)





if __name__ == "__main__":
    import GameManager

    pg.init
    pg.font.init()
    pg.display.set_caption("survie")
    screen = pg.display.set_mode((1920,1080))
    clock = pg.time.Clock()
    dt = 0

    lit = Lit(gameManager=GameManager.GameManager(screen), width=1, height=1, position=pg.Vector2(0, 0))
    lit.startInteraction()
    while(lit.isActive):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

        
        dt = clock.tick(60)
        lit.update(dt)
        pg.display.flip()

import pygame as pg
import Parameters
import random

class Lit(pg.sprite.Sprite):
    def __init__(self, gameManager, width, height, position : pg.Vector2, screen, parameters:Parameters.Parameters) -> None:
        super().__init__()

        self.width = width
        self.height = height

        self.gameManager = gameManager
        self.sleep = self.gameManager.sleepBar
        
        self.screenUser = screen

        self.isActive = False
        self.pos = 0
        self.speed = 0.1
        self.speedDifference = 3
        self.progress = 0.02
        self.zonePos = 50 # En pourcentage %
        self.zoneLength = 10 # En pourcentage %

        # Creation des rectangles
        self.image = pg.Surface([width,height])
        self.position = position
        self.rect = pg.Rect(position.x, position.y, width, height)

    def startInteraction(self):
        # Rend aléatoire la position de la bar succès dans un intervale entre [50 et 80] avec un pas de 10 pixel
        self.zonePos = random.randrange(50, 80, 10)
        # Création du rectangle principale du jeu
        self.imageProgLen = 300 # Width de la bar principale du miniJeu
        self.imageProg = pg.Surface([self.imageProgLen,20])
        self.rectProg = pg.Rect(self.imageProgLen, self.position.y - 75, self.width, self.height)
        self.imageProg.fill("green")

        # Calcul de la longer de la bar success
        barWidth = (self.zoneLength / 100) * self.imageProgLen
        # Calcul de la position de la bar success
        barPos = ((self.zonePos / 100) * self.imageProgLen) - (barWidth/2)
        # Longueur de l'image selon la zone ou le joueur doit rester
        self.imageSuccess = pg.Surface([barWidth,20])
        # Position du rect de l'image rouge selon l'attribut barPos
        self.rectSuccess = pg.Rect(self.imageProgLen + barPos, self.position.y - 75, barWidth, self.height)
        self.imageSuccess.fill("red")

        print("Début de l'interaction")
        self.isActive = True
    
    def stopInteraction(self):
        print("Fin de l'interaction")
        self.isActive = False
        self.pos=0
    
    def update(self, dt):
        if self.isActive:
            # Création de la bar du joueur
            barPos = ((self.pos / 100) * self.imageProgLen)
            print(barPos)
            self.imagePlayer = pg.Surface([5,30])
            self.rectPlayer = pg.Rect(self.imageProgLen + barPos, self.position.y - 80, 5, 30) # Height - 5(offset pour démarquer la barPlayer de l'ensemble des bar du miniJeu)
            self.imagePlayer.fill("yellow")

            self.screenUser.blit(self.imageProg, self.rectProg)
            self.screenUser.blit(self.imageSuccess, self.rectSuccess)
            self.screenUser.blit(self.imagePlayer, self.rectPlayer)

        if not self.isActive:
            return

        self.pos -= self.speed * dt
        if(self.pos < 0):
            self.pos = 0

        keys = pg.key.get_pressed()
        # augmente le score
        if keys[pg.K_SPACE]:
            self.pos += self.speed * self.speedDifference * dt
            if(self.pos > 100):
                self.pos = 100
                
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

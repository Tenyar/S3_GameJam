import pygame as pg
import Parameters
import random

class Lit(pg.sprite.Sprite):
    def __init__(self, gameManager, width, height, position : pg.Vector2, parameters:Parameters.Parameters) -> None:
        super().__init__()

        self.width = width
        self.height = height

        self.gameManager = gameManager
        self.sleep = self.gameManager.sleepBar
        
        self.isActive = False
        self.pos = 0
        self.speed = parameters.parameters["litSpeed"]
        self.speedDifference = parameters.parameters["litSpeedDifference"]
        self.progress = parameters.parameters["litSleepBarProgressPerSuccess"]
        self.zonePos = 50
        self.zoneLength = parameters.parameters["litZoneLength"]
        self.position = position

        self.timeBeforeSound = 0 # init à 0 seconde

        self.imageProgLen = 300 # Width de la bar principale du miniJeu

        # Création du rectangle principale du jeu
        # Chargement de l'image
        self.imageJeuUI = pg.image.load("Art/Bed_Bar.png").convert()
        self.imageJeuUI.set_colorkey(0)
        self.imageJeuUI = self.imageJeuUI.convert_alpha()
        self.JeuUI = pg.transform.scale(self.imageJeuUI, ((self.imageJeuUI.get_width() * 5) + 5, self.imageJeuUI.get_height() * 5))
        self.rectJeu =  pg.Rect(self.imageProgLen -5, self.position.y - 80, self.width, self.height)
        
        # Creation des rectangles
        self.image = pg.Surface([width,height])
        self.rect = pg.Rect(position.x, position.y, width, height)

    def startInteraction(self):
        # Joue une musique marquant le début de la tâche
        self.gameManager.soundManager.playMusic("InBed", 1, 0, 1, 0)

        # Rend aléatoire la position de la bar succès dans un intervale entre [50 et 80] avec un pas de 10 pixel
        self.zonePos = random.randrange(30, 80, 10)

        # Calcul de la longer de la bar success
        barWidth = (self.zoneLength / 100) * self.imageProgLen
        # Calcul de la position de la bar success
        barPos = ((self.zonePos / 100) * self.imageProgLen) - (barWidth/2)
        # Longueur de l'image selon la zone ou le joueur doit rester
        self.imageSuccess = pg.Surface([barWidth,20])
        # Position du rect success selon l'attribut barPos
        self.rectSuccess = pg.Rect(self.imageProgLen + barPos, self.position.y - 75, barWidth, self.height)
        self.imageSuccess.fill((141,72,194))

        print("Début de l'interaction")
        self.isActive = True
    
    def stopInteraction(self):
        # Joue une musique marquant la fin de la tâche
        self.gameManager.soundManager.playMusic("OutBed", 1, 0, 1, 0)
        print("Fin de l'interaction")
        self.isActive = False
        self.pos=0
    
    def update(self, deltaTime):

        if self.isActive:
            # Création de la bar du joueur
            barPos = ((self.pos / 100) * self.imageProgLen)
            print(barPos)
            self.imagePlayer = pg.Surface([5,30])
            self.rectPlayer = pg.Rect(self.imageProgLen + barPos, self.position.y - 80, 5, 30) # Height - 5(offset pour démarquer la barPlayer de l'ensemble des bar du miniJeu)
            self.imagePlayer.fill("white")

            self.gameManager.screen.blit(self.JeuUI, self.rectJeu)
            self.gameManager.screen.blit(self.imageSuccess, self.rectSuccess)
            self.gameManager.screen.blit(self.imagePlayer, self.rectPlayer)

        # Cooldown
        if self.timeBeforeSound > 0:
            if (self.timeBeforeSound - deltaTime) < 0:
                self.timeBeforeSound = 0
            else:
                self.timeBeforeSound -= deltaTime

        if not self.isActive:
            return

        self.pos -= self.speed * deltaTime
        if(self.pos < 0):
            self.pos = 0

        keys = pg.key.get_pressed()
        # augmente le score
        if keys[pg.K_SPACE]:
            self.pos += self.speed * self.speedDifference * deltaTime
            if(self.pos > 100):
                self.pos = 100

        if self.zonePos - self.zoneLength/2 < self.pos < self.zonePos + self.zoneLength/2:
            # Ajout d'un montant de sommeil à la barre de progression 'sleep'
            self.sleep.addProgress(self.progress * deltaTime * 0.01) #0.01 -> convertion en seconde de delta time pour cohérence si on demande en paramètre on peut donner une échelle de temps en seconde et non en milliseconde qui est plus dur à comprendre pour l'utilisateur
            if self.sleep.getProg() == 100 and self.timeBeforeSound == 0:
                self.gameManager.soundManager.playMusic("ProgBarFull", 2, 0, 1, 0)
                self.timeBeforeSound = 2000 # 2 seconde

        print(self.pos)





if __name__ == "__main__":
    import GameManager

    pg.init
    pg.font.init()
    pg.display.set_caption("survie")
    screen = pg.display.set_mode((1920,1080))
    clock = pg.time.Clock()
    deltaTime = 0

    lit = Lit(gameManager=GameManager.GameManager(screen), width=1, height=1, position=pg.Vector2(0, 0))
    lit.startInteraction()
    while(lit.isActive):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

        
        deltaTime = clock.tick(60)
        lit.update(deltaTime)
        pg.display.flip()

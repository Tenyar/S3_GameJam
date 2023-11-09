import pygame as pg
import Parameters
import random
import SpriteSheet

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

        # Load l'image qu'une fois à la création (performance)
        self.imageProgLen = 200 # Width de la bar principale du miniJeu
        # Création du rectangle principale du jeu
        # Chargement de l'image
        self.imageJeuSurface = pg.image.load("Art/Bed_Bar.png").convert()
        self.imageJeuSurface.set_colorkey(0)
        self.imageJeuSurface = self.imageJeuSurface.convert_alpha()
        self.JeuUI = pg.transform.scale(self.imageJeuSurface, ((self.imageJeuSurface.get_width() * 5) + 5, self.imageJeuSurface.get_height() * 5))
        self.rectJeuUI =  pg.Rect(self.imageProgLen -5, self.position.y - 80, self.width, self.height)
        
        # Creation des rectangles
        self.spriteSheet = SpriteSheet.SpriteSheet("Art/Bed_Spritesheet_Corrected.png",1,4,53,37)
        self.image = self.spriteSheet.getSpriteAt(0, 0)
        self.rect = pg.Rect(position.x, position.y - 10, width, height)

        # vitesse de l'animation
        self.animationSpeed = 2
        #compteur de temps depuis le dernier changement de sprite
        self.animationTime = 0


    def startInteraction(self):
        # Joue une musique marquant le début de la tâche
        self.gameManager.soundManager.playMusic("InBed", 1, 0, 0.3, 0)

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

        #print("Début de l'interaction")
        self.isActive = True
    
    def stopInteraction(self):
        # Joue une musique marquant la fin de la tâche
        self.gameManager.soundManager.playMusic("OutBed", 1, 0, 0.3, 0)
        #print("Fin de l'interaction")
        self.isActive = False
        self.pos=0
    
    def update(self, deltaTime):

        pg.draw.lines(pg.display.get_surface(), (200, 55, 0), True,
                [self.rect.topleft, self.rect.topright, self.rect.bottomright, self.rect.bottomleft])


        if self.isActive:
            # Création de la bar du joueur
            barPos = ((self.pos / 100) * self.imageProgLen)
            print(barPos)
            self.imagePlayer = pg.Surface([5,30])
            self.rectPlayer = pg.Rect(self.imageProgLen + barPos, self.position.y - 80, 5, 30) # Height - 5(offset pour démarquer la barPlayer de l'ensemble des bar du miniJeu)
            self.imagePlayer.fill("white")

            self.gameManager.screen.blit(self.JeuUI, self.rectJeuUI)
            self.gameManager.screen.blit(self.imageSuccess, self.rectSuccess)
            self.gameManager.screen.blit(self.imagePlayer, self.rectPlayer)

            self.gameManager.setPlayerVisible(False)
        else:
            self.image = self.spriteSheet.getSpriteAt(0,0)
            self.image = pg.transform.scale(self.image,(53*5, 37*5))
            self.gameManager.setPlayerVisible(True)
            return

        # Cooldown
        if self.timeBeforeSound > 0:
            if (self.timeBeforeSound - deltaTime) < 0:
                self.timeBeforeSound = 0
            else:
                self.timeBeforeSound -= deltaTime

        self.pos -= self.speed * deltaTime
        if(self.pos < 0):
            self.pos = 0

        keys = pg.key.get_pressed()
        # Avance vers la droite
        if keys[pg.K_SPACE]:
            self.pos += self.speed * self.speedDifference * deltaTime
            if(self.pos > 100):
                self.pos = 100

        if self.zonePos - self.zoneLength/2 < self.pos < self.zonePos + self.zoneLength/2:
            # Play animation
            self.image = self.spriteSheet.getSpriteAt((int)(self.animationTime % 2.0) + 2, 0)
            self.image = pg.transform.scale(self.image,(53*5, 37*5))

            # Ajout d'un montant de sommeil à la barre de progression 'sleep'
            #0.001 -> convertion en seconde de delta time pour cohérence si on demande en paramètre on peut donner une échelle de temps en seconde et non en milliseconde qui est plus dur à comprendre pour l'utilisateur
            self.sleep.addProgress(self.progress * deltaTime * 0.001)
            if self.sleep.getProg() == 100 and self.timeBeforeSound == 0:
                self.gameManager.soundManager.playMusic("ProgBarFull", 2, 0, 1, 0)
                self.timeBeforeSound = 2000 # 2 seconde
        else:
            self.image = self.spriteSheet.getSpriteAt(1, 0)
            #(0, 720 - self.bedBase.get_height())
            self.image = pg.transform.scale(self.image,(53*5, 37*5))

        #print(self.pos)
        self.animationTime += deltaTime * 0.001 * self.animationSpeed






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

import pygame as pg
import random
import Parameters
import SpriteSheet

class Social(pg.sprite.Sprite):
    def __init__(self, gameManager, width, height, position : pg.Vector2, parameters:Parameters.Parameters) -> None:
        super().__init__()

        self.gameManager = gameManager
        self.social = self.gameManager.socialBar
        self.parameters = parameters.parameters
        # 52* 40
        self.spriteSheet = SpriteSheet.SpriteSheet("Art/Social_Spritesheet.png",7,2,52,40)
        self.image = self.spriteSheet.getSpriteAt(0,0)
        self.animationTime = 0
        self.animationSpeed = 1.5
        self.position = position
        self.rect = pg.Rect(position.x, position.y, width, height)

        self.isActive = False
        # self.pos = [0.0]
        self.pos = [[], [], []]
        self.zoneLength = self.parameters["socialZoneLength"]
        self.speed = self.parameters["socialSpeed"]
        self.progress = self.parameters["socialBarProgressPerSuccess"]
        self.timeBeforeNextBar = 0
        self.timeAfterError = self.parameters["socialTimeAfterError"]
        self.timeBeforeNextTry = 0

        # Interval de réussite pour le joueur
        self.IndexInterval = 95
        self.intervalBegin = self.IndexInterval - 10/2
        self.intervalEnd = self.IndexInterval + 10/2
        # Multiplicateur du parcours en pixels des bar
        self.intervalSuccess = (self.intervalEnd) - (self.intervalBegin)
        self.distAffichage = 2
        # Offset qui détermine la position du jeu dans la fenêtre
        self.barOffsetX = 830
        self.barOffsetY = 100
        # Size des barres défilantes
        self.barWidth = 100
        self.barHeigt = 5
        # 200 = offset de toutes les barres du miniJeu de l'axe Y; ((85*2)-10) = position de l'interval de réussite
        self.barSuccessOffsetY = self.barOffsetY + ((self.IndexInterval*2) -10) 
        # Load l'image qu'une fois à la création (performance)
        # Image (contour de la barre sociale)
        SocialeSurface = pg.image.load("Art/Social_Bar.png")
        # Si pixel noir / transaprent (compte comme noir), considérer cette valeur comme transaprent pour le convert_alpha()
        SocialeSurface.set_colorkey(0)
        # Si pixel tranparent, les converties à l'affichage
        #print("SUS", self.intervalSuccess)
        SocialeSurface = SocialeSurface.convert_alpha()
        self.SocialeUI = pg.transform.scale(SocialeSurface, (SocialeSurface.get_width()*5, SocialeSurface.get_height()*5 )) #+ self.intervalSuccess - 5
        #print("TAILLE DE L'IMGAE: ", SocialeSurface.get_height()*5)
        #print("TAILLE DE L'IMGAE:  AVEC l'interval couver : ", SocialeSurface.get_height()*5 + self.intervalSuccess)
        self.rectSocialeUI = SocialeSurface.get_rect(topleft=(self.barOffsetX, self.barSuccessOffsetY))
        #self.rectSocialeUI =  pg.Rect(self.barOffsetX, self.barSuccessOffsetY, SocialeSurface.get_width()*5, 10)

    
    def startInteraction(self):
        # Joue une musique marquant le début de la tâche
        self.gameManager.soundManager.playMusic("Social", 1, -1, 1, 1000)

        #print("Début de l'interaction")
        self.isActive = True
        self.pos = [[], [], []]
    
    def stopInteraction(self):
        self.gameManager.soundManager.fadeOutMusic(1, 1000)
        #print("Fin de l'interaction")
        self.isActive = False
    
    def update(self, dt):

        self.image = self.spriteSheet.getSpriteAt((int)(self.animationTime % self.spriteSheet.spritePerColumn),(int)(self.animationTime % self.spriteSheet.spritePerLine))
        self.animationTime += dt * 0.001 * self.animationSpeed
        self.image = pg.transform.scale(self.image,(52*5, 40*5))

        if not self.isActive:
            return

        # Dessin du background de la barre à succès
        #pg.draw.rect(self.gameManager.screen, ("gray"), (self.barOffsetX, self.barSuccessOffsetY, self.barWidth*3, self.intervalSuccess + 10))
        self.gameManager.screen.blit(self.SocialeUI, self.rectSocialeUI)
        
        # Boucle pour les 3 listes(Barres)
        for item in self.pos:
            # Pour toute les position des barres dans chaque liste sur l'axe Y
            for posY in item:
                if posY in self.pos[0]:
                    pg.draw.rect(self.gameManager.screen, ((82 + 70, 192 + 50, 38 + 80)), (self.barOffsetX, (posY * self.distAffichage) + self.barOffsetY, self.barWidth, self.barHeigt)) # posY = combien de pixel il parcours sur Y (chiffre croissant)
                elif posY in self.pos[1]:
                    pg.draw.rect(self.gameManager.screen, ((37 + 80, 187 + 40, 237 + 13)), (self.barOffsetX + 100, (posY * self.distAffichage) + self.barOffsetY, self.barWidth, self.barHeigt))
                elif posY in self.pos[2]:
                    pg.draw.rect(self.gameManager.screen, ((239 + 11, 187 + 50, 66 + 70)), (self.barOffsetX + 200, (posY * self.distAffichage) + self.barOffsetY, self.barWidth, self.barHeigt))
        if self.timeBeforeNextTry > 0:
            self.timeBeforeNextTry -= dt*0.001
            return
        
        self.timeBeforeNextBar -= dt*0.001
        if self.timeBeforeNextBar <= 0:
            # Rend aléatoire l'affectation d'une nouvelle bar dans une des 3 liste (position sur l'écran)
            self.pos[random.randrange(0, 3, 1)].append(0.0)
            self.timeBeforeNextBar = random.uniform(self.parameters["socialBarMinTime"], self.parameters["socialBarMaxTime"])

        # Parcours des listes dans pos
        for i in range(0, len(self.pos)):
            # Parcours des "barre" / "pos" dans une des liste
            for j in range(0, len(self.pos[i])):
                if j < len(self.pos[i]):
                    # Incrémente la position en pixel
                    self.pos[i][j] += self.speed * dt
                    if self.pos[i][j] > 100:
                        self.pos[i].pop(j)

        keys = pg.key.get_pressed()
        # Action spaceBar enfoncé
        # Si l'utilisateur n'a plus la touche spaceBar enfoncé et la retouche à nouveau
        if keys[pg.K_SPACE] and not keys[self.oldKey]:
            # variable si success pour au moins une barre
            success = False
            # Si l'utilisateur touche la spaceBar pour la première fois, on le sauvegarde pour empêcher le spam par frame
            self.oldKey = pg.K_SPACE
            # Parcours des listes
            for i in range(0, len(self.pos)):
                # Parcours de chaque bar pour chaque liste
                for j in range(0, len(self.pos[i])):
                    if j < len(self.pos[i]):
                        # Regarde si la position de la barre est dans l'interval de réussite
                        if  self.intervalBegin < self.pos[i][j] < self.intervalEnd:
                            self.pos[i].pop(j)
                            success = True
                            self.social.addProgress(self.progress)
                            # Si barre sociale à 100% après un succès jouer un autre son.
                            if self.social.getProg() == 100:
                                self.gameManager.soundManager.playMusic("ProgBarFull", 2, 0, 4, 0)
                            else:
                                self.gameManager.soundManager.playMusic("TaskDone", 2, 0, 0.5, 0)

            # Cooldown général si échec
            if not success:
                self.gameManager.soundManager.playMusic("Error", 2, 0, 0.8, 0)
                self.timeBeforeNextTry = self.timeAfterError
            # Si la spaceBar n'est plus enfoncé, reset la variable avec une touche par défaut
        elif not keys[pg.K_SPACE]:
            self.oldKey = pg.K_ESCAPE 
        #print(self.pos)

        self.animationTime += dt * 0.001 * self.animationSpeed
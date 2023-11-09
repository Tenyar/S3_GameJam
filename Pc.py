import pygame as pg
import random
import Parameters
import SpriteSheet

class Pc(pg.sprite.Sprite):

    def __init__(self, gameManager, width, height, position : pg.Vector2, parameters:Parameters.Parameters) -> None:
        super().__init__()
        self.gameManager = gameManager
        self.taskManager = self.gameManager.taskManager

        self.image = pg.Surface([width,height])
        self.position = position
        self.rect = pg.Rect(position.x, position.y, width, height)

        # Création de la spriteSheet
        self.spritesSheet = SpriteSheet.SpriteSheet("Art/Spritesheet_Keyboard.png", 2, 26, 16, 16)

        # Création du rectangle qui prendra les images des touches.
        self.rectKey = pg.Rect(position.x, position.y -50, 16*5, 16*5)

        # Liste des touches du clavier
        self.possibleKeys = [
            (pg.K_a, 0),
            #pg.K_b,
            #pg.K_c,
            (pg.K_d, 3),
            (pg.K_e, 4),
            #pg.K_f,
            #pg.K_g,
            #pg.K_h,
            #pg.K_i,
            #pg.K_j,
            #pg.K_k,
            #pg.K_l,
            #pg.K_m,
            #pg.K_n,
            #pg.K_o,
            #pg.K_p,
            (pg.K_q, 16),
            #(pg.K_r, 17),
            (pg.K_s, 18),
            #(pg.K_t, 19),
            #pg.K_u,
            #pg.K_v,
            #pg.K_w,
            #pg.K_x,
            #pg.K_y,
            (pg.K_z, 25)
        ]

        # Attributs conditionnel
        self.isActive = False
        self.currentKeyId = -1
        self.oldKeyId = -1
        self.progressPerSuccessMin = parameters.parameters["tasksProgressPerSuccessMin"]
        self.progressPerSuccessMax = parameters.parameters["tasksProgressPerSuccessMax"]
        self.timeAfterError = parameters.parameters["tasksTimeAfterError"]
        self.timeBeforeNextTry = 0


    def startInteraction(self):
        if self.gameManager.taskManager.getTaskAmount() == 0:
            return
        # Joue une musique marquant le début de la tâche
        self.gameManager.soundManager.playMusic("Pc", 1, 0, 1, 0)
        
        if len(self.taskManager.tasks) == 0:
            return
        #print("Début de l'interaction")
        self.isActive = True
        self.currentKeyId = self.choseRandomKey()
        # self.showKey(self.currentKey)
    
    def stopInteraction(self):
        #print("Fin de l'interaction")
        self.isActive = False
        
    def update(self, dt):

        if not self.isActive:
            return
        if len(self.taskManager.tasks) == 0:
            return
        
        if self.timeBeforeNextTry > 0:
            self.timeBeforeNextTry -= dt * 0.001 # Cooldown en action à chaque boucle
            self.drawKey(self.oldKeyId, 1)
            return
        
        self.drawKey(self.currentKeyId, 0)

        # Enlève un peu de % de sociabilité
        self.gameManager.socialBar.subProgress(3*dt*0.001)
        keys = pg.key.get_pressed()
        
        # Check si une autre touche que la touche précédente ou les flèches de déplacement est enfoncé.
        if keys.count(True) == 1 and (self.oldKeyId == -1 or not keys[self.possibleKeys[self.oldKeyId][0]]) \
            and not keys[pg.K_LEFT] and not keys[pg.K_RIGHT] and not keys[pg.K_UP] and not keys[pg.K_DOWN]:

            if keys[self.possibleKeys[self.currentKeyId][0]]:
                # Play a sound of success
                self.gameManager.soundManager.playMusic("TaskDone", 2, 0, 0.2, 0)
                # si le progrès de la tache est fini (100%)
                if self.taskManager.progressCurrentTask(random.randrange(int(self.progressPerSuccessMin), int(self.progressPerSuccessMax), 1)):
                    #print("End of interaction")
                    self.isActive = False
            else:
                # Play a sound of Error
                self.gameManager.soundManager.playMusic("Error", 2, 0, 0.5, 0)

                # Ajout de seconde de 'cooldown' si c'est un raté.
                self.timeBeforeNextTry = self.timeAfterError

            self.oldKeyId = self.currentKeyId
            self.currentKeyId = self.choseRandomKey()

        elif keys.count(True) == 0:
            self.oldKeyId = -1

    def choseRandomKey(self) -> int:
        return random.randint(0, len(self.possibleKeys) - 1)

    def drawKey(self, keyValue, columnId):
        # Récupère l'index(position) de la touche dans la liste (parcours implicite)
        # self.keyIndex = self.possibleKeys[self.currentKeyId][1]
        # Transformation pour mettre une touche de 16 pixel à 5 fois sa taille d'origine
        spriteOriginal = self.spritesSheet.getSpriteAt(self.possibleKeys[keyValue][1], columnId)
        spriteScaled = pg.transform.scale(spriteOriginal,(int(spriteOriginal.get_width() * 5), int(spriteOriginal.get_height() * 5)))
        # Affichage du rectangle créée pour les touches si tâche activé
        self.gameManager.screen.blit(spriteScaled, self.rectKey)



#    if __name__ == "__main__":
#        pg.init
#        pg.font.init()
#        pg.display.set_caption("survie")
#        screen = pg.display.set_mode((1920,1080))
#        clock = pg.time.Clock()
#        dt = 0
#
#        pc = Pc(width=1, height=1, position=pg.Vector2(0, 0))
#        pc.startInteraction()
#        while(True):
#            for event in pg.event.get():
#                if event.type == pg.QUIT:
#                    pg.quit()
#
#            pc.update()
#            dt = clock.tick(60)
#            pg.display.flip()

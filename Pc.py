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
        self.sprites = SpriteSheet.SpriteSheet("Art/Spritesheet_Keyboard.png", 2, 26, 16, 16)

        # Création du rectangle qui prendra les images des touches.
        self.rectKey = pg.Rect(position.x, position.y -50, 16*5, 16*5)

        # Liste des touches du clavier
        self.keyboard = [
            pg.K_a,
            pg.K_b,
            pg.K_c,
            pg.K_d,
            pg.K_e,
            pg.K_f,
            pg.K_g,
            pg.K_h,
            pg.K_i,
            pg.K_j,
            pg.K_k,
            pg.K_l,
            pg.K_m,
            pg.K_n,
            pg.K_o,
            pg.K_p,
            pg.K_q,
            pg.K_r,
            pg.K_s,
            pg.K_t,
            pg.K_u,
            pg.K_v,
            pg.K_w,
            pg.K_x,
            pg.K_y,
            pg.K_z
        ]

        # Attributs conditionnel
        self.isActive = False
        self.currentKey = pg.K_ESCAPE
        self.oldKey = pg.K_ESCAPE
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
        print("Début de l'interaction")
        self.isActive = True
        self.currentKey = self.choseRandomKey()
        self.showKey(self.currentKey)
    
    def stopInteraction(self):
        print("Fin de l'interaction")
        self.isActive = False
        
    def update(self, dt):

        if not self.isActive:
            return
        if len(self.taskManager.tasks) == 0:
            return
        if self.timeBeforeNextTry > 0:
            self.timeBeforeNextTry -= dt # Cooldown en action à chaque boucle
            # Transformation pour mettre une touche de 16 pixel à 5 fois sa taille d'origine
            spriteOriginal = self.sprites.getSpriteAt(self.keyboard.index(self.oldKey), 1)
            spriteScaled = pg.transform.scale(spriteOriginal,(int(spriteOriginal.get_width() * 5), int(spriteOriginal.get_height() * 5)))
            # Affichage de la touche raté
            self.gameManager.screen.blit(spriteScaled, self.rectKey)
            return
        
        if self.isActive:
            # Récupère l'index(position) de la touche dans la liste (parcours implicite)
            self.result = self.keyboard.index(self.currentKey)
            # Transformation pour mettre une touche de 16 pixel à 5 fois sa taille d'origine
            spriteOriginal = self.sprites.getSpriteAt(self.keyboard.index(self.currentKey), 0)
            spriteScaled = pg.transform.scale(spriteOriginal,(int(spriteOriginal.get_width() * 5), int(spriteOriginal.get_height() * 5)))
            # Affichage du rectangle créée pour les touches si tâche activé
            self.gameManager.screen.blit(spriteScaled, self.rectKey)

        # Enlève un peu de % de sociabilité
        self.gameManager.socialBar.subProgress(3*dt*0.001)
        self.showKey(self.currentKey)
        keys = pg.key.get_pressed()
        '''for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    keys = pg.key.get_pressed()
                    self.oldKey = event.key'''
        # Check si une touche autre que les flèches de déplacement sont enfoncé.
        if keys.count(True) == 1 and not keys[self.oldKey] and not keys[pg.K_LEFT] and not keys[pg.K_RIGHT] and not keys[pg.K_UP] and not keys[pg.K_DOWN]:
            if keys[self.currentKey]:
                # Play a sound of success

                self.gameManager.soundManager.playMusic("TaskDone", 2, 0, 0.5, 0)
                # si le progrès de la tache est fini (100%)
                if self.taskManager.progressCurrentTask(random.randrange(int(self.progressPerSuccessMin), int(self.progressPerSuccessMax), 1)):
                    print("End of interaction")
                    self.isActive = False
            else:
                # Play a sound of Error
                self.gameManager.soundManager.playMusic("Error", 2, 0, 0.5, 0)

                # Ajout de seconde de 'cooldown' si c'est un raté.
                self.timeBeforeNextTry = self.timeAfterError

            self.oldKey = self.currentKey
            self.currentKey = self.choseRandomKey()

        elif keys.count(True) == 0:
            self.oldKey = pg.K_ESCAPE

    def choseRandomKey(self) -> int:
        return random.choice([pg.K_a, pg.K_b, pg.K_c, pg.K_d, pg.K_e, pg.K_f, pg.K_g, pg.K_h, pg.K_i, pg.K_j, pg.K_k, pg.K_l, pg.K_m, pg.K_n, pg.K_o, pg.K_p, pg.K_q, pg.K_r, pg.K_s, pg.K_t, pg.K_u, pg.K_v, pg.K_w, pg.K_x, pg.K_y, pg.K_z])

    def showKey(self, keyValue):
        print("Appuyez sur : ", pg.key.name(keyValue))


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

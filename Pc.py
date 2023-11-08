import pygame as pg
import random

class Pc(pg.sprite.Sprite):

    def __init__(self, gameManager, width, height, position : pg.Vector2, screen) -> None:
        super().__init__()
        self.screenUser = screen
        self.gameManager = gameManager
        self.taskManager = self.gameManager.taskManager

        self.image = pg.Surface([width,height])
        self.position = position
        self.rect = pg.Rect(position.x, position.y, width, height)

        # Chargement de l'image
        self.imageKey = pg.image.load("Art/A.png").convert()
        # Création du rectangle qui prendra les images des touches.
        self.rectKey = pg.Rect(position.x, position.y -50, 69, 64)


        # Liste des touches du clavier (hashmap / dico)
        self.keyboard = {
            pg.K_a: 0,
            pg.K_b: 1,
            pg.K_c: 2,
            pg.K_d: 3,
            pg.K_e: 4,
            pg.K_f: 5,
            pg.K_g: 6,
            pg.K_h: 7,
            pg.K_i: 8,
            pg.K_j: 9,
            pg.K_k: 10,
            pg.K_l: 11,
            pg.K_m: 12,
            pg.K_n: 13,
            pg.K_o: 14,
            pg.K_p: 15,
            pg.K_q: 16,
            pg.K_r: 17,
            pg.K_s: 18,
            pg.K_t: 19,
            pg.K_u: 20,
            pg.K_v: 21,
            pg.K_w: 22,
            pg.K_x: 23,
            pg.K_y: 24,
            pg.K_z: 25
        }

        # Attributs conditionnel
        self.isActive = False
        self.currentKey = pg.K_ESCAPE
        self.oldKey = pg.K_ESCAPE
        self.progressPerSuccess = 20
        self.timeBeforeNextTry = 0


    def startInteraction(self):
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
        
        if self.isActive:
            # Affichage du rectangle créée pour les touches si tâche activé
            for clef in self.keyboard:
                if clef == self.currentKey:
                    print(self.keyboard[clef])
                    self.screenUser.blit(self.imageKey, self.rectKey)

        self.imageKey.blit(self.screenUser, (self.position.x, self.position.y -50 ))
        if not self.isActive:
            return
        if len(self.taskManager.tasks) == 0:
            return
        if self.timeBeforeNextTry > 0:
            self.timeBeforeNextTry -= dt
            return
        
        self.showKey(self.currentKey)
        keys = pg.key.get_pressed()
        '''for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    keys = pg.key.get_pressed()
                    self.oldKey = event.key'''
        if keys.count(True) == 1 and not keys[self.oldKey] and not keys[pg.K_LEFT] and not keys[pg.K_RIGHT] and not keys[pg.K_UP] and not keys[pg.K_DOWN]:
            if keys[self.currentKey]:
                if self.taskManager.progressCurrentTask(self.progressPerSuccess):
                    print("End of interaction")
                    self.isActive = False
            else:
                self.timeBeforeNextTry = 1000
            self.oldKey = self.currentKey
            self.currentKey = self.choseRandomKey()
        elif keys.count(True) == 0:
            self.oldKey = pg.K_ESCAPE

    def choseRandomKey(self) -> int:
        return random.choice([pg.K_a, pg.K_b, pg.K_c, pg.K_d, pg.K_e, pg.K_f, pg.K_g, pg.K_h, pg.K_i, pg.K_j, pg.K_k, pg.K_l, pg.K_m, pg.K_n, pg.K_o, pg.K_p, pg.K_q, pg.K_r, pg.K_s, pg.K_t, pg.K_u, pg.K_v, pg.K_w, pg.K_x, pg.K_y, pg.K_z])

    def showKey(self, keyValue):
        print("Appuyez sur : ", pg.key.name(keyValue))





if __name__ == "__main__":
    pg.init
    pg.font.init()
    pg.display.set_caption("survie")
    screen = pg.display.set_mode((1920,1080))
    clock = pg.time.Clock()
    dt = 0

    pc = Pc(width=1, height=1, position=pg.Vector2(0, 0))
    pc.startInteraction()
    while(True):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

        pc.update()
        dt = clock.tick(60)
        pg.display.flip()

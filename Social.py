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
        #self.pos = [0.0]
        self.pos = [[], [], []]
        self.zoneLength = parameters.parameters["socialZoneLength"]
        self.speed = parameters.parameters["socialSpeed"]
        self.progress = parameters.parameters["socialBarProgressPerSuccess"]
        self.timeBeforeNextBar = random.uniform(3000 * self.speed, 50000 * self.speed)
        self.timeAfterError = parameters.parameters["socialTimeAfterError"]
        self.timeBeforeNextTry = 0
    
    def startInteraction(self):
        print("Début de l'interaction")
        self.isActive = True
        self.pos = [[], [], []]
    
    def stopInteraction(self):
        print("Fin de l'interaction")
        self.isActive = False
    
    def update(self, dt):

        if not self.isActive:
            return
        intervalSuccess = (85 + self.zoneLength/2) - (85 - self.zoneLength/2)
        barHeight = 200 + ((85*2) -6) # 200 = offset de toutes les bar du miniJeu, 85 = distance maximal parcourue par les bar colorées
        pg.draw.rect(self.gameManager.screen, ("gray"), (800, barHeight, 300, intervalSuccess + 4))
        
        # Boucle pour les 3 listes
        for item in self.pos:
            # boucle pour les éléments dans les 3 listes
            for i in item:
                if i in self.pos[0]:
                    pg.draw.rect(self.gameManager.screen, ("green"), (800, i*2 + 200, 100, 5))
                elif i in self.pos[1]:
                    pg.draw.rect(self.gameManager.screen, ((255,255,100)), (800 + 100, i*2 + 200, 100, 5)) # i*2 = plus de parcours sur y à l'écran
                elif i in self.pos[2]:
                    pg.draw.rect(self.gameManager.screen, ("orange"), (800 + 200, i*2 + 200, 100, 5))
        if self.timeBeforeNextTry > 0:
            self.timeBeforeNextTry -= dt
            return
        
        self.timeBeforeNextBar -= dt
        if self.timeBeforeNextBar <= 0:
            # Rend aléatoire l'affectation d'une nouvelle bar dans une des 3 liste (position sur l'écran)
            self.pos[random.randrange(0, 3, 1)].append(0.0)
            self.timeBeforeNextBar = random.uniform(10000 * self.speed, 50000 * self.speed)

        # Parcours des listes dans pos
        for i in range(0, len(self.pos)):
            # Parcours des "barre" / "pos" dans une des liste
            for j in range(0, len(self.pos[i])):
                if j < len(self.pos[i]):
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
                        # Interval de succès
                        if 85 - self.zoneLength/2 < self.pos[i][j] < 85 + self.zoneLength/2:
                            self.gameManager.soundManager.playMusic("TaskDone")
                            self.pos[i].pop(j)
                            self.social.addProgress(self.progress)
                            success = True
            # Cooldown général si échec
            if not success:
                self.gameManager.soundManager.playMusic("Error")
                self.timeBeforeNextTry = self.timeAfterError
            # Si la spaceBar n'est plus enfoncé, reset la variable avec une touche par défaut
        elif not keys[pg.K_SPACE]:
            self.oldKey = pg.K_ESCAPE 
          
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


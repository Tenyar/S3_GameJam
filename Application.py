import pygame
import GameManager
import Parameters
import sys

## Patterne Singleton
class Application(object):
    # Variable static (de classe)
    instance = None

    # On créer une instance de la classe seulement si il n'y en à pas d'autres sinon on retourne celui déjà créée. 
    def __init__(self, screenWidth, screenHeight, parameters:Parameters.Parameters):
        if Application.instance != None:
            raise Exception("Une instace existe déjà !")
        else:
            # attributs du l'instance "application"
            Application.instance = self
            self.screenWidth = screenWidth
            self.screenHeight = screenHeight
            # Taille de l'écran
            self.screen = pygame.display.set_mode((screenWidth, screenHeight))
            # Nom de la fenêtre
            pygame.display.set_caption("JamingJamers")
            self.deltaTime = 0
            # Gère temps entre deux images
            self.clock = pygame.time.Clock()
            # Gère les paramètres
            self.parameters = parameters

    def startGame(self):
        gameManager = GameManager.GameManager(self.screen, self.parameters)

        while gameManager.isRunning():
            # On regarde si l'évenement "quitter la fenêtre" est déclenché.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #print("******** Position finale du player **********")
                    #print("X : ", player.pos_x)
                    #print("Y : ", player.pos_y)
                    pygame.quit()
                    sys.exit()

            # remplir la scène(fenêtre) à chaque fois qu'il change de position
            self.screen.fill((255,255,255))

            self.deltaTime = self.clock.tick(60)
            gameManager.update(self.deltaTime)
            pygame.display.update() # Update les données sur la fenêtre
            pygame.display.flip()

        

def main():

    # Initialisation de pygame
    pygame.init()
    
    # Initalisation du module de gestion des fonts
    pygame.font.init()

    # Création du singleton
    app = Application(1280, 720, Parameters.Parameters(sys.argv))

    # 2 méthodes pour mettre en FullScreen
    #pygame.display.toggle_fullscreen()
    #pygame.display.set_mode(flags=pygame.FULLSCREEN)

    app.startGame()

    # pygame.quit()
    # sys.exit()

main()
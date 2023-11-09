import pygame, GameManager, Parameters, sys

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

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
            # Temps en ms
            self.deltaTime = 0
            # Gère temps entre deux images
            self.clock = pygame.time.Clock()
            # Gère les paramètres
            self.parameters = parameters

    def startGame(self):
        gameManager = GameManager.GameManager(self.screen, self.parameters)
        pygame.display.set_caption("MainMenu")

        while gameManager.isRunning():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # 60 FPS
            self.deltaTime = self.clock.tick(60)
            gameManager.update(self.deltaTime)
            pygame.display.update() # Update les données sur la fenêtre
            pygame.display.flip() # Met les "dessins" stocké dans le buffer à l'écran


def draw_text(text, size, default_color, color_direction, color_speed, x, y, screen):
    font = pygame.font.Font("Font/Quinquefive-ALoRM.ttf", 15)
    text_surface = font.render(text, False, default_color)
    text_rect = text_surface.get_rect()
    # Met le centre du rectangle de text au centre de la fenêtre
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

    textColorChange(default_color, color_direction, color_speed, 0 ,255)


def textColorChange(default_color, direction, speed , valueMin , valueMax):
    for i in range(3): # RGB
        #print(default_color)
        default_color[i] += speed * direction[i]
        default_color[i] = max(valueMin, min(valueMax, default_color[i]))
        if default_color[i] >= valueMax or default_color[i] <= valueMin:
            direction[i] *= -1




def MainGame(app : Application):

    # 2 méthodes pour mettre en FullScreen
    #pygame.display.toggle_fullscreen()
    #pygame.display.set_mode(flags=pygame.FULLSCREEN)
    app.deltaTime = app.clock.tick(60)
    app.startGame()

    # pygame.quit()
    # sys.exit()

def mainMenu():
    
    # Initialisation de pygame
    pygame.init()
    # Initalisation du module de gestion des fonts
    pygame.font.init()

    # Nom de la fenêtre
    pygame.display.set_caption("MainMenu")

    # Création du singleton
    app = Application(WINDOW_WIDTH, WINDOW_HEIGHT, Parameters.Parameters(sys.argv))

    # variable de la font
    color_speed = 2
    color_direction = [1,1,1] # pas d'incrémentation
    default_color = [0,0,0] # couleur par défaut

    while True:
        for event in pygame.event.get():
            # On regarde si l'évenement "quitter la fenêtre" est déclenché.
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # On regarde si n'importe quel autre touche que Escape est enfoncé
            elif event.type == pygame.KEYDOWN and not event.key == pygame.K_ESCAPE:
                MainGame(app)

        # remplir la scène(fenêtre) à chaque fois qu'il change de position
        app.screen.fill((25,50,200)) # Background du menu
        

        # Affichage consigne pour lancer la partie
        draw_text("Appuyez sur n'importe quel bouton pour lancer une partie", 15, default_color, color_direction, color_speed, app.screenWidth / 2, app.screenHeight / 1.25, app.screen)
        # Update les données sur la fenêtre
        pygame.display.update() 
        # Met les "dessins" stocké dans le buffer à l'écran
        pygame.display.flip()

mainMenu()
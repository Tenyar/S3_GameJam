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

    def startGame(self, score : int, isScore : bool):
        gameManager = GameManager.GameManager(self.screen, self.parameters)
        pygame.display.set_caption("MainMenu")

        gameManager.soundManager.playMusic("Background", 0, -1, 0.35, 4000) # boucle infinie
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
        score = gameManager.taskManager.getCompteurPoints()
        isScore = True
        gameManager.deleteInstance()
        return score, isScore


def draw_text(text, size, default_color, color_direction, color_speed, x, y, screen):
    font = pygame.font.Font("Font/Quinquefive-ALoRM.ttf", size)
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
    score = 0
    isScore = False
    
    app.deltaTime = app.clock.tick(60)
    score, isScore = app.startGame(score, isScore)
    return score, isScore, 5000

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
    scoreFinal = 0
    isScore = False
    timeBeforeNextGame = 0

    # Chargement des images
    foregroundImage = pygame.image.load("Art/Menu_Foreground.png")
    foreground = pygame.transform.scale(foregroundImage, (256 * 5, 144 * 5))


    # variable de la font
    color_speed = 2
    color_direction = [1,1,1] # pas d'incrémentation
    default_color = [0,0,0] # couleur par défaut

    while True:
        app.deltaTime = app.clock.tick(60)
        timeBeforeNextGame -= app.deltaTime
        if timeBeforeNextGame <= 0:
            for event in pygame.event.get():
                # On regarde si l'évenement "quitter la fenêtre" est déclenché.
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                # On regarde si n'importe quel autre touche que Escape est enfoncé
                elif event.type == pygame.KEYDOWN and not event.key == pygame.K_ESCAPE and not event.key == pygame.K_LEFT and not event.key == pygame.K_RIGHT and not event.key == pygame.K_UP and not event.key == pygame.K_DOWN:
                        scoreFinal, isScore, timeBeforeNextGame = MainGame(app)

        # remplir la scène(fenêtre) à chaque fois qu'il change de position
        app.screen.blit(foreground, (0,0))

        font = pygame.font.Font("Font/Quinquefive-ALoRM.ttf", 9)
        line1 = font.render('La vie etudiante n’est pas facile, et l’INFO n’y fait pas exception.', True, (0,0,0))
        app.screen.blit(line1, (60, 130))
        line2 = font.render('DM, SAE, Revision, tout ca c’est sympa mais il faut aussi dormir, et parfois parler a des gens.', True, (0,0,0))
        app.screen.blit(line2, (60, 150))
        line3 = font.render('Dans ce jeu d’arcade les auteurs on voulu representer leur quotidien passionnant sous format video-ludique.', True, (0,0,0))
        app.screen.blit(line3, (60, 170))
        line4 = font.render('Combien de tache pourrez-vous faire avant de perdre votre sommeil ou vos amis…', True, (0,0,0))
        app.screen.blit(line4, (60, 190))
        line5 = font.render('           Mouvement du joueur      |      Travaux sur l’ordinateur      |      Autres mini-jeu', True, (0,0,0))
        app.screen.blit(line5, (60, 490))
        line5 = font.render('                                    |                                    |', True, (0,0,0))
        app.screen.blit(line5, (60, 500))
        line6 = font.render('         fleches directionnelles    |      touches A, Z, E, Q, S, D      |      barre d’espace', True, (0,0,0))
        app.screen.blit(line6, (60, 510))

        if isScore:
            # Nouvelle font pour score
            fontScore = pygame.font.Font("Font/Quinquefive-ALoRM.ttf", 15)
            line7 = fontScore.render('score de partie : ' + str(int(scoreFinal)), True, (0,0,0))
            app.screen.blit(line7, (app.screen.get_width() / 2 - line7.get_width() / 2, 570))

        fontCredit = pygame.font.Font("Font/Quinquefive-ALoRM.ttf", 5)
        credit1 = fontCredit.render("Fait avec PyGame dans le cadre d'une game jam", True, (150,150,150))
        app.screen.blit(credit1, (30, 645))
        credit1 = fontCredit.render("au sein de l'IUT2 Grenoble", True, (150,150,150))
        app.screen.blit(credit1, (30, 655))
        credit2 = fontCredit.render('Sons : onlinesound.net/8bit-sfx-generator et', True, (150,150,150))
        app.screen.blit(credit2, (30, 670))
        credit2 = fontCredit.render('       pixabay.com', True, (150,150,150))
        app.screen.blit(credit2, (30, 680))
        credit3 = fontCredit.render('Police : Quinque Five Font by GGBotNet', True, (150,150,150))
        app.screen.blit(credit3, (30, 695))

        # Affichage consigne pour lancer la partie
        draw_text("Appuyez sur n'importe quel bouton pour lancer une partie", 15, default_color, color_direction, color_speed, app.screenWidth / 2, app.screenHeight / 1.15, app.screen)
        # Affichage consigne pour quitter le menu
        draw_text("Appuyez sur echap pour quitter", 15, default_color, color_direction, color_speed, app.screenWidth / 2, app.screenHeight / 1.10, app.screen)
        # Update les données sur la fenêtre
        pygame.display.update() 
        # Met les "dessins" stocké dans le buffer à l'écran
        pygame.display.flip()

mainMenu()
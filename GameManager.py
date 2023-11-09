import pygame
import Player
import Pc
import Lit
import Social
import TaskManager
import ProgressBar
import Parameters

class GameManager():
    instance = None
    def __init__(self, screen : pygame.display, parameters:Parameters.Parameters) -> None:
# simulation d'un singleton : Si on essaye de créer une nouvelle instance de GameManager, une exception est levée        
        if GameManager.instance != None : 
            raise Exception("instance already exists")
        GameManager.instance = self
        
        self.parameters = parameters.parameters
        self.taskManager = TaskManager.TaskManager(parameters)

        self.screen = screen

        # Création du background et du foreground
        backgroundImage = pygame.image.load("Art/Background.png")
        self.background = pygame.transform.scale(backgroundImage, (256 * 5, 144 * 5))
        foregroundImage = pygame.image.load("Art/Foreground.png")
        self.foreground = pygame.transform.scale(foregroundImage, (1280, 720))
        treeImage = pygame.image.load("Art/Arbre.png")
        self.tree = pygame.transform.scale(treeImage, (55 * 5, 40 * 5))
        treeShadowImage = pygame.image.load("Art/Arbre_Ombre.png")
        self.treeShadow = pygame.transform.scale(treeShadowImage, (75 * 5, 60 * 5))
        self.treeShadow.set_alpha(100)
        bedBaseImage = pygame.image.load("Art/Lit_Base.png")
        self.bedBase = pygame.transform.scale(bedBaseImage, (84 * 5, 35 * 5))

        # Création d'un player
        self.player = Player.Player(50, 110, 300, 350, (255, 75, 25), parameters)
        # Group du joueur
        self.playerGroup = pygame.sprite.Group()
        self.playerGroup.add(self.player)

        # Données pour les progressBar
        self.social = 100
        self.sleep = 100

        # Création des barres de progressions
        self.socialBar = ProgressBar.ProgressBar("SocialBar", 300, 15, 100, pygame.Vector2(50,50), (255,25,50), True)
        self.sleepBar = ProgressBar.ProgressBar("SleepBar", 300, 15, 100, pygame.Vector2(50,25), (0,0,200), True)
        # Group des barres de progression
        self.barGroup = pygame.sprite.Group()
        self.barGroup.add(self.sleepBar)
        self.barGroup.add(self.socialBar)

        # On ajoute chaque objet dans un groupe
        self.interactibleGroup = pygame.sprite.Group()

        self.interactibleGroup.add(Pc.Pc(self, 180, 50, pygame.Vector2(440, 90), parameters))
        self.interactibleGroup.add(Lit.Lit(self, 290, 110, pygame.Vector2(150,555), parameters))
        self.interactibleGroup.add(Social.Social(self, 70, 70, pygame.Vector2(950, 200), parameters))

        #Création des collisions
        bedCollision = pygame.Rect(150, 585, 270, 110)
        socialCollision = pygame.Rect(950, 200, 50, 50)
        tablesCollision = pygame.Rect(0, 0, 650, 80)
        self.collisions = [bedCollision, socialCollision, tablesCollision]


    def isRunning(self):
        if self.sleepBar.getProg() <= 0 or self.socialBar.getProg() <= 0 or self.taskManager.isTaskTimeOut:
            #return False
            print ("fin du jeu")
        return True

    def update(self, deltaTime):
        #print(deltaTime)

        self.socialBar.subProgress(self.parameters["socialBarSpeed"] * deltaTime)
        self.sleepBar.subProgress(self.parameters["sleepBarSpeed"] * deltaTime)

        self.tryInteraction(self.player.rect)
        self.taskManager.update(deltaTime)

        self.screen.blit(self.background, (0,0))
        self.playerGroup.draw(self.screen)
        self.screen.blit(self.bedBase, (0, 720 - self.bedBase.get_height()))
        self.screen.blit(self.treeShadow, (1280 - self.treeShadow.get_width(), 720 - self.treeShadow.get_height()))
        self.screen.blit(self.tree, (1280 - self.tree.get_width(), 720 - self.tree.get_height()))
        self.screen.blit(self.foreground, (0,0))
        self.interactibleGroup.draw(self.screen)
        self.taskManager.draw(self.screen)
        self.barGroup.update(self.screen)

        self.player.update(deltaTime, self.collisions, pygame.Rect(150, 45, 980, 635))

        #Rect dedebugging
        #pygame.draw.rect(self.foreground, (100,0,0), pygame.Rect(150, 45, 980, 635))

        for item in self.interactibleGroup.sprites():
            item.update(deltaTime)
        
    def stopInteractions(self):
        for item in self.interactibleGroup.sprites():
            item.stopInteraction()

    def tryInteraction(self, position : pygame.Rect):
        for item in self.interactibleGroup.sprites(): # .values() qui accède via la clé à la valeur, l'objet en l'occurence
            if item.rect.colliderect(position):
                if not item.isActive:
                    #print("interaction avec ", item)
                    item.startInteraction()
            elif item.isActive:
                item.stopInteraction()

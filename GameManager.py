import pygame
import Player
import Pc
import Lit
import Social
import TaskManager
import ProgressBar
import Parameters
from pygame import mixer


class GameManager():
    instance = None
    def __init__(self, screen : pygame.display, parameters:Parameters.Parameters) -> None:
# simulation d'un singleton : Si on essaye de créer une nouvelle instance de GameManager, une exception est levée        
        if GameManager.instance != None : 
            raise Exception("instance already exists")
        GameManager.instance = self
        
        self.taskManager = TaskManager.TaskManager(5, 0.5, 5, 5, parameters)

        self.screen = screen

        # Instantie mixer
        mixer.init()

        # PlayList des musiques jouables en jeux
        self.playList = {
            "Transition": "Sound/Transition_Sound.wav",
            "Pc": "Sound/Pc_Sound.wav",
            "TaskDone": "Sound/TaskDone_Sound.wav",
            "Bed": "Sound/Bed_Sound.wav",
            "Social": "Sound/Social_Env_Sound.mp3",
            "Error": "Sound/Error_Sound.wav"
        }
        # Charge le(s) fichier(s) audio
        mixer.music.load("Sound/Transition_Sound.wav")
        # Met le volume du gestionnaire de musique
        mixer.music.set_volume(0.2)
        # Joue la musique 
        mixer.music.play()

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
        self.player = Player.Player(50, 110, 300, 500, (255, 75, 25), parameters)
        # Group du joueur
        self.playerGroup = pygame.sprite.Group()
        self.playerGroup.add(self.player)

        # Données pour les progressBar
        self.social = 100
        self.sleep = 100

        # Création des barres de progressions
        self.socialBar = ProgressBar.ProgressBar("SocialBar", 300, 15, pygame.Vector2(50,50), (255,25,50), True)
        self.sleepBar = ProgressBar.ProgressBar("SleepBar", 300, 15, pygame.Vector2(50,25), (0,0,200), True)
        # Group des barres de progression
        self.barGroup = pygame.sprite.Group()
        self.barGroup.add(self.sleepBar)
        self.barGroup.add(self.socialBar)

        # Liste des objets interactibles
        self.interactibles = {
            "Pc": Pc.Pc(self, 50, 50, pygame.Vector2(500,100), self.screen, parameters),
            "Lit": Lit.Lit(self, 50, 50, pygame.Vector2(250,250), parameters),
            "Social": Social.Social(self, 50, 50, pygame.Vector2(1250, 500), parameters)
        }
        # On ajoute chaque objet dans un groupe
        self.interactibleGroup = pygame.sprite.Group()
        for key in self.interactibles:
            self.interactibleGroup.add(self.interactibles[key])

        #Ajout de collisions supplémentaires
        collisionTables = pygame.sprite.Sprite()
        collisionTables.rect = pygame.Rect(0, 0, 650, 180)
        collisionTables.image = pygame.Surface((0,0))
        collisionTables.image.set_alpha(0)
        self.interactibleGroup.add(collisionTables)

    def isRunning(self):
        return True

    def update(self, deltaTime):
        print(deltaTime)

        self.socialBar.subProgress(0.01 * deltaTime)
        self.sleepBar.subProgress(0.01 * deltaTime)

        self.screen.blit(self.background, (0,0))
        self.playerGroup.draw(self.screen)
        self.interactibleGroup.draw(self.screen)
        self.tryInteraction(self.player.rect)
        self.taskManager.update(deltaTime)
        self.player.update(deltaTime, self.interactibleGroup, pygame.Rect(150, 45, 980, 635))

        self.screen.blit(self.bedBase, (0, 720 - self.bedBase.get_height()))
        self.screen.blit(self.treeShadow, (1280 - self.treeShadow.get_width(), 720 - self.treeShadow.get_height()))
        self.screen.blit(self.tree, (1280 - self.tree.get_width(), 720 - self.tree.get_height()))
        self.screen.blit(self.foreground, (0,0))

        self.barGroup.update(self.screen)
        self.taskManager.draw(self.screen)

        #Rect dedebugging
        #pygame.draw.rect(self.foreground, (100,0,0), pygame.Rect(150, 45, 980, 635))

        for item in self.interactibles.values():
            item.update(deltaTime)
        
    def stopInteractions(self):
        for item in self.interactibles.values():
            item.stopInteraction()

    def tryInteraction(self, position : pygame.Rect):
        for item in self.interactibles.values(): # .values() qui accède via la clé à la valeur, l'objet en l'occurence
            if item.rect.colliderect(position):
                if not item.isActive:
                    #print("interaction avec ", item)
                    item.startInteraction()
            elif item.isActive:
                item.stopInteraction()

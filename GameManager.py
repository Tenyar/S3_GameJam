import pygame
import Player
import Pc
import Lit
import TaskManager
import ProgressBar
from pygame import mixer

class GameManager():
    instance = None
    def __init__(self, screen : pygame.display) -> None:
# simulation d'un singleton : Si on essaye de créer une nouvelle instance de GameManager, une exception est levée        
        if GameManager.instance != None : 
            raise Exception("instance already exists")
        GameManager.instance = self

        self.taskManager = TaskManager.TaskManager(10, 0.5, 5, 10)

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
        # mixer.music.load("Sound/Transition_Sound.wav")
        # Met le volume du gestionnaire de musique
        mixer.music.set_volume(0.2)
        # Joue la musique 
        mixer.music.play()

        # Création du background et affichage de celui ci sur la fenêtre
        backgroundImage = pygame.image.load("Art/Background.png")
        self.background = pygame.transform.scale(backgroundImage, (1280, 720))
        foregroundImage = pygame.image.load("Art/Foreground.png")
        self.foreground = pygame.transform.scale(foregroundImage, (1280, 720))

        # Création d'un player
        self.player = Player.Player(50, 110, 0, 0, (255, 75, 25))
        # Group du joueur
        self.playerGroup = pygame.sprite.Group()
        self.playerGroup.add(self.player)

        # Données pour les progressBar
        self.hunger = 100
        self.sleep = 100

        # Création des barres de progressions
        self.sleepBar = ProgressBar.ProgressBar("SleepBar", 300, 15, pygame.Vector2(50,25), (0,0,200))
        self.hungerBar = ProgressBar.ProgressBar("HungerBar", 300, 15, pygame.Vector2(50,50), (255,75,25))
        # Group des barres de progression
        self.barGroup = pygame.sprite.Group()
        self.barGroup.add(self.sleepBar)
        self.barGroup.add(self.hungerBar)

        # Liste des objets interactibles.
        self.interactibles = {
            "Pc": Pc.Pc(self, 50, 50, pygame.Vector2(500,100)),
            "Lit": Lit.Lit(self, 50, 50, pygame.Vector2(250,250))
        }
        # On ajoute chaque objet dans un groupe
        self.interactibleGroup = pygame.sprite.Group()
        for key in self.interactibles:
            self.interactibleGroup.add(self.interactibles[key])

        self.taskManager.addTask()

    def isRunning(self):
        return True

    def update(self, deltaTime):
        self.hungerBar.subProgress(0.1/deltaTime)
        self.screen.blit(self.background, (0,0))
        self.playerGroup.draw(self.screen)
        self.interactibleGroup.draw(self.screen)
        self.tryInteraction(self.player.rect)
        self.taskManager.update(deltaTime)
        self.player.update(deltaTime, self.interactibleGroup, pygame.Rect(90, 20, 1105, 610))

        self.screen.blit(self.foreground, (0,0))

        self.barGroup.update(self.screen)
        self.taskManager.draw(self.screen)
        #pygame.draw.rect(self.background, (0,0,0), pygame.Rect(90, 20, 1105, 610))

        for item in self.interactibles:
            item.update(deltaTime)
        
    def stopInteractions(self):
        for item in self.interactibles:
            item.stopInteraction()

    def tryInteraction(self, position : pygame.Rect):
        for item in self.interactibles:
            if item.rect.colliderect(position):
                if not item.isActive:
                    #print("interaction avec ", item)
                    item.startInteraction()
            elif item.isActive:
                item.stopInteraction()
            

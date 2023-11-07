import pygame
import Player
import Interactible
import TaskManager

class GameManager():
    instance = None
    def __init__(self, screen : pygame.display) -> None:
# simulation d'un singleton : Si on essaye de créer une nouvelle instance de GameManager, une exception est levée        
        if GameManager.instance != None : 
            raise Exception("instance already exists")
        GameManager.instance = self

        self.taskManager = TaskManager.TaskManager()

        self.screen = screen

        # Création du background et affichage de celui ci sur la fenêtre
        image = pygame.image.load("Art/Background.png")
        self.background = pygame.transform.scale(image, (1280, 720))

        # Création d'un player
        self.player = Player.Player(50, 110, 0, 0, (255, 75, 25))
        self.playerGroup = pygame.sprite.Group()
        self.playerGroup.add(self.player)

        self.interactibles = [Interactible.Interactible(10, 10, pygame.Vector2(0,0))]
        self.interactibleGroup = pygame.sprite.Group()
        self.interactibleGroup.add(self.interactibles[0])

    def isRunning(self):
        return True

    def update(self, deltaTime):
        self.screen.blit(self.background, (0,0))
        self.taskManager.draw(self.screen)
        self.playerGroup.draw(self.screen)
        self.interactibleGroup.draw(self.screen)
        self.player.update(deltaTime)

        for item in self.interactibles:
            item.update()
        
    def stopInteractions(self):
        for item in self.interactibles:
            item.stopInteraction()

    def tryInteraction(self, position : pygame.Vector2):
        for item in self.interactibles:
            if item.rect.collidepoint(position.x, position.y):
                print("interaction avec ", item)

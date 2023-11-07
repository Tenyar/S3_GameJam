import pygame
import Player
import Interactible
import TaskManager

class GameManager():
    instance = None
    def __init__(self) -> None:
# simulation d'un singleton : Si on essaye de créer une nouvelle instance de GameManager, une exception est levée        
        if GameManager.instance != None : 
            raise Exception("instance already exists")
        GameManager.instance = self

        self.taskManager = TaskManager.TaskManager()

        # Création d'un player
        self.player = Player.Player(50, 110, 0, 0, (255, 75, 25))
        self.player_group = pygame.sprite.Group()
        self.player_group.add(self.player)

        self.interactibles = [Interactible.Interactible(10, 10)]

    def isRunning(self):
        return True

    def update(self):
        self.taskManager.draw()
        #self.player_group.draw(self.screen)
        
    def stopInteractions(self):
        print("Interaction stopped")
        #

    def tryInteraction(self, position : pygame.Vector2):
        for i in self.interactibles:
            if i.rect.collidepoint(position.x, position.y):
                print("interaction avec ", i)

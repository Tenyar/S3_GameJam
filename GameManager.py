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
        taskManager = TaskManager.TaskManager()
        self.player = Player.Player(50, 50)
        self.interactibles = [Interactible.Interactible(10, 10)]

    def isRunning(self):
        return True

    def update(self):
        TaskManager.draw()
        
    def stopInteractions(self):
        print("Interaction stopped")
        #

    def tryInteraction(self):
        """for i in self.interactibles:
            if ((self.player.rect.x - i.rect.x)**2 + (self.player.rect.y - i.rect.y)**2)**0.5 <= 50:
                print("interaction avec ", i)"""
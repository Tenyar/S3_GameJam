import pygame
import Player

class GameManager():
    instance = None
    def __init__(self) -> None:
# simulation d'un singleton : Si on essaye de créer une nouvelle instance de GameManager, une exception est levée        
        if GameManager.instance != None : 
            raise Exception("instance already exists")
        GameManager.instance = self
        self.Player = Player.Player(50, 50)

    def isRunning(self):
        return True

    def update(self, i):
        return
        


        
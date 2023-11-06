import pygame
import Player

class GameManager():
    instance = None
    def __init__(self) -> None:
        if GameManager.instance != None : 
            raise Exception("instance already exists")
        GameManager.instance = self
        self.Player = Player.Player()
# on simule un singleton

    def isRunning():
        return True

    
        


        
import pygame 

class GameManager():
    instance = None
    def __init__(self) -> None:
        if GameManager.instance != None : 
            raise Exception("instance already exists")
        GameManager.instance = self
        # self.Player = Player()
# on simule un singleton
    
        


        
import pygame
#import Application


screen = pygame.display.set_mode((1920,1080))
class Task ():
    def __init__(self) -> None:
        self.completionPercentage = 0
        self.taskContainer = pygame.image.load("Art/Task_ProofOfConcept.png")

    def addProgress(self, amount : float):
        self.completionPercentage += amount

    def isFinished(self):
        return self.completionPercentage >= 100
    
    def draw(self, position : pygame.Vector2):
        return#Application.screen.blit(self.taskContainer,(position.x,position.y))
        

        


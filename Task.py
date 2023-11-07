import pygame
#import Application


screen = pygame.display.set_mode((1920,1080))
class Task ():
    def __init__(self) -> None:
        self.completionPercentage = 0
        self.taskContainer = pygame.image.load("Art/Task_ProofOfConcept.png")
        self.position = pygame.Vector2
        self.position.x = 0
        self.position.y = 5

    def addProgress(self, amount : float):
        self.completionPercentage += amount

    def isFinished(self):
        return self.completionPercentage >= 100
    
    def draw(self,screen : pygame.display):
        screen.blit(self.taskContainer,(self.position.x,self.position.y))
        

        


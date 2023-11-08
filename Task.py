import pygame
#import Application


screen = pygame.display.set_mode((1920,1080))
class Task (pygame.sprite.Sprite):
    def __init__(self) -> None:
        # initialise l'objet dont on hérite
        super().__init__()
        self.completionPercentage = 0
        self.image = pygame.image.load("Art/Task_ProofOfConcept.png")
        self.image = pygame.transform.scale(self.image, (30 * 4, 18 * 4))
        self.rect = self.image.get_rect()
        self.position = pygame.Vector2(5,20)
        self.rect.topleft = (self.position.x,self.position.y)

    def addProgress(self, amount : float):
        self.completionPercentage += amount

    def isFinished(self):
        return self.completionPercentage >= 100

    def draw(self,screen : pygame.display):
        screen.blit(self.image,(self.position.x,self.position.y))


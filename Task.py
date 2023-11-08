import pygame
import ProgressBar


screen = pygame.display.set_mode((1920,1080))
class Task (pygame.sprite.Sprite):
    def __init__(self,title : str) -> None:
        # initialise l'objet dont on hérite
        super().__init__()
        # pourcentage de completion de la barre : utilisé pour l'affichage de l'avancement de la tâche
        self.completionPercentage = 0
        # image de fond de la tâche
        self.image = pygame.image.load("Art/Task.png")
        # on agrandit l'image
        self.image = pygame.transform.scale(self.image, (40 * 4, 20 * 4))
        # le rectangle qui représente la tâche dans l'espace
        self.rect = self.image.get_rect()
        # on crée un vecteur qui stocke la position de l'image
        self.position = pygame.Vector2(5,20)
        # on place l'image en partant du bord haut gauche de l'écran de jeu
        self.rect.topleft = (self.position.x,self.position.y)
        # on crée un vecteur pour la barre de progression positionné en fonction du fond 
        self.progressBarPosition = pygame.Vector2(self.rect.bottomleft)
        self.progressBarPosition.x += 1.5*4
        # on crée une barre de progression associée à la tâche
        self.progressBar = ProgressBar.ProgressBar(title, 36*4, 2*4, self.progressBarPosition, (100, 100, 100),False)

        self.title = title

         


    def addProgress(self, amount : float):
        self.completionPercentage += amount

    def isFinished(self):
        return self.completionPercentage >= 100

    def draw(self,screen : pygame.display, font : pygame.font.Font):
        # dessin du fond de la tâche
        screen.blit(self.image,(self.position.x,self.position.y))
        # dessin de la barre de progression de la tâche
        self.progressBar.update(screen)
        # dessing de font
        text = font.render(self.title, False, (0,0,0))
        screen.blit(text, (self.position.x + 10, self.position.y + 10))

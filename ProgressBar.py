import pygame

class ProgressBar(pygame.sprite.Sprite):

    def __init__(self, title : str, width, height, progInitiale : int,pos : pygame.Vector2, color, withBackground : bool):

        # constructeur du sprite
        super().__init__()
        # nom de la bar
        self.title = title
        # taille de la bar
        self.width = width
        self.height = height
        # position de la bar dans la fenêtre (via vecteur 2D)
        self.posX = pos.x
        self.posY = pos.y
        # montant de la progression
        self.progAmount = progInitiale
        # couleur de la bar
        self.color = color

        self.withBackground = withBackground

    def getProg(self):
        return self.progAmount

    def addProgress(self, progAmount) -> None:
        # Si l'ajout est supérieure à 100 on bride à 100 %
        if (self.progAmount + progAmount) > 100:
            self.progAmount = 100
        elif self.progAmount < 100:
            self.progAmount += progAmount

    def subProgress(self, progAmount):
        # Si le retrait est inférieure à 0 on bride à 0 %
        if (self.progAmount + progAmount) < 0:
                self.progAmount = 0
        elif self.progAmount > 0:
                self.progAmount -= progAmount

    # A chaque tick change la longueur de la barre avec le montant de progression
    def update(self, screen):
        # Calcule la progression de la barre
        barWidth = (self.progAmount / 100) * self.width

        # Background
        if self.withBackground:
            pygame.draw.rect(screen, (100,100,100), (self.posX, self.posY, self.width + 4, self.height + 4))
        # Progression
        pygame.draw.rect(screen, self.color, (self.posX + 2, self.posY + 2, barWidth, self.height))
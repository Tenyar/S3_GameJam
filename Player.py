import pygame

class Player(pygame.sprite.Sprite):
# Déclaration des variables de cette classe.


    # Constructeur de la classe
    # pos_x/pos_y sont les coordonées de ce player(sprite)
    def __init__(self, width, height):
        # Initialise l'objet qu'on hérite
        super().__init__()
        # Créer une image
        self.image = pygame.Surface([width,height])
        # Remplie l'image d'une couleur
        self.image.fill((255,0,25))
        # Dessine un rectangle autour de l'image qui prendra comme grandeur la width et height de l'image
        self.rect = self.image.get_rect()

    # Destructeur (rarement utile)
    # def __del__(self):
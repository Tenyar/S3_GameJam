import pygame
#import Application

class Player(pygame.sprite.Sprite):
# Déclaration des variables de cette classe.

    # Constructeur de la classe
    # pos_x/pos_y sont les coordonées de ce player(sprite)
    def __init__(self, width, height, pos_x, pos_y, color):

        # Création des attributs de l'instance
        self.width = width
        self.height = height
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        # Initialise l'objet qu'on hérite
        super().__init__()
        # Créer une image
        self.image = pygame.Surface([width,height])
        # Remplie l'image d'une couleur
        self.image.fill(color) # une couleur = rgb soit (..., ..., ...)
        # Dessine un rectangle autour de l'image qui prendra comme grandeur la width et height de l'image
        self.rect = self.image.get_rect()


    def move(self):

        # Récupération de l'instance d'application
        app = None#Application.Application.instance

        # Prise d'informations sur les touches saisit.
        keys = pygame.key.get_pressed()

        # Check dans la structure de donnée sur une clé K_LEFT ou autre
        # True si la touche K_LEFT ou autre touche est déclenché.
        if keys[pygame.K_LEFT]:
            if self.pos_x > 0:
                self.pos_x -= 3
                
                # pour des pixels de différence avec la vélocité
                # Si il dépasse à gauche 
                if self.pos_x < (app.screenWidth - (self.width)):
                    self.pos_x = (app.screenWidth - (self.width))

        if keys[pygame.K_RIGHT]:
            if self.pos_x < (app.screenWidth - self.width): # Prise de la taille de la fenêtre et du joueur en compte
                self.pos_x += 3

                if self.pos_x > (app.screenWidth - (self.width)):
                    self.pos_x = (app.screenWidth - (self.width))

        if keys[pygame.K_DOWN]:
            if self.pos_y < (app.screenHeight - (self.height)):
                self.pos_y += 3

                if self.pos_y > (app.screenHeight - (self.height)):
                    self.pos_y = (app.screenHeight - (self.height))

        if keys[pygame.K_UP]:
            if self.pos_y > 0:
                self.pos_y -= 3

                if self.pos_y < (app.screenHeight - (self.height)):
                    self.pos_y = (app.screenHeight - (self.height))

        self.rect.topleft = (self.pos_x, self.pos_y) # définit la position du player dans la scène # Set the top-left position of the player's rect

    # Destructeur (rarement utile)
    def __del__(self):
        print("Player détruit")
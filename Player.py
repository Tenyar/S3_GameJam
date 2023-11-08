import pygame
import Parameters
import SpriteSheet

class Player(pygame.sprite.Sprite):
# Déclaration des variables de cette classe.

    # Constructeur de la classe
    # pos_x/pos_y sont les coordonées de ce player(sprite)
    def __init__(self, width, height, pos_x, pos_y, color, parameters:Parameters.Parameters):
        # vitesse de l'animation
        self.animationSpeed = 3
        #compteur de temps depuis le dernier changement de sprite
        self.animationTime = 0
        # Création des attributs de l'instance
        self.parameters = parameters.parameters
        self.width = width
        self.height = height
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color

        self.speed = parameters.parameters["playerSpeed"]

        self.screenWidth = pygame.display.get_surface().get_width()
        self.screenHeight = pygame.display.get_surface().get_height()

        # Initialise l'objet qu'on hérite
        super().__init__()
        self.sprite_sheet = SpriteSheet.SpriteSheet("Art/joueur_spriteSheet.png",3,4,20,30)
        self.image = self.sprite_sheet.getSpriteAt(0,0)
        self.image = pygame.transform.scale(self.image,(20*5, 30*5))
        # Dessine un rectangle autour de l'image qui prendra comme grandeur la width et height de l'image
        self.rect = self.image.get_rect()

    def update(self, deltaTime, interactibleGroup, backgroundRect : pygame.Rect):

        # Check collisions
        doesContactTop = False
        doesContactBottom = False
        doesContactLeft = False
        doesContactRight = False

        if self.rect.clipline(backgroundRect.topleft, backgroundRect.topright):
            doesContactTop = True
        if self.rect.clipline(backgroundRect.bottomleft, backgroundRect.bottomright):
            doesContactBottom = True
        if self.rect.clipline(backgroundRect.topleft, backgroundRect.bottomleft):
            doesContactLeft = True
        if self.rect.clipline(backgroundRect.topright, backgroundRect.bottomright):
            doesContactRight = True

        for sprite in interactibleGroup:
            if sprite.rect.clipline(self.rect.topleft, self.rect.topright):
                doesContactTop = True
            if sprite.rect.clipline(self.rect.bottomleft, self.rect.bottomright):
                doesContactBottom = True
            if sprite.rect.clipline(self.rect.topleft, self.rect.bottomleft):
                doesContactLeft = True
            if sprite.rect.clipline(self.rect.topright, self.rect.bottomright):
                doesContactRight = True

        # Prise d'informations sur les touches saisit.
        keys = pygame.key.get_pressed()

        # Check dans la structure de donnée sur une clé K_LEFT ou autre
        # True si la touche K_LEFT ou autre touche est déclenché.
        if keys[pygame.K_LEFT]:
            if not doesContactLeft:
                self.pos_x -= self.speed * deltaTime
                self.image = self.sprite_sheet.getSpriteAt(2, (int)(self.animationTime % 2.0) + 1)
                self.image = pygame.transform.scale(self.image,(20*5, 30*5))
                # pour des pixels de différence avec la vélocité
                # Si il dépasse à gauche 
                #if self.pos_x < (self.screenWidth - (self.width)):
                #    self.pos_x = (self.screenWidth - (self.width))

        if keys[pygame.K_RIGHT]:
            if not doesContactRight: # Prise de la taille de la fenêtre et du joueur en compte
                self.pos_x += self.speed * deltaTime
                self.image = self.sprite_sheet.getSpriteAt(3,1)
                self.image = self.sprite_sheet.getSpriteAt(3, (int)(self.animationTime % 2.0) + 1)
                self.image = pygame.transform.scale(self.image,(20*5, 30*5))
                if self.pos_x > (self.screenWidth - (self.width)):
                    self.pos_x = (self.screenWidth - (self.width))

        if keys[pygame.K_DOWN]:
            if not doesContactBottom:
                self.pos_y += self.speed * deltaTime
                self.image = self.sprite_sheet.getSpriteAt(0,1)
                self.image = self.sprite_sheet.getSpriteAt(0, (int)(self.animationTime % 2.0) + 1)
                self.image = pygame.transform.scale(self.image,(20*5, 30*5))
                if self.pos_y > (self.screenHeight - (self.height)):
                    self.pos_y = (self.screenHeight - (self.height))     

        if keys[pygame.K_UP]:
            if not doesContactTop:
                self.pos_y -= self.speed * deltaTime
                self.image = self.sprite_sheet.getSpriteAt(1,1)
                self.image = self.sprite_sheet.getSpriteAt(1, (int)(self.animationTime % 2.0) + 1)
                self.image = pygame.transform.scale(self.image,(20*5, 30*5))
                #if self.pos_y < (self.screenHeight - (self.height)):
                #    self.pos_y = (self.screenHeight - (self.height))

        
        self.animationTime += deltaTime * 0.001 * self.animationSpeed  
        self.rect.topleft = (self.pos_x, self.pos_y) # définit la position du player dans la scène # Set the top-left position of the player's rect

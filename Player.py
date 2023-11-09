import pygame
import Parameters
import SpriteSheet

class Player(pygame.sprite.Sprite):
# Déclaration des variables de cette classe.

    # Constructeur de la classe
    # pos_x/pos_y sont les coordonées de ce player(sprite)
    def __init__(self, width, height, posX, posY, color, parameters:Parameters.Parameters):
        # vitesse de l'animation
        self.animationSpeed = 5
        #compteur de temps depuis le dernier changement de sprite
        self.animationTime = 0
        # Création des attributs de l'instance
        self.parameters = parameters.parameters
        self.width = width
        self.height = height
        self.position = pygame.Vector2(posX, posY)
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

    def update(self, deltaTime, collisionGroup : list[pygame.Rect], backgroundRect : pygame.Rect):

        # Prise d'informations sur les touches saisit.
        keys = pygame.key.get_pressed()

        translation = pygame.Vector2(0,0)

        # Check dans la structure de donnée sur une clé K_LEFT ou autre
        # True si la touche K_LEFT ou autre touche est déclenché.
        if keys[pygame.K_LEFT]:
            #if not doesContactLeft:
            translation.x -= 1
            self.image = self.sprite_sheet.getSpriteAt(2, (int)(self.animationTime % 2.0) + 1)
            self.image = pygame.transform.scale(self.image,(20*5, 30*5))
            # pour des pixels de différence avec la vélocité
            # Si il dépasse à gauche 
            #if self.pos_x < (self.screenWidth - (self.width)):
            #    self.pos_x = (self.screenWidth - (self.width))

        if keys[pygame.K_RIGHT]:
            #if not doesContactRight: # Prise de la taille de la fenêtre et du joueur en compte
            translation.x += 1
            self.image = self.sprite_sheet.getSpriteAt(3,1)
            self.image = self.sprite_sheet.getSpriteAt(3, (int)(self.animationTime % 2.0) + 1)
            self.image = pygame.transform.scale(self.image,(20*5, 30*5))
            #if self.pos_x > (self.screenWidth - (self.width)):
            #    self.pos_x = (self.screenWidth - (self.width))

        if keys[pygame.K_DOWN]:
            #if not doesContactBottom:
            translation.y += 1
            self.image = self.sprite_sheet.getSpriteAt(0,1)
            self.image = self.sprite_sheet.getSpriteAt(0, (int)(self.animationTime % 2.0) + 1)
            self.image = pygame.transform.scale(self.image,(20*5, 30*5))
            #if self.pos_y > (self.screenHeight - (self.height)):
            #    self.pos_y = (self.screenHeight - (self.height))     

        if keys[pygame.K_UP]:
            #if not doesContactTop:
            translation.y -= 1
            self.image = self.sprite_sheet.getSpriteAt(1,1)
            self.image = self.sprite_sheet.getSpriteAt(1, (int)(self.animationTime % 2.0) + 1)
            self.image = pygame.transform.scale(self.image,(20*5, 30*5))
            #if self.pos_y < (self.screenHeight - (self.height)):
            #    self.pos_y = (self.screenHeight - (self.height))

        if translation.length() != 0:
            translation.normalize_ip()
        translation *= self.speed * deltaTime


        # Représente si les mouvements X et Y sont possible respectivement
        translationDirectionChecks = [True, True]

        # Check collisions entre player et la map
        translatedRect = pygame.Rect(self.rect.left, self.rect.top, self.rect.width, self.rect.height)
        translatedXRect = translatedRect.move(translation.x * 1.1, 0)
        translatedYRect = translatedRect.move(0, translation.y * 1.1)
        # Les translations X et Y respectivement
        translatedRects = [translatedXRect, translatedYRect]
        for i in range(2):
            if translatedRects[i].clipline(backgroundRect.topleft, backgroundRect.topright):
                translationDirectionChecks[i] = False
                pygame.draw.lines(pygame.display.get_surface(), (255, 0, 0), True, [backgroundRect.topleft, backgroundRect.topright])
            if translatedRects[i].clipline(backgroundRect.bottomleft, backgroundRect.bottomright):
                translationDirectionChecks[i] = False
                pygame.draw.lines(pygame.display.get_surface(), (255, 0, 0), True, [backgroundRect.bottomleft, backgroundRect.bottomright])
            if translatedRects[i].clipline(backgroundRect.topleft, backgroundRect.bottomleft):
                translationDirectionChecks[i] = False
                pygame.draw.lines(pygame.display.get_surface(), (255, 0, 0), True, [backgroundRect.topleft, backgroundRect.bottomleft])
            if translatedRects[i].clipline(backgroundRect.topright, backgroundRect.bottomright):
                translationDirectionChecks[i] = False
                pygame.draw.lines(pygame.display.get_surface(), (255, 0, 0), True, [backgroundRect.topright, backgroundRect.bottomright])

            # Check collisions entre player et tout les sprites
            for collisionRect in collisionGroup:
                #if sprite.rect.clipline(translatedRect.topleft, translatedRect.topright):
                #    isPositionPossible = False
                #if sprite.rect.clipline(translatedRect.bottomleft, translatedRect.bottomright):
                #    isPositionPossible = False
                #if sprite.rect.clipline(translatedRect.topleft, translatedRect.bottomleft):
                #    isPositionPossible = False
                #if sprite.rect.clipline(translatedRect.topright, translatedRect.bottomright):
                #    isPositionPossible = False
                if pygame.Rect.colliderect(collisionRect, translatedRects[i]):
                    translationDirectionChecks[i] = False
                    pygame.draw.rect(pygame.display.get_surface(), (255, 0, 0), collisionRect, 1)


        if translationDirectionChecks[0]:
            self.position += (translation.x, 0)
        else:
            pygame.draw.lines(pygame.display.get_surface(), (200, 55, 0), True,
                [translatedRect.topleft, translatedRect.topright, translatedRect.bottomright, translatedRect.bottomleft])
            
        if translationDirectionChecks[1]:
            self.position += (0, translation.y)
        else:
            pygame.draw.lines(pygame.display.get_surface(), (200, 55, 0), True,
                [translatedRect.topleft, translatedRect.topright, translatedRect.bottomright, translatedRect.bottomleft])

        
        self.animationTime += deltaTime * 0.001 * self.animationSpeed  
        self.rect.topleft = (self.position) # définit la position du player dans la scène # Set the top-left position of the player's rect

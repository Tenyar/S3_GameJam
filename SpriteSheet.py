import pygame 

class SpriteSheet(object):

    def __init__(self,filename : str, spritePerLine, spritePerColumn, spriteWidth, spriteHeight):
        # Chargement de l'image.
        image = pygame.image.load(filename).convert()
        # Nombre de sprite totale.
        NumberOfSprites = spritePerLine*spritePerColumn
        # Tableau ou sont stocké les sprites.
        self.sprites = {}
        # autres Attributs de l'instance.
        self.spritePerLine = spritePerLine
        self.spritePerColumn = spritePerColumn
        # Séparation des sprites et rangement des sprites dans le tableau.
        for index in range(NumberOfSprites):
            # Calcul sur quel ligne et colonne on est.
            currentLine = index%spritePerLine
            currentColumn = index//spritePerLine
            self.sprites[currentLine,currentColumn] = image.subsurface((currentLine)*spriteWidth,(currentColumn)*spriteHeight,spriteWidth,spriteHeight)
            print("SRPTIES")
            print(self.sprites)

    # Retourne le sprite demandé.
    def getSpriteAt(self, line : int, column : int) -> pygame.Surface:
        if line > self.spritePerLine - 1 or line < 0:
            raise Exception("line index not valid")
        if column > self.spritePerColumn - 1 or column < 0:
            raise Exception("column index not valid")
        return self.sprites[line,column]
    
import pygame 
#classe qui représente la notion de sprite sheet 
# Elle permet de stocker toutes les images d'une sprite sheet dans l'ordre avec leur numéro de colonne et de ligne
#TODO ajout offsets
class SpriteSheet():
    # filename : Path to the sprite sheet file
    # spritePerline : number of sprites on each line
    # spriteperColumn : number of sprites on each column
    # spriteWidth : width of one sprite
    # spriteHeight : height of one sprite
    # WARNING : This class will work correctly only if every sprite of the sprite sheet has the same dimensions, if there is the same number of sprites on every line and if every sprite is placed with the same offset on the sheet.
    def __init__(self,filename : str, spritePerLine : int , spritePerColumn : int , spriteWidth, spriteHeight):
        image = pygame.image.load(filename)
        #total number of sprite
        NumberOfSprites = spritePerLine*spritePerColumn
        # dictionnary that will contain all the sprites
        # each entry will be in the following format : position->[sprite] with position being a 2 entry list saying in witch column and wich line is the sprite linked, like this : [Column,line]
        self.sprites = {}
        self.spritePerLine = spritePerLine
        self.spritePerColumn = spritePerColumn
          
        for index in range(NumberOfSprites):
            # currentLine : the result of index%spritePerLine will loop between the index of the first line and the index of the last line
            # i.e : NumberOfSprites = 12 spritePerLine = 2 :
            # for index = 0 currentLine = 0%2 = 0 <- index of the current line 
            # for index = 9 currentLine = 9%2 = 1 <- index of the current line ...
            currentLine = index%spritePerLine
            # currentColumn : the result of index%spritePerLine will loop between the index of the first column and the index of the last column 
            # (i.e : NumberOfSprites = 12 spritePerLine = 2 :
            # for index = 0 currentColumn = 0//2 = 0 <- index of the current column
            # for index = 9 currentColumn = 9//2 = 4)<- index of the current column ...
            currentColumn = index//spritePerLine
            # Adding every sprite to the sprites dictionniary (position->[sprite]) using subsurface.
            # subsurface allows to create a sub surface of the main surface ( the sprite sheet) given 4 parameters : 
            # left : horizontal coordinate ("x") of the new surface  
            # top : vertical coordinate ("y") of the new surface
            # width : width of the new surface
            # height : height of the new surface
            self.sprites[currentLine,currentColumn] = image.subsurface((currentLine)*spriteWidth,(currentColumn)*spriteHeight,spriteWidth,spriteHeight)
            print(self.sprites[currentLine,currentColumn])

    # return the sprite at the position given in the parameters
    def getSpriteAt(self, column : int, line : int) -> pygame.surface:
        if line > self.spritePerLine - 1 | line < 0:
            raise Exception("line index not valid")
        if column > self.spritePerColumn - 1 | column < 0:
            raise Exception("column index not valid")
        return self.sprites[line,column]
    
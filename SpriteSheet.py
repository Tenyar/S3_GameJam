import pygame 

class SpriteSheet():

    def __init__(self,filename : str, spritePerLine, spritePerColumn, spriteWidth, spriteHeight):
        image = pygame.image.load(filename)
        NumberOfSprites = spritePerLine*spritePerColumn
        self.sprites = {}
        self.spritePerLine = spritePerLine
        self.spritePerColumn = spritePerColumn
          
        for index in range(NumberOfSprites):
            currentLine = index%spritePerLine
            currentColumn = index//spritePerLine
            self.sprites[currentLine,currentColumn] = image.subsurface((currentLine)*spriteWidth,(currentColumn)*spriteHeight,spriteWidth,spriteHeight)
            print(self.sprites[currentLine,currentColumn])

    def getSpriteAt(self, column : int, line : int) -> pygame.surface:
        if line > self.spritePerLine - 1 | line < 0:
            raise Exception("line index not valid")
        if column > self.spritePerColumn - 1 | column < 0:
            raise Exception("column index not valid")
        return self.sprites[line,column]
    
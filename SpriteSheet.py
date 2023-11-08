import pygame 

class SpriteSheet():

    def __init__(self,filename : str ,spritePerLine , spritePerColumn , spriteWidth , spriteHeight,):
        image = pygame.image.load(filename)
        NumberOfSprites = spritePerLine*spritePerColumn
        self.sprites = {}
        self.spritePerLine = spritePerLine
        self.spritePerColumn = spritePerColumn
          
        for index in range(NumberOfSprites):
            currentLine = index%spritePerLine
            currentColumn = index//spritePerLine
        self.sprites[currentLine,currentColumn] = image.subsurface((currentLine)*spriteWidth,(currentColumn)*spriteWidth,spriteWidth,spriteHeight)
        print(self.sprites[currentLine,currentColumn])

    def getSpriteAt(self,line : int, column : int):
        if line > self.spritePerLine | line < 0:
            raise Exception("line index not valid")
        if column > self.spritePerColumn | column < 0:
            raise Exception("column index not valid")
        return self.sprites[line,column]
    
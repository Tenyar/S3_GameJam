import pygame
from pygame.sprite import AbstractGroup

class Interactible(pygame.sprite.Sprite):

    def __init__(self, width, height) -> None:
        super().__init__()

        self.image = pygame.Surface([width,height])


    def startInteraction():
        print("Interaction")
import pygame
from pygame.sprite import AbstractGroup

class Interactible(pygame.sprite.Sprite):

    def __init__(self, *groups: AbstractGroup, width, height) -> None:
        super().__init__(*groups)

        self.image = pygame.Surface([width,height])


    def startInteraction():
        print("Interaction")
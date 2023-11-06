import pygame

class Task ():
    def __init__(self) -> None:
        self.completionPercentage = 0

    def addProgress(self, amount : float):
        self.completionPercentage += amount

    def isFinished(self):
        return self.completionPercentage >= 100

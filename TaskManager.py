import Task
import pygame

class TaskManager:
    instance = None
    #simulation d'un singleton : Si on essaye de créer une nouvelle instance de TaskManager, une exception est levée    
    def __init__(self) -> None:
        if TaskManager.instance != None : 
            raise Exception("instance already exists")
        TaskManager.instance = self
        self.tasks = []
        

    def getTaskAmount(self):
        return len(self.tasks)
    
    def progressCurrentTask(self, amount : float):
        self.tasks[0].addProgress(amount)
        

    def addTask(self):
        self.tasks.append(Task.Task())
    
    def deleteFinishedTask(self):
        if self.tasks[0].isFinished():
            self.tasks.pop(0)

    def draw(self,screen : pygame.display,):
        for task in self.tasks :
            task.draw(screen)
            task.position.y += 2

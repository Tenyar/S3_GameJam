import Task
import pygame
import Parameters

class TaskManager:

    instance = None

    #simulation d'un singleton : Si on essaye de créer une nouvelle instance de TaskManager, une exception est levée
    def __init__(self, startCounteurValue, counterDecreaseStep, counterClampMin, maxTask, parameters:Parameters.Parameters) -> None:
        if TaskManager.instance != None :
            raise Exception("instance already exists")
        TaskManager.instance = self

        self.tasks = []
        self.counter = startCounteurValue
        self.counterDecreaseStep = counterDecreaseStep
        self.counterCurrentMax = startCounteurValue
        self.counterClampMin = counterClampMin
        self.maxTask = maxTask

        self.font = pygame.font.Font("Font/Quinquefive-ALoRM.ttf", 15)

    
    def update(self, deltaTime):

        self.counter -= deltaTime * 0.001

        if(self.counter <= 0 and self.getTaskAmount() < self.maxTask):
            self.counterCurrentMax = max(self.counterCurrentMax - self.counterDecreaseStep, self.counterClampMin)
            self.counter = self.counterCurrentMax
            self.addTask("Test")


    def getTaskAmount(self):
        return len(self.tasks)

    def progressCurrentTask(self, amount : float):
        self.tasks[0].addProgress(amount)
        if self.tasks[0].isFinished():
            self.deleteCurrentTask()
            return True
    

    def addTask(self, title):
        self.tasks.append(Task.Task(title))

    def deleteCurrentTask(self):
            self.tasks.pop(0)

    def draw(self,screen : pygame.display,):
        currentTaskId = 0
        for task in self.tasks :
            task.position.y = currentTaskId * 95 + 180
            task.progressBar.posY = currentTaskId * 95 + 34 + 180
            task.draw(screen, self.font)
            currentTaskId += 1





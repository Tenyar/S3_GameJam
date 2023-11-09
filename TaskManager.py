import Task
import pygame
import Parameters
import random

class TaskManager:

    instance = None

    #simulation d'un singleton : Si on essaye de créer une nouvelle instance de TaskManager, une exception est levée
    def __init__(self,parameters:Parameters.Parameters) -> None:
        if TaskManager.instance != None :
            raise Exception("instance already exists")
        TaskManager.instance = self
        self.parameters = parameters.parameters

        self.listTasks = [
            ("SAE", 30, 10, 10),
            ("REVISION", 30, 10, 10),
            ("ORAL", 30, 10, 30),
            ("DM", 30, 10, 20),
            ("GAME JAM", 30, 10, 40),
            ("EXERCICE", 30, 10, 5)
        ]

        self.firstTask = []
        self.tasks = []
        self.addTask()
        self.counter = self.parameters["startCounteurValue"]
        self.counterDecreaseStep = self.parameters["counterDecreaseStep"]
        self.counterCurrentMax = self.parameters["startCounteurValue"]
        self.counterClampMin = self.parameters["counterClampMin"]
        self.maxTask = self.parameters["maxTask"]

        self.font = pygame.font.Font("Font/Quinquefive-ALoRM.ttf", 15)

        self.pointsCounter = 0


    def update(self, deltaTime):

        self.counter -= deltaTime * 0.001

        if(self.counter <= 0 and self.getTaskAmount() < self.maxTask):
            self.counterCurrentMax = max(self.counterCurrentMax - self.counterDecreaseStep, self.counterClampMin)
            self.counter = self.counterCurrentMax
            self.addTask()


        if self.getTaskAmount() > 0:
            self.tasks[0].update(deltaTime)


    def isTaskTimedOut(self):
        if self.getTaskAmount() > 0 and self.tasks[0].hasNoTimeRemaining():
            self.deleteCurrentTask()
            return True
        return False

    def getTaskAmount(self):
        return len(self.tasks)
    
    def getCurrentTaskScore(self):
        return self.tasks[0].getTaskScore()


    def addPoints(self):
        points = self.getCurrentTaskScore()
        self.pointsCounter += points

    def getCompteurPoints(self):
        return self.pointsCounter

    def progressCurrentTask(self, amount : float):
        self.tasks[0].addProgress(amount)
        if self.tasks[0].isFinished():
            self.deleteCurrentTask()
            return True
    

    def addTask(self):
        title, time, amount ,points = random.choice(self.listTasks)
        self.tasks.append(Task.Task(title, time, amount,points))

    def deleteCurrentTask(self):
            self.tasks.pop(0)

    def draw(self,screen : pygame.display,):
        currentTaskId = 0

        for task in self.tasks :
            task.position.y = currentTaskId * 95 + 180
            task.progressBar.posY = currentTaskId * 95 + 34 + 180
            self.firstTask.append(self.tasks[0])
            self.firstTask.pop(0)
            task.draw(screen, self.font)
            currentTaskId += 1





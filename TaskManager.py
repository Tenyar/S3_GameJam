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


        self.tasksDifficulty = self.parameters["tasksDifficulty"]/2
        # list of possible tasks 
        self.listTasks = [
            ("SAE", 120, 1, 80*self.tasksDifficulty),
            ("REVISION", 40, 2.5, 35*self.tasksDifficulty),
            ("ORAL", 20, 5, 30*self.tasksDifficulty),
            ("DM", 30, 5, 20*self.tasksDifficulty),
            ("GAME JAM", 60, 1.25, 55*self.tasksDifficulty),
            ("EXERCICE", 20, 7, 5*self.tasksDifficulty)
        ]

        self.firstTask = []
        self.tasks = []
        self.addTask()
        self.counter = self.parameters["startCounterValue"]
        self.counterDecreaseStep = self.parameters["counterDecreaseStep"]
        self.counterCurrentMax = self.parameters["startCounterValue"]
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

    # check if the task is failed and does not have to be on screen anymore. If so, delete the current task from the tasks list and returns True, else returns False
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
        self.pointsCounter += self.getCurrentTaskScore()

    def getPointsCounter(self) -> int:
        return self.pointsCounter

    # adds amount to the progress of the current task. If after adding the amount, the task is finished , adds the task points to the score counter and delete the current task from the tasks list.
    def progressCurrentTask(self, amount : float):
        self.tasks[0].addProgress(amount)
        if self.tasks[0].isFinished():
            self.addPoints()
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

    def deleteInstance(self):
        TaskManager.instance = None


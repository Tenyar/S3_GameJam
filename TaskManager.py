import Task

class TaskManager:
    def __init__(self) -> None:
        self.tasks = []

    def getTaskAmount(self):
        return len(self.tasks)
    
    def progressCurrentTask(self, amount : float):
        self.tasks[0].addProgress(amount)
        if self.tasks[0].isFinished():
            self.tasks.pop(0)

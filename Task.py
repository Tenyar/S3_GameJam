import pygame
import ProgressBar


screen = pygame.display.set_mode((1920,1080))
class Task (pygame.sprite.Sprite):
    instance = 0
    def __init__(self,title : str, timerLenght, amountPerKey) -> None:
        # initialise l'objet dont on hérite
        super().__init__()
        # pourcentage de completion de la barre : utilisé pour l'affichage de l'avancement de la tâche
        self.completionPercentage = 0
        # image de fond de la tâche
        self.image = pygame.image.load("Art/Task.png")
        # on agrandit l'image
        self.image = pygame.transform.scale(self.image, (40 * 4, 20 * 4))
        # le rectangle qui représente la tâche dans l'espace
        self.rect = self.image.get_rect()
        # on crée un vecteur qui stocke la position de l'image
        self.position = pygame.Vector2(5,20)
        # on place l'image en partant du bord haut gauche de l'écran de jeu
        self.rect.topleft = (self.position.x,self.position.y)
        # on crée un vecteur pour la barre de progression positionné en fonction du fond 
        self.progressBarPosition = pygame.Vector2(self.rect.bottomleft)
        self.progressBarPosition.x += 1.5*4
        # on crée une barre de progression associée à la tâche
        self.progressBar = ProgressBar.ProgressBar(title, 36*4, 2*4, 0, self.progressBarPosition, (34, 177, 76),False)
        # time remaining to do the task (in seconds)
        self.remainingTime = timerLenght
        # same as remainingTime but casted to int and then to string ( used to blit the timer on screen)
        self.timer = ""
        # time when initialising the task
        #self.timeAtInit = pygame.time.get_ticks()*0.001
        self.title = title
        self.amountPerKey = amountPerKey
        Task.instance+=1  


    def addProgress(self, amount : float):
        self.completionPercentage += amount * self.amountPerKey
        self.progressBar.setProgress(self.completionPercentage)

    def isFinished(self):
        return self.completionPercentage >= 100
    
    def hasNoTimeRemaining(self):
        return self.remainingTime <= -1
    
    def update(self,deltaTime):
        self.remainingTime -= deltaTime*0.001
        self.timer = str(int(self.remainingTime+1))
        pygame.time.delay
        #print("remainingTime = " + str(self.remainingTime))
        #print("timer = " + self.timer)

    def draw(self,screen : pygame.display, font : pygame.font.Font):
        # dessin du fond de la tâche
        screen.blit(self.image,(self.position.x,self.position.y))
        # dessin de la barre de progression de la tâche
        self.progressBar.update(screen)
        # dessing de font
        text = font.render(self.title, False, (0,0,0))
        screen.blit(text, (self.position.x + 10, self.position.y + 10))

        if self.remainingTime >0.0 and self.remainingTime < 6.0:
            timer = font.render(self.timer,False,(255,0,0))
        elif self.remainingTime >= 6.0:
            timer = font.render(self.timer,False,(0,0,0))
        elif self.progressBar.getProg == 100:
            timer = font.render("REUSSITE",False,(0,255,0))
        else:
            timer = font.render("ECHEC",False,(255,0,0))  

        screen.blit(timer, (self.position.x + 40, self.position.y + 50))

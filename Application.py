import pygame
import GameManager
import sys
import Player

print("\n\n\n", sys.argv, "\n\n\n")

pygame.init
pygame.font.init()
pygame.display.set_caption("survie")
screen = pygame.display.set_mode((1920,1080))
clock = pygame.time.Clock()
dt = 0

player = Player.Player(25, 25)
player_group = pygame.sprite.Group()
player_group.add(player)
background_image = pygame.image.load("Art/Background.png")
background_image = pygame.transform.scale(background_image,screen.get_size())
task = pygame.image.load("Art/Task_ProofOfConcept.png")


gameManager = GameManager.GameManager()
while gameManager.isRunning():
    # On regarde si l'évenement "quitter la fenêtre" est déclenché.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    player_group.draw(screen)
    screen.blit(task,(0,0))
    screen.blit(background_image,(0,0))
    
    

    dt = clock.tick(60)
    gameManager.update(dt)
    pygame.display.flip()
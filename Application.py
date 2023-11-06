import pygame
import GameManager
import sys
import Player

print("\n\n\n", sys.argv, "\n\n\n")

pygame.init
pygame.font.init()
pygame.display.set_caption("PONG")
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
dt = 0

player = Player.Player(25, 25)
player_group = pygame.sprite.Group()
player_group.add(player)

gameManager = GameManager.GameManager()
while gameManager.isRunning():
    # On regarde si l'évenement "quitter la fenêtre" est déclenché.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    dt = clock.tick(60)
    gameManager.update(dt)
    player_group.draw(screen)
    pygame.display.flip()
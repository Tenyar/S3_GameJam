import pygame
import GameManager

pygame.init
pygame.font.init()
pygame.display.set_caption("PONG")
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
dt = 0

gameManager = GameManager()
while gameManager.isrunning():
    dt = clock.tick(60)
    gameManager.update(dt)
    pygame.display.flip()

pygame.quit()

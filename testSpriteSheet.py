from pygame import *
import SpriteSheet
fenetre = display.set_mode((620,350))
display.set_caption('Tutoriel pygame')
init()
 
#les images
 
#les spritesheets
danse = image.load('Art/joueur_spriteSheet.png')
#On associe les touches aux images
danseSprite = {}
for x in range(12):
    danseSprite[x%3,x//3] = danse.subsurface((x%3)*20,(x//3)*30,20,30)
                
#paramètres de départ
jouer = True
sprite_x = 0
sprite_y = 0
sprite_sheet = SpriteSheet.SpriteSheet("Art/joueur_spriteSheet.png",3,4,20,30)
 
#les fonctions du jeu
   
while jouer:
    for events in event.get():
         if events.type == QUIT:
             quit()
    #les 4 lignes pour afficher le sprite animé
    sprite_x = (sprite_x+1)%2
    sprite_y = (sprite_y+1)%3
    fenetre.fill((255,255,255))
    fenetre.blit(sprite_sheet.sprites[0,1],(100,100))
    display.flip()
    #définir les FPS on fait une pause 50ms entre chaque frame
    time.wait(50)
    
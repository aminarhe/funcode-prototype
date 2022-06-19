import pygame
import sys
from character import Character

def run():
    pygame.init()
    screen = pygame.display .set_mode((800, 600))
    pygame.display.set_caption = 'Gameplay'
    bg_pic = pygame.image.load('media/grass_sample.png')
    bg_pic = pygame.transform.scale(bg_pic,(800,600))
    character = Character(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        screen.blit(bg_pic,(0,0))
        character.output()
        pygame.display.flip()

        

run()
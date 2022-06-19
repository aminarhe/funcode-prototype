import pygame

class Character():
    def __init__(self, screen):
        #Создание персонажа

        self.screen = screen
        self.image = pygame.image.load('media/pngegg1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def output(self):
        #Прорисовка персонажа
        self.screen.blit(self.image, self.rect)

    def go(self,screen,direction):
        #Ходьба по заданному направлению
        if direction == 'up':
            self.rect.centery = self.rect.centery + 2
        elif direction == 'down':
            self.rect.centery = self.rect.centery - 2
        elif direction == 'right':
            self.rect.centerx = self.rect.centerx + 2
        elif direction == 'left':
            self.rect.centerx = self.rect.centerx - 2

    


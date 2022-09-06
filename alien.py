import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    
    def __init__(self, ai_game):
        super().__init__()
        # Game variables and settings
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        
        # Image of the alien
        self.image = pygame.transform.scale(pygame.image.load('images/alien.png'), (0.05*self.screen_rect.width, 0.05*self.screen_rect.height))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Aliens's position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.direction = True # True - right, False - left
        
    def update(self):
        self.check_edges()
        if self.direction:
            self.x += self.settings.alien_speed_x
        else:
            self.x -= self.settings.alien_speed_x
        self.rect.x = self.x
        
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if (self.rect.right >= screen_rect.right+self.rect.width or 
            self.rect.left <= -self.rect.width):
            self.change_direction()
            
    def change_direction(self):
        self.direction = not self.direction
        self.rect.y += 2*self.rect.height
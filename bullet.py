import pygame
from pygame.sprite import Sprite

from settings import Settings

class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        # Game variables and settings
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        # Image of the bullet
        self.image = pygame.transform.scale(pygame.image.load(
                                            'images/bullet.png'), (5, 20))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        
        # Bullet's position
        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)
        
    # Update bullet's position
    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)
import pygame

class Ship(object):
    def __init__(self, ai_game):
        # Game variables and settings
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        
        # Image of the ship
        self.image = pygame.transform.scale(pygame.image.load('images/ship.png'), 
                                            (0.07*self.screen_rect.width, 
                                             0.12*self.screen_rect.height))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.mask = pygame.mask.from_surface(self.image)
        
        # Ship's movement
        self.speed = self.settings.ship_speed
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
        # Ship's position
        self.position = {'x':float(self.rect.x), 'y':float(self.rect.y)}
       
    # Draw ship on screen
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        
    # Update ship's position
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.position['x'] += self.speed
        if self.moving_left and self.rect.left > 0:
            self.position['x'] -= self.speed
        if self.moving_up and self.rect.top > 0:
            self.position['y'] -= self.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.position['y'] += self.speed
            
        self.rect.x = self.position['x']
        self.rect.y = self.position['y']
    
    def reset_position(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.position = {'x':float(self.rect.x), 'y':float(self.rect.y)}
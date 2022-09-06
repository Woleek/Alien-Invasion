import pygame

class LifeBar(object):
    
    def __init__(self, ai_game):
        # Game variables and settings
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        self.lifes =  self.settings.lifes_limit
        self.image = pygame.transform.scale(pygame.image.load('images/heart.png'), (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 20, self.settings.screen_height - self.rect.height - 10
        
    def decrease_life_bar(self):
        self.lifes -= 1
            
    def blitme(self):
        for life in range(self.lifes):
            self.screen.blit(self.image, 
                             (self.rect.x + life*self.rect.width, 
                              self.rect.y))
            
class Points(object):
        
    def __init__(self, ai_game):
        # Game variables and settings
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.font = pygame.font.SysFont("agencyfb", 40)
        self.score = 0
        
    def blitme(self):
        text = self.font.render(str(self.score), True, (255, 255, 255))
        self.screen.blit(text, (self.settings.screen_width - 50, 
                         self.settings.screen_height - 60))
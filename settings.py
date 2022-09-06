import pygame

class Settings(object):
    def __init__(self):
        # Screen initialization
        self.screen_width = 1400
        self.screen_height = 800
        self.bg_img = pygame.image.load('images/bg.jpg')
        
        # Ship settings
        self.ship_speed = 1.5
        
        # Bullet settings
        self.bullet_speed = 1.5
        
        # Alien settings
        self.alien_speed_x = 1.0
        
        # Lifes settings
        self.lifes_limit = 3
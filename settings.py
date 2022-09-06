import pygame

class Settings(object):
    def __init__(self, width=1200, height=800):
        # Screen initialization
        self.screen_width = width
        self.screen_height = height
        self.bg_img = pygame.image.load('images/bg.jpg')
        
        # Ship settings
        self.ship_speed = 1.5
        
        # Bullet settings
        self.bullet_speed = 1.0
        
        # Alien settings
        self.alien_speed_x = 1.0  
import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion(object):
    def __init__(self):
        # Initialize game window
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, 
                                               self.settings.screen_height))
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        self.settings.bg_img = pygame.transform.scale(self.settings.bg_img,
                                                      (self.settings.screen_width, self.settings.screen_height) )
        pygame.display.set_caption("Alien Invasion")
        
        # Initialize game elements
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        
    def run_game(self):
        # Keep game windows updated 
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()
            
    def _check_events(self):
        # Checking what events occured
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    sys.exit()
                case pygame.KEYDOWN:
                    self._check_keydown_events(event)
                case pygame.KEYUP:
                    self._check_keyup_events(event)
                        
    def _check_keydown_events(self, event):
        match event.key:
            case pygame.K_RIGHT:
                self.ship.moving_right = True
            case pygame.K_LEFT:
                self.ship.moving_left = True
            case pygame.K_UP:
                self.ship.moving_up = True
            case pygame.K_DOWN:
                self.ship.moving_down = True
            case pygame.K_SPACE:
                self._fire_bullet()
            case pygame.K_ESCAPE:
                sys.exit()
    
    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
        
    def _check_keyup_events(self, event):  
        match event.key:
            case pygame.K_RIGHT:
                self.ship.moving_right = False
            case pygame.K_LEFT:
                self.ship.moving_left = False
            case pygame.K_UP:
                self.ship.moving_up = False
            case pygame.K_DOWN:
                self.ship.moving_down = False
            
    def _update_screen(self):
        self.screen.blit(self.settings.bg_img, (0, 0))
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.blitme()
        pygame.display.flip()
            
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet()
        
    def run_game(self):
        # Keep game windows updated 
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()
            self._update_aliens()
            self._update_bullets()
            
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
        self.aliens.draw(self.screen)
        pygame.display.flip()
        
    def _update_bullets(self):
        # using copy to not change list during loop
        for bullet in self.bullets.copy(): 
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            
    def _create_fleet(self):
        alien = Alien(self)
        
        # space for alien fleet
        alien_width, alien_height = alien.rect.size
        ship_height = self.ship.rect.height
        available_space_x = (self.settings.screen_width - (2*alien_width))
        available_space_y = (self.settings.screen_height - (3*alien_height) 
                             - ship_height)
        number_aliens_y = available_space_y // (2*alien_height)
        number_aliens_x = available_space_x // (2*alien_width)
        
        for row_number in range(number_aliens_y):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
            
    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        if row_number % 2 == 0:
            alien.x = (alien_width + 
                       2*alien_width*alien_number)
        else:
            alien.x = (self.settings.screen_width - 
                       (2*alien_width*(alien_number+1)))
            alien.direction = False
        alien.rect.x = alien.x
        alien.rect.y = (alien_height + (2*alien.rect.height*row_number) -
                        (self.settings.screen_height*0.7))
        self.aliens.add(alien)
        
    def _update_aliens(self):
        self.aliens.update()   
        
        
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
import sys
import pygame
from time import sleep
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from stats import LifeBar, Points

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
        self.life_bar =  LifeBar(self)
        self.points = Points(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.game_over_image = pygame.transform.scale(pygame.image.load('images/over.png'),
                                                      (400, 400))
        self.game_over_rect = self.game_over_image.get_rect()
        self.game_over_rect.center = (self.settings.screen_width/2, 
                                      self.settings.screen_height/2)
        self.game_over = False
        
        self._create_fleet()
        
    def run_game(self):
        # Keep game windows updated 
        while True:
            self._check_events()
            if not self.game_over:
                self.ship.update()
                self.bullets.update()
                self._update_aliens()
                self._update_bullets()
                self._update_screen()
            else:
                self._end_game() 
            
    def _end_game(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.game_over_image, self.game_over_rect)
        pygame.display.flip()
    
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
        self.life_bar.blitme()
        self.points.blitme()
        self.aliens.draw(self.screen)
        pygame.display.flip()
        
    def _update_bullets(self):
        # using copy to not change list during loop
        for bullet in self.bullets.copy(): 
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_hit()
            
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
        if not self.aliens:
            self._level_up()
        self.aliens.update()
        self._check_alien_collision()
        
    def _check_bullet_hit(self):
        for bullet in self.bullets.copy():
            for alien in self.aliens.copy():
                offset = (bullet.rect.x - alien.rect.x, bullet.rect.y - alien.rect.y)
                if alien.mask.overlap(bullet.mask, offset):
                    self.aliens.remove(alien)
                    self.bullets.remove(bullet)
                    
    def _check_alien_collision(self):
        for alien in self.aliens:
            offset = (self.ship.rect.x - alien.rect.x, self.ship.rect.y - alien.rect.y)
            if (alien.mask.overlap(self.ship.mask, offset) or 
                alien.rect.y >= self.screen.get_rect().bottom):
                self._take_hit()
    
    def _take_hit(self):
        if self.life_bar.lifes > 1:
            self.life_bar.decrease_life_bar()
            self.ship.reset_position()
            self.aliens.empty()
            self._create_fleet()
            sleep(0.1)
        else:
            self.game_over = True
    
    def _level_up(self):
        self.settings.alien_speed_x += 1
        self.points.score += 1
        self.life_bar.lifes += 1
        self._create_fleet()
    
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
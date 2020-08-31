import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """A class to mange the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load t1e ship image and get its rect
        self.image = pygame.image.load('/Users/luisfernando/Pictures/StarFox.bmp')
        self.rect = self.image.get_rect()
        # Start each new ship ate the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        #self.rect.center = self.screen_rect.center

        #Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False

    def update(self):
        """Update the ship's position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
            #self.rect.x += 1
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed
            #self.rect.x -= 1
        elif self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        #Update rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """"Center the ship on the screen """
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

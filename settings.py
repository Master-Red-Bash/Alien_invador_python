import sys
import pygame


class Settings:
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize te game's settings"""
       # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        #Ship speed
        self.ship_speed = 20
        self.ship_limit = 3
       # Bullet Settings
        self.bullet_speed = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 20
        # Alien settings
        self.alien_speed = 10
        self.fleet_drop_speed = 30
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # How quicly the game speed up
        self.speedup_scale = 1.1

        #How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that ahcnge throughut the game"""
        self.ship_speed = 20
        self.bullet_speed = 10
        self.alien_speed = 10

        # Fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        #print(self.alien_points)

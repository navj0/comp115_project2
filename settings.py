class Settings:
    """A class to store all settings for Alien Invasion."""
     
    def __init__(self):
        """Initialize the game's static settings."""
        self.screen_width = 1200 # Screen settings
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 5 # Ship settings
        self.ship_limit = 3
        self.bullet_speed = 3 # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 20
        self.fleet_drop_speed = 10 # Alien settings
        self.speedup_scale = 1.1 # How quickly the game speeds up
        self.score_scale = 1.5 # How quickly the alien point values increase
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
       """Initialize settings that change throughout the game."""
       self.ship_speed = 1.5
       self.bullet_speed = 2.5
       self.alien_speed = 1.0
       self.fleet_direction = 1 # fleet_direction of 1 represents right; -1 represents left.
       self.alien_points = 50 # Scoring settings

    def increase_speed(self):
       """Increase speed settings and alien point values.."""
       self.ship_speed *= self.speedup_scale
       self.bullet_speed *= self.speedup_scale
       self.alien_speed *= self.speedup_scale
       self.alien_points = int(self.alien_points * self.score_scale)
       
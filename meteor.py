import pygame
from pygame.sprite import Sprite
from img_paths import ASTEROID1_PATH
import random

class Meteor(Sprite):
    """Represents Meteor Obstacles."""

    def __init__(self, game):
        """Initialize meteor and set start position."""

        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.width, self.height = 60, 60

        # load meteor and get_rect
        self.image_load = pygame.image.load(ASTEROID1_PATH)
        self.image = pygame.transform.scale(self.image_load, (self.width, self.height))

        self.rect = self.image.get_rect()

        self.rect.x = self.settings.SCREEN_WIDTH + random.randint(80,120)
        self.rect.y = self.settings.SCREEN_HEIGHT - 100


        # store meteor's position
        self.meteor_x = float(self.rect.x)
        # Calculate x offset for the second meteor
        self.x_offset = 40

        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        """Move meteor along ground."""

        self.meteor_x -= self.settings.meteor_speed
        self.rect.x = self.meteor_x

        if self.meteor_x < -self.width:
            self.meteor_x = self.settings.SCREEN_WIDTH + self.x_offset

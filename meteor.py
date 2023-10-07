import pygame
from pygame.sprite import Sprite
from img_paths import ASTEROID1_PATH

class Meteor(Sprite):
    """Represents Meteor Obstacles."""

    def __init__(self, game):
        """Initialize meteor and set start position."""

        super().__init__()
        self.screen = game.screen
        self.setup = game.settings

        # load meteor and get_rect
        self.image = pygame.image.load(ASTEROID1_PATH)
        self.rect = self.image.get_rect()

        self.rect.x = 800
        self.rect.y = self.setup.SCREEN_HEIGHT - 64

        # store meteor's position
        self.x = float(self.rect.x)

    def update(self):
        """Move meteor along ground."""

        self.x -= self.setup.meteor_speed

        if self.x < -self.setup.SCREEN_WIDTH:
            self.x = 800

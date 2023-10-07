import pygame
from img_paths import DINO_PATH

class Dino:
    """Manages Dino character."""

    def __init__(self, game):
        """Initialize Dino and set start position."""

        self.width, self.height = 170, 118
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # load image and get rect
        self.image_load = pygame.image.load(DINO_PATH)
        self.image = pygame.transform.scale(self.image_load, (self.width, self.height))
        self.rect = self.image.get_rect()

        # start position
        self.x_position, self.y_position = 50, 240

    def blitme(self):
        """Draw dino at location."""
        self.screen.blit(self.image, (self.x_position, self.y_position))

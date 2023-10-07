import pygame
from img_paths import BG_PATH, GROUND_PATH, FONT_PATH
from settings import Settings

class Background:
    """Creates the background."""

    def __init__(self, game):
        """Initialize background elements."""
        self.bg = game.settings

        self.background_img = pygame.image.load(BG_PATH)
        self.ground_img = pygame.image.load(GROUND_PATH)

        self.title_surface = pygame.font.Font(FONT_PATH, 50)

        self.background = pygame.transform.scale(
            self.background_img,
            (self.bg.SCREEN_WIDTH, self.bg.SCREEN_HEIGHT))
        self.ground = pygame.transform.scale(
                    self.ground_img,
                    (self.bg.SCREEN_WIDTH, 64)) # keep the initial height of img
        self.ground_x = 0

        self.title = self.title_surface.render('Dino Run', False, 'Black')

    def update_ground(self):
        """Moves the ground in continuous loop"""
        self.ground_x -= self.bg.ground_speed

        if self.ground_x < -self.bg.SCREEN_WIDTH:
            self.ground_x = 0


    def blitme(self, screen):
        """Draw background to screen."""
        screen.blit(
            self.background,
            (0,0))

        screen.blit(
            self.ground,
            (self.ground_x, self.bg.SCREEN_HEIGHT - 64))
        screen.blit(
            self.ground,
            (self.ground_x + self.bg.SCREEN_WIDTH,
             self.bg.SCREEN_HEIGHT - 64))
        screen.blit(
            self.title,
            (self.bg.SCREEN_WIDTH // 2 - 100, 50))

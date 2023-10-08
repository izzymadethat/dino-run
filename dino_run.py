import pygame
from sys import exit
import os
import random

from settings import Settings
from background import Background
from dino import Dino
from meteor import Meteor

class DinoRun:
    """Overall game assets and behaviors."""


    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.background = Background(self)
        self.screen = pygame.display.set_mode(
            (self.settings.SCREEN_WIDTH, self.settings.SCREEN_HEIGHT))
        pygame.display.set_caption('DINO RUNNER')
        self.dino = Dino(self)
        self.meteors = pygame.sprite.Group()
        self.meteor_timer = random.randint(60, 120)

    def draw_window(self):
        self.screen.fill(self.settings.bg_fill) #reset screen. fills with white

        self.background.blitme(self.screen)
        self.dino.blitme()
        self.meteors.draw(self.screen)

    def create_meteor(self):
        meteor_group_size = random.randint(1,2)
        for _ in range(meteor_group_size):
            meteor = Meteor(self)
            self.meteors.add(meteor)

    def update_screen(self):
        self.draw_window()
        pygame.display.flip()

    def check_events(self, keys_pressed):
        """Respond to key press events"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                exit()

        if keys_pressed[pygame.K_SPACE]:
            self.dino.jump()

    
    def check_for_collision(self):
        pass


    def run(self):
        """Loop for main game."""
        gameplay = True
        while gameplay:
            keys_pressed = pygame.key.get_pressed()
            self.check_events(keys_pressed)
            self.background.update_ground()
            self.dino.update()

            self.meteor_timer -= 1
            if self.meteor_timer <= 0:
                self.create_meteor()
                self.meteor_timer = random.randint(60, 120)

            for meteor in self.meteors:
                meteor.update()
                if meteor.rect.right < 0:
                    self.meteors.remove(meteor)

            self.check_for_collision()
            self.update_screen()

            self.clock.tick(self.settings.FPS) # 60 FPS


        exit()



# # background settings
# background_img = pygame.image.load(BG_PATH)
# ground_img = pygame.image.load(GROUND_PATH)
# BACKGROUND = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
# GROUND = pygame.transform.scale(ground_img, (SCREEN_WIDTH, 64))

# # font settings
# title_surface = pygame.font.Font(FONT_PATH, 50)
# TITLE = title_surface.render('Dino Run', False, 'Green')

# # character/obstacle settings and positions
# DINO_WIDTH, DINO_HEIGHT = 170, 118

# DINO_IMG = pygame.image.load(DINO_PATH)
# DINO = pygame.transform.scale(DINO_IMG, (DINO_WIDTH, DINO_HEIGHT))

# ASTEROID1 = pygame.image.load(ASTEROID1_PATH)




if __name__ == "__main__":
    dino = DinoRun()
    dino.run()

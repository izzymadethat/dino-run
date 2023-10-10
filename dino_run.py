import pygame
from sys import exit
import os
import random

from settings import Settings
from stats import GameStats
from button import Button
from scoreboard import ScoreBoard
from background import Background
from dino import Dino
from meteor import Meteor

class DinoRun:
    """Overall game assets and behaviors."""


    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.SCREEN_WIDTH, self.settings.SCREEN_HEIGHT))
        self.stats = GameStats(self)
        self.sb = ScoreBoard(self)
        self.background = Background(self)
        pygame.display.set_caption('DINO RUNNER')
        self.dino = Dino(self)

        self.meteors = pygame.sprite.Group()
        self.meteor_timer = random.randint(60, 120)
        self.score_timer = 0
        self.game_active = False
        self.play_button = Button(self, "Play Game")

    def draw_window(self):
        self.screen.fill(self.settings.bg_fill) #reset screen. fills with white
        self.background.blitme(self.screen)
        self.sb.show_score()
        self.dino.blitme()
        self.meteors.draw(self.screen)

    def create_meteor(self):
        meteor_group_size = random.randint(1,2)
        for _ in range(meteor_group_size):
            meteor = Meteor(self)
            self.meteors.add(meteor)

    def update_meteors(self):
        self.meteor_timer -= 1
        self.score_timer += 1
        if self.meteor_timer <= 0:
            self.create_meteor()
            self.meteor_timer = random.randint(60, 120)

        for meteor in self.meteors:
            meteor.update()
            if meteor.rect.right < 0:
                self.meteors.remove(meteor)

    def update_screen(self):
        self.draw_window()

        if not self.game_active:
                self.play_button.draw_button()

        pygame.display.flip()

    def check_events(self, keys_pressed):
        """Respond to key press events"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_play_button(mouse_pos)

        if keys_pressed[pygame.K_SPACE]:
            if not self.game_active: # the spacebar starts the game
                self.reset_game()
                self.game_active = True
            else: # or the spacebar makes the dino jump
                self.dino.jump()

    def check_play_button(self, mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos):
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.game_active = True


    def check_for_collision(self):
        for meteor in self.meteors:
            dino_mask = self.dino.mask
            meteor_mask = meteor.mask

            offset = (meteor.meteor_x - self.dino.x, meteor.rect.y - self.dino.y)

            if dino_mask.overlap(meteor_mask, offset):
                self.meteors.empty()
                self.game_active = False
                return True

        return False

    def check_score(self):
        if not self.check_for_collision():
            self.stats.score += self.settings.run_score
            self.sb.prep_score()
            self.sb.check_high_score()

    def reset_game(self):
        self.settings.initialize_dynamic_settings()
        self.stats.reset_stats()


    def increase_speeds(self):
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.start_time  # start_time should be a timestamp when the game started

        if elapsed_time >= 15000:  # 15000 milliseconds (15 seconds)
            self.settings.increase_speed()
            self.start_time = current_time

    def run(self):
        """Loop for main game."""
        gameplay = True
        self.start_time = pygame.time.get_ticks()

        while gameplay:
            keys_pressed = pygame.key.get_pressed()
            self.check_events(keys_pressed)

            self.background.update_ground()
            self.dino.update()

            if self.game_active:
                self.update_meteors()
                self.increase_speeds()
                self.check_score()
                collision = self.check_for_collision()
                if collision:
                    self.reset_game()
                    self.game_active = False

            elif not self.game_active:
                self.play_button.draw_button()


            self.update_screen()
            self.clock.tick(self.settings.FPS) # 60 FPS

        exit()

if __name__ == "__main__":
    dino = DinoRun()
    dino.run()

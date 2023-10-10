import pygame.font

class ScoreBoard:

    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats

        # font settings for score
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        rounded_score = round(self.stats.score, -1)
        score = f"{rounded_score:,}"
        self.score_img = self.font.render(score, True,
                                          self.text_color)
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right -20
        self.score_rect.top = 20

    def prep_high_score(self):
        high_score = round(self.stats.high_score, -1)
        score_str = f"{high_score:,}"
        self.high_score_img = self.font.render(score_str, True,
                                          self.text_color)
        self.high_score_rect = self.high_score_img.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

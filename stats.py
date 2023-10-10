class GameStats:
    def __init__(self, game):
        """Initialize Statistics."""

        self.settings = game.settings
        self.reset_stats()
        self.high_score = 0
        self.score = 0

    def reset_stats(self):
        self.jump_height = self.settings.jump_height
        self.jump_gravity = self.settings.jump_gravity
        self.ground_speed = self.settings.ground_speed
        self.meteor_speed = self.settings.meteor_speed
        self.score = 0

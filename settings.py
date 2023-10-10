import img_paths

class Settings:
    """Stores all Dino Run Settings"""

    def __init__(self):
        """Initialize game settings."""

        # Screen and Frame Rate settings
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 800, 400
        self.FPS = 60
        self.bg_fill = (255, 255, 255)



        # increase by scales
        self.increase_scale = 1.2
        self.score_increase_scale = 1.5



        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):

        # background speed
        self.ground_speed = 6

        # dino jump settings
        self.jump_height = 23
        self.jump_gravity = 1.2

        # meteor settings
        self.meteor_speed = 6.0

        self.run_score = 1
        self.meteor_jump_score = 5


    def increase_speed(self):
        """Increase all speed settings"""
        self.ground_speed *= self.increase_scale
        self.jump_height *= self.increase_scale
        self.jump_gravity *= self.increase_scale
        self.meteor_speed *= self.increase_scale

        self.run_score = int(self.run_score * self.increase_scale)
        # self.meteor_jump_score = int(self.meteor_jump_score * self.score_increase_scale)

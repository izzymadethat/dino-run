import img_paths

class Settings:
    """Stores all Dino Run Settings"""

    def __init__(self):
        """Initialize game settings."""

        # Screen and Frame Rate settings
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 800, 400
        self.FPS = 60
        self.bg_fill = (255, 255, 255)

        # background speed
        self.ground_speed = 6

        # dino jump settings
        self.jump_height = 20
        self.jump_gravity = 2

        # meteor settings
        self.meteor_speed = 6.0

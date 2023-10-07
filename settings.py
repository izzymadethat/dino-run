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
        self.ground_speed = 5

        # meteor settings
        self.meteor_speed = 1.0

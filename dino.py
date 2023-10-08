import pygame
from img_paths import DINO_PATH
from os import listdir
from os.path import isfile, join

class Dino(pygame.sprite.Sprite):
    """Manages Dino character."""

    def load_sprite_images(self, dir1, dir2, width, height):
        path = join("assets", dir1, dir2)
        images = [f for f in listdir(path) if isfile(join(path, f))]

        all_sprites = {}

        for image in images:
            sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()
            sprites = []

            for i in range(sprite_sheet.get_width() // width):
                rect = pygame.Rect(i * width, 0, width, height)
                sprite = sprite_sheet.subsurface(rect)
                sprites.append(pygame.transform.scale(sprite, (self.width, self.height)))

            all_sprites[image.replace(".png", "")] = sprites

        return all_sprites

    def __init__(self, game):
        """Initialize Dino and set start position."""
        self.width, self.height = 170, 118
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings
        self.x, self.y = 50, 240
        self.animation_delay = 5
        self.animation_count = 0

        self.running_sprites = self.load_sprite_images("dino", "running", 680, 472)
        self.jumping_sprites = self.load_sprite_images("dino", "jumping", 680, 472)
    
        self.y_vel = 0

        # dino abilities
        self.is_jumping = False
        self.state = "running"
        self.spacebar_pressed = False
        self.jump_height = 23  # Adjust this value to control jump height
        self.gravity = 1.2

    def blitme(self):
        """Draw dino at location."""
        self.screen.blit(self.sprite, (self.x, self.y))

    def check_collision(self):
        pass

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.y_vel = -self.jump_height # Initial jump velocity
            self.state = "jumping"

    def update(self):
        if self.is_jumping:
            self.y_vel += self.gravity  # Apply gravity
            self.y += self.y_vel

            if self.y >= 240:  # Check if the character is on the ground
                self.y = 240
                self.is_jumping = False
                self.y_vel = 0  # Reset the velocity
                self.state = "running"

        self.animate_movement()

    def animate_movement(self):
        frames_per_second = 12

        if self.state == "jumping":
            sprite_sheet_name = "Jump (6)"
            sprites = self.jumping_sprites[sprite_sheet_name]
            self.sprite = sprites[0]

        else:
            sprite_sheet = "Run"
            sprite_index = (self.animation_count // (60 // frames_per_second)) % 8  # Assumes 60 FPS
            sprite_sheet_name = f"{sprite_sheet} ({sprite_index + 1})"
            sprites = self.running_sprites[sprite_sheet_name]
            self.sprite = sprites[0]  # Use frame_index to select the appropriate sprite
            
        self.animation_count += 1
                


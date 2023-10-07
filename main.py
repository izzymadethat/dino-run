import pygame
import os
from sys import exit

pygame.init()

CLOCK = pygame.time.Clock()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 500
WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Run, Jump (My First Game)")



WHITE = (255, 255, 255)
FPS = 60
VEL = 5
Y_GRAVITY = 5
JUMP_HEIGHT = 20
X_POSITION = 100
Y_POSITION = 300
Y_VELOCITY = JUMP_HEIGHT
is_jumping = False

CHARACTER_WIDTH, CHARACTER_HEIGHT = 170, 118
CHARACTER_IDLE = pygame.image.load(os.path.join('assets\dino', 'Idle (1).png'))
CHARACTER_JUMPING = pygame.image.load(os.path.join('assets\dino', 'Jump (5).png'))
CHARACTER = pygame.transform.scale(CHARACTER_IDLE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))

def draw_window(character):
    WINDOW.fill(WHITE)
    WINDOW.blit(CHARACTER, (character.x, character.y))
    pygame.display.update()

def check_character_movement(keys_pressed, character):
    if keys_pressed[pygame.K_a] and character.x - VEL > 0:
        character.x -= VEL
    elif keys_pressed[pygame.K_d] and character.x + VEL + character.width < SCREEN_WIDTH + 50:
        character.x += VEL

def check_for_jumps(keys_pressed, character):
    global is_jumping, Y_POSITION, Y_VELOCITY, CHARACTER

    if keys_pressed[pygame.K_SPACE]:
        is_jumping = True

    if is_jumping:
        Y_POSITION -= Y_VELOCITY
        Y_VELOCITY -= Y_GRAVITY
        if Y_VELOCITY < -JUMP_HEIGHT:
            is_jumping = False
            Y_POSITION = 300
            Y_VELOCITY = JUMP_HEIGHT
        CHARACTER = pygame.transform.scale(CHARACTER_JUMPING, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
    else:
        CHARACTER = pygame.transform.scale(CHARACTER_IDLE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))



def main():
    character = pygame.Rect(X_POSITION, Y_POSITION, CHARACTER_WIDTH, CHARACTER_HEIGHT)

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        check_character_movement(keys_pressed, character)
        check_for_jumps(keys_pressed, character)
        draw_window(character)

        CLOCK.tick(FPS)

    exit()


if __name__ == "__main__":
    main()

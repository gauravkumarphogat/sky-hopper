import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# Game variables
bird_y = HEIGHT // 2
bird_x = 50
gravity = 0.5
bird_movement = 0
pipe_speed = 5
pipe_width = 50
pipe_gap = 150
pipes = []

# Function to create new pipes
def create_pipe():
    height = random.randint(100, 400)
    pipe_top = pygame.Rect(WIDTH, height - pipe_gap - HEIGHT, pipe_width, HEIGHT)
    pipe_bottom = pygame.Rect(WIDTH, height, pipe_width, HEIGHT)
    return pipe_top, pipe_bottom

# Function to move pipes
def move_pipes(pipes):
    for pipe in pipes:
        pipe.x -= pipe_speed
    return pipes

# Function to draw pipes
def draw_pipes(pipes):
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, pipe)

# Function to check for collisions
def check_collision(pipes):
    for pipe in pipes:
        if bird_y < 0 or bird_y > HEIGHT - 30:
            return True
        if pygame.Rect(bird_x, bird_y, 30, 30).colliderect(pipe):
            return True
    return False

# Main game loop
def game_loop():
    global bird_y, bird_movement, pipes

    # Add initial pipes
    pipes.extend(create_pipe())

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_movement = -10  # Negative movement to make the bird go up

        bird_movement += gravity
        bird_y += bird_movement

        # Move and draw pipes
        pipes = move_pipes(pipes)

        # Add new pipe when the last one reaches the middle of the screen
        if pipes[-1].x < WIDTH // 2:
            pipes.extend(create_pipe())  # Add both top and bottom pipes

        # Remove pipes that have gone off the screen
        if pipes[0].x < -pipe_width:
            pipes.pop(0)  # Remove the oldest pipe

        # Fill the screen with color
        screen.fill(WHITE)

        # Draw the bird
        pygame.draw.rect(screen, YELLOW, (bird_x, bird_y, 30, 30))

        # Draw pipes
        draw_pipes(pipes)

        # Check for collisions
        if check_collision(pipes):
            break  # End the game if a collision is detected

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(30)

if __name__ == "__main__":
    game_loop()

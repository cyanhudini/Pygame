import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define the screen size
WIDTH = 1280
HEIGHT = 720
# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")

# Function to draw the game board with walls
def draw_board():
    # Fill the screen with black
    screen.fill(BLACK)

    # Draw the top and bottom walls
    pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, 5))
    pygame.draw.rect(screen, WHITE, (0, HEIGHT - 5, WIDTH, 5))

    # Draw the left and right walls
    pygame.draw.rect(screen, WHITE, (0, 0, 5, HEIGHT))
    pygame.draw.rect(screen, WHITE, (WIDTH - 5, 0, 5, HEIGHT))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the game board
    draw_board()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
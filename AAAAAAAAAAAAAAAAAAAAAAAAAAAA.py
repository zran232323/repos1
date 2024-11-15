import pygame
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Breakable Window Simulation")

# Load images
glass_image = pygame.image.load('glass.png')  # Replace with the path to your glass image
crack_image = pygame.image.load('crack.png')  # Replace with the path to your crack image

# Resize images to fit the screen
glass_image = pygame.transform.scale(glass_image, (screen_width, screen_height))
crack_image = pygame.transform.scale(crack_image, (screen_width, screen_height))

# Variables to track the state of the window
window_broken = False
crack_positions = []

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not window_broken:
                window_broken = True
                crack_positions.append(event.pos)

    # Draw the window
    screen.blit(glass_image, (0, 0))

    # Draw cracks if the window is broken
    if window_broken:
        for pos in crack_positions:
            screen.blit(crack_image, pos)

    pygame.display.flip()

# Quit Pygame
pygame.quit()

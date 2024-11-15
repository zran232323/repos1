import pygame
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the clock
clock = pygame.time.Clock()

# Set up the player
player_x, player_y = WIDTH / 2, HEIGHT / 2
player_speed = 5

# Set up the bacteria
bacteria = []
for _ in range(10):
    bacteria_x, bacteria_y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
    bacteria.append((bacteria_x, bacteria_y))

# Set up the AI bacteriophages
ai_bacteriophages = []

# Game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                # Infect bacteria
                for bacteria_x, bacteria_y in bacteria:
                    if abs(player_x - bacteria_x) < 10 and abs(player_y - bacteria_y) < 10:
                        # Release AI bacteriophages
                        for _ in range(5):
                            ai_bacteriophage_x, ai_bacteriophage_y = bacteria_x, bacteria_y
                            ai_bacteriophages.append((ai_bacteriophage_x, ai_bacteriophage_y))

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_y -= player_speed
    if keys[pygame.K_s]:
        player_y += player_speed
    if keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_d]:
        player_x += player_speed

    # Move AI bacteriophages
    for i, (ai_bacteriophage_x, ai_bacteriophage_y) in enumerate(ai_bacteriophages):
        ai_bacteriophage_x += random.randint(-5, 5)
        ai_bacteriophage_y += random.randint(-5, 5)
        ai_bacteriophages[i] = (ai_bacteriophage_x, ai_bacteriophage_y)

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (int(player_x), int(player_y)), 10)
    for bacteria_x, bacteria_y in bacteria:
        pygame.draw.circle(screen, GREEN, (int(bacteria_x), int(bacteria_y)), 10)
    for ai_bacteriophage_x, ai_bacteriophage_y in ai_bacteriophages:
        pygame.draw.circle(screen, RED, (int(ai_bacteriophage_x), int(ai_bacteriophage_y)), 5)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
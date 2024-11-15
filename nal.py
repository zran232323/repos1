import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
GLITCH_COUNT = 20

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GLITCH_COLORS = [(255, 0, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Glitchy Colorful Game")

# Create glitch entities
glitches = []
for _ in range(GLITCH_COUNT):
    x, y = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
    color = random.choice(GLITCH_COLORS)
    glitches.append((x, y, color))

# Main game loop
clock = pygame.time.Clock()
score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move glitches randomly
    for i in range(GLITCH_COUNT):
        glitches[i] = (glitches[i][0] + random.randint(-2, 2),
                       glitches[i][1] + random.randint(-2, 2),
                       glitches[i][2])

    # Check for collision with mouse click
    if pygame.mouse.get_pressed()[0]:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for i in range(GLITCH_COUNT):
            x, y, color = glitches[i]
            if pygame.Rect(x - 10, y - 10, 20, 20).collidepoint(mouse_x, mouse_y):
                if color == GREEN:
                    glitches[i] = (-100, -100, random.choice(GLITCH_COLORS))
                else:
                    glitches[i] = (-100, -100, GREEN)
                score += 1

    # Draw glitches
    screen.fill(WHITE)
    for x, y, color in glitches:
        pygame.draw.circle(screen, color, (x, y), 10)

    pygame.display.flip()
    clock.tick(FPS)




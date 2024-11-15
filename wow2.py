import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
GRAVITY_CONSTANT = 0.1

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rogue Planet Defense")

# Planet class
class Planet:
    def __init__(self, x, y, mass):
        self.x = x
        self.y = y
        self.mass = mass

    def apply_gravity(self, other_planet):
        dx = other_planet.x - self.x
        dy = other_planet.y - self.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        force = GRAVITY_CONSTANT * (self.mass * other_planet.mass) / distance ** 2
        angle = math.atan2(dy, dx)
        acceleration_x = force * math.cos(angle) / self.mass
        acceleration_y = force * math.sin(angle) / self.mass
        return acceleration_x, acceleration_y

# Create planets
player_planet = Planet(WIDTH // 4, HEIGHT // 2, 100)
rogue_planet = Planet(3 * WIDTH // 4, HEIGHT // 2, 200)

# Main game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Calculate gravitational forces
    acceleration_x, acceleration_y = player_planet.apply_gravity(rogue_planet)
    player_planet.x += acceleration_x
    player_planet.y += acceleration_y

    # Draw planets
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLUE, (int(player_planet.x), int(player_planet.y)), 20)
    pygame.draw.circle(screen, BLUE, (int(rogue_planet.x), int(rogue_planet.y)), 30)

    pygame.display.flip()
    clock.tick(FPS)

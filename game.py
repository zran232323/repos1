       





import pygame
import math
import random

# Initialize pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define the elements
elements = {
    1: {'name': 'Earth', 'color': (128, 64, 0), 'density': 1.0, 'gravity': 1.0},
    2: {'name': 'Water', 'color': (0, 0, 255), 'density': 0.5, 'gravity': 0.5},
    3: {'name': 'Lava', 'color': (255, 128, 0), 'density': 2.0, 'gravity': 2.0},
    4: {'name': 'Ice', 'color': (0, 255, 255), 'density': 0.2, 'gravity': 0.2},
    5: {'name': 'Vapor', 'color': (255, 255, 255), 'density': 0.01, 'gravity': 0.01},
    6: {'name': 'Stone', 'color': (128, 128, 128), 'density': 3.0, 'gravity': 3.0},
    7: {'name': 'Plant', 'color': (0, 128, 0), 'density': 0.5, 'gravity': 0.5},
    8: {'name': 'Oil', 'color': (128, 128, 0), 'density': 0.8, 'gravity': 0.8},
    9: {'name': 'Smoke', 'color': (128, 128, 128), 'density': 0.01, 'gravity': 0.01},
    10: {'name': 'Metal', 'color': (192, 192, 192), 'density': 4.0, 'gravity': 4.0},
    11: {'name': 'Sand', 'color': (255, 192, 128), 'density': 1.5, 'gravity': 1.5},
    12: {'name': 'Hydrogen', 'color': (255, 255, 255), 'density': 0.01, 'gravity': 0.01}
}

# Define the Particle class
class Particle:
    def __init__(self, x, y, element, velocity_x, velocity_y):
        self.x = x
        self.y = y
        self.element = element
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

    def update(self):
        # Update the position based on velocity
        self.x += self.velocity_x
        self.y += self.velocity_y

        # Apply gravity
        self.velocity_y += elements[self.element]['gravity']

    def draw(self, screen):
        pygame.draw.circle(screen, elements[self.element]['color'], (int(self.x), int(self.y)), 2)

# Define the collision function
def collide(p1, p2):
    # Check if the particles are close enough to collide
    if math.hypot(p1.x - p2.x, p1.y - p2.y) < 4:
        # Calculate the relative velocity
        rel_velocity_x = p1.velocity_x - p2.velocity_x
        rel_velocity_y = p1.velocity_y - p2.velocity_y

        # Check if the collision is fast enough to spew out lava
        if math.hypot(rel_velocity_x, rel_velocity_y) > 5:
            return 3  # Lava
        else:
            return None

# Create a list to store the particles
particles = []

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Add new particles randomly
    if random.random() < 0.1:
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        element = random.choice(list(elements.keys()))
        velocity_x = random.uniform(-1, 1)
        velocity_y = random.uniform(-1, 1)
        particles.append(Particle(x, y, element, velocity_x, velocity_y))

    # Update and draw the particles
    screen.fill(BLACK)
    for particle in particles:
        particle.update()
        particle.draw(screen)
        for other_particle in particles:
            if particle!= other_particle:
                collision_element = collide(particle, other_particle)
                if collision_element is not None:
                    # Create a new lava particle at the collision point
                    lava_particle = Particle((particle.x + other_particle.x) / 2, (particle.y + other_particle.y) / 2, collision_element, 0, 0)
                    particles.append(lava_particle)

    # Update the screen
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
import pygame
import numpy as np
import math

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
NUM_POINTS = 10
SPRING_STRENGTH = 0.01
DAMPING = 0.95
CELL_RADIUS = 100
BRAIN_RADIUS = 40

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Softbody Cell Infection")

clock = pygame.time.Clock()

# Softbody Cell Class
class SoftbodyCell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.points = np.zeros((NUM_POINTS, 2))
        self.velocities = np.zeros((NUM_POINTS, 2))

        angle_step = 2 * np.pi / NUM_POINTS
        for i in range(NUM_POINTS):
            angle = i * angle_step
            self.points[i] = [x + np.cos(angle) * CELL_RADIUS, y + np.sin(angle) * CELL_RADIUS]

    def update(self):
        center = np.mean(self.points, axis=0)
        forces = np.zeros_like(self.points)

        for i in range(NUM_POINTS):
            # Spring force towards the original circular position
            angle = 2 * np.pi * i / NUM_POINTS
            target = np.array([self.x + np.cos(angle) * CELL_RADIUS, self.y + np.sin(angle) * CELL_RADIUS])
            displacement = target - self.points[i]
            forces[i] += SPRING_STRENGTH * displacement

        # Apply forces and update velocities
        self.velocities += forces
        self.velocities *= DAMPING
        self.points += self.velocities

    def draw(self):
        for i in range(NUM_POINTS):
            next_i = (i + 1) % NUM_POINTS
            pygame.draw.line(screen, BLUE, self.points[i], self.points[next_i], 2)

# Brain Class
class Brain:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), BRAIN_RADIUS)

    def check_collision(self, cell):
        center = np.mean(cell.points, axis=0)
        distance = np.linalg.norm(center - np.array([self.x, self.y]))
        return distance < CELL_RADIUS + BRAIN_RADIUS

# AI Control Function
def ai_control(cell, brain):
    center = np.mean(cell.points, axis=0)
    angle_to_brain = np.arctan2(brain.y - center[1], brain.x - center[0])
    direction = np.array([np.cos(angle_to_brain), np.sin(angle_to_brain)])
    cell.x += direction[0]
    cell.y += direction[1]

# Main game loop
def main():
    run = True
    cell = SoftbodyCell(WIDTH // 4, HEIGHT // 2)
    brain = Brain(WIDTH - 100, HEIGHT // 2)

    while run:
        clock.tick(FPS)
        screen.fill(WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # AI control
        ai_control(cell, brain)

        # Update cell
        cell.update()

        # Check collision with brain
        if brain.check_collision(cell):
            print("Brain infected!")
            run = False

        # Draw everything
        cell.draw()
        brain.draw()

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()

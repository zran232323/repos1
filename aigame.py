import pygame
import random
import numpy as np

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Ragdoll class representing the ragdoll with limbs and AI
class Ragdoll:
    def __init__(self):
        self.position = np.array([SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2])
        self.velocity = np.array([0, 0])
        self.angle = 0
        self.learning_rate = 0.1
        self.q_table = {}  # Q-table for reinforcement learning
        self.state = None

    def update(self):
        """Update the position of the ragdoll based on its velocity."""
        self.position += self.velocity
        self.position = np.clip(self.position, [0, 0], [SCREEN_WIDTH, SCREEN_HEIGHT])

    def act(self):
        """Choose an action based on the current state using epsilon-greedy strategy."""
        if random.random() < 0.1:  # Exploration
            return random.choice(['left', 'right', 'jump'])
        else:  # Exploitation
            return self.best_action()

    def best_action(self):
        """Return the best action based on the Q-table."""
        state_key = str(self.state)
        if state_key not in self.q_table:
            self.q_table[state_key] = np.zeros(3)  # 3 actions
        return np.argmax(self.q_table[state_key])

    def learn(self, action, reward):
        """Update the Q-table based on the action taken and the reward received."""
        state_key = str(self.state)
        if state_key not in self.q_table:
            self.q_table[state_key] = np.zeros(3)  # 3 actions
        action_index = ['left', 'right', 'jump'].index(action)
        self.q_table[state_key][action_index] += self.learning_rate * (reward - self.q_table[state_key][action_index])

    def reset(self):
        """Reset the ragdoll's position and velocity."""
        self.position = np.array([SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2])
        self.velocity = np.array([0, 0])

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ragdoll Simulation")
clock = pygame.time.Clock()

# Create a ragdoll instance
ragdoll = Ragdoll()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update ragdoll state
    ragdoll.update()
    
    # Choose action and update velocity
    action = ragdoll.act()
    if action == 'left':
        ragdoll.velocity[0] = -5
    elif action == 'right':
        ragdoll.velocity[0] = 5
    elif action == 'jump':
        ragdoll.velocity[1] = -10  # Jump upwards

    # Simple reward system
    reward = -1  # Default penalty for each step
    if ragdoll.position[1] >= SCREEN_HEIGHT - 50:  # If on the ground
        reward = 10  # Reward for being on the ground

    # Learn from the action taken
    ragdoll.learn(action, reward)

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the ragdoll as a rectangle
    pygame.draw.rect(screen, (0, 0, 255), (*ragdoll.position, 50, 100))  # Body
    pygame.draw.rect(screen, (0, 255, 0), (ragdoll.position[0] - 25, ragdoll.position[1], 25, 50))  # Left leg
    pygame.draw.rect(screen, (0, 255, 0), (ragdoll.position[0] + 25, ragdoll.position[1], 25, 50))  # Right leg
    pygame.draw.rect(screen, (255, 0, 0), (ragdoll.position[0] - 50, ragdoll.position[1] + 25, 25, 50))  # Left arm
    pygame.draw.rect(screen, (255, 0, 0), (ragdoll.position[0] + 50, ragdoll.position[1] + 25, 25, 50))  # Right arm

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()





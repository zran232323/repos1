import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Nuclear Reactor Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Font
font = pygame.font.Font(None, 36)

# Game variables
coolant_level = 100
pressure = 50
temperature = 20
reactor_started = False
console_open = False

# Button dimensions
button_width, button_height = 200, 50
button_x, button_y = WIDTH // 2 - button_width // 2, HEIGHT // 2 - button_height // 2

# Main game loop
def main():
    global coolant_level, pressure, temperature, reactor_started, console_open
    clock = pygame.time.Clock()

    while True:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                    console_open = not console_open

        # Update game logic
        if reactor_started:
            temperature += 0.1
            pressure += 0.05
            coolant_level -= 0.05

            if coolant_level < 0:
                coolant_level = 0
            if pressure > 100:
                pressure = 100

        # Draw elements
        draw_button()
        draw_console()
        draw_status()

        pygame.display.flip()
        clock.tick(60)

def draw_button():
    """Draw the button to open/close the console."""
    button_color = GREEN if not console_open else RED
    pygame.draw.rect(screen, button_color, (button_x, button_y, button_width, button_height))
    button_text = font.render("Enter Console" if not console_open else "Close Console", True, BLACK)
    screen.blit(button_text, (button_x + 10, button_y + 10))

def draw_console():
    """Draw the console if it is open."""
    if console_open:
        pygame.draw.rect(screen, BLACK, (50, 50, WIDTH - 100, HEIGHT - 100))
        console_text = font.render("Console: Press 'S' to Start Reactor", True, WHITE)
        screen.blit(console_text, (60, 60))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            global reactor_started
            reactor_started = True

def draw_status():
    """Draw the reactor status on the screen."""
    coolant_text = font.render(f"Coolant Level: {coolant_level:.2f}", True, BLUE)
    pressure_text = font.render(f"Pressure: {pressure:.2f}", True, BLUE)
    temperature_text = font.render(f"Temperature: {temperature:.2f}", True, BLUE)

    screen.blit(coolant_text, (50, HEIGHT - 100))
    screen.blit(pressure_text, (50, HEIGHT - 70))
    screen.blit(temperature_text, (50, HEIGHT - 40))

if __name__ == "__main__":
    main()


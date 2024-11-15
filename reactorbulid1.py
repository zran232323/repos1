import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nuclear Reactor Simulator")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Fonts
font = pygame.font.Font(None, 36)

# Game variables
reactor_on = False
coolant_level = 100
pressure = 0
temperature = 20
max_temperature = 1000
meltdown_temperature = 800

class Button:
    """A class to represent clickable buttons"""
    def __init__(self, x, y, width, height, text, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color

    def draw(self, surface):
        """Draw the button on the given surface"""
        pygame.draw.rect(surface, self.color, self.rect)
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        """Check if the button is clicked"""
        return self.rect.collidepoint(pos)

# Create buttons
console_button = Button(50, 50, 200, 50, "Enter Console", GREEN)
start_button = Button(300, 400, 200, 50, "Start Reactor", GREEN)
stop_button = Button(300, 460, 200, 50, "Stop Reactor", RED)

def draw_reactor_status():
    """Draw the reactor status on the screen"""
    status_text = f"Reactor: {'ON' if reactor_on else 'OFF'}"
    status_surface = font.render(status_text, True, WHITE)
    screen.blit(status_surface, (50, 150))

    coolant_text = f"Coolant: {coolant_level:.1f}%"
    coolant_surface = font.render(coolant_text, True, WHITE)
    screen.blit(coolant_surface, (50, 200))

    pressure_text = f"Pressure: {pressure:.1f} MPa"
    pressure_surface = font.render(pressure_text, True, WHITE)
    screen.blit(pressure_surface, (50, 250))

    temp_text = f"Temperature: {temperature:.1f}°C"
    temp_surface = font.render(temp_text, True, WHITE)
    screen.blit(temp_surface, (50, 300))

def update_reactor():
    """Update reactor parameters"""
    global coolant_level, pressure, temperature

    if reactor_on:
        temperature += random.uniform(0.1, 0.5)
        pressure += random.uniform(0.01, 0.05)
        coolant_level -= random.uniform(0.1, 0.3)

        if coolant_level < 0:
            coolant_level = 0

        if temperature > max_temperature:
            temperature = max_temperature

        if coolant_level > 0:
            temperature -= random.uniform(0, 0.2)
            pressure -= random.uniform(0, 0.02)

    else:
        temperature = max(20, temperature - 0.5)
        pressure = max(0, pressure - 0.1)
        coolant_level = min(100, coolant_level + 0.2)

def check_meltdown():
    """Check if a meltdown occurs"""
    global reactor_on
    if temperature >= meltdown_temperature:
        reactor_on = False
        return True
    return False

def main():
    """Main game loop"""
    global reactor_on, coolant_level, pressure, temperature

    clock = pygame.time.Clock()
    console_mode = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if console_button.is_clicked(event.pos):
                    console_mode = not console_mode
                elif start_button.is_clicked(event.pos) and not reactor_on:
                    reactor_on = True
                elif stop_button.is_clicked(event.pos) and reactor_on:
                    reactor_on = False

        screen.fill(BLACK)

        if not console_mode:
            console_button.draw(screen)
            draw_reactor_status()
        else:
            # Console mode
            if reactor_on:
                start_button.draw(screen)
            else:
                stop_button.draw(screen)

            # Add coolant button
            add_coolant_button = Button(300, 520, 200, 50, "Add Coolant", BLUE)
            add_coolant_button.draw(screen)

            if add_coolant_button.is_clicked(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                coolant_level = min(100, coolant_level + 5)

        update_reactor()

        if check_meltdown():
            meltdown_text = "MELTDOWN! Game Over!"
            meltdown_surface = font.render(meltdown_text, True, RED)
            screen.blit(meltdown_surface, (WIDTH // 2 - 100, HEIGHT // 2))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
11

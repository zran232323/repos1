import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Boss Fight")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

# Boss settings
boss_size = 60
boss_pos = [screen_width // 2 - boss_size // 2, 50]
boss_color = red
boss_health = 100
boss_speed = 2
boss_shoot_delay = 30
boss_shoot_timer = boss_shoot_delay
boss_attacks = []

# Player settings
player_pos = [screen_width // 2, screen_height - 50]
player_size = 30
player_color = white
player_health = 100
player_speed = 5

# Bullet settings
bullets = []
bullet_size = (5, 10)
bullet_color = red
bullet_speed = 10

# Boss attack settings
attack_size = 20
attack_colors = [blue, green, red]
attack_speed = 5

# CMD prompt windows
cmd_windows = []
cmd_window_size = 20

# Glitch effect
def draw_glitch_effect(screen):
    for _ in range(50):
        x, y = random.randint(0, screen_width), random.randint(0, screen_height)
        width, height = random.randint(10, 100), random.randint(10, 100)
        color = random.choice([red, white])
        pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height))

# Health bar function
def draw_health_bar(screen, x, y, health, max_health, color):
    ratio = health / max_health
    pygame.draw.rect(screen, red, (x, y, 100, 10))
    pygame.draw.rect(screen, color, (x, y, 100 * ratio, 10))

# Function to create a new attack
def create_attack():
    attack_type = random.choice(['energy_ball', 'minion', 'tackle', 'laser'])
    x = random.randint(0, screen_width - attack_size)
    y = -attack_size
    return {'type': attack_type, 'pos': [x, y], 'color': random.choice(attack_colors)}

# Function to create a new boss attack
def create_boss_attack():
    x = boss_pos[0] + boss_size // 2 - attack_size // 2
    y = boss_pos[1] + boss_size
    return {'type': 'energy_ball', 'pos': [x, y], 'color': red}

# Main game loop
clock = pygame.time.Clock()
running = True
final_phase = False
boss_sliding = False
attack_delay = 0
attacks = []
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and final_phase:
                mouse_pos = pygame.mouse.get_pos()
                cmd_windows.append([mouse_pos[0], mouse_pos[1], cmd_window_size])
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not final_phase:
                # Shoot a bullet
                mouse_pos = pygame.mouse.get_pos()
                bullets.append([player_pos[0] + player_size // 2 - bullet_size[0] // 2, player_pos[1] - bullet_size[1]])

    # Update game logic
    if not final_phase:
        # Boss movement and shooting AI
        boss_pos[0] += boss_speed
        if boss_pos[0] <= 0 or boss_pos[0] >= screen_width - boss_size:
            boss_speed = -boss_speed

        # Boss shooting
        boss_shoot_timer -= 1
        if boss_shoot_timer <= 0:
            boss_attacks.append(create_boss_attack())
            boss_shoot_timer = boss_shoot_delay

        # Move boss attacks
        boss_attacks = [{'type': a['type'], 'pos': [a['pos'][0], a['pos'][1] + attack_speed], 'color': a['color']} for a in boss_attacks if a['pos'][1] < screen_height]

        # Check collision with player
        for attack in boss_attacks:
            if pygame.Rect(player_pos[0], player_pos[1], player_size, player_size).colliderect(pygame.Rect(attack['pos'][0], attack['pos'][1], attack_size, attack_size)):
                player_health -= 10
                boss_attacks.remove(attack)
                if player_health <= 0:
                    running = False

        # Move bullets
        bullets = [[b[0], b[1] - bullet_speed] for b in bullets if b[1] > 0]

        # Check collisions with the boss
        for bullet in bullets:
            if boss_pos[0] < bullet[0] < boss_pos[0] + boss_size and boss_pos[1] < bullet[1] < boss_pos[1] + boss_size:
                bullets.remove(bullet)
                boss_health -= 10

        # Transition to final phase if boss health is depleted
        if boss_health <= 0:
            final_phase = True
            pygame.time.delay(2000)
            boss_pos = [screen_width // 2 - boss_size // 2, -boss_size]
            boss_sliding = True

    if final_phase:
        if boss_sliding:
            # Boss slides down into view
            boss_pos[1] += 5
            if boss_pos[1] >= screen_height // 2 - boss_size // 2:
                boss_sliding = False

            # Create attacks periodically
            if attack_delay <= 0:
                attacks.append(create_attack())
                attack_delay = 30
            else:
                attack_delay -= 1

            # Move and check attacks
            for attack in attacks:
                attack['pos'][1] += attack_speed
                if attack['pos'][1] > screen_height:
                    attacks.remove(attack)
                # Check collision with CMD windows
                for cmd_window in cmd_windows:
                    if pygame.Rect(cmd_window[0], cmd_window[1], cmd_window_size, cmd_window_size).colliderect(
                            pygame.Rect(attack['pos'][0], attack['pos'][1], attack_size, attack_size)):
                        cmd_windows.remove(cmd_window)
                        attacks.remove(attack)
                        # Handle reconstruction with a hammer tool
                        # (Placeholder for hammer tool functionality)
                        break

            # Move bullets
            bullets = [[b[0], b[1] - bullet_speed] for b in bullets if b[1] > 0]

            # Check collisions with the boss
            for bullet in bullets:
                if boss_pos[0] < bullet[0] < boss_pos[0] + boss_size and boss_pos[1] < bullet[1] < boss_pos[1] + boss_size:
                    bullets.remove(bullet)
                    boss_health -= 10

            # Simulate boss attacks on player
            if random.randint(1, 100) < 5:
                player_health -= 5
                if player_health <= 0:
                    running = False

    # Move player with mouse
    mouse_x, mouse_y = pygame.mouse.get_pos()
    player_pos[0] = mouse_x - player_size // 2
    player_pos[1] = screen_height - player_size - 10

    # Drawing
    screen.fill(black)

    if not final_phase:
        pygame.draw.rect(screen, boss_color, pygame.Rect(boss_pos[0], boss_pos[1], boss_size, boss_size))
        pygame.draw.rect(screen, player_color, pygame.Rect(player_pos[0], player_pos[1], player_size, player_size))

        # Draw boss attacks
        for attack in boss_attacks:
            pygame.draw.rect(screen, attack['color'], pygame.Rect(attack['pos'][0], attack['pos'][1], attack_size, attack_size))
    
    if final_phase:
        if boss_sliding:
            pygame.draw.rect(screen, boss_color, pygame.Rect(boss_pos[0], boss_pos[1], boss_size, boss_size))

            # Draw attacks
            for attack in attacks:
                pygame.draw.rect(screen, attack['color'], pygame.Rect(attack['pos'][0], attack['pos'][1], attack_size, attack_size))

            # Draw CMD windows
            for cmd_window in cmd_windows:
                pygame.draw.rect(screen, white, pygame.Rect(cmd_window[0], cmd_window[1], cmd_window_size, cmd_window_size))

                        # Draw player
            pygame.draw.rect(screen, player_color, pygame.Rect(player_pos[0], player_pos[1], player_size, player_size))

            # Draw bullets
            for bullet in bullets:
                pygame.draw.rect(screen, bullet_color, pygame.Rect(bullet[0], bullet[1], bullet_size[0], bullet_size[1]))

            # Draw health bars
            draw_health_bar(screen, 10, 10, player_health, 100, white)
            draw_health_bar(screen, screen_width - 110, 10, boss_health, 100, red)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()

            

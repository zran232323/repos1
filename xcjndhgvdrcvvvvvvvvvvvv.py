import curses
import random
import time

# Constants
HEIGHT, WIDTH = 20, 40
TRIANGLE = "^"
CIRCLE = "O"
BULLET = "-"
BOSS = "B"
EMPTY = " "
UPGRADES = 1

# Initialize the screen
stdscr = curses.initscr()
curses.curs_set(0)
stdscr.keypad(1)
curses.noecho()
curses.cbreak()
stdscr.nodelay(1)

def draw_border(stdscr):
    for i in range(HEIGHT):
        stdscr.addstr(i, 0, "|")
        stdscr.addstr(i, WIDTH-1, "|")
    for i in range(WIDTH):
        stdscr.addstr(0, i, "-")
        stdscr.addstr(HEIGHT-1, i, "-")

def main(stdscr):
    global UPGRADES
    
    # Player position and direction
    player_x, player_y = WIDTH//2, HEIGHT-2
    direction = 0
    
    # Enemy and boss initialization
    boss_alive = False
    boss_x, boss_y = WIDTH//2, 2
    boss_hp = 10
    minions = []
    
    bullets = []
    score = 0
    lives = 3
    level = 1
    enemy_alive = True
    
    while True:
        stdscr.clear()
        draw_border(stdscr)
        
        # Draw player
        stdscr.addstr(player_y, player_x, TRIANGLE)
        
        # Draw bullets
        for bx, by in bullets:
            stdscr.addstr(by, bx, BULLET)
        
        # Boss behavior
        if boss_alive:
            stdscr.addstr(boss_y, boss_x, BOSS)
            if random.randint(0, 10) < 3:
                minions.append((random.randint(1, WIDTH-2), random.randint(1, HEIGHT//2)))
            if random.randint(0, 10) < 3:
                boss_x += random.choice([-1, 1])
                boss_y += random.choice([-1, 1])
        
        # Draw minions
        for mx, my in minions:
            stdscr.addstr(my, mx, CIRCLE)
        
        # Input handling
        key = stdscr.getch()
        if key == curses.KEY_UP and player_y > 1:
            player_y -= 1
        elif key == curses.KEY_DOWN and player_y < HEIGHT-2:
            player_y += 1
        elif key == curses.KEY_LEFT and player_x > 1:
            player_x -= 1
        elif key == curses.KEY_RIGHT and player_x < WIDTH-2:
            player_x += 1
        elif key == ord('q'):
            direction = (direction - 1) % 4
        elif key == ord('e'):
            direction = (direction + 1) % 4
        elif key == ord(' '):
            if direction == 0:  # Up
                bullets.append((player_x, player_y-1))
            elif direction == 1:  # Right
                bullets.append((player_x+1, player_y))
            elif direction == 2:  # Down
                bullets.append((player_x, player_y+1))
            elif direction == 3:  # Left
                bullets.append((player_x-1, player_y))
        
        # Move bullets
        new_bullets = []
        for bx, by in bullets:
            if direction == 0:
                by -= 1
            elif direction == 1:
                bx += 1
            elif direction == 2:
                by += 1
            elif direction == 3:
                bx -= 1
            
            if 0 < bx < WIDTH-1 and 0 < by < HEIGHT-1:
                if boss_alive and bx == boss_x and by == boss_y:
                    boss_hp -= 1
                    if boss_hp <= 0:
                        boss_alive = False
                        score += 100
                        UPGRADES += 1
                        stdscr.addstr(HEIGHT//2, WIDTH//2-7, "Boss Defeated!")
                        stdscr.refresh()
                        time.sleep(2)
                else:
                    new_bullets.append((bx, by))
        
        bullets = new_bullets
        
        # Check for minion hits
        new_minions = []
        for mx, my in minions:
            hit = False
            for bx, by in bullets:
                if mx == bx and my == by:
                    hit = True
                    score += 10
                    break
            if not hit:
                new_minions.append((mx, my))
        minions = new_minions
        
        # Boss appearance based on level
        if level % 5 == 0 and not boss_alive:
            boss_alive = True
            boss_x, boss_y = WIDTH//2, 2
            boss_hp = 10 + level
        
        # Update and refresh screen
        stdscr.addstr(0, WIDTH//2-10, f"Score: {score} Lives: {lives} Level: {level}")
        stdscr.addstr(1, WIDTH//2-10, f"Upgrades: {UPGRADES}")
        stdscr.refresh()
        
        time.sleep(0.1)
        
        if not enemy_alive:
            stdscr.addstr(HEIGHT//2, WIDTH//2-5, "You Win!")
            stdscr.refresh()
            time.sleep(2)
            break
        
        if lives <= 0:
            stdscr.addstr(HEIGHT//2, WIDTH//2-5, "Game Over!")
            stdscr.refresh()
            time.sleep(2)
            break
    
    curses.endwin()

if __name__ == "__main__":
    curses.wrapper(main)

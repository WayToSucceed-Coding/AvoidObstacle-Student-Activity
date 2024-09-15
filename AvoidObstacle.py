import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Avoid Falling Obstacles")

# Define colors
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Font for score display
font = pygame.font.SysFont("comicsans", 30)

# Player dictionary to store position, size, and speed
player = [
    "x": screen_width // 2 - 25,
    "y": screen_height - 80,
    "width": 50,
    "height": 60,
    "speed": 7
]

# Obstacle dictionary to store attributes (more obstacles added later)
obstacles = []

# Function to create a new obstacle
def create_obstacle():
    obstacle = {
        x: random.randint(0, screen_width - 50),
        y: -50,
        "width": 50,
        "height": 50,
        "speed": random.randint(4, 8)
    }
    obstacles.append(obstacle)

# Score tracking
score = 0

# Game clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    clock.tick(30)  # FPS

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
    
    # Player movement with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player["x"] - player["speed"] > 0:
        player["x"] -= player["speed"]
    if keys[pygame.K_RIGHT] and player["x"] + player["width"] + player["speed"] < screen_width:
        player["x"] += player["speed"]

    # Create obstacles over time
    if random.randint(0, 20) == 1:  # Low chance to create new obstacles randomly
        create_obstacle()

    # Move obstacles
    for obstacle in obstacles:
        obstacle["y"] += obstacle["speed"]

    # Remove obstacles that are off-screen
    obstacles = [obstacle for obstacle in obstacles if obstacle["y"] < screen_height]

    # Check for collisions between player and obstacles
    for obstacle in obstacles:
        if (player["x"] < obstacle["x"] + obstacle["width"] and
            player["x"] + player["width"] > obstacle["x"] and
            player["y"] < obstacle["y"] + obstacle["height"] and
            player["y"] + player["height"] > obstacle["y"]):
            print("Game Over!")
            running = False
    
    # Increase score over time
    score += 1

    # Drawing everything on screen
    screen.fill(white)

    # Draw player
    pygame.draw.rect(screen, blue, (player["x"], player["y"], player["width"], player["height"]))

    # Draw obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen, red, (obstacle["x"], obstacle["y"], obstacle["width"], obstacle["height"]))

    # Display score
    score_text = font.render(f"Score: {score}", True, black)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.update()

# Quit Pygame
pygame.quit()

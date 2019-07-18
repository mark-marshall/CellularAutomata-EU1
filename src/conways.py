import pygame, random
 
# Define some colors and other constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (25, 25, 25)
BTN_COLOUR = (175, 203, 255)
MARGIN = 3
SQ_LENGTH = 20
SQ_NUM = 25
WIN_SIZE = (SQ_NUM + 1) * MARGIN + SQ_NUM * SQ_LENGTH
BTN_SIZE = 30

# TODO: add some variables to track generations and speed of game start and stop etc
generations = 0
time_step = 5
running = True

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (WIN_SIZE, WIN_SIZE + BTN_SIZE + 20)
screen = pygame.display.set_mode(size)

automata = [0] * (SQ_NUM * SQ_NUM)

# Assign Random Values to our Automata
for row in range(SQ_NUM):
    for col in range(SQ_NUM):
        automata[row * SQ_NUM + col] = random.randint(0, 1)

# Add a title
pygame.display.set_caption("Conway's Game of Life")

# add font
font = pygame.font.Font('freesansbold.ttf', 16)

# Add button
inc_timestep_button = pygame.draw.rect(screen, BTN_COLOUR, pygame.Rect(10, WIN_SIZE + 10, 3 * BTN_SIZE, BTN_SIZE))
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
    # Create a new automata for the next state
    new_automata = [0] * (SQ_NUM * SQ_NUM)

    for i in range(len(automata)):
        # Initliaze an int of live neighbours
        live = 0
        # Check status of neighbours
        # Left
        if (i - 1) >= 0 and automata[i - 1]:
            live += 1
        # Right
        if (i + 1) < (SQ_NUM * SQ_NUM) and automata[i + 1]:
            live += 1
        # Up
        if (i - SQ_NUM) >= 0 and automata[i - SQ_NUM]:
            live += 1
        # Down
        if (i + SQ_NUM) < (SQ_NUM * SQ_NUM) and automata[i + SQ_NUM]:
            live += 1
        # Left Up
        if (i - SQ_NUM - 1) >= 0 and automata[i - SQ_NUM - 1]:
            live += 1
        # Left Dowm
        if (i + SQ_NUM - 1) < (SQ_NUM * SQ_NUM) and automata[i + SQ_NUM -1]:
            live += 1
        # Right UP
        if (i - SQ_NUM + 1) >= 0 and automata[i - SQ_NUM + 1]:
            live += 1
        # Right Down
        if (i + SQ_NUM + 1) < (SQ_NUM * SQ_NUM) and automata[i + SQ_NUM + 1]:
            live += 1

        # Update state based on game rules
        # Death: a "live" cell with a single neighbor will "die"
        if automata[i] and live == 1:
            new_automata[i] = 0
        # Death: a "live" cell with 4+ live neighbors will "die"
        elif automata[i] and live >= 4:
            new_automata[i] = 0
        # Life: a "live" cell with exactly 2 or 3 live neighbors will "stay alive"
        elif automata[i] and ((live == 2) or (live == 3)):
            new_automata[i] = 1
        # Birth: a "dead" cell with exactly 3 live neighbors will "come to life"
        elif not automata[i] and live == 3:
            new_automata[i] = 1
        # If none of the above conditions are met, cell is "dead" and shouly stay "dead"
        else:
            new_automata[i] = 0

    # swap the data for the next generations data
    automata = new_automata

    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to gray. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(GRAY)

    # --- Drawing code should go here
    # pygame.draw.rect(screen, RED, pygame.Rect(20, 20, 20, 20))
    y = MARGIN
    i = 0
    while y < WIN_SIZE:
        x = MARGIN
        while x < WIN_SIZE:
            if automata[i] == 0:
                pygame.draw.rect(screen, BLACK, pygame.Rect(x, y, SQ_LENGTH, SQ_LENGTH))
            else:
                pygame.draw.rect(screen, WHITE, pygame.Rect(x, y, SQ_LENGTH, SQ_LENGTH))
            i += 1
            x += SQ_LENGTH + MARGIN
        y += SQ_LENGTH + MARGIN

    # Update inc Timestep button
    inc_timestep_button = pygame.draw.rect(screen, BTN_COLOUR, pygame.Rect(10, WIN_SIZE + 10, 3 * BTN_SIZE, BTN_SIZE))
    text = font.render("Button", True, (14, 28, 54)) # TODO: change text in button and refactor colour
    textRect = text.get_rect()
    textRect.center = (inc_timestep_button.center[0], inc_timestep_button.center[1])
    screen.blit(text, textRect)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 5 frames per second
    clock.tick(5)
 
# Close the window and quit.
pygame.quit()
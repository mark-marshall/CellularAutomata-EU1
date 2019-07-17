import pygame, random
 
# Define some colors and other constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (25, 25, 25)
RED = (255, 0, 0)
MARGIN = 3
SQ_LENGTH = 20
SQ_NUM = 25
WIN_SIZE = (SQ_NUM + 1) * MARGIN + SQ_NUM * SQ_LENGTH

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (WIN_SIZE, WIN_SIZE)
screen = pygame.display.set_mode(size)

automata = [0] * (SQ_NUM * SQ_NUM)

# Assign Random Values to our Automata
# rowx:
#     col:
#         automata[row * SQ_NUM + col] = set to a random number

# for i in range(SQ_NUM * SQ_NUM):
#     automata[i] = random.randint(0, 1)

for row in range(SQ_NUM):
    for col in range(SQ_NUM):
        automata[row * SQ_NUM + col] = random.randint(0, 1)


# Update State ( Add Rules to update each cell based on it's previous state )

# Create a new automata for the next state
new_automata = [0] * (SQ_NUM * SQ_NUM)

for i in range(len(automata)):
    live = 0
    dead = 8

    # look at neighbors
    # (8 if conditions)
    if i - 1 >= 0 and automata[i - 1]:
        live += 1
    if i + 1 < (SQ_NUM * SQ_NUM) and automata[i + 1]:
        live += 1
    # TODO: the other neighbours

    # Update State
    # if there are less than 2 living neighbors the cell dies
    if automata[i] and live < 2:
        new_automata[i] = 0
    # if alive and has less than 4 neighbors then cell carrys on living
    elif automata[i] and live < 4:
        new_automata[i] = 1
    # TODO: 3 more conditions


# swap the data for the next generations data
automata = new_automata






# Add a title
pygame.display.set_caption("Conway's Game of Life")
 
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
    

 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to gray. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(GRAY)
    automata[12] = 1
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

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 5 frames per second
    clock.tick(5)
 
# Close the window and quit.
pygame.quit()
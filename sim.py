import pygame
from organism.Organism import Individual
import random
import math
import time




tick = 0
FPS=60
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize pygame
pygame.init()



# Grid size
gridX = 100
gridY = 100

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE_X = 2000
WINDOW_SIZE = [WINDOW_SIZE_X, WINDOW_SIZE_X]
screen = pygame.display.set_mode(WINDOW_SIZE)

# This sets the margin between each cell
MARGIN = 0

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = math.floor(WINDOW_SIZE_X/gridX)+MARGIN
HEIGHT = math.floor(WINDOW_SIZE_X/gridX)+MARGIN



# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(gridX):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(gridY):
        grid[row].append(0)  # Append a cell




# Set title of screen
pygame.display.set_caption("Simulator")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# List of individuals
individuals=[]
retiredIndivduals=[]
for i in xrange(1000):
    individuals.append(Individual(random.randrange(1,1024),random.randrange(0,gridX),random.randrange(0,gridY)))


for indvi in individuals:
    indvi.tick()




# -------- Main Program Loop -----------
while not done:
    tick += 1
    start_time = time.time()
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)

    alive=0
    dead=0
    # Set the screen background
    screen.fill(BLACK)

    # Draw the grid
    for row in range(gridX):
        for column in range(gridY):
            color = BLACK

        pygame.draw.rect(screen,
                         color,
                         [(MARGIN + WIDTH) * column + MARGIN,
                          (MARGIN + HEIGHT) * row + MARGIN,
                          WIDTH,
                          HEIGHT])

    # Limit to 120 frames per second
    clock.tick(FPS)

    for indvi in individuals:
        indvi.tick()
        print
        indvi.takeInEnergy(random.randrange(0,1024))
        pygame.draw.rect(screen,
                         indvi.getColor(),
                         [(MARGIN + WIDTH) * indvi.getX() + MARGIN,
                          (MARGIN + HEIGHT) * indvi.getY() + MARGIN,
                          WIDTH,
                          HEIGHT])
        if indvi.alive:
            alive += 1
        else:
            dead += 1
            retiredIndivduals.append(individuals.pop(individuals.index(indvi)))


    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    end_time = time.time()
    looptime = round(end_time - start_time,4)
    if (tick%150==1 and tick != 0):
        print "Slow down factor: X%s " % (looptime)
        print "alive: %s | Dead: %s"%(alive,dead)

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()

import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
WIDTH = 100
HEIGHT = 100
MARGIN = 5
grid = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
pygame.init()
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [325, 325]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Tic Tac Toe")
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)
    # Set the screen background
    screen.fill(BLACK)
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
    # Limit to 60 frames per second
    clock.tick(60)
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
pygame.quit()

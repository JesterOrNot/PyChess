import pygame, time
def text_to_screen(screen, text, x, y, size = 50, color = (200, 000, 000)):
        text = str(text)
        screen.blit(text, (x, y))
        time.sleep(5)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255,0,0)
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
is_x_turn = True
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
            if is_x_turn:
                grid[row][column] = 1
                is_x_turn = False
            else:
                grid[row][column] = 2
                is_x_turn = True
            print("Click ", pos, "Grid coordinates: ", row, column)
            if ((grid[0][0] == 1 and grid[0][1] == 1 and grid[0][2] == 1) or 
                (grid[1][0] == 1 and grid[1][1] == 1 and grid[1][2] == 1) or
                (grid[2][0] == 1 and grid[2][1] == 1 and grid[2][2] == 1) or
                (grid[0][0] == 1 and grid[1][0] == 1 and grid[2][0] == 1) or
                (grid[0][1] == 1 and grid[1][1] == 1 and grid[2][1] == 1) or
                (grid[0][2] == 1 and grid[1][2] == 1 and grid[2][2] == 1)):
                text_to_screen(screen,"X wins",10,10)
                time.sleep(10)
                done=True
            elif ((grid[0][0] == 2 and grid[0][1] == 2 and grid[0][2] == 2) or 
                (grid[1][0] == 2 and grid[1][1] == 2 and grid[1][2] == 2) or
                (grid[2][0] == 2 and grid[2][1] == 2 and grid[2][2] == 2) or
                (grid[0][0] == 2 and grid[1][0] == 2 and grid[2][0] == 2) or
                (grid[0][1] == 2 and grid[1][1] == 2 and grid[2][1] == 2) or
                (grid[0][2] == 2 and grid[1][2] == 2 and grid[2][2] == 2)):
                text_to_screen(screen,"Y wins",10,10)
                time.sleep(10)
                done=True
    # Set the screen background
    screen.fill(BLACK)
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            elif grid[row][column] == 2:
                color = RED
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

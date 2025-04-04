import pygame
import random

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

pygame.font.init()

# GLOBALS VARS
s_width = 800
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per blo ck
block_size = 30

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height


# SHAPE FORMATS

S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
# index 0 - 6 represent shape


class Piece(object):
    rows = 20  # y
    columns = 10  # x

    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0  # number from 0-3


def create_grid(locked_positions={}):
    # Initialize a 20x10 grid filled with black (0, 0, 0) representing empty cells
    grid = [[(0,0,0) for x in range(10)] for x in range(20)]

    # Fill in the grid with locked positions, if any
    for i in range(len(grid)):  # Iterate over rows
        for j in range(len(grid[i])):  # Iterate over columns
            # Check if the current position (x=j, y=i) is in locked_positions
            if (j, i) in locked_positions:
                c = locked_positions[(j, i)]  # Get the color for that position
                grid[i][j] = c  # Set the grid cell to the locked color
    return grid


def convert_shape_format(shape):
    positions = []

    # Get the current rotation layout of the shape
    format = shape.shape[shape.rotation % len(shape.shape)]

    # Loop through each row and column in the layout
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                # Translate local shape coordinates to grid position
                positions.append((shape.x + j, shape.y + i))

    # Adjust for padding in the shape's definition grid
    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)

    return positions



def valid_space(shape, grid):
    # Get all empty positions on the grid
    accepted_positions = [[(j, i) for j in range(10) if grid[i][j] == (0,0,0)] for i in range(20)]
    accepted_positions = [j for sub in accepted_positions for j in sub]

    # Get the current occupied positions by the shape
    formatted = convert_shape_format(shape)

    # Check for collisions or out-of-bound placements
    for pos in formatted:
        if pos not in accepted_positions:
            if pos[1] > -1:  # Ignore positions above the visible screen
                return False

    return True


def check_lost(positions):
    # Check if any locked position is above the top of the play area
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False


def get_shape():
    # Create a new random piece at the starting position (center top)
    global shapes, shape_colors

    return Piece(5, 0, random.choice(shapes))


def draw_text_middle(text, size, color, surface):
    # Create and center a text label
    font = pygame.font.SysFont('comicsans', size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(label, (top_left_x + play_width/2 - (label.get_width() / 2), top_left_y + play_height/2 - label.get_height()/2))


def draw_grid(surface, row, col):
    # Draw grid lines to separate cells
    sx = top_left_x
    sy = top_left_y
    for i in range(row):
        pygame.draw.line(surface, (128,128,128), (sx, sy+ i*30), (sx + play_width, sy + i * 30))  # horizontal lines
        for j in range(col):
            pygame.draw.line(surface, (128,128,128), (sx + j * 30, sy), (sx + j * 30, sy + play_height))  # vertical lines


def clear_rows(grid, locked):
    inc = 0  # Number of cleared rows
    for i in range(len(grid)-1, -1, -1):  # Bottom-up
        row = grid[i]
        if (0, 0, 0) not in row:
            inc += 1
            ind = i
            for j in range(len(row)):
                try:
                    del locked[(j, i)]  # Remove from locked positions
                except:
                    continue

    # Shift rows above cleared rows downward
    if inc > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y + inc)
                locked[newKey] = locked.pop(key)


def draw_next_shape(shape, surface):
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Next Shape', 1, (255,255,255))

    # Position to draw the next shape
    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height / 2 - 100
    format = shape.shape[shape.rotation % len(shape.shape)]

    # Draw each filled block of the shape
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface, shape.color, (sx + j*30, sy + i*30, 30, 30), 0)

    surface.blit(label, (sx + 10, sy - 30))


def draw_window(surface):
    surface.fill((0,0,0))
    # Tetris Title
    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('TETRIS', 1, (255,255,255))

    surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), 30))

    # Draw all grid cells
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j* 30, top_left_y + i * 30, 30, 30), 0)

    # draw grid and border
    draw_grid(surface, 20, 10)
    pygame.draw.rect(surface, (255, 0, 0), (top_left_x, top_left_y, play_width, play_height), 5)
    # pygame.display.update()


def main():
    """
    The main game loop for the Tetris game.

    This function initializes the game state, including the playing grid, score,
    current and next pieces, and timing mechanisms. It handles user input for controlling
    pieces, updates the grid state as pieces fall, checks for collisions, clears rows,
    and renders the game window in real time using Pygame. The game continues until a
    "Game Over" state is detected.

    Parameters:
        None

    Returns:
        None

    Exceptions:
        This function may raise exceptions related to:
        - Pygame initialization or rendering errors if Pygame is not properly set up.
        - Unexpected `pygame.event.get()` results, particularly if used outside a running Pygame environment.

    Example:
        >>> if __name__ == "__main__":
        >>>     main()

    Notes:
        - `grid` is treated as a global variable and used across various draw and state functions.
        - Uses `pygame` to handle rendering and keyboard inputs; must be run within a properly initialized
          Pygame context.
        - Game difficulty increases over time as `fall_speed` decreases.
        - Key controls:
            LEFT / RIGHT arrows: Move piece left or right
            UP arrow: Rotate piece
            DOWN arrow: Soft drop
            (SPACEBAR code for hard drop is commented out)
        - The `clear_rows()` function should return a value (e.g. `True` or number of rows cleared)
          for score tracking to work as expected.
    """
    global grid

    locked_positions = {}  # Dictionary of locked positions in the format {(x, y): (R, G, B)}
    grid = create_grid(locked_positions)

    change_piece = False  # Flag to determine when to lock the current piece and spawn the next one
    run = True  # Game loop control flag
    current_piece = get_shape()  # Generate the first piece
    next_piece = get_shape()     # Generate the next piece preview
    clock = pygame.time.Clock()
    fall_time = 0  # Timer to manage automatic piece falling
    level_time = 0  # Timer to control difficulty level progression
    fall_speed = 0.27  # Initial fall speed (in seconds)
    score = 0  # Player's score

    while run:
        grid = create_grid(locked_positions)  # Refresh the grid with updated locked positions
        fall_time += clock.get_rawtime()  # Time since last frame in ms
        level_time += clock.get_rawtime()
        clock.tick()  # Advance the clock (typically caps at ~60 FPS)

        # Speed up the game every 4 seconds
        if level_time / 1000 > 4:
            level_time = 0
            if fall_speed > 0.15:
                fall_speed -= 0.005  # Increase fall speed, making the game harder

        # Handle piece falling automatically
        if fall_time / 1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not valid_space(current_piece, grid) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True  # Piece has landed

        # Handle user inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1  # Undo move if invalid

                elif event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1

                elif event.key == pygame.K_UP:
                    # Rotate the piece
                    current_piece.rotation = current_piece.rotation + 1 % len(current_piece.shape)
                    if not valid_space(current_piece, grid):
                        current_piece.rotation = current_piece.rotation - 1 % len(current_piece.shape)

                elif event.key == pygame.K_DOWN:
                    # Soft drop
                    current_piece.y += 1
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1

                # Optional: Uncomment to enable hard drop functionality
                # if event.key == pygame.K_SPACE:
                #     while valid_space(current_piece, grid):
                #         current_piece.y += 1
                #     current_piece.y -= 1
                #     print(convert_shape_format(current_piece))

        shape_pos = convert_shape_format(current_piece)

        # Draw current piece on the grid temporarily
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color

        # If piece landed, lock it and get the next one
        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False

            # Clear full rows and update score
            if clear_rows(grid, locked_positions):
                score += 10

        # Draw everything
        draw_window(win)
        draw_next_shape(next_piece, win)
        pygame.display.update()

        # Check for game over condition
        if check_lost(locked_positions):
            run = False

    # Display "You Lost" screen
    draw_text_middle("You Lost", 40, (255, 255, 255), win)
    pygame.display.update()
    pygame.time.delay(2000)



def main_menu():
    """
    Displays the main menu screen and waits for user input to start the game.

    This function renders a simple "Press any key to begin." message at the center
    of the screen using Pygame. It listens for either a key press to start the game or
    a window close event to exit. Once a key is pressed, it transitions to the main
    Tetris game loop by calling `main()`.

    Parameters:
        None

    Returns:
        None

    Exceptions:
        - May raise errors if Pygame is not initialized before this function is called.
        - If `win` or `draw_text_middle` are not defined globally, NameErrors will occur.

    Example:
        >>> if __name__ == "__main__":
        >>>     main_menu()

    Notes:
        - Assumes `win` is a global Pygame display surface object.
        - Requires Pygame to be initialized prior to calling this function.
        - After the user starts the game, this function does not return until the game ends.
    """
    run = True
    while run:
        win.fill((0, 0, 0))  # Clear screen with black background
        draw_text_middle('Press any key to begin.', 60, (255, 255, 255), win)  # Draw prompt text
        pygame.display.update()  # Refresh the screen with updated visuals

        # Event loop to handle user inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  # Exit the menu loop

            if event.type == pygame.KEYDOWN:
                main()  # Start the main game loop

    pygame.quit()  # Close Pygame once the menu loop ends



win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption('Tetris')

main_menu()  # start game







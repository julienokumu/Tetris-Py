# Tetris Game Implementation

## Overview
This module implements a simple Tetris game using the Pygame library. The game includes basic features such as moving, rotating, and dropping tetrominoes, as well as clearing completed lines.

## Dependencies
- **pygame**: For game development
- **random**: For generating random tetrominoes

## Screen Dimensions
- **SCREEN_WIDTH**: 300 pixels
- **SCREEN_HEIGHT**: 600 pixels
- **BLOCK_SIZE**: 30 pixels

## Colors
- **BLACK**: (0, 0, 0)
- **WHITE**: (255, 255, 255)
- **RED**: (255, 0, 0)
- **GREEN**: (0, 255, 0)
- **BLUE**: (0, 0, 255)
- **CYAN**: (0, 255, 255)
- **MAGENTA**: (255, 0, 255)
- **YELLOW**: (255, 255, 0)
- **ORANGE**: (255, 165, 0)
- **PURPLE**: (128, 0, 128)

## Tetromino Shapes
- **I shape**: `[[1, 1, 1, 1]]`
- **O shape**: `[[1, 1], [1, 1]]`
- **T shape**: `[[0, 1, 0], [1, 1, 1]]`
- **S shape**: `[[1, 1, 0], [0, 1, 1]]`
- **Z shape**: `[[0, 1, 1], [1, 1, 0]]`
- **L shape**: `[[1, 0, 0], [1, 1, 1]]`
- **J shape**: `[[0, 0, 1], [1, 1, 1]]`

## Corresponding Colors for the Shapes
- **CYAN**
- **YELLOW**
- **PURPLE**
- **GREEN**
- **RED**
- **ORANGE**
- **BLUE**

## Grid Dimensions
- **GRID_WIDTH**: `SCREEN_WIDTH // BLOCK_SIZE`
- **GRID_HEIGHT**: `SCREEN_HEIGHT // BLOCK_SIZE`

## Grid Initialization
- **grid**: A 2D list initialized with zeros

## Classes

### Tetromino
**Attributes:**
- **x (int)**: X position on the grid.
- **y (int)**: Y position on the grid.
- **shape (list)**: The 2D list defining the shape of the tetromino.
- **color (tuple)**: Color of the shape.

**Methods:**
- **__init__(self, x, y, shape, color)**: Initializes a new tetromino with the given position, shape, and color.
- **rotate(self)**: Rotates the tetromino clockwise.

## Functions

### draw_grid
**Description**: Draws the grid lines on the screen.
**Parameters**:
- **surface (pygame.Surface)**: The surface to draw the grid on.

### draw_tetromino
**Description**: Draws the tetromino on the screen.
**Parameters**:
- **surface (pygame.Surface)**: The surface to draw the tetromino on.
- **tetromino (Tetromino)**: The tetromino to draw.

### check_collision
**Description**: Checks if the tetromino collides with the grid or goes out of bounds.
**Parameters**:
- **tetromino (Tetromino)**: The tetromino to check for collision.
**Returns**:
- **bool**: True if there is a collision, False otherwise.

### merge_tetromino
**Description**: Adds the tetromino to the grid.
**Parameters**:
- **tetromino (Tetromino)**: The tetromino to merge with the grid.

### clear_lines
**Description**: Clears completed lines from the grid.

### main
**Description**: Main game loop.
**Parameters**: None
**Returns**: None

## Main Game Loop
1. **Initialize Pygame and set up the screen**.
2. **Create a clock to control the frame rate**.
3. **Spawn the first tetromino**.
4. **Main loop**:
   - **Fill the screen with black**.
   - **Handle events**:
     - **Quit the game if the window is closed**.
     - **Move the tetromino left, right, or down based on key presses**.
     - **Rotate the tetromino if the up arrow key is pressed**.
   - **Move the tetromino down automatically**.
   - **Check for collisions**:
     - **If a collision occurs, move the tetromino back up**.
     - **Merge the tetromino with the grid**.
     - **Clear completed lines**.
     - **Spawn a new tetromino**.
     - **Check for game over condition**.
   - **Draw the grid and the current tetromino**.
   - **Update the display**.
   - **Limit the frame rate**.

## Running the Game
To run the game, execute the `tetris.py` file:
python tetris.py

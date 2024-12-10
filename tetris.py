# import libraries
import pygame
import random

# intialize pygame
pygame.init()

# screen dimensions
screen_width = 800
screen_height = 600
grid_width = 10
grid_height = 20
block_size = 30

# colors
black = (0, 0, 0)
white = (255, 255, 255)
colors = [
    (255, 0, 0), # red
    (0, 255, 0), # green
    (0, 0, 255), # blue
    (255, 255, 0), # yellow
    (255, 0, 255), # magenta
    (0, 255, 255), # cyan
]

# tetromino shapes
shapes = [
    [[1, 1, 1, 1]], # I-shape
    [[1, 1], [1, 1]], # square
    [[1, 1, 1], [0, 1, 0]], # T-shape
    [[1, 1, 1], [1, 0, 0]], # L-shape
    [[1, 1, 1], [0, 0, 1]], # reverse L-shape
    [[1, 1, 0], [0, 1, 1]], #  Z-shape
    [[0, 1, 1], [1, 1, 0]], # reverse Z-shape
]

# tetris class
class Tetris:
    def __init__(self):
        # set up game screen
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Tetris | Julien Okumu")

        # game state varibles
        self.grid = [[0 for _ in range(grid_width)] for _ in range(grid_height)]
        self.current_piece = self.get_new_piece()
        self.game_over = False
        self.score = 0

        # clock for controlling game speed
        self.clock = pygame.time.Clock()

        # font for displaying score
        self.font = pygame.font.Font(None, 36)

    def get_new_piece(self):
        # generate a new random tetromino
        shape = random.choice(shapes)
        color = random.choice(colors)
        return {
            'shape': shape,
            'color': color,
            'x': grid_width // 2 - len(shape[0]) // 2,
            'y': 0
        }
    
    def draw_grid(self):
        # draw the game grid
        for y in range(grid_height):
            for x in range(grid_width):
                rect = pygame.Rect(
                    x * block_size,
                    y * block_size,
                    block_size - 1,
                    block_size - 1
                )
                if self.grid[y][x]:
                    pygame.draw.rect(self.screen, self.grid[y][x], rect)
                else:
                    pygame.draw.rect(self.screen, white, rect, 1)
    
    def draw_piece(self, piece):
        for y, row in enumerate(piece['shape']):
            for x, cell in enumerate(row):
                if cell:
                    rect = pygame.Rect(
                        (piece['x'] + x) * block_size,
                        (piece['y'] + y) * block_size,
                        block_size - 1,
                        block_size
                    )
                    pygame.draw.rect(self.screen, piece['color'], rect)

    def is_valid_move(self, piece, new_x, new_y):
        # check if a move is valid
        for y, row in enumerate(piece['shape']):
            for x, cell in enumerate(row):
                if cell:
                    grid_x = new_x + x
                    grid_y = new_y + y

                    # check boundaries
                    if (grid_x < 0 or grid_x >= grid_width or grid_y >= grid_height):
                        return False
                    
                    # check collision with existing pieces
                    if grid_y >= 0 and self.grid[grid_y][grid_x]:
                        return False
                    
        return True
    
    def lock_piece(self, piece):
        # lock the piece in place when it cant move
        for y, row in enumerate(piece['shape']):
            for x, cell in enumerate(row):
                if cell:
                    grid_x = piece['x'] + x
                    grid_y = piece['y'] + y
                    if 0 <= grid_y < grid_height:
                        self.grid[grid_y][grid_x] = piece['color']

        # clear completed lines
        self.clear_lines()

        # create new piece
        self.current_piece = self.get_new_piece()

        # check for game over
        if not self.is_valid_move(self.current_piece, self.current_piece['x'], self.current_piece['y']):
            self.game_over = True
    
    def clear_lines(self):
        # remove completed lines and update score
        lines_cleared = 0
        y = grid_height -1
        while y >= 0:
            if all(self.grid[y]):
                del self.grid[y]
                self.grid.insert(0, [0 for _ in range(grid_width)])
                lines_cleared += 1
            else:
                y -= 1

        # scoring system
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500
        elif lines_cleared == 4:
            self.score += 800

    def rotate_piece(self, piece):
        # rotate the piece 90 degrees clockwise
        rotated = list(zip(*piece['shape'][::-1]))
        test_piece = piece.copy()
        test_piece['shape'] = rotated

        # check if rotation is possible
        if self.is_valid_move(test_piece, piece['x'], piece['y']):
            piece['shape'] = rotated

    def run(self):
        # main game loop
        fall_time = 0
        fall_speed = 0.5 # piece falls every 0.5 seconds

        while not self.game_over:
            # event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                
                # keyboard controls
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        # move piece left
                        if self.is_valid_move(self.current_piece, self.current_piece['x'] - 1, self.current_piece['y']):
                            self.current_piece['x'] -= 1
                    
                    if event.key == pygame.K_RIGHT:
                        # move piece right
                        if self.is_valid_move(self.current_piece, self.current_piece['x'] + 1, self.current_piece['y']):
                            self.current_piece['x'] += 1

                    if event.key == pygame.K_DOWN:
                        # move piece down faster
                        if self.is_valid_move(self.current_piece, self.current_piece['x'], self.current_piece['y'] + 1):
                            self.current_piece['y'] += 1

                    if event.key == pygame.K_UP:
                        # rotate piece
                        self.rotate_piece(self.current_piece)

            # piece falling mechanism
            fall_time += self.clock.get_rawtime()
            if fall_time / 250 >= fall_speed:
                fall_time = 0
                # move piece down
                if self.is_valid_move(self.current_piece, self.current_piece['x'], self.current_piece['y'] + 1):
                    self.current_piece['y'] += 1
                else:
                    # lock the piece if it cant move down
                    self.lock_piece(self.current_piece)

            # draw everything
            self.screen.fill(black) # clear the screen
            self.draw_grid() # draw the grid
            self.draw_piece(self.current_piece) # draw the current piece

            # display the score
            score_text = self.font.render(f'Score: {self.score}', True, white)
            self.screen.blit(score_text, (450, 450))

            pygame.display.flip() # update the display
            self.clock.tick(60) # limit frame rate to 60fps

        # game over message
        self.screen.fill(black)
        game_over_text = self.font.render('Game Over', True, white)
        self.screen.blit(game_over_text, (screen_width // 2 - 50, screen_height // 2 - 20))
        pygame.display.flip()
        pygame.time.wait(2000) # wait 2 seconds before closing

# start the game
if __name__ == "__main__":
    game = Tetris()
    game.run()
    pygame.quit() # quit the pygame when the game is over
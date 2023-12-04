import pygame
import sys


pygame.init()

# Define the consts
WIDTH, HEIGHT = 540, 540
GRID_SIZE = 9
CELL_SIZE = WIDTH // GRID_SIZE

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Sample Sudoku board (0 represents empty cells)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Create a function to draw the Sudoku board
def draw_board():
    for i in range(GRID_SIZE + 1):
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), 2)
        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), 2)

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if board[i][j] != 0:
                font = pygame.font.Font(None, 36)
                text = font.render(str(board[i][j]), True, BLACK)
                screen.blit(text, (j * CELL_SIZE + 20, i * CELL_SIZE + 20))

# Create a function to check if a number is valid in a given position
def is_valid(num, row, col):
    # Check row and column
    for i in range(GRID_SIZE):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

# Create a function to solve the Sudoku puzzle using backtracking
def solve():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(num, i, j):
                        board[i][j] = num
                        if solve():
                            return True
                        board[i][j] = 0
                return False
    return True

# Set up the pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")

# Main game loop
running = True
solve_button_pressed = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                solve_button_pressed = True

    if solve_button_pressed:
        solve()
        solve_button_pressed = False

    # Draw the Sudoku board
    screen.fill(WHITE)
    draw_board()
    pygame.display.flip()

pygame.quit()
sys.exit()

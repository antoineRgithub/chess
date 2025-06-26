import pygame

# Constants
SQUARE_SIZE = 60
BOARD_SIZE = 8
LIGHT_SQUARE = (240, 217, 181)
DARK_SQUARE = (181, 136, 99)

# Function to draw the chessboard
def draw_board(screen):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            square_color = LIGHT_SQUARE if (row + col) % 2 == 0 else DARK_SQUARE
            pygame.draw.rect(screen, square_color, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    # Draw grid lines (optional)
    for row in range(BOARD_SIZE + 1):
        pygame.draw.line(screen, (0, 0, 0), (0, row * SQUARE_SIZE), (BOARD_SIZE * SQUARE_SIZE, row * SQUARE_SIZE))
    for col in range(BOARD_SIZE + 1):
        pygame.draw.line(screen, (0, 0, 0), (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, BOARD_SIZE * SQUARE_SIZE))

# Function to draw chess pieces
def draw_pieces(screen, pieces):
    font = pygame.font.SysFont(None, 60)

    # Draw pieces on the board
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            piece = pieces[row][col]
            if piece:
                text = font.render(piece, True, (0, 0, 0) if piece.islower() else (255, 255, 255))
                screen.blit(text, (col * SQUARE_SIZE + SQUARE_SIZE // 4, row * SQUARE_SIZE + SQUARE_SIZE // 4))

import pygame
import sys

# Constants
SQUARE_SIZE = 60
BOARD_SIZE = 8
LIGHT_SQUARE = (240, 217, 181)
DARK_SQUARE = (181, 136, 99)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initial pieces setup (simplified)
pieces = [
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
]

# Colors
LIGHT_SQUARE = (240, 217, 181)
DARK_SQUARE = (181, 136, 99)

# Game state
selected_piece = None
selected_pos = None
current_state = 'None'


# Initialize pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((SQUARE_SIZE * BOARD_SIZE, SQUARE_SIZE * BOARD_SIZE))
pygame.display.set_caption('Chess')

# Function to draw the chessboard
def draw_board():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            square_color = LIGHT_SQUARE if (row + col) % 2 == 0 else DARK_SQUARE
            pygame.draw.rect(screen, square_color, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    # Draw grid lines (optional)
    for row in range(BOARD_SIZE + 1):
        pygame.draw.line(screen, BLACK, (0, row * SQUARE_SIZE), (BOARD_SIZE * SQUARE_SIZE, row * SQUARE_SIZE))
    for col in range(BOARD_SIZE + 1):
        pygame.draw.line(screen, BLACK, (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, BOARD_SIZE * SQUARE_SIZE))

# Function to draw chess pieces
def draw_pieces():
    font = pygame.font.SysFont(None, 60)

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            piece = pieces[row][col]
            if piece:
                text = font.render(piece, True, BLACK if piece.islower() else WHITE)
                screen.blit(text, (col * SQUARE_SIZE + SQUARE_SIZE // 4, row * SQUARE_SIZE + SQUARE_SIZE // 4))

# Function to get the row and column from a position (mouse click)
def get_square_from_pos(pos):
    return pos[1] // SQUARE_SIZE, pos[0] // SQUARE_SIZE

# Function to handle human player's interaction
def handle_input():
    global selected_piece, selected_pos, current_state

    mouse_pos = pygame.mouse.get_pos()
    row, col = get_square_from_pos(mouse_pos)

    if current_state == 'None':
        handle_piece_selection(mouse_pos)
    elif current_state == 'DraggingPiece':
        handle_drag_movement(mouse_pos)
    elif current_state == 'PieceSelected':
        handle_point_and_click_movement(mouse_pos)

    if pygame.mouse.get_pressed()[2]:  # Right mouse button
        cancel_piece_selection()

def handle_piece_selection(mouse_pos):
    global selected_piece, selected_pos, current_state

    if pygame.mouse.get_pressed()[0]:  # Left mouse button
        row, col = get_square_from_pos(mouse_pos)
        if pieces[row][col]:
            selected_pos = (row, col)
            selected_piece = pieces[row][col]
            current_state = 'DraggingPiece'

def handle_drag_movement(mouse_pos):
    global selected_piece, selected_pos

    row, col = get_square_from_pos(mouse_pos)
    # Display the piece following the mouse
    draw_board()
    draw_pieces()
    font = pygame.font.SysFont(None, 60)
    text = font.render(selected_piece, True, BLACK if selected_piece.islower() else WHITE)
    screen.blit(text, (mouse_pos[0] - SQUARE_SIZE // 4, mouse_pos[1] - SQUARE_SIZE // 4))

    # If mouse is released, try placing the piece
    if pygame.mouse.get_pressed()[0] == 0:
        handle_piece_placement(mouse_pos)

def handle_point_and_click_movement(mouse_pos):
    if pygame.mouse.get_pressed()[0]:
        handle_piece_placement(mouse_pos)

def handle_piece_placement(mouse_pos):
    global selected_piece, selected_pos, current_state

    row, col = get_square_from_pos(mouse_pos)

    # Place the piece on the new square
    if pieces[row][col] == '':
        pieces[row][col] = selected_piece
        pieces[selected_pos[0]][selected_pos[1]] = ''
        current_state = 'None'
    else:
        cancel_piece_selection()

def cancel_piece_selection():
    global selected_piece, selected_pos, current_state

    if current_state != 'None':
        current_state = 'None'
        selected_piece = None
        selected_pos = None

# Main game loop
def main():
    global selected_piece, selected_pos, current_state

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Handle player input
        handle_input()

        # Redraw the screen
        screen.fill(WHITE)
        draw_board()
        draw_pieces()

        pygame.display.flip()

if __name__ == "__main__":
    main()

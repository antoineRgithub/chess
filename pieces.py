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

# Function to get the row and column from a position (mouse click)
def get_square_from_pos(pos):
    return pos[1] // 60, pos[0] // 60

# Function to move a piece
def move_piece(pieces, start_pos, end_pos):
    piece = pieces[start_pos[0]][start_pos[1]]
    pieces[end_pos[0]][end_pos[1]] = piece
    pieces[start_pos[0]][start_pos[1]] = ''

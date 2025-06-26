# Utility function for getting square from position
def get_square_from_pos(pos, square_size=60):
    return pos[1] // square_size, pos[0] // square_size

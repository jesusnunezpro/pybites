DOWN, UP, LEFT, RIGHT = '⇓', '⇑', '⇐', '⇒'
START_VALUE = 1


def print_sequence_route(grid, start_coordinates=None):
    """Receive grid string, convert to 2D matrix of ints, find the
       START_VALUE coordinates and move through the numbers in order printing
       them.  Each time you turn append the grid with its corresponding symbol
       (DOWN / UP / LEFT / RIGHT). See the TESTS for more info."""

    lines = grid.splitlines()
    int_matrix = list()

    for line in lines[1::2]: # This cycles through every other line where we actually expect data
        numbers = [int(token) for token in line.split(' ') if token.isdigit()]
        if len(numbers) > 0:
            int_matrix.append(numbers)
    
    # At this point we have a matrix of numbers
    # we'll now try to locate the starting point
    x,y = 0, 0
    for i, row in enumerate(int_matrix):
        for j, value in enumerate(row):
            if value == 1:
                y,x = i,j
                break
    
    # We're assuming we need to turn clockwise DOWN, LEFT, UP and RIGHT
    straight_numbers = ["1"]
    last_number = 1
    x += 1 # move one position to the right
    while True:
        # Scroll RIGHT until it doesn't increase by one
        for x1 in range(x, len(int_matrix)):
            if int_matrix[y][x1] == (int_matrix[y][x1-1]+1):
                straight_numbers.append(str(int_matrix[y][x1]))
                x += 1
            else:
                break
        # Assuming examples end in the top-right corner
        if y==0 and x == len(int_matrix):
            print(" ".join(straight_numbers))
            break
        else:
            straight_numbers.append(DOWN)
        print(" ".join(straight_numbers))
        x -= 1
        y += 1
        straight_numbers.clear()
        # Scroll DOWN until it doesn't increase by one
        for y1 in range(y, len(int_matrix)):
            if int_matrix[y1][x] == (int_matrix[y1-1][x]+1):
                straight_numbers.append(str(int_matrix[y1][x]))
                y += 1
            else:

                break
        straight_numbers.append(LEFT)
        print(" ".join(straight_numbers))
        y -= 1
        x -= 1
        straight_numbers.clear()
        # Scroll LEFT until it doesn't increase by one
        for x1 in range(x, -1, -1):
            if int_matrix[y][x1] == (int_matrix[y][x1+1]+1):
                straight_numbers.append(str(int_matrix[y][x1]))
                x -= 1
            else:
                break
        straight_numbers.append(UP)
        print(" ".join(straight_numbers))
        x += 1
        y -= 1
        straight_numbers.clear()
        # Scroll UP until it doesn't increase by one
        for y1 in range(y, -1, -1):
            if int_matrix[y1][x] == (int_matrix[y1+1][x]+1):
                straight_numbers.append(str(int_matrix[y1][x]))
                y -= 1
            else:
                break
        straight_numbers.append(RIGHT)
        print(" ".join(straight_numbers))
        y += 1
        x += 1
        straight_numbers.clear()
        


small_grid = """
21 - 22 - 23 - 24 - 25
 |
20    7 -  8 -  9 - 10
 |    |              |
19    6    1 -  2   11
 |    |         |    |
18    5 -  4 -  3   12
 |                   |
17 - 16 - 15 - 14 - 13
"""

if __name__ == "__main__":
    print_sequence_route(small_grid)
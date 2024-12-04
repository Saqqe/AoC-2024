import re
import os
os.chdir(os.path.dirname(__file__))


def count_occurrences(grid, word):
    # Define all 8 directions
    directions = [
        (0, 1),  # Right
        (0, -1),  # Left
        (1, 0),  # Down
        (-1, 0),  # Up
        (1, 1),  # Diagonal Down-Right
        (1, -1),  # Diagonal Down-Left
        (-1, 1),  # Diagonal Up-Right
        (-1, -1),  # Diagonal Up-Left
    ]
    
    def is_within_bounds(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])
    
    def search_from(x, y, direction):
        dx, dy = direction
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            if not is_within_bounds(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True

    count = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for direction in directions:
                if search_from(x, y, direction):
                    count += 1
    return count


def read_grid_from_file(file_path):
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file.readlines() if line.strip()]
    return grid


def count_x_mas_patterns(grid):
    """
    Count the number of "X-MAS" patterns in the grid where the "X" can have 
    MAS written forwards or backwards along the diagonals.
    """
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def is_mas_x_pattern_any_order(r, c):
        # Check bounds for a 3x3 submatrix
        if r - 1 < 0 or r + 1 >= rows or c - 1 < 0 or c + 1 >= cols:
            return False
        # Ensure the center is 'A'
        if grid[r][c] != 'A':
            return False
        # Get diagonal elements
        top_left = grid[r - 1][c - 1]
        top_right = grid[r - 1][c + 1]
        bottom_left = grid[r + 1][c - 1]
        bottom_right = grid[r + 1][c + 1]
        # Check if diagonals form a valid "X" pattern (forwards or backwards)
        return (
            (top_left, bottom_right) in [('M', 'S'), ('S', 'M')] and
            (top_right, bottom_left) in [('M', 'S'), ('S', 'M')]
        )

    # Search for the pattern
    for r in range(rows):
        for c in range(cols):
            if is_mas_x_pattern_any_order(r, c):
                count += 1

    return count



if __name__ == "__main__":
    file_path = "input.txt"
    #file_path = "testData_day4.txt"

    grid = read_grid_from_file(file_path)

    # Count occurrences of "XMAS"
    word_to_find = "XMAS"
    occurrences = count_occurrences(grid, word_to_find)
    print(occurrences)

    # Count "X-MAS" patterns
    xmas_count = count_x_mas_patterns(grid)
    print(f'puzzel 2: ', xmas_count)
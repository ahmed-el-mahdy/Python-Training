grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# Outer loop iterates over columns (x-coordinates)
for col in range(len(grid[0])):  # len(grid[0]) gives the number of columns (6 in this case)
    # Inner loop iterates over rows (y-coordinates)
    for row in range(len(grid)):  # len(grid) gives the number of rows (9 in this case)
        print(grid[row][col], end='')  # Print the character at (row, col) without a newline
    print()  # After printing one column, move to the next line

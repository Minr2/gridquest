def findinputs(grid):
    start = (-1, -1)
    end = (-1, -1)
    rows = len(grid)
    cols = len(grid[0])
    checkpoints = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 's':
                start = (i, j)
            if grid[i][j] == 'e':
                end = (i, j)
            if grid[i][j] == 'c':
                checkpoints += 1
    return (start, end, rows, cols, checkpoints)
# AOC DAY 6

def day6(p_row, p_col, grid, new_obstacle=None):

    d = 'N'
    rotation = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
    proceed = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}
    path = []
    obstacles = set()

    c_row, c_col = p_row - 1, p_col
    while c_row in range(0, s) and c_col in range(0, s):
        if new_obstacle:
            if (d, c_row, c_col) in obstacles:
                return None
            else:
                obstacles.add((d, c_row, c_col))

        if new_obstacle == (c_row, c_col):
            current = '#'
        else:
            current = grid[c_row][c_col]

        if current == '#':
            d = rotation[d]
            c_row, c_col = p_row, p_col
        else:
            path.append((c_row, c_col))

        p_row, p_col = c_row, c_col
        c_row, c_col = c_row + proceed[d][0], c_col + proceed[d][1]

    return set(path)




if __name__ == "__main__":
    with open('input/6.txt') as f:
        data = f.read()

    clean_data = data.splitlines()
    s = len(clean_data)
    g_id = data.replace('\n', '').index('^')
    row, col = g_id//s, g_id%s

    grid = clean_data.copy()
    path = day6(row, col, grid)

    print("The solution for part 1 is:", len(path))
    print('Working on solution 2 (may take up to 15 seconds)')

    path.discard((row, col))
    path_list = list(path)
    c = 0
    for p in path:
        if not day6(row, col, grid, p):
            c += 1

    print("The solution for part 2 is:", c)

import astarbasic

def aStaradvanced(grid, start, end, rows, cols, cps) -> list:
    checked_states = {}

    # finding distances between checkpoints
    checkpoints = [(start[0], start[1])]
    ind = 1
    for i in range(rows):
        for j in range(cols):
           if grid[i][j] == 'c':
                checkpoints.append((i, j))
                ind += 1
    checkpoints.append((end[0], end[1]))

    cp_aStar = [[0 for _ in range(cps+2)] for _ in range(cps+2)]

    for i in range(cps+2):
        for j in range(cps+2):
            if not i == j:
                if not astarbasic.aStar(grid, checkpoints[i], checkpoints[j], rows, cols) == []:
                    cp_aStar[i][j] = len(astarbasic.aStar(grid, checkpoints[i], checkpoints[j], rows, cols)) - 1
                else:
                    cp_aStar[i][j] = 9999999999

    def visit(mask, u):
        # Using some bitmasking in this function
        # check if everything is visited!
        if mask == (1 << cps) -1:
            # print(f'{u}. {cp_aStar[u][cps+1]}')
            return cp_aStar[u][cps + 1], [cps + 1]
        
        cur_state = (mask, u)
        if cur_state in checked_states:
            return checked_states[cur_state]
        
        min_dist = float('inf')
        shortest_path = []

        for i in range(cps):
            # checks if visited (bitmask)
            if not (mask & (1<<i)):
                new_mask = mask | (1<<i)
                # print(new_mask)
                g, path = visit(new_mask, i+1)
                # print(f'{u}  {i+1}   {cp_aStar[u][i+1]}     {g}')
                f = cp_aStar[u][i+1] + g

                if f < min_dist:
                    min_dist = f
                    shortest_path = [i+1] + path


        checked_states[cur_state] = (min_dist, shortest_path)
        return checked_states[cur_state]

    final_min_dist, final_shortest_path = visit(0, 0)
    print(final_min_dist)
    final_shortest_path = [0] + final_shortest_path
    for i in range(cps + 1):
        for j in range(1, len(astarbasic.aStar(grid, checkpoints[final_shortest_path[i]], checkpoints[final_shortest_path[i+1]], rows, cols))):
            print(astarbasic.aStar(grid, checkpoints[final_shortest_path[i]], checkpoints[final_shortest_path[i+1]], rows, cols)[j])
    return final_shortest_path

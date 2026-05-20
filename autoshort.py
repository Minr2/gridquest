# calculate shortest distance
def findstart(list, rows, cols):
    for i in range(rows):
        for j in range(cols):
            if list[i][j] == 's':
                return [i, j]
    return [-1, -1]

vchen = []
visited = []

def popnew(list, cur, rows, cols) -> bool:
    vchen.pop(0)
    # print(cur[0], end= ' ')
    # print(cur[1])
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            r = cur[0] + i
            c = cur[1] + j
            if r >= 0 and r < rows:
                if c >= 0 and c < cols:
                    # print(r, end='')
                    # print(c)
                    try:
                        if not list[r][c] == 'x' and not visited[r][c]:
                            if list[r][c] == 'e':
                                return True
                            # print("append")
                            vchen.append([r, c])
                            visited[r][c] = True
                    except:
                        # print("fail")
                        continue
    return False

def autoshort(list, rows, cols) -> int:
    global visited
    start = findstart(list, rows, cols)
    vchen.append(start)
    # print(start[0])
    # print(start[1])

    visited = [[False for _ in range(rows)] for _ in range(cols)]
    visited[start[0]][start[1]] = True

    steps = 0
    while steps < 5:
        steps += 1
        length = len(vchen)
        # print(f"len = {length}")
        for i in range(length):
            if popnew(list, vchen[0], rows, cols):
                return steps
    return -1
        

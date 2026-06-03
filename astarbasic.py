import heapq

class Node:
    def __init__(self, prev, state):
        self.prev = prev
        self.state = state
        self.f = 0
        self.g = 0
        self.h = 0

    def __lt__(self, other):
        if self.f == other.f:
            return self.g > other.g
        return self.f < other.f
    
def distance(pos1, pos2):
    # min distance ignoring obstacles (underestimation)
    return(max(abs(pos1[0] - pos2[0]), abs(pos1[1] - pos2[1])))

def aStar(grid, start, end, rows, cols) -> list:
    start_n = Node(None, start)

    # open_list is a heap
    open_list = []
    heapq.heappush(open_list, start_n)

    # set so we can do _ in _
    closed_list = set()

    # lowest g score for each coordinate
    lowest_g = {start: 0}

    while len(open_list) > 0:
        cur_n = heapq.heappop(open_list)
        closed_list.add(cur_n.state)

        # reached end
        if cur_n.state == end:
            retpath = []
            cur = cur_n
            # like backtrack to find the tracked path
            while cur is not None:
                retpath.append(cur.state)
                cur = cur.prev
            # reversed list
            return retpath[::-1]
        
        # find neighbours
        neighbours = []
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for dir in dirs:
            nrow = cur_n.state[0] + dir[0]
            ncol = cur_n.state[1] + dir[1]
            if (nrow < 0 or nrow >= rows or ncol < 0 or ncol >= cols):
                continue
            if grid[nrow][ncol] == 'x':
                continue
            neighbours.append(Node(cur_n, (nrow, ncol)))
        
        for neighbour in neighbours:
            if neighbour.state in closed_list:
                continue

            # now passed conditions, run a# again
            neighbour.g += 1
            neighbour.h = distance(neighbour.state, end)
            neighbour.f = neighbour.g + neighbour.h

            if neighbour.state not in lowest_g or 1 + cur_n.g < lowest_g[neighbour.state]:
                lowest_g[neighbour.state] = 1 + cur_n.g
            
            # print(closed_list)
            heapq.heappush(open_list, neighbour)


    
    return []



            







    
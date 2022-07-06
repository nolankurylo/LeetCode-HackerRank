
# BFS 1 by one trakcng total distance
def BFS(start, goal, grid, width, height):
    queue = [[(start[0], start[1],0)]]
    visited = []
    new_dist = 0
    while queue:
        path = queue.pop(0)
        x, y, dist = path[-1]
        new_dist = dist + 1
        if (x, y) == goal:
            return new_dist
        nextNodes = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        for nextNode in nextNodes:
            nextX, nextY = nextNode
            # print(f"nextX {nextX} nextY {nextY}")
            if (nextX, nextY) in visited:
                continue
            if 0 <= nextX < width and 0 <= nextY < height and grid[nextX][nextY] != 'X':
                queue.append(path + [(nextX, nextY, new_dist)])
                visited.append((nextX, nextY))
                # print(f"added xy: {(nextX, nextY)}")
    return -1



# BFS by number corners
from collections import deque

def BFS(start, goal, grid, width, height):
    visited_nodes = set()
    queue = deque()
    queue.appendleft((start[0], start[1], 0))
    

    while queue:
        (x, y, dist) = queue.pop()
        new_dist = dist + 1
        nextNodes = [(-1, 0),(1, 0), (0, -1),(0, 1),]
        for neighbour in nextNodes:
            nextX, nextY = x+neighbour[0], y+neighbour[1]

            while (0 <= nextX < width) and (0 <= nextY < height) and (grid[nextX][nextY] != 'X'):
                if (nextX, nextY) == (goalX, goalY):
                    return new_dist
                elif (nextX, nextY) not in visited_nodes:
                    queue.appendleft((nextX, nextY, new_dist))
                    visited_nodes.add((nextX, nextY))
                nextX += neighbour[0]
                nextY += neighbour[1]     
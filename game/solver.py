
from collections import deque


def solve_maze(maze, start=(1, 1), goal=None):
    rows, cols = len(maze), len(maze[0])

    if goal is None:
        goal = (rows - 2, cols - 2)

    queue = deque([start])
    parent = {start: None}

    while queue:
        r, c = queue.popleft()

        if (r, c) == goal:
            path = []
            current = goal

            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1]

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            neighbor = (nr, nc)

            if (
                0 <= nr < rows
                and 0 <= nc < cols
                and maze[nr][nc] == 0
                and neighbor not in parent
            ):
                parent[neighbor] = (r, c)
                queue.append(neighbor)

    return []

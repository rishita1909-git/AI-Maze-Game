
import random


def generate_maze(size=21):
    # Maze size must be odd and at least 5
    size = max(5, size)

    if size % 2 == 0:
        size += 1

    maze = [[1 for _ in range(size)] for _ in range(size)]

    def carve(r, c):
        maze[r][c] = 0

        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        random.shuffle(directions)

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            if (
                1 <= nr < size - 1
                and 1 <= nc < size - 1
                and maze[nr][nc] == 1
            ):
                maze[r + dr // 2][c + dc // 2] = 0
                carve(nr, nc)

    carve(1, 1)

    # Ensure the goal cell is accessible
    maze[size - 2][size - 2] = 0

    return maze

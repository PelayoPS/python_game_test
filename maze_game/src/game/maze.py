# maze.py
import random
from settings import CELL_EMPTY, CELL_WALL, CELL_EXIT, CELL_START

def generate_maze(width, height):
    """
    Genera un laberinto de tamaño `width` x `height` usando Recursive Backtracking.
    """
    width = (width // 2) * 2 + 1
    height = (height // 2) * 2 + 1
    maze = [[CELL_WALL for _ in range(width)] for _ in range(height)]
    start_x, start_y = 1, 1
    maze[start_y][start_x] = CELL_EMPTY
    directions = [(0, -2), (2, 0), (0, 2), (-2, 0)]

    def carve(x, y):
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx < width - 1 and 1 <= ny < height - 1 and maze[ny][nx] == CELL_WALL:
                maze[y + dy // 2][x + dx // 2] = CELL_EMPTY
                maze[ny][nx] = CELL_EMPTY
                carve(nx, ny)

    carve(start_x, start_y)
    maze[0][1] = CELL_EMPTY
    maze[height - 1][width - 2] = CELL_EXIT
    return maze

if __name__ == "__main__":
    maze = generate_maze(10, 10)
    for row in maze:
        print(row)
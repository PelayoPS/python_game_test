# maze.py

import random

def generate_maze(width, height):
    """
    Genera un laberinto de tamaño `width` x `height` usando Recursive Backtracking.
    0 representa camino y 1 representa pared.
    """
    maze = [[1 for _ in range(width)] for _ in range(height)]
    

    def carve_passages(cx, cy):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = cx + dx * 2, cy + dy * 2
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 1:
                maze[cy + dy][cx + dx] = 0
                maze[ny][nx] = 0
                carve_passages(nx, ny)

    # Asegurar que la casilla de entrada y salida sean caminos
    maze[1][1] = 0
    maze[height - 2][width - 2] = 0

    # Iniciar en la posición (1,1)
    maze[1][1] = 0
    carve_passages(1, 1)

    # Añadir un marco al laberinto
    for i in range(width):
        maze[0][i] = 1
        maze[height - 1][i] = 1
    for i in range(height):
        maze[i][0] = 1
        maze[i][width - 1] = 1

    return maze

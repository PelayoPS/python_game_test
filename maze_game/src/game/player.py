# player.py

import numpy as np

class Player:
    def __init__(self, start_pos, start_angle):
        self.pos = np.array(start_pos, dtype=float)  # Usar numpy array para precisión
        self.angle = start_angle
        self.direction = np.array([0, 0], dtype=float)

    def move(self, velocity, maze):
        """
        Mueve al jugador si la nueva posición no es una pared.
        """
        if np.linalg.norm(velocity) != 0:
            self.direction = np.array(velocity)
        new_pos = self.pos + np.array(velocity)
        if 1 <= int(new_pos[0]) < len(maze[0]) - 1 and 1 <= int(new_pos[1]) < len(maze) - 1:
            if maze[int(new_pos[1])][int(new_pos[0])] == 0:
                self.pos = new_pos
            else:
                # Ajustar la posición para evitar superposición con paredes
                if maze[int(self.pos[1])][int(new_pos[0])] == 0:
                    self.pos[0] = new_pos[0]
                if maze[int(new_pos[1])][int(self.pos[0])] == 0:
                    self.pos[1] = new_pos[1]
        else:
            # Check individual directions to avoid getting stuck in walls
            if 1 <= int(new_pos[0]) < len(maze[0]) - 1 and maze[int(self.pos[1])][int(new_pos[0])] == 0:
                self.pos[0] = new_pos[0]
            if 1 <= int(new_pos[1]) < len(maze) - 1 and maze[int(new_pos[1])][int(self.pos[0])] == 0:
                self.pos[1] = new_pos[1]

    def get_direction(self):
        """
        Obtiene la dirección del movimiento del jugador.
        """
        if np.linalg.norm(self.direction) == 0:
            return np.array([0, 0])
        return self.direction / np.linalg.norm(self.direction)

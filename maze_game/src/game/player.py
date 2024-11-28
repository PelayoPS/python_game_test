# player.py

import numpy as np

class Player:
    def __init__(self, start_pos, start_angle):
        self.pos = np.array(start_pos, dtype=float)  # Usar numpy array para precisión
        self.angle = start_angle
        self.direction = np.array([0, 0], dtype=float)

    def move(self, velocity, maze):
        """
        Mueve al jugador sin tener en cuenta las paredes o los límites del mapa.
        """
        if np.linalg.norm(velocity) != 0:
            self.direction = np.array(velocity)
        self.pos += np.array(velocity)

    def get_direction(self):
        """
        Obtiene la dirección del movimiento del jugador.
        """
        if np.linalg.norm(self.direction) == 0:
            return np.array([0, 0])
        return self.direction / np.linalg.norm(self.direction)

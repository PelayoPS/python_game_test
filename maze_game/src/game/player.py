# player.py

import numpy as np

class Player:
    def __init__(self, start_pos, start_angle):
        self.pos = np.array(start_pos, dtype=float)  # Usar numpy array para precisión
        self.angle = start_angle
        self.direction = np.array([0, 0], dtype=float)

    def move(self, velocity, maze):
        """
        Mueve al jugador de una casilla a otra teniendo en cuenta las paredes o los límites del mapa.
        """
        if np.linalg.norm(velocity) != 0:
            self.direction = np.array(velocity)
        new_pos = self.pos + velocity

        if not self.check_collision(new_pos, maze) and self.check_bounds(new_pos, maze):
            # Redondear la posición a la casilla más cercana
            self.pos = np.round(new_pos)
        else:
            self.pos = np.round(self.pos)
        

    def get_direction(self):
        """
        Obtiene la dirección del movimiento del jugador.
        """
        if np.linalg.norm(self.direction) == 0:
            return np.array([0, 0])
        return self.direction / np.linalg.norm(self.direction)
    
    def check_collision(self, new_pos, maze):
        """
        Verifica si hay una colisión en la nueva posición antes de que el jugador se mueva en las cuatro direcciones.
        """
        x, y = new_pos.astype(int)
        return maze[y][x] == 1
        
    
    def check_bounds(self, new_pos, maze):
        """
        Verifica si la nueva posición está dentro de los límites del mapa.
        """
        x, y = new_pos.astype(int)
        return maze[y][x] == 2

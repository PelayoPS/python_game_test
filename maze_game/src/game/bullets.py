# bullets.py

import numpy as np
from settings import CELL_SIZE, COLORS
import pygame

class Bullet:
    def __init__(self, pos, direction):
        self.pos = np.array(pos, dtype=float) + np.array([0.5, 0.5])  # Usar numpy array para precisión y ajustar la posición al centro del jugador
        self.direction = np.array(direction, dtype=float)
        self.speed = 0.2

    def update(self, maze):
        """
        Actualiza la posición de la bala.
        """
        new_pos = self.pos + self.direction * self.speed
        if 0 <= int(new_pos[0]) < len(maze[0]) and 0 <= int(new_pos[1]) < len(maze):
            if maze[int(new_pos[1])][int(new_pos[0])] == 0:
                self.pos = new_pos
            else:
                # Si golpea una pared, podrías eliminar la bala
                # Aquí se puede implementar la lógica para eliminar la bala
                pass
        else:
            # Fuera de los límites, podrías eliminar la bala
            pass

    def draw(self, screen):
        """
        Dibuja la bala en la pantalla principal.
        """
        pygame.draw.circle(
            screen,
            COLORS["YELLOW"],
            (
                int(self.pos[0] * CELL_SIZE),
                int(self.pos[1] * CELL_SIZE),
            ),
            CELL_SIZE // 5,
        )

# visuals/rendering.py

import pygame
from settings import *

def draw_player(screen, player):
    """
    Dibuja al jugador en la vista principal.
    """
    cell_size = CELL_SIZE
    pygame.draw.circle(
        screen,
        COLORS["WHITE"],
        (
            int(player.pos[0] * cell_size + cell_size / 2),
            int(player.pos[1] * cell_size + cell_size / 2),
        ),
        int(cell_size / 4),  # Ajustar el tamaño del jugador
    )

def draw_bullets(screen, bullets):
    """
    Dibuja las balas en la vista principal.
    """
    for bullet in bullets:
        pygame.draw.circle(
            screen,
            COLORS["YELLOW"],
            (
                int(bullet.pos[0] * CELL_SIZE),
                int(bullet.pos[1] * CELL_SIZE),
            ),
            CELL_SIZE // 5,
        )

def draw_map(screen, map_data):
    """
    Dibuja el mapa en la pantalla principal.
    """
    cell_size = CELL_SIZE
    for y, row in enumerate(map_data):
        for x, cell in enumerate(row):
            color = COLORS["GREEN"] if cell == 0 else COLORS["BLUE"]
            pygame.draw.rect(
                screen,
                color,
                (
                    x * cell_size,
                    y * cell_size,
                    cell_size,
                    cell_size,
                )
            )

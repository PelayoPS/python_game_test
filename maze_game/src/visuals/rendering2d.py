# visuals/rendering.py

import pygame
from settings import *



def get_textures():
    """
    Carga las texturas del juego.
    """
    cell_1 = pygame.image.load("maze_game/assets/2d/grass.png")
    cell_2 = pygame.image.load("maze_game/assets/2d/wall.png")
    cell_1 = pygame.transform.scale(cell_1, (CELL_SIZE, CELL_SIZE))
    cell_2 = pygame.transform.scale(cell_2, (CELL_SIZE, CELL_SIZE))
    return cell_1, cell_2
    

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


def draw_map(screen, map_data, cell_1, cell_2):
    """
    Dibuja el mapa en la pantalla principal.
    """
    cell_size = CELL_SIZE
    for y, row in enumerate(map_data):
        for x, cell in enumerate(row):
            if (x, y) == (1, 1):
                color = COLORS["WHITE"]  # Casilla de entrada
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
            elif (x, y) == (len(row) - 2, len(map_data) - 2):
                color = COLORS["RED"]  # Casilla de salida
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
            elif cell == 0:
                # Dibuja la textura en las celdas transparentes
                screen.blit(cell_1, (x * cell_size, y * cell_size))
            elif cell == 1:
                screen.blit(cell_2, (x * cell_size, y * cell_size))
            else:
                color = COLORS["BLACK"]
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
                    
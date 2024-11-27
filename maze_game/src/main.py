# main.py

import pygame
from pygame.locals import *
from settings import *
from game.maze import generate_maze
from game.player import Player
from game.bullets import Bullet
from visuals.rendering import draw_player, draw_bullets, draw_map
import numpy as np

def handle_events():
    """
    Maneja los eventos de pygame.
    """
    for event in pygame.event.get():
        if event.type == QUIT:
            return False
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            return False
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            bullets.append(Bullet(player.pos, player.get_direction()))
    return True

def update_player_movement(keys):
    """
    Actualiza el movimiento del jugador basado en las teclas presionadas.
    """
    velocity_changes = {
        K_UP: (0, -MOVE_SPEED),
        K_DOWN: (0, MOVE_SPEED),
        K_LEFT: (-MOVE_SPEED, 0),
        K_RIGHT: (MOVE_SPEED, 0)
    }
    velocity = [sum(change) for change in zip(*[velocity_changes[key] for key in velocity_changes if keys[key]])] or [0, 0]
    player.move(velocity, map_data)

def update_bullets():
    """
    Actualiza la posición de las balas y elimina las que han salido del mapa.
    """
    global bullets
    bullets = [bullet for bullet in bullets if bullet.update(map_data) or (0 <= bullet.pos[0] < MAP_WIDTH and 0 <= bullet.pos[1] < MAP_HEIGHT)]

def draw_screen(screen, map_data, player, bullets):
    """
    Dibuja todos los elementos en la pantalla.
    """
    screen.fill(COLORS["BLACK"])
    draw_map(screen, map_data)
    draw_player(screen, player)
    draw_bullets(screen, bullets)
    pygame.display.flip()

def main():
    # Inicializar pygame
    pygame.init()
    if FULLSCREEN:
        screen = pygame.display.set_mode((0, 0), pygame.NOFRAME)
        screen_width, screen_height = screen.get_size()
    else:
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        screen_width, screen_height = SCREEN_WIDTH, SCREEN_HEIGHT
    pygame.display.set_caption("Laberinto 2D")
    clock = pygame.time.Clock()

    # Ajustar las dimensiones del mapa al tamaño de la ventana
    global MAP_WIDTH, MAP_HEIGHT, map_data, player, bullets
    MAP_WIDTH = screen_width // CELL_SIZE
    MAP_HEIGHT = screen_height // CELL_SIZE

    # Generar laberinto
    map_data = generate_maze(MAP_WIDTH, MAP_HEIGHT)

    # Crear jugador
    player = Player(START_POS, START_ANGLE)

    # Lista para almacenar las balas
    bullets = []

    # Bucle principal
    running = True
    while running:
        running = handle_events()
        keys = pygame.key.get_pressed()
        update_player_movement(keys)
        update_bullets()
        draw_screen(screen, map_data, player, bullets)
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()

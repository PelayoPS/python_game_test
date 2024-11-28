# main.py

import pygame
from pygame.locals import *
from settings import *
from game.maze import generate_maze
from game.player import Player
from game.bullets import Bullet
from visuals.rendering2d import draw_player, draw_bullets, draw_map, get_textures
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
    Actualiza la posición de las balas y elimina las que han salido del mapa o colisionado.
    """
    global bullets
    bullets = [bullet for bullet in bullets if bullet.update(map_data)]

def draw_screen(screen, map_data, player, bullets):
    """
    Dibuja todos los elementos en la pantalla.
    """
    cell_1, cell_2 = get_textures()
    screen.fill(COLORS["BLACK"])
    draw_map(screen, map_data, cell_1, cell_2)
    draw_player(screen, player)
    draw_bullets(screen, bullets)
    pygame.display.flip()

def check_victory():
    """
    Verifica si el jugador ha llegado a la casilla de salida.
    """
    return int(player.pos[0]) == EXIT_POS[0] and int(player.pos[1]) == EXIT_POS[1]

def draw_victory_screen(screen):
    """
    Dibuja la pantalla de victoria con dos botones: volver a jugar y salir.
    """
    screen.fill(COLORS["BLACK"])
    font = pygame.font.Font(None, 74)
    text = font.render("¡Victoria!", True, COLORS["WHITE"])
    screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, screen.get_height() // 4))

    font = pygame.font.Font(None, 36)
    replay_button = pygame.Rect(screen.get_width() // 4, screen.get_height() // 2, 200, 50)
    exit_button = pygame.Rect(screen.get_width() // 2 + 50, screen.get_height() // 2, 200, 50)

    pygame.draw.rect(screen, COLORS["GREEN"], replay_button)
    pygame.draw.rect(screen, COLORS["RED"], exit_button)

    replay_text = font.render("Volver a jugar", True, COLORS["BLACK"])
    exit_text = font.render("Salir", True, COLORS["BLACK"])

    screen.blit(replay_text, (replay_button.x + (replay_button.width - replay_text.get_width()) // 2, replay_button.y + (replay_button.height - replay_text.get_height()) // 2))
    screen.blit(exit_text, (exit_button.x + (exit_button.width - exit_text.get_width()) // 2, exit_button.y + (exit_button.height - exit_text.get_height()) // 2))

    pygame.display.flip()
    return replay_button, exit_button

def main():
    # Inicializar pygame
    pygame.init()
    
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
    victory = False
    while running:
        if victory:
            replay_button, exit_button = draw_victory_screen(screen)
            for event in pygame.event.get():
                if (
                    event.type != QUIT
                    and event.type == MOUSEBUTTONDOWN
                    and replay_button.collidepoint(event.pos)
                ):
                    map_data = generate_maze(MAP_WIDTH, MAP_HEIGHT)
                    player = Player(START_POS, START_ANGLE)
                    bullets = []
                    victory = False
                elif (
                    event.type != QUIT
                    and event.type == MOUSEBUTTONDOWN
                    and not replay_button.collidepoint(event.pos)
                    and exit_button.collidepoint(event.pos)
                    or event.type == QUIT
                ):
                    running = False
        else:
            if not handle_events():
                running = False
            keys = pygame.key.get_pressed()
            update_player_movement(keys)
            update_bullets()
            draw_screen(screen, map_data, player, bullets)
            if check_victory():
                victory = True
            clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()

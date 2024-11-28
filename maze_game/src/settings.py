# settings.py

# Configuración de la pantalla
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FULLSCREEN = True  # Cambiar a True para modo windowed fullscreen

# Tamaño de cada celda del mapa
CELL_SIZE = 15 # Aumentar el tamaño de la celda para mayor precisión

# Dimensiones del mapa
MAP_WIDTH = SCREEN_WIDTH // CELL_SIZE
MAP_HEIGHT = SCREEN_HEIGHT // CELL_SIZE

# Posición y ángulo inicial del jugador
START_POS = [1, 1]  # Asegurar que el jugador empiece en la casilla de entrada
START_ANGLE = 0

# Casilla de salida
EXIT_POS = [MAP_WIDTH - 2, MAP_HEIGHT - 2]  # Asegurar que la salida esté en la esquina opuesta

# Velocidad de movimiento y rotación
MOVE_SPEED = 0.1
ROTATION_SPEED = 0.03

# Frames por segundo
FPS = 60

# Ruta de la textura de la pared
TEXTURE_PATH = "assets/textures/texture_wall.png"

# Valores de las casillas del mapa
CELL_EMPTY = 0
CELL_WALL = 1
CELL_EXIT = 2
CELL_START = 3

# Colores
COLORS = {
    "WHITE": (255, 255, 255),
    "GREEN": (0, 255, 0),
    "BLUE": (0, 0, 255),
    "RED": (255, 0, 0),
    "BLACK": (0, 0, 0),
    "YELLOW": (255, 255, 0),
    "TRANSPARENT": (0, 0, 0, 0),
}

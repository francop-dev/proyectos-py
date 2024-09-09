import pygame
import sys

# Inicializa Pygame
pygame.init()

# Configura la pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Movimiento con teclas personalizadas")

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Configura el objeto
x, y = 400, 300
width, height = 50, 50
velocity = 5

# Teclas personalizadas
MOVE_LEFT_KEY = pygame.K_a  # Cambia esto por la tecla que prefieras para mover a la izquierda
MOVE_RIGHT_KEY = pygame.K_d  # Cambia esto por la tecla que prefieras para mover a la derecha
MOVE_UP_KEY = pygame.K_w     # Cambia esto por la tecla que prefieras para mover hacia arriba
MOVE_DOWN_KEY = pygame.K_s   # Cambia esto por la tecla que prefieras para mover hacia abajo

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Obtiene el estado de todas las teclas
    keys = pygame.key.get_pressed()

    # Mueve el objeto según las teclas presionadas
    if keys[MOVE_LEFT_KEY]:
        x -= velocity
    if keys[MOVE_RIGHT_KEY]:
        x += velocity
    if keys[MOVE_UP_KEY]:
        y -= velocity
    if keys[MOVE_DOWN_KEY]:
        y += velocity

    # Llena la pantalla de blanco
    screen.fill(WHITE)

    # Dibuja el objeto en la pantalla
    pygame.draw.rect(screen, RED, (x, y, width, height))

    # Actualiza la pantalla
    pygame.display.flip()

    # Controla la velocidad del bucle
    pygame.time.Clock().tick(60)

import pygame as pg

pg.init()

# pantalla
PANTALLA = pg.display.set_mode((900,600))
fuente = pg.font.Font(None, 44)

# sonidos
pg.mixer.init()
sonido_rebote_jugadores = pg.mixer.Sound('sonido1.mp3')
sonido_punto = pg.mixer.Sound('sonidopunto.mp3')
sonido_rebote = pg.mixer.Sound('sonido2.mp3')

# Cambiar el titulo y el icono
pg.display.set_caption('Pong')
icono = pg.image.load('138451.png')
pg.display.set_icon(icono)

# valores de inicializacion
ejecutando = True
mi_reloj = pg.time.Clock()

# paleta de colores
BLANCO = (255,255,255)
COLOR_FONDO = (150, 200, 170)
AZUL = (70, 130, 180)
ROJO = (200,70,90)

# puntaje jugadores
jugador_1_puntaje = 0
jugador_2_puntaje = 0
ganador = 3
juego_terminado = False  # Para detener el juego una vez que alguien gane

# valores para tamaño y coordenadas de jugadores
j1_x = 50
j1_y = 250
j2_x = 820
j2_y = 250
ANCHO_PALETA = 30
ALTO_PALETA = 100
velocity = 5

# coordenadas y dimensiones de la pelota
pelota_x = 450
pelota_y = 300
ANCHO_PELOTA = 10
ALTO_PELOTA = 10
pelota_limite_y = 900
pelota_limite_x = 600
pelota_vel_x = 3
pelota_vel_y = 3

# CREAR LOS ELEMENTOS DEL JUEGO
paleta_j1 = pg.Rect(j1_x, j1_y, ANCHO_PALETA, ALTO_PALETA)
paleta_j2 = pg.Rect(j2_x, j2_y, ANCHO_PALETA, ALTO_PALETA)
pelota = pg.Rect(pelota_x, pelota_y, ANCHO_PELOTA, ALTO_PELOTA)

# teclas a utilizar
MOVE_UP_J1 = pg.K_w
MOVE_DOWN_J1 = pg.K_s
MOVE_UP_J2 = pg.K_DOWN
MOVE_DOWN_J2 = pg.K_UP

def dibujar_pantalla():
    PANTALLA.fill(COLOR_FONDO)
    pg.draw.rect(PANTALLA, ROJO, paleta_j2)
    pg.draw.rect(PANTALLA, AZUL, paleta_j1)
    pg.draw.rect(PANTALLA, BLANCO, pelota)

# reiniciar el juego
def resetear_pelota_y_paletas():
    global pelota_x, pelota_y, pelota_vel_x, pelota_vel_y, j1_y, j1_x
    pelota_x = 450
    pelota_y = 300
    pelota_vel_x = 3
    pelota_vel_y = 3
    j1_y = 250
    j2_y = 250

# anunciar ganador
def anunciar_ganador(jugador):
    global superficie_txt_ganador
    superficie_txt_ganador = fuente.render(f'¡GANASTE JUGADOR {jugador}!', True, BLANCO)

# Bucle principal del juego
while ejecutando:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            ejecutando = False

    # Detener el juego cuando haya un ganador
    if not juego_terminado:
        # Movimiento de los rectangulos
        teclas = pg.key.get_pressed()

        # Mover los rectangulos segun la tecla presionada
        if teclas[MOVE_UP_J1]:
            j1_y -= velocity
        if teclas[MOVE_DOWN_J1]:
            j1_y += velocity
        if teclas[MOVE_UP_J2]:
            j2_y += velocity
        if teclas[MOVE_DOWN_J2]:
            j2_y -= velocity

        # Coordenadas de la pelota
        pelota_x += pelota_vel_x
        pelota_y += pelota_vel_y

        # Actualizar posiciones de paletas
        paleta_j1.y = j1_y
        paleta_j2.y = j2_y
        pelota.x = pelota_x
        pelota.y = pelota_y

        # Rebotes y aumento de velocidad cuando un jugador toca la pelota
        if pelota.top < 0 or pelota.bottom > 600:
            pelota_vel_y = -pelota_vel_y
            sonido_rebote.play()
        if pelota.colliderect(paleta_j1):
            pelota_vel_x = -pelota_vel_x
            pelota_vel_x += 0.5
            sonido_rebote_jugadores.play()
        if pelota.colliderect(paleta_j2):
            pelota_vel_x = -pelota_vel_x
            pelota_vel_x -= 0.5
            sonido_rebote_jugadores.play()

        if pelota.right < 0:
            jugador_2_puntaje += 1
            sonido_punto.play()
            resetear_pelota_y_paletas()

        if pelota.left > 900:
            jugador_1_puntaje += 1
            sonido_punto.play()
            resetear_pelota_y_paletas()

        # Verificar si hay ganador
        if jugador_1_puntaje == ganador:
            anunciar_ganador(1)
            juego_terminado = True  # Detener el juego
        elif jugador_2_puntaje == ganador:
            anunciar_ganador(2)
            juego_terminado = True  # Detener el juego

    # Dibujar los puntajes y la pantalla
    dibujar_pantalla()

    # Superficie de texto
    superficie_txt_j1 = fuente.render(f'Puntaje J1: {jugador_1_puntaje}', True, AZUL)
    superficie_txt_j2 = fuente.render(f'Puntaje J2: {jugador_2_puntaje}', True, ROJO)

    PANTALLA.blit(superficie_txt_j1, (150, 80))
    PANTALLA.blit(superficie_txt_j2, (550, 80))

    # Si el juego ha terminado, mostrar al ganador
    if juego_terminado:
        PANTALLA.blit(superficie_txt_ganador, (300, 250))

    pg.display.flip()
    mi_reloj.tick(60)

pg.quit()
quit()

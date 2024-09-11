
import pygame as pg

pg.init()

#pantalla
PANTALLA = pg.display.set_mode((900,600))

#Cambiar el titulo y el icono
pg.display.set_caption('Pong')
icono = pg.image.load('138451.png')
pg.display.set_icon(icono)

#valores de inicializacion
ejecutando = True
mi_reloj = pg.time.Clock()

#paleta de colores
BLANCO = (255,255,255)
COLOR_FONDO = (150, 200, 170)
AZUL = (70, 130, 180)
ROJO = (200,70,90)

#valores para tamaño y coordenadas de jugadores
j1_x = 50
j1_y = 250
j2_x = 820
j2_y = 250
ANCHO_PALETA = 30
ALTO_PALETA = 100
velocity = 5

#coordenadas y dimensiones de la pelota
pelota_x = 450
pelota_y = 300
ANCHO_PELOTA = 10
ALTO_PELOTA = 10

#CREAR LOS ELEMENTOS DEL JUEGO
paleta_j1 = pg.Rect(j1_x, j1_y, ANCHO_PALETA, ALTO_PALETA)
paleta_j2 = pg.Rect(j2_x, j2_y, ANCHO_PALETA, ALTO_PALETA)
pelota = pg.Rect(pelota_x, pelota_y, ANCHO_PELOTA, ALTO_PELOTA)


#teclas a utilizar
MOVE_UP_J1 = pg.K_w
MOVE_DOWN_J1 = pg.K_s
MOVE_UP_J2 = pg.K_DOWN
MOVE_DOWN_J2 = pg.K_UP

def dibujar_pantalla():
    PANTALLA.fill(COLOR_FONDO)
    pg.draw.rect(PANTALLA, ROJO, paleta_j2)
    pg.draw.rect(PANTALLA, AZUL, paleta_j1)
    pg.draw.rect(PANTALLA, BLANCO, pelota)

# Bucle principal del juego
while ejecutando:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            ejecutando = False
    
#movimiento de los rectangulos
    teclas = pg.key.get_pressed()


#mover los rectangulos segun la tecla presionada
    if teclas[MOVE_UP_J1]:
        j1_y -= velocity
    if teclas[MOVE_DOWN_J1]:
        j1_y += velocity
    if teclas[MOVE_UP_J2]:
        j2_y += velocity
    if teclas[MOVE_DOWN_J2]:
        j2_y -= velocity

#actualizar posiciones de paletas

    paleta_j1.y = j1_y
    paleta_j2.y = j2_y

    dibujar_pantalla()


    pg.display.flip()

    mi_reloj.tick(60)


pg.quit
quit()
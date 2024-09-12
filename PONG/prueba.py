import pygame
import sys

# Inicializa Pygame
pygame.init()

# Configura la pantalla
# Inicializar Pygame

pygame.init()



# Configurar la pantalla

pantalla = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Texto con Pygame")



# Configurar la fuente

mi_fuente = pygame.font.Font(None, 74)



# Crear una superficie con el texto

superficie_texto = mi_fuente.render("Hola, Pygame!", True, (255, 255, 255))



# Bucle principal

while True:

  for evento in pygame.event.get():

    if evento.type == pygame.QUIT:

      pygame.quit()

      quit()



  # Dibujar el texto en la pantalla

  pantalla.blit(superficie_texto, (100, 100))



  # Actualizar la pantalla

  pygame.display.flip()
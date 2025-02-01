import pygame
import sys
import time
import os

# Pedir el peso antes de abrir la ventana
peso = float(input("Ingrese su peso: "))

if peso > 60:
    # Inicializar pygame
    pygame.init()

    # Configuración de pantalla
    width, height = 500, 500
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Peso y Reacción")

    # Intentar forzar la ventana al frente (para Windows)
    try:
        import ctypes
        ctypes.windll.user32.SetForegroundWindow(pygame.display.get_wm_info()["window"])
    except:
        pass  # Si no funciona, se ignora el error

    # Cargar imagen y ajustarla a la ventana
    image = pygame.image.load("imagen.png")
    image = pygame.transform.scale(image, (250, 250))

    # Cargar y reproducir la canción
    pygame.mixer.music.load("cancion.mp3")
    pygame.mixer.music.play()

    angle = 0  # Ángulo de rotación
    running = True

    while running:
        screen.fill((255, 255, 255))  # Fondo blanco
        angle += 5  # Aumentar ángulo para girar la imagen
        rotated_image = pygame.transform.rotate(image, angle)  # Rotar imagen
        rect = rotated_image.get_rect(center=(width // 2, height // 2))  # Centrar imagen
        screen.blit(rotated_image, rect.topleft)  # Dibujar imagen girando

        pygame.display.flip()  # Actualizar pantalla
        time.sleep(0.05)  # Controlar velocidad del giro

        # Manejo de eventos para cerrar la ventana
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
    sys.exit()

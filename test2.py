import pygame
import random

# Inicialización de Pygame
pygame.init()

# Definición de constantes
ANCHO, ALTO = 800, 800
CELDA_SIZE = 20
FPS = 10

# Definición de colores
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
MARRON = (139, 69, 19)
AZUL = (0, 0, 255)

# Creación de la ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Simulador de Ecosistemas")

# Definición de clases
class Organismo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Bioma:
    def __init__(self, tipo):
        self.tipo = tipo

# Herencia múltiple para Animal, Planta y Bioma
class Animal(Organismo, Bioma):
    def __init__(self, x, y, color, tipo):
        Organismo.__init__(self, x, y)
        Bioma.__init__(self, tipo)
        self.color = color

    def mover(self, dx, dy):
        self.x += dx
        self.y += dy

class Planta(Organismo, Bioma):
    def __init__(self, x, y, tipo):
        Organismo.__init__(self, x, y)
        Bioma.__init__(self, tipo)

# Inicialización de objetos
cazador = Animal(0, 0, ROJO, "tierra")
presa = Animal(0, 0, VERDE, "tierra")
planta = Planta(0, 0, "tierra")

# Creación de la matriz del bioma
bioma = [["" for _ in range(40)] for _ in range(40)]

# Colocación inicial de organismos
for i in range(10):  # Desierto (primer tercio)
    for j in range(40):
        bioma[i][j] = Bioma("desierto")

for i in range(10, 30):  # Bosque (segundo tercio)
    for j in range(40):
        bioma[i][j] = Bioma("bosque")

for i in range(30, 40):  # Agua (último tercio)
    for j in range(40):
        bioma[i][j] = Bioma("agua")

# Función para dibujar biomas
def dibujar_bioma():
    for i in range(40):
        for j in range(40):
            if bioma[i][j].tipo == "desierto":
                pygame.draw.rect(ventana, pygame.Color("yellow"), (j * CELDA_SIZE, i * CELDA_SIZE, CELDA_SIZE, CELDA_SIZE))
            elif bioma[i][j].tipo == "bosque":
                pygame.draw.rect(ventana, MARRON, (j * CELDA_SIZE, i * CELDA_SIZE, CELDA_SIZE, CELDA_SIZE))
            elif bioma[i][j].tipo == "agua":
                pygame.draw.rect(ventana, AZUL, (j * CELDA_SIZE, i * CELDA_SIZE, CELDA_SIZE, CELDA_SIZE))

# Función para dibujar organismos
def dibujar_organismos():
    pygame.draw.rect(ventana, cazador.color, (cazador.x * CELDA_SIZE, cazador.y * CELDA_SIZE, CELDA_SIZE, CELDA_SIZE))
    pygame.draw.rect(ventana, presa.color, (presa.x * CELDA_SIZE, presa.y * CELDA_SIZE, CELDA_SIZE, CELDA_SIZE))
    pygame.draw.rect(ventana, pygame.Color("green"), (planta.x * CELDA_SIZE, planta.y * CELDA_SIZE, CELDA_SIZE, CELDA_SIZE))

# Función principal
def main():
    reloj = pygame.time.Clock()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Movimiento aleatorio de los organismos
        cazador.mover(random.choice([-2, 0, 2]), random.choice([-2, 0, 2]))
        presa.mover(random.choice([-1, 0, 1]), random.choice([-1, 0, 1]))

        # Limitar la posición de los organismos dentro de la matriz
        cazador.x = max(0, min(cazador.x, 39))
        cazador.y = max(0, min(cazador.y, 39))
        presa.x = max(0, min(presa.x, 39))
        presa.y = max(0, min(presa.y, 39))

        # Dibujar el bioma y los organismos
        ventana.fill(BLANCO)
        dibujar_bioma()
        dibujar_organismos()

        pygame.display.flip()
        reloj.tick(FPS)

if __name__ == "__main__":
    main()

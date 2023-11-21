import pygame
import random

# Tamaño de la ventana y de la matriz
WIDTH, HEIGHT = 1500, 1000
MATRIX_SIZE = 100  # Ahora es una matriz 20x20

# Definición de la clase Bioma
class Bioma:
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path)

# Definición de las clases para cada bioma
class Desierto(Bioma):
    def __init__(self):
        super().__init__("arena.png")  # Reemplaza con la ruta de tu imagen de desierto

class Agua(Bioma):
    def __init__(self):
        super().__init__("agua.png")  # Reemplaza con la ruta de tu imagen de agua

class Bosque(Bioma):
    def __init__(self):
        super().__init__("tierra.png")  # Reemplaza con la ruta de tu imagen de bosque

class Nieve(Bioma):
    def __init__(self):
        super().__init__("nieve.png")  # Reemplaza con la ruta de tu imagen de nieve

# Definición de la clase Animal
class Animal:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        # Implementa la lógica de movimiento aquí
        pass

# Definición de la subclase Leon que hereda de Animal
class Leon(Animal):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        # Implementa la lógica de movimiento específica para el león aquí
        self.x += random.choice([-1, 0, 1])
        self.y += random.choice([-1, 0, 1])

# Función para dibujar la matriz y los animales en la ventana
def draw_matrix(screen, matrix):
    cell_width = WIDTH // MATRIX_SIZE
    cell_height = HEIGHT // MATRIX_SIZE

    # Dibuja los cuadros y líneas de la cuadrícula
    for row in range(MATRIX_SIZE):
        for col in range(MATRIX_SIZE):
            bioma = matrix[row][col]
            image = bioma.image
            image = pygame.transform.scale(image, (cell_width, cell_height))  # Ajusta el tamaño de la imagen
            screen.blit(image, (col * cell_width, row * cell_height))

            pygame.draw.rect(screen, (0, 0, 0), (col * cell_width, row * cell_height, cell_width, cell_height), 1)

    # Líneas de la cuadrícula para los bordes derecho e inferior
    for i in range(1, MATRIX_SIZE):
        pygame.draw.line(screen, (0, 0, 0), (i * cell_width, 0), (i * cell_width, HEIGHT), 1)
        pygame.draw.line(screen, (0, 0, 0), (0, i * cell_height), (WIDTH, i * cell_height), 1)

# Función principal
def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Simulador de Ecosistemas")

    clock = pygame.time.Clock()

    # Crear la matriz que representa el mapa con diferentes biomas
    matrix = [[random.choice([Desierto(), Agua(), Bosque(), Nieve()]) for _ in range(MATRIX_SIZE)] for _ in range(MATRIX_SIZE)]

    # Crear un león en una posición aleatoria
    leon = Leon(random.randint(0, MATRIX_SIZE - 1), random.randint(0, MATRIX_SIZE - 1))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Mueve al león en la matriz
        leon.move()
        leon.x = max(0, min(leon.x, MATRIX_SIZE - 1))
        leon.y = max(0, min(leon.y, MATRIX_SIZE - 1))

        # Limpia la pantalla
        screen.fill((255, 255, 255))

        # Dibuja la matriz y al león en la ventana
        draw_matrix(screen, matrix)
        pygame.draw.rect(screen, (255, 0, 0), (leon.x * (WIDTH // MATRIX_SIZE), leon.y * (HEIGHT // MATRIX_SIZE), WIDTH // MATRIX_SIZE, HEIGHT // MATRIX_SIZE))

        pygame.display.flip()
        clock.tick(5)  # Ajusta la velocidad del juego

    pygame.quit()

if __name__ == "__main__":
    main()

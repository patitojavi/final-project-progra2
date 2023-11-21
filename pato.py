import pygame
import random

# Tamaño de la ventana y de la matriz
WIDTH, HEIGHT = 1600, 1000
MATRIX_SIZE = 100  # Ahora es una matriz 20x20

# Colores
WHITE = (255, 255, 255)
SNOW = (255, 255, 255)
DESERT = (255, 255, 102)
WATER = (102, 178, 255)
FOREST = (34, 139, 34)
GRID_COLOR = (0, 0, 0)

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
            pygame.draw.rect(screen, matrix[row][col], (col * cell_width, row * cell_height, cell_width, cell_height), 0)
            pygame.draw.rect(screen, GRID_COLOR, (col * cell_width, row * cell_height, cell_width, cell_height), 1)

    # Líneas de la cuadrícula para los bordes derecho e inferior
    for i in range(1, MATRIX_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (i * cell_width, 0), (i * cell_width, HEIGHT), 1)
        pygame.draw.line(screen, GRID_COLOR, (0, i * cell_height), (WIDTH, i * cell_height), 1)

# Función principal
def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Simulador de Ecosistemas")

    clock = pygame.time.Clock()

    # Crear la matriz que representa el mapa con diferentes biomas
    matrix = [[FOREST] * MATRIX_SIZE for _ in range(MATRIX_SIZE)]  # Inicializa con nieve en todas las celdas

    # Añadir diferentes biomas de manera aleatoria
    for _ in range(MATRIX_SIZE * MATRIX_SIZE // 4):
        row = random.randint(0, MATRIX_SIZE - 1)
        col = random.randint(0, MATRIX_SIZE - 1)
        matrix[row][col] = random.choice([DESERT, WATER, SNOW])

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
        screen.fill(WHITE)

        # Dibuja la matriz y al león en la ventana
        draw_matrix(screen, matrix)
        pygame.draw.rect(screen, (255, 0, 0), (leon.x * (WIDTH // MATRIX_SIZE), leon.y * (HEIGHT // MATRIX_SIZE), WIDTH // MATRIX_SIZE, HEIGHT // MATRIX_SIZE))

        pygame.display.flip()
        clock.tick(1)  # Ajusta la velocidad del juego

    pygame.quit()

if __name__ == "__main__":
    main()

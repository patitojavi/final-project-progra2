import pygame
import random

# Tamaño de la ventana y de la matriz
WIDTH, HEIGHT = 800, 600
MATRIX_SIZE = 50  # Ahora es una matriz 50x50

# Colores
WHITE = (255, 255, 255)
GRID_COLOR = (0, 0, 0)
LEON_COLOR = (255, 0, 0)  # Rojo
VACA_COLOR = (0, 255, 0)  # Verde
ARBOl_COLOR = (0, 0, 255)  # Azul

class Bioma:
    def __init__(self, color):
        self.color = color

class Desierto(Bioma):
    def __init__(self):
        super().__init__((255, 255, 102))  # Amarillo claro

class Agua(Bioma):
    def __init__(self):
        super().__init__((102, 178, 255))  # Azul claro

class Bosque(Bioma):
    def __init__(self):
        super().__init__((34, 139, 34))  # Verde oscuro

# Definición de la clase Organismo
class Organismo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        # Implementa la lógica de movimiento aquí
        pass

# Definición de la subclase Animales que hereda de Organismo
class Animales(Organismo):
    def __init__(self, x, y, color):
        super().__init__(x, y)
        self.color = color
        self.nivel_agua = 50  # Nivel de agua inicial

    def move(self, bioma):
        # Implementa la lógica de movimiento específica para animales aquí
        self.x += random.choice([-1, 0, 1])
        self.y += random.choice([-1, 0, 1])

        # Actualiza el nivel de agua según el tipo de bioma
        if isinstance(bioma, Agua):
            self.nivel_agua = 100
        elif isinstance(bioma, Desierto):
            self.nivel_agua -= 5
        elif isinstance(bioma, Bosque):
            self.nivel_agua -= 1

        # Asegúrate de que el nivel de agua esté dentro del rango [0, 100]
        self.nivel_agua = max(0, min(self.nivel_agua, 100))

# Definición de la subclase Plantas que hereda de Organismo
class Plantas(Organismo):
    def __init__(self, x, y, color):
        super().__init__(x, y)
        self.color = color

    def grow(self):
        # Implementa la lógica de crecimiento específica para plantas aquí
        pass

# Función para dibujar la matriz y los organismos en la ventana
def draw_matrix(screen, matrix, animales, plantas):
    cell_width = WIDTH // MATRIX_SIZE
    cell_height = HEIGHT // MATRIX_SIZE

    # Dibuja los cuadros y líneas de la cuadrícula
    for row in range(MATRIX_SIZE):
        for col in range(MATRIX_SIZE):
            pygame.draw.rect(screen, matrix[row][col].color, (col * cell_width, row * cell_height, cell_width, cell_height), 0)
            pygame.draw.rect(screen, GRID_COLOR, (col * cell_width, row * cell_height, cell_width, cell_height), 1)

    # Dibuja los animales en la ventana
    for animal in animales:
        pygame.draw.rect(screen, animal.color, (animal.x * (WIDTH // MATRIX_SIZE), animal.y * (HEIGHT // MATRIX_SIZE), WIDTH // MATRIX_SIZE, HEIGHT // MATRIX_SIZE))

    # Dibuja las plantas en la ventana
    for planta in plantas:
        pygame.draw.rect(screen, planta.color, (planta.x * (WIDTH // MATRIX_SIZE), planta.y * (HEIGHT // MATRIX_SIZE), WIDTH // MATRIX_SIZE, HEIGHT // MATRIX_SIZE))

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
    matrix = [[random.choice([Bosque()]) if random.random() < 0.7 else Desierto() if random.random() < 0.1 else Agua() for _ in range(MATRIX_SIZE)] for _ in range(MATRIX_SIZE)]

    # Crear animales y plantas en posiciones aleatorias
    animales = [Animales(random.randint(0, MATRIX_SIZE - 1), random.randint(0, MATRIX_SIZE - 1), LEON_COLOR) for _ in range(5)]  # Crear 5 leones
    animales += [Animales(random.randint(0, MATRIX_SIZE - 1), random.randint(0, MATRIX_SIZE - 1), VACA_COLOR) for _ in range(5)]  # Crear 5 vacas

    plantas = [Plantas(random.randint(0, MATRIX_SIZE - 1), random.randint(0, MATRIX_SIZE - 1), ARBOl_COLOR) for _ in range(10)]  # Crear 10 árboles

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Mueve a los animales en la matriz y maneja la aparición en los bordes
        for animal in animales:
            x, y = animal.x, animal.y
            animal.move(matrix[x][y])

            # Maneja la aparición en los bordes
            animal.x = animal.x % MATRIX_SIZE
            animal.y = animal.y % MATRIX_SIZE

        # Limpia la pantalla
        screen.fill(WHITE)

        # Dibuja la matriz, animales y plantas en la ventana
        draw_matrix(screen, matrix, animales, plantas)

        pygame.display.flip()
        clock.tick(5)  # Ajusta la velocidad del juego

    pygame.quit()
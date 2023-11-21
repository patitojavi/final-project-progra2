import pygame
import random

# Tamaño de la ventana y de la matriz
WIDTH, HEIGHT = 1200, 800
MATRIX_SIZE = 100  # Ahora es una matriz 100x100

# Colores
WHITE = (255, 255, 255)
GRID_COLOR = (0, 0, 0)

# Rutas de las imágenes
DESIERTO_IMAGE = "arena.png"
AGUA_IMAGE = "agua.png"
BOSQUE_IMAGE = "tierra.png"
LEON_IMAGE = "lobo1.png"
VACA_IMAGE = "vaca.png"
ARBOl_IMAGE = "panda.png"

class Bioma:
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path)

class Desierto(Bioma):
    def __init__(self):
        super().__init__(DESIERTO_IMAGE)

class Agua(Bioma):
    def __init__(self):
        super().__init__(AGUA_IMAGE)

class Bosque(Bioma):
    def __init__(self):
        super().__init__(BOSQUE_IMAGE)

# Definición de la clase Organismo
class Organismo:
    def __init__(self, x, y, image_path):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)

    def move(self):
        # Implementa la lógica de movimiento aquí
        pass

# Definición de la subclase Animales que hereda de Organismo
class Animales(Organismo):
    def __init__(self, x, y, image_path):
        super().__init__(x, y, image_path)
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

        # Maneja la aparición en los bordes
        self.x = (self.x + MATRIX_SIZE) % MATRIX_SIZE
        self.y = (self.y + MATRIX_SIZE) % MATRIX_SIZE

# Función para dibujar la matriz y los organismos en la ventana
def draw_matrix(screen, matrix, animales):
    cell_width = WIDTH // MATRIX_SIZE
    cell_height = HEIGHT // MATRIX_SIZE

    # Dibuja los cuadros y líneas de la cuadrícula
    for row in range(MATRIX_SIZE):
        for col in range(MATRIX_SIZE):
            bioma = matrix[row][col]
            screen.blit(bioma.image, (col * cell_width, row * cell_height, cell_width, cell_height))

    # Dibuja los animales en la ventana
    for animal in animales:
        screen.blit(animal.image, (animal.x * cell_width, animal.y * cell_height, cell_width, cell_height))

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
    matrix = [[random.choice([Bosque()]) if random.random() < 0.7 else Desierto() if random.random() < 0.7 else Agua() for _ in range(MATRIX_SIZE)] for _ in range(MATRIX_SIZE)]

    # Crear animales y plantas en posiciones aleatorias
    animales = [Animales(random.randint(0, MATRIX_SIZE - 1), random.randint(0, MATRIX_SIZE - 1), LEON_IMAGE) for _ in range(5)]  # Crear 5 leones
    animales += [Animales(random.randint(0, MATRIX_SIZE - 1), random.randint(0, MATRIX_SIZE - 1), VACA_IMAGE) for _ in range(5)]  # Crear 5 vacas

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Mueve a los animales en la matriz
        for animal in animales:
            x, y = animal.x, animal.y
            animal.move(matrix[y][x])

        # Limpia la pantalla
        screen.fill(WHITE)

        # Dibuja la matriz, animales y plantas en la ventana
        draw_matrix(screen, matrix, animales)

        pygame.display.flip()
        clock.tick(1)  # Ajusta la velocidad del juego

    pygame.quit()

if __name__ == "__main__":
    main()
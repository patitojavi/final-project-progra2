import pygame
import random

# Tamaño de la ventana y de la matriz
WIDTH, HEIGHT = 1200, 800
MATRIX_SIZE = 50  # Ahora es una matriz 100x100

# Colores
WHITE = (255, 255, 255)
GRID_COLOR = (0, 0, 0)

# Rutas de las imágenes
DESIERTO_IMAGE = "arena.png"
AGUA_IMAGE = "agua.png"
BOSQUE_IMAGE = "tierra.png"
LEON_IMAGE = "lobo1.png"
VACA_IMAGE = "vaca.png"
CAZADOR_IMAGE = "lobo1.png"

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

    def move(self, matrix):
        # Implementa la lógica de movimiento aquí
        pass

# Definición de la subclase Animales que hereda de Organismo
class Animales(Organismo):
    def __init__(self, x, y, image_path):
        super().__init__(x, y, image_path)
        self.nivel_agua = 50  # Nivel de agua inicial
        self.muerto = False
        self.tiempo_restante = 0

    def move(self, matrix):
        if not self.muerto:
            new_x = self.x + random.choice([-1, 0, 1])
            new_y = self.y + random.choice([-1, 0, 1])

            # Asegúrate de que el nuevo lugar esté dentro de la matriz
            new_x = (new_x + MATRIX_SIZE) % MATRIX_SIZE
            new_y = (new_y + MATRIX_SIZE) % MATRIX_SIZE

            # Actualiza el nivel de agua según el tipo de bioma
            bioma = matrix[new_y][new_x]
            if isinstance(bioma, Agua):
                self.nivel_agua = 100
            elif isinstance(bioma, Desierto):
                self.nivel_agua -= 5
            elif isinstance(bioma, Bosque):
                self.nivel_agua -= 1

            # Asegúrate de que el nivel de agua esté dentro del rango [0, 100]
            self.nivel_agua = max(0, min(self.nivel_agua, 100))

            # Verifica si hay un cazador en la nueva posición
            if isinstance(bioma, Cazador):
                bioma.atacar(self)

            # Reproducción si hay otro animal en la misma posición
            elif isinstance(bioma, Animales) and bioma is not self:
                # Crea un nuevo animal en una posición aleatoria
                new_animal = Animales(random.randint(0, MATRIX_SIZE - 1), random.randint(0, MATRIX_SIZE - 1), LEON_IMAGE)
                # Agrega el nuevo animal a la lista de animales
                matrix[new_animal.y][new_animal.x] = new_animal

            # Actualiza la posición del animal en la matriz
            matrix[self.y][self.x] = None
            matrix[new_y][new_x] = self
            self.x = new_x
            self.y = new_y

            # Actualiza el tiempo restante si el animal está muerto
            if self.muerto:
                self.tiempo_restante -= 1
                if self.tiempo_restante <= 0:
                    matrix[self.y][self.x] = None
                    self.muerto = False

# Definición de la subclase Cazador que hereda de Organismo
class Cazador(Organismo):
    def __init__(self, x, y, image_path):
        super().__init__(x, y, image_path)

    def atacar(self, presa):
        # Ataca a la presa (la marca como muerta y establece el tiempo restante)
        presa.muerto = True
        presa.tiempo_restante = 5  # Cambia esto a la cantidad deseada de tiempo que el cuerpo permanece en el mismo lugar

# Función para dibujar la matriz y los organismos en la ventana
def draw_matrix(screen, matrix):
    cell_width = WIDTH // MATRIX_SIZE
    cell_height = HEIGHT // MATRIX_SIZE

    # Dibuja los cuadros y líneas de la cuadrícula
    for row in range(MATRIX_SIZE):
        for col in range(MATRIX_SIZE):
            bioma = matrix[row][col]
            if bioma:
                screen.blit(bioma.image, (col * cell_width, row * cell_height, cell_width, cell_height))

    # Dibuja los animales y cazadores en la ventana
    for row in range(MATRIX_SIZE):
        for col in range(MATRIX_SIZE):
            organism = matrix[row][col]
            if organism and isinstance(organism, (Animales, Cazador)):
                screen.blit(organism.image, (col * cell_width, row * cell_height, cell_width, cell_height))

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

    # Crear animales y cazadores en posiciones aleatorias
    animales = [Animales(random.randint(0, MATRIX_SIZE - 1), random.randint(0, MATRIX_SIZE - 1), LEON_IMAGE) for _ in range(5)]  # Crear 5 leones
    animales += [Animales(random.randint(0, MATRIX_SIZE - 1), random.randint(0, MATRIX_SIZE - 1), VACA_IMAGE) for _ in range(5)]  # Crear 5 vacas
    cazadores = [Cazador(random.randint(0, MATRIX_SIZE - 1), random.randint(0, MATRIX_SIZE - 1), CAZADOR_IMAGE) for _ in range(3)]  # Crear 3 cazadores

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Mueve a los animales y cazadores en la matriz
        for organism in animales + cazadores:
            organism.move(matrix)

        # Limpia la pantalla
        screen.fill(WHITE)

        # Dibuja la matriz, animales y cazadores en la ventana
        draw_matrix(screen, matrix)

        pygame.display.flip()
        clock.tick(10)  # Ajusta la velocidad del juego

    pygame.quit()

if __name__ == "__main__":
    main()

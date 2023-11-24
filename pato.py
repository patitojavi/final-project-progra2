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
LOBO_IMAGE = "lobo1.png"
PRESA_IMAGE = "vaca.png"  # Cambia a la imagen que quieras para la presa

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
        self.nivel_agua = 50  # Nivel de agua inicial
        self.muerto = False
        self.tiempo_restante = 0
        self.energia = 100  # Energía inicial
        self.movimientos_realizados = 0

    def move(self, matrix):
        if not self.muerto:
            if self.movimientos_realizados >= 50:
                # Si se han realizado 50 movimientos, el organismo descansa y recupera energía
                self.descansar()
            else:
                new_x = self.x + random.choice([-1, 0, 1])
                new_y = self.y + random.choice([-1, 0, 1])

                # Asegúrate de que el nuevo lugar esté dentro de la matriz
                new_x = (new_x + MATRIX_SIZE) % MATRIX_SIZE
                new_y = (new_y + MATRIX_SIZE) % MATRIX_SIZE

                # Actualiza el nivel de agua según el tipo de bioma
                bioma = matrix[new_y][new_x]
                self.beber(matrix)  # Llama al método beber

                # Verifica si hay un Carnivoro en la nueva posición
                if isinstance(bioma, Carnivoro):
                    bioma.atacar(self)

                # Reproducción si hay otro organismo de la misma especie en la misma posición
                elif isinstance(bioma, Organismo) and bioma is not self and isinstance(self, type(bioma)):
                    self.reproducir(matrix, bioma)

                # Actualiza la posición del organismo en la matriz
                matrix[self.y][self.x] = None
                matrix[new_y][new_x] = self
                self.x = new_x
                self.y = new_y

                # Actualiza el tiempo restante si el organismo está muerto
                if self.muerto:
                    self.tiempo_restante -= 1
                    if self.tiempo_restante <= 0:
                        matrix[self.y][self.x] = None
                        self.muerto = False

                # Actualiza el conteo de movimientos realizados
                self.movimientos_realizados += 1

    def beber(self, matrix):
        bioma = matrix[self.y][self.x]
        if isinstance(bioma, Agua):
            self.nivel_agua = min(100, self.nivel_agua + 10)  # Ajusta la cantidad de agua que se puede beber
        elif isinstance(bioma, Desierto):
            self.nivel_agua = max(0, self.nivel_agua - 5)
        elif isinstance(bioma, Bosque):
            self.nivel_agua = max(0, self.nivel_agua - 1)
        self.nivel_agua = max(0, min(self.nivel_agua, 100))

    def descansar(self):
        # Restablece la cantidad de movimientos realizados y recupera energía
        self.movimientos_realizados = 0
        self.energia += 10  # Ajusta la cantidad de energía recuperada según sea necesario
        self.energia = min(self.energia, 100)  # Asegúrate de que la energía no supere el máximo

    def reproducir(self, matrix, partner):
        # Verifica si hay espacio adyacente para la reproducción
        adjacent_positions = [(self.x + dx, self.y + dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1]]
        available_positions = [(x, y) for x, y in adjacent_positions if 0 <= x < MATRIX_SIZE and 0 <= y < MATRIX_SIZE and matrix[y][x] is None]

        if available_positions:
            # Elige una posición aleatoria para la reproducción
            new_x, new_y = random.choice(available_positions)

            # Crea un nuevo organismo de la misma especie en la posición seleccionada
            new_organism = type(self)(new_x, new_y, self.image_path)
            
            # Agrega el nuevo organismo a la matriz
            matrix[new_y][new_x] = new_organism

# Definición de la subclase Carnivoro que hereda de Organismo
class Carnivoro(Organismo):
    def __init__(self, x, y, image_path):
        super().__init__(x, y, image_path)

    def atacar(self, presa):
        # Ataca a la presa (la marca como muerta y establece el tiempo restante)
        presa.muerto = True
        presa.tiempo_restante = 5  # Cambia esto a la cantidad deseada de tiempo que el cuerpo permanece en el mismo lugar

# Definición de la subclase Lobo que hereda de Carnivoro
class Lobo(Carnivoro):
    def __init__(self, x, y, image_path):
        super().__init__(x, y, image_path)

# Definición de la subclase Herviboro que hereda de Organismo
class Herviboro(Organismo):
    def __init__(self, x, y, image_path):
        super().__init__(x, y, image_path)

# Definición de la subclase Vaca que hereda de Herviboro
class Vaca(Herviboro):
    def __init__(self, x, y, image_path):
        super().__init__(x, y, image_path)

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

    # Dibuja los organismos en la ventana
    for row in range(MATRIX_SIZE):
        for col in range(MATRIX_SIZE):
            organism = matrix[row][col]
            if organism and isinstance(organism, Organismo):
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

    # Crear organismos en posiciones aleatorias
    organisms = [Lobo(random.randint(0, MATRIX_SIZE - 1), random.randint(0, MATRIX_SIZE - 1), LOBO_IMAGE) for _ in range(5)]  # Crear 5 Lobos
    organisms += [Vaca(random.randint(0, MATRIX_SIZE - 1), random.randint(0, MATRIX_SIZE - 1), VACA_IMAGE) for _ in range(5)]  # Crear 5 Vacas

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Mueve a los organismos en la matriz
        for organism in organisms:
            organism.move(matrix)

        # Limpia la pantalla
        screen.fill(WHITE)

        # Dibuja la matriz y organismos en la ventana
        draw_matrix(screen, matrix)

        pygame.display.flip()
        clock.tick(10)  # Ajusta la velocidad del juego

    pygame.quit()

if __name__ == "__main__":
    main()

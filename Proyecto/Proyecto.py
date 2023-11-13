import pygame as PY
import random as RA

PY.init()

# Tamaño de pantalla dinámico
pW = 800
pH = 800
screen = PY.display.set_mode((pW, pH))
PY.display.set_caption("Ecosistema Simulator")

# Color de fondo
fondo_color = (0, 0, 0)

class Organismo:
    def __init__(self, posicion, vida, energia, velocidad):
        self.posicion = posicion
        self.vida = vida
        self.energia = energia
        self.velocidad = velocidad

class Animal(Organismo):
    def __init__(self, posicion, vida, energia, velocidad, especie, dieta, ):
        super().__init__(posicion, vida, energia, velocidad)
        self.especie = especie
        self.dieta = dieta

class Planta(Organismo):
    def __init__(self, posicion, vida, energia, velocidad, tipo_planta):
        super().__init__(posicion, vida, energia, velocidad)
        self.tipo_planta = tipo_planta

class Carnivoro(Animal):
    def __init__(self, posicion, vida, energia, velocidad, especie, ):
        super().__init__(posicion, vida, energia, velocidad, especie, "Carnívoro")

class Herbivoro(Animal):
    def __init__(self, posicion, vida, energia, velocidad, especie, ):
        super().__init__(posicion, vida, energia, velocidad, especie, "Herbívoro")

# Parámetros de la matriz
nxC = 100
nyC = 100

# Tamaño de la celda en función del tamaño de la pantalla y la matriz
cH = pW // nxC
cW = pH // nyC

# Dividir la matriz en cuatro regiones
mX = nxC // 2
mY = nyC // 2

# Inicializar matriz con una lista vacía para cada celda
matriz_espacial = [[[] for _ in range(nxC)] for _ in range(nyC)]

# Definir tipos de plantas y sus colores
tipos_de_plantas = {
    "Flor": (255, 0, 0),          # Rojo
    "Arbusto": (0, 255, 0),       # Verde
    "Hierba": (0, 0, 255),        # Azul
    "Árbol Pequeño": (255, 255, 0),  # Amarillo
    "Árbol Grande": (255, 165, 0)    # Naranja
}

# Definir tipos de animales y sus colores
tipos_de_animales = {
    "León": (255, 0, 0),        # Rojo
    "Tigre": (255, 165, 0),     # Naranja
    "Leopardo": (0, 0, 0),      # Blanco y negro
    "Lobo": (0, 255, 0),        # Verde
    "Oso": (150, 75, 0),        # Marrón
    "Vaca": (255, 255, 255),    # Blanco
    "Cabra": (128, 0, 128),     # Púrpura
    "Cebra": (0, 0, 0),         # Blanco y negro
    "Jirafa": (255, 255, 0),    # Amarillo
    "Elefante": (128, 64, 0)    # Marrón oscuro
}

class PintaPlanta(Planta):
    def __init__(self):
        # Generar posición aleatoria
        posicion = (RA.randint(0, nxC - 1), RA.randint(0, nyC - 1))
        vida = RA.randint(50, 100)
        energia = RA.randint(20, 50)
        velocidad = RA.uniform(0.5, 2.0)
        tipo_planta = RA.choice(list(tipos_de_plantas.keys()))

        super().__init__(posicion, vida, energia, velocidad, tipo_planta)

class PintaCarnivoro(Carnivoro):
    def __init__(self, especie):
        # Generar posición aleatoria
        posicion = (RA.randint(0, nxC - 1), RA.randint(0, nyC - 1))
        vida = RA.randint(50, 100)
        energia = RA.randint(20, 50)
        velocidad = RA.uniform(0.5, 2.0)
        super().__init__(posicion, vida, energia, velocidad, especie)

class PintaHerbivoro(Herbivoro):
    def __init__(self, especie):
        # Generar posición aleatoria
        posicion = (RA.randint(0, nxC - 1), RA.randint(0, nyC - 1))
        vida = RA.randint(50, 100)
        energia = RA.randint(20, 50)
        velocidad = RA.uniform(0.5, 2.0)
        super().__init__(posicion, vida, energia, velocidad, especie)

num_plantas = 0
num_carnivoros = 4
num_herbivoros = 5

# Crear plantas
plantas = [PintaPlanta() for _ in range(num_plantas)]

# Crear carnívoros
carnivoros = [PintaCarnivoro("León"), PintaCarnivoro("Tigre"), PintaCarnivoro("Leopardo"), PintaCarnivoro("Lobo"), PintaCarnivoro("Oso")][:num_carnivoros]

# Crear herbívoros
herbivoros = [PintaHerbivoro("Vaca"), PintaHerbivoro("Cabra"), PintaHerbivoro("Cebra"), PintaHerbivoro("Jirafa"), PintaHerbivoro("Elefante")][:num_herbivoros]

# Colocar las plantas en la matriz
for planta in plantas:
    matriz_espacial[planta.posicion[1]][planta.posicion[0]].append(planta)

# Colocar los carnívoros en la matriz
for carnivoro in carnivoros:
    matriz_espacial[carnivoro.posicion[1]][carnivoro.posicion[0]].append(carnivoro)

# Colocar los herbívoros en la matriz
for herbivoro in herbivoros:
    matriz_espacial[herbivoro.posicion[1]][herbivoro.posicion[0]].append(herbivoro)


# Función para dibujar la matriz en la pantalla
def dibujar_matriz():
    # Establecer el color de fondo
    screen.fill(fondo_color)

    for y in range(0, nyC):
        for x in range(0, nxC):
            # Dibujar cada celda como un rectángulo
            rect = (x * cW, y * cH, cW, cH)

            # Obtener el tipo de organismo y sus colores
            tipos_organismos = set()
            colores = set()

            for organismo in matriz_espacial[y][x]:
                if isinstance(organismo, Planta):
                    tipos_organismos.add("Planta")
                    colores.add(tipos_de_plantas.get(organismo.tipo_planta, (0, 0, 0)))
                elif isinstance(organismo, Animal):
                    tipos_organismos.add(organismo.dieta)
                    colores.add(tipos_de_animales.get(organismo.especie, (0, 0, 0)))

            # Asignar color según el tipo de organismo
            color = max(colores) if colores else (0, 0, 0)

            # Dibujar la celda
            PY.draw.rect(screen, color, rect, 0)

# Bucle principal
ejecutando = True
while ejecutando:
    for evento in PY.event.get():
        if evento.type == PY.QUIT:
            ejecutando = False

    dibujar_matriz()

    # Actualizar pantalla
    PY.display.flip()

# Salir del programa
PY.quit()

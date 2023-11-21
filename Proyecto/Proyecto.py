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

    def moverse(self, direccion, distancia=1):
        # Obtener la posición actual
        x, y = self.posicion

        # Definir los cambios en las coordenadas según la dirección
        if direccion == "arriba":
            nueva_y = max(0, y - distancia)
            nueva_x = x
        elif direccion == "abajo":
            nueva_y = min(nyC - 1, y + distancia)
            nueva_x = x
        elif direccion == "izquierda":
            nueva_x = max(0, x - distancia)
            nueva_y = y
        elif direccion == "derecha":
            nueva_x = min(nxC - 1, x + distancia)
            nueva_y = y
        else:
            # Si la dirección no es válida, no se mueve
            return

        # Actualizar la posición del animal
        self.posicion = (nueva_x, nueva_y)

class Planta(Organismo):
    def __init__(self, posicion, vida, energia, velocidad, tipo_planta):
        super().__init__(posicion, vida, energia, velocidad)
        self.tipo_planta = tipo_planta

    def crecer(self):
        # Incrementar vida y energía de la planta
        self.vida += RA.randint(1, 5)
        self.energia += RA.randint(1, 10)

class Ambiente:
    def __init__(self, fact_ambioticos, eve_climaticos):
        self.fac_ambioticos = fact_ambioticos
        self.eve_climaticos = eve_climaticos

class Ecosistema:
    def __init__(self):
        self.organismos = []
        self.plantas = []
        self.ambiente = None

class Carnivoro(Animal):
    def __init__(self, posicion, vida, energia, velocidad, especie, ):
        super().__init__(posicion, vida, energia, velocidad, especie, "Carnívoro")

class Herbivoro(Animal):
    def __init__(self, posicion, vida, energia, velocidad, especie, ):
        super().__init__(posicion, vida, energia, velocidad, especie, "Herbívoro")

# Parámetros de la matriz
nxC = 50
nyC = 50

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

tipos_de_biomas = {
    "Bosque": (34, 139, 34),     # Verde oscuro
    "Pradera": (154, 205, 50),   # Verde claro
    "Desierto": (244, 164, 96),  # Marrón claro
    # Agrega más tipos de biomas si es necesario
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
        velocidad = RA.uniform(5, 2)
        super().__init__(posicion, vida, energia, velocidad, especie)

class PintaHerbivoro(Herbivoro):
    def __init__(self, especie):
        # Generar posición aleatoria
        posicion = (RA.randint(0, nxC - 1), RA.randint(0, nyC - 1))
        vida = RA.randint(50, 100)
        energia = RA.randint(20, 50)
        velocidad = RA.uniform(5, 2)
        super().__init__(posicion, vida, energia, velocidad, especie)

num_plantas = 2
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

# Velocidad de movimiento
velocidad_movimiento = 130 # Puedes ajustar este valor para cambiar la velocidad

# Bucle principal
ejecutando = True
contador = 0
while ejecutando:
    for evento in PY.event.get():
        if evento.type == PY.QUIT:
            ejecutando = False

    # Mover los animales según la velocidad de movimiento
    if contador % velocidad_movimiento == 0:
        for carnivoro in carnivoros:
            # Generar una dirección aleatoria
            direccion = RA.choice(["arriba", "abajo", "izquierda", "derecha"])
            carnivoro.moverse(direccion, distancia=1)  # Movimiento de dos casillas
            
        for herbivoro in herbivoros:
            # Generar una dirección aleatoria
            direccion = RA.choice(["arriba", "abajo", "izquierda", "derecha"])
            herbivoro.moverse(direccion, distancia=1)  # Movimiento de dos casillas

    contador += 1

    # Crecimiento de las plantas
    for planta in plantas:
        planta.crecer()

    # Limpiar la matriz
    matriz_espacial = [[[] for _ in range(nxC)] for _ in range(nyC)]

    # Colocar las plantas en la matriz actualizada
    for planta in plantas:
        matriz_espacial[planta.posicion[1]][planta.posicion[0]].append(planta)

    # Colocar los carnívoros en la matriz actualizada
    for carnivoro in carnivoros:
        matriz_espacial[carnivoro.posicion[1]][carnivoro.posicion[0]].append(carnivoro)

    # Colocar los herbívoros en la matriz actualizada
    for herbivoro in herbivoros:
        matriz_espacial[herbivoro.posicion[1]][herbivoro.posicion[0]].append(herbivoro)

    dibujar_matriz()

    # Actualizar pantalla
    PY.display.flip()

# Salir del programa
PY.quit()
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
    def __init__(self, posicion, vida, energia, velocidad, especie, dieta, imagen):
        super().__init__(posicion, vida, energia, velocidad)
        self.especie = especie
        self.dieta = dieta
        self.imagen = imagen

class Planta(Organismo):
    def __init__(self, posicion, vida, energia, velocidad, tipo_planta):
        super().__init__(posicion, vida, energia, velocidad)
        self.tipo_planta = tipo_planta

class Ambiente:
    def __init__(self, fact_ambioticos, eve_climaticos):
        self.fac_ambioticos = fact_ambioticos
        self.eve_climaticos = eve_climaticos

class Ecosistema:
    def __init__(self):
        self.organismos = []
        self.plantas = []
        self.ambiente = None

# Parámetros de la matriz
nxC =100
nyC = 100

# Tamaño de la celda en función del tamaño de la pantalla y la matriz
cH = pW // nxC
cW = pH // nyC

# Dividir la matriz en cuatro regiones
mitad_x = nxC // 2
mitad_y = nyC // 2

matriz_espacial = [
    [None for _ in range(mitad_x)] + [None for _ in range(mitad_x, nxC)] for _ in range(mitad_y)
] + [
    [None for _ in range(mitad_x)] + [None for _ in range(mitad_x, nxC)] for _ in range(mitad_y, nyC)
]

# Definir tipos de plantas y sus colores
tipos_de_plantas = {
    "Flor": (255, 0, 0),          # Rojo
    "Arbusto": (0, 255, 0),       # Verde
    "Hierba": (0, 0, 255),        # Azul
    "Árbol Pequeño": (255, 255, 0),  # Amarillo
    "Árbol Grande": (255, 165, 0)    # Naranja
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


# Crear 5 plantas aleatorias en diferentes regiones
plantas = [PintaPlanta() for _ in range(20)]

# Colocar las plantas en la matriz
for planta in plantas:
    matriz_espacial[planta.posicion[1]][planta.posicion[0]] = planta

# Función para dibujar la matriz en la pantalla
def dibujar_matriz():
    # Establecer el color de fondo
    screen.fill(fondo_color)

    for y in range(0, nyC):
        for x in range(0, nxC):
            # Dibujar cada celda como un rectángulo
            rect = (x * cW, y * cH, cW, cH)

            # Obtener el tipo de planta 
            tipo_planta = None
            if matriz_espacial[y][x] is not None and isinstance(matriz_espacial[y][x], Planta):
                tipo_planta = matriz_espacial[y][x].tipo_planta

            # Asignar color según el tipo de planta
            color = tipos_de_plantas.get(tipo_planta, (255, 255, 255))  # Blanco si no hay planta

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

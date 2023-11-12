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
    def __init__(self, posicion, vida, energia, velocidad, fotosintesis, repro_semilla):
        super().__init__(posicion, vida, energia, velocidad)
        self.fotosintesis = fotosintesis
        self.repro_semilla = repro_semilla

class Ambiente:
    def __init__(self, fact_ambioticos, eve_climaticos):
        self.fac_ambioticos = fact_ambioticos
        self.eve_climaticos = eve_climaticos

class Ecosistema:
    def __init__(self):
        self.organismos = []
        self.plantas = []
        self.ambiente = None

# Diccionario de imágenes para cada especie de animal
#imagenes_animales = {
    #"León": PY.image.load("Animales/leon.png"),

#}

# Parámetros de la matriz
nxC = 25
nyC = 25

# Tamaño de la celda en función del tamaño de la pantalla y la matriz
cH = pW // nxC
cW = pH // nyC

matriz_espacial = [[None for _ in range(nxC)] for _ in range(nyC)]

# Ejemplo: inicializar algunas celdas con organismos
organismo1 = Animal((5, 5), 100, 50, 2, "León", "Carnívoro", None)
matriz_espacial[organismo1.posicion[1]][organismo1.posicion[0]] = organismo1

# Función para dibujar la matriz en la pantalla
def dibujar_matriz():
    # Establecer el color de fondo
    screen.fill(fondo_color)
    
    for y in range(0, nyC):
        for x in range(0, nxC):
            # Dibujar cada celda como un rectángulo
            rect = (x * cW, y * cH, cW, cH)

            # Cambiar el color de la celda completa si hay un organismo en la celda
            color = (128, 128, 128)
            if matriz_espacial[y][x] is not None:
                color = (0, 255, 0)  # Verde para el organismo

            PY.draw.rect(screen, color, rect,1)

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

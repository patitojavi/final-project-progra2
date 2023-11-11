import pygame as PY
import random as RA

PY.init()

Panta_ancho = 800
Panta_largo = 600
screen = PY.display.set_mode((Panta_ancho, Panta_largo))
PY.display.set_caption("Ecosistema Simulator")

class Organismo:
    def __init__(self, posicion, vida, energia, velocidad):
        self.posicion = posicion
        self.vida = vida
        self.energia = energia
        self.velocidad = velocidad

class Animal(Organismo):
    def __init__(self, posicion, vida, energia, velocidad, especie, dieta):
        super().__init__(posicion, vida, energia, velocidad)
        self.especie = especie
        self.dieta = dieta

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




#----------------Matriz--------------#

# Crear una matriz para representar el espacio del ecosistema
filas = 100
columnas = 100
celda_ancho = Panta_ancho // columnas
celda_largo = Panta_largo // filas
matriz_espacial = [[None for _ in range(columnas)] for _ in range(filas)]

# Ejemplo: inicializar algunas celdas con organismos
organismo1 = Organismo((2, 3), 100, 50, 2)
organismo2 = Organismo((5, 9), 80, 40, 1)

matriz_espacial[1][1] = organismo1
matriz_espacial[5][9] = organismo2

# Función para dibujar la matriz en la pantalla
def dibujar_matriz():
    for fila in range(filas):
        for col in range(columnas):
            # Dibujar cada celda
            color = (255, 255, 255)  # Color de fondo (blanco) por defecto
            if matriz_espacial[fila][col] is not None:
                color = (0, 255, 0)  # Cambiar el color si hay algo en la celda

            PY.draw.rect(screen, color, (col * celda_ancho, fila * celda_largo, celda_ancho, celda_largo), 0)

# Bucle principal
ejecutando = True
while ejecutando:
    for evento in PY.event.get():
        if evento.type == PY.QUIT:
            ejecutando = False

    dibujar_matriz()

    # Actualizar panta
    PY.display.flip()

# Salir 
PY.quit()

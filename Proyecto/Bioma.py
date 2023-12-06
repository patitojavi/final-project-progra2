import pygame as PY
import random as RA
from constantes import pW, pH
from plantas import Nenufar, ArbolDesierto, ArbolTierra

PY.init()

# Tamaño de pantalla dinámico

screen = PY.display.set_mode((pW, pH))
PY.display.set_caption("Ecosistema Simulator")

class Bioma:
    def __init__(self, image_path, comida, agua):
        self.image = PY.image.load(image_path)
        self.comida = comida
        self.agua = agua
        self.plantas = []  # Lista para almacenar plantas en el bioma


    def agregar_planta(self, planta):
        self.plantas.append(planta)


class Desierto(Bioma):
    def __init__(self):
        super().__init__("Proyecto/imagenes/arena.png", RA.randint(0, 1), 0)


class Agua(Bioma):
    def __init__(self):
        super().__init__("Proyecto/imagenes/agua.png", 0, RA.randint(0, 5))


class Tierra(Bioma):
    def __init__(self):
        super().__init__("Proyecto/imagenes/tierra.png", RA.randint(0, 5), 0)


class Lava(Bioma):
    def __init__(self):
        super().__init__("Proyecto/imagenes/lava.png", 0, 0)

class Lluvia:
    def __init__(self):
        self.velocidad = 1 # Ajusta la velocidad de la lluvia
        self.lluvia_activa = False
        self.gotas = []  # Lista para almacenar las posiciones de las gotas de lluvia

    def activar_lluvia(self):
        self.lluvia_activa = True

    def desactivar_lluvia(self):
        self.lluvia_activa = False

    def generar_gota(self, x, y):
        return [x, y]  # Crea una gota en una posición x, y dada

    def dibujar(self, screen):
        if self.lluvia_activa:
            for gota in self.gotas:
                # Dibujar un rectángulo para simular una gota más ancha
                rect = (gota[0], gota[1], 3, 10)  # Ancho y alto del rectángulo
                PY.draw.rect(screen, (0, 0, 255), rect)  # Color azul para las gotas

    def actualizar(self):
        if self.lluvia_activa:
            for _ in range(self.velocidad):
                x = RA.randint(0, pW)  # Generar una posición aleatoria en el ancho de la pantalla
                y = RA.randint(-pH, 0)  # Generar una posición aleatoria por encima del límite superior
                self.gotas.append(self.generar_gota(x, y))  # Agregar gotas a la lista de posiciones de gotas

            # Mover las gotas hacia abajo simulando la lluvia
            index = 0
            while index < len(self.gotas):
                self.gotas[index][1] += 4  # Ajustar la distancia a la que caen las gotas
                if self.gotas[index][1] > pH:
                    del self.gotas[index]
                else:
                    index += 1

bioma_dict = {
    "A": Agua(),
    "D": Desierto(),
    "T": Tierra(),
    "L": Lava(),
}


patron_biomas = [
    "TTTTTTTTTTTTTTTTTTAAAAAAAADDDDDDDDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTTAAAAAAAAADDDDDDDDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTTAAAAAAAAADDDDDDDDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTTAAAAAAAAADDDDDDDDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTTAAAAAAAAAADDDDDDDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTTAAAAAAAAAADDDDDDDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTTAAAAAAAAADDDDDDDDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTTTTTAAAAAAAAAADDDDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTTTTTTTAAAAAADDDDDDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTTTTTTTTAAAAAADDDDDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTTTTTTTTAAAAAAADDDDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTTTTTTTAAAADDDDDDDDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTTTTTTTAAAADDDDDDDDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTTTTTAAAAAAAADDDDDDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTTTTTAAAAAAAADDDDDDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTTTTTAAAAAAAADDDDDDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTTTTTTTAAAAADDDDDDDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTTTTTTTTAAAAAADDDDDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTTTTTTTTTAAAAAAAAADDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTTTTTTTAAAAAAAAAADDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTTTTTTTTTAAAAAAAAADDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTTAAAAAAAAAAAAADDDDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTTAAAAAAAAAAAAADDDDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTTAAAAAAAAAAAAADDDDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTTTTAAAAAAAAAAAADDDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTTTTAAAAAAAAAAAAAADDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTTTTAAAAAAAAAAAAAADDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTTTTTAAAAAAAAAAAADDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTTTTAAAAAAAAAAAAADDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTTTTTAAAAAAAAAADDDDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTTTAAAAAAAAAAAAAAAADDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTTAAAAAAAAAAAAADDDDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTTAAAAAAAAAAAAAADDDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTTAAAAAAAAAAAAAAADDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTTTAAAAAAAAAAAADDDDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTTTTAAAAAAAAAAAADDDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTTTTAAAAAAAAAAAAAADDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTTTTAAAAAAAAAAAAADDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTTAAAAAAAAAAAADDDDDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTAAAAAAAAAAAADDDDDDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTAAAAAAAAAAAAADDDDDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTAAAAAAAAAAAAADDDDDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTAAAAAAAAAAAAADDDDDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTAAAAAAAAAAAAAAADDDDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTAAAAAAAAAAAAAAAAADDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTAAAAAAAAAAAAAAAAADDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTAAAAAAAAAAAAAAAAADDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTAAAAAAAAAAAAAAADDDDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTAAAAAAAAAAAAAADDDDDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTTAAAAAAAAAAAAAADDDDDDDDDDDDDDDDDDD",
]


matriz_biomas = []
for fila_patron in patron_biomas:
    fila_biomas = []
    for letra in fila_patron:
        if letra == "D":
            fila_biomas.append(Desierto())
        elif letra == "A":
            fila_biomas.append(Agua())
        elif letra == "T":
            fila_biomas.append(Tierra())
    matriz_biomas.append(fila_biomas)


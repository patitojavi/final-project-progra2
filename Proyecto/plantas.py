import random as RA
import pygame as PY
from organismo import Organismo
from constantes import cW, cH, nxC, nyC, min_cW, min_cH, pW, pH

class Planta(Organismo):
    def __init__(self, posicion, vida, energia, velocidad, tipo_planta):
        super().__init__(posicion, vida, energia, velocidad)
        self.tipo_planta = tipo_planta

class Nenufar(Planta):
    def __init__(self):
        super().__init__("Proyecto/imagenes/nenufar.png", 1, 3, 1, "A")

class ArbolDesierto(Planta):
    def __init__(self):
        super().__init__("Proyecto/imagenes/arboldesierto.png", 2, 4, 1, "D")

class ArbolTierra(Planta):
    def __init__(self):
        super().__init__("Proyecto/imagenes/arboltierra.png", 2, 4, 1, "T")
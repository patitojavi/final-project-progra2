
import pygame as PY
from organismo import Organismo
from constantes import cW, cH, nxC, nyC, min_cW, min_cH, pW, pH


class Planta(Organismo):
    def __init__(self, imagen, vida, energia, velocidad, tipo_planta, posicion):
        super().__init__(posicion, vida, energia, velocidad)
        self.tipo_planta = tipo_planta
        self.imagen_original = PY.image.load(imagen)
        self.imagen = PY.transform.scale(self.imagen_original, (cW, cH))
        self.valor_comida = energia  

class Nenufar(Planta):
    def __init__(self, posicion):
        super().__init__("Proyecto/imagenes/nenufar.png", 1, 3, 1, "Nenufar", posicion)
        self.valor_comida = 1  

class ArbolDesierto(Planta):
    def __init__(self, posicion):
        super().__init__("Proyecto/imagenes/arboldesierto.png", 2, 4, 2, "ArbolDesierto", posicion)
        self.valor_comida = 2  

class ArbolTierra(Planta):
    def __init__(self, posicion):
        super().__init__("Proyecto/imagenes/arboltierra.png", 2, 5, 3, "ArbolTierra", posicion)
        self.valor_comida = 4  
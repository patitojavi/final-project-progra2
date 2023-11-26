import random as RA
import pygame as PY
from organismo import Organismo

class Planta(Organismo):
    def __init__(self, posicion, vida, energia, velocidad, tipo_planta):
        super().__init__(posicion, vida, energia, velocidad)
        self.tipo_planta = tipo_planta

    def crecer(self):
        self.vida += RA.randint(1, 5)
        self.energia += RA.randint(1, 10)
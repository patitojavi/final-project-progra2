import pygame as py
import sys as sys
import random as ra

py.init()

ventanaAncho = 1200
ventanaAlto = 1000
filas = 50
columnas = 50
celdaAlto = ventanaAlto // filas
celdaAncho = ventanaAncho // columnas

ventana = py.display.set_mode((ventanaAncho, ventanaAlto))
py.display.set_caption(" Ecosistema ")


class Desierto:
    def __init__(self):
        self.imagen = py.image.load("/arena.png")


class Pradera:
    def __init__(self):
        self.imagen = py.image.load("/tierra.png")


class Agua:
    def __init__(self):
        self.imagen = py.image.load("/agua.png")




class Organismo:
    def __init__(self):
        self.vivo = True


class Animal(Organismo):
    def __init__(self, energia=100,comida=100,velocidad=1):
        super().__init__()
        self.energia = energia
        self.comida = comida
        self.velocidad = velocidad

    def reproducir():
        pass

    def morir(self):
        self.vivo = False
        

    def moverse():
        pass


class Planta(Organismo):
    def __init__(self, energia=100,velocidad=0):
        super().__init__(energia, velocidad)
        
        
    def morir(self):
        self.vivo = False


class Lobo(Animal):
    def __init__(self, energia, comida, velocidad):
        super().__init__(energia, comida, velocidad)
        pass
    
    
    def morir(self):
        self.vivo = False


matriz_biomas = [[None for _ in range(columnas)] for _ in range(filas)]

for i in range(filas):
    for j in range(columnas):
        bioma_aleatorio = ra.choice([Desierto(), Pradera(), Agua()])
        matriz_biomas[i][j] = bioma_aleatorio

def main():
    while True:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()

        for fila in range(filas):
            for col in range(columnas):
                py.draw.rect(ventana, (255, 255, 255), (col * celdaAncho, fila * celdaAlto, celdaAncho, celdaAlto), 1)
        py.display.flip()


main()
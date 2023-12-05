import logging

import pygame as PY
import random as RA
from organismo import Organismo
from constantes import cW, cH, nxC, nyC, min_cW, min_cH, pW, pH
from logger import logger



logging.basicConfig(filename='simulador.log', level=logging.INFO)

class Animal(Organismo):
    total_animales = 0
    def __init__(self, posicion, vida, energia, velocidad, especie, dieta):
        super().__init__(posicion, vida, energia, velocidad)
        self.especie = especie
        self.dieta = dieta
        self.imagen = None
        Animal.total_animales += 1

    def moverse(self, direccion, distancia=1):
        if self.vida <= 0:
            return
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


    def reproducirse(self, otros):
        if Animal.total_animales < 20:  # Limitar la reproducción si se alcanza el límite
            for otro in otros:
                if (
                    isinstance(otro, type(self))
                    and self.especie == otro.especie
                    and self.__class__ == otro.__class__
                ):
                    if RA.random() < 0.1:
                        nueva_posicion_x = min(max(self.posicion[0] + RA.randint(-1, 1), 0), nxC - 1)
                        nueva_posicion_y = min(max(self.posicion[1] + RA.randint(-1, 1), 0), nyC - 1)

                        nuevo_animal = self.__class__(
                            especie=self.especie,
                            posicion=(nueva_posicion_x, nueva_posicion_y),
                            vida=(self.vida + otro.vida) // 2,
                            energia=(self.energia + otro.energia) // 2,
                            velocidad=self.velocidad,
                            dieta=self.dieta
                        )

                        Animal.total_animales += 1  # Incrementar el número total de animales al reproducirse
                        logging.info(f"{self.especie} se ha reproducido con {otro.especie}. Nueva posicion: {nuevo_animal.posicion}")
                        return nuevo_animal

        return None

    def cazar(self, presas, herbivoros):
        if self.dieta == "Carnívoro" and presas:
            presa = RA.choice(presas)
            if isinstance(presa, Animal) and self.especie != presa.especie:
                logging.info(f"{self.especie} cazó a {presa.especie}")# Evitar cazar a animales de la misma especie
                vida_restante_presa = presa.vida - 20
                presa.vida = max(vida_restante_presa, 0)
                if presa.vida <= 0:
                    if presa in herbivoros:
                        herbivoros.remove(presa)
                    self.energia += RA.randint(1, 3)
                    self.vida = min(self.vida + 10, 100)


    def recuperar_energia(self, cantidad):
        if self.dieta == "herbivoro":
            self.vida += 2 + cantidad

        self.energia += cantidad

        # Limitar el valor máximo de vida y energía a 100
        self.vida = min(self.vida, 100)
        self.energia = min(self.energia, 100)


    def dibujar(self, pantalla, celda_ancho, celda_alto):
        alto_barra = 5  # Mueve la declaración de alto_barra aquí

        pantalla.blit(self.imagen, (self.posicion[0] * celda_ancho, self.posicion[1] * celda_alto))

        vida_restante = max(self.vida, 0)
        vida_maxima = 100
        ancho_barra = celda_ancho - 4
        borde_barra = 1
        color_fondo = (255, 0, 0)
        color_vida = (0, 255, 0)

        vida_proporcion = vida_restante / vida_maxima
        ancho_vida = int(ancho_barra * vida_proporcion)
        x_barra = self.posicion[0] * celda_ancho + 2
        y_barra = self.posicion[1] * celda_alto - alto_barra - 2

        PY.draw.rect(pantalla, color_fondo, (x_barra, y_barra, ancho_barra, alto_barra))
        PY.draw.rect(pantalla, color_vida, (x_barra, y_barra, ancho_vida, alto_barra))
        PY.draw.rect(pantalla, (0, 0, 0), (x_barra, y_barra, ancho_barra, alto_barra), borde_barra)


        # Mostrar la vida como texto sobre la barra
        font = PY.font.Font(None, 24)
        vida_texto = font.render(f"Vida: {self.vida}", True, (255, 255, 255))
        pantalla.blit(vida_texto, (x_barra, y_barra - 20))  # Ajusta la posición del texto según tu preferencia


class Conejo(Animal):
    def __init__(self, posicion, vida, energia, velocidad, especie, dieta):
        super().__init__(posicion, vida, energia, velocidad, especie, dieta)
        self.imagen_original = PY.image.load("Proyecto/imagenes/conejo.png")  
        self.imagen = PY.transform.scale(self.imagen_original, (cW, cH))


class Lobo(Animal):
    def __init__(self, posicion, vida, energia, velocidad, especie, dieta):
        super().__init__(posicion, vida, energia, velocidad, especie, dieta)
        self.imagen_original = PY.image.load("Proyecto/imagenes/lobo.png")  
        self.imagen = PY.transform.scale(self.imagen_original, (cW, cH))


class Leon(Animal):
    def __init__(self, posicion, vida, energia, velocidad, especie, dieta):
        super().__init__(posicion, vida, energia, velocidad, especie, dieta)
        self.imagen_original = PY.image.load("Proyecto/imagenes/leon.png")  
        self.imagen = PY.transform.scale(self.imagen_original, (cW, cH))


class Zorro(Animal):
    def __init__(self, posicion, vida, energia, velocidad, especie, dieta):
        super().__init__(posicion, vida, energia, velocidad, especie, dieta)
        self.imagen_original = PY.image.load("Proyecto/imagenes/zorro.png")  
        self.imagen = PY.transform.scale(self.imagen_original, (cW, cH))


class Guepardo(Animal):
    def __init__(self, posicion, vida, energia, velocidad, especie, dieta):
        super().__init__(posicion, vida, energia, velocidad, especie, dieta)
        self.imagen_original = PY.image.load("Proyecto/imagenes/guepardo.png")  
        self.imagen = PY.transform.scale(self.imagen_original, (cW, cH))

class Oso(Animal):
    def __init__(self, posicion, vida, energia, velocidad, especie, dieta):
        super().__init__(posicion, vida, energia, velocidad, especie, dieta)
        self.imagen_original = PY.image.load("Proyecto/imagenes/oso.png")  
        self.imagen = PY.transform.scale(self.imagen_original, (cW, cH))


class Cerdo(Animal):
    def __init__(self, posicion, vida, energia, velocidad, especie, dieta):
        super().__init__(posicion, vida, energia, velocidad, especie, dieta)
        self.imagen_original = PY.image.load("Proyecto/imagenes/cerdo.png")  
        self.imagen = PY.transform.scale(self.imagen_original, (cW, cH)) 

class Gallina(Animal):
    def __init__(self, posicion, vida, energia, velocidad, especie, dieta):
        super().__init__(posicion, vida, energia, velocidad, especie, dieta)
        self.imagen_original = PY.image.load("Proyecto/imagenes/gallina.png")  
        self.imagen = PY.transform.scale(self.imagen_original, (cW, cH))

class Oveja(Animal):
    def __init__(self, posicion, vida, energia, velocidad, especie, dieta):
        super().__init__(posicion, vida, energia, velocidad, especie, dieta)
        self.imagen_original = PY.image.load("Proyecto/imagenes/oveja.png")  
        self.imagen = PY.transform.scale(self.imagen_original, (cW, cH))


class Vaca(Animal):
    def __init__(self, posicion, vida, energia, velocidad, especie, dieta):
        super().__init__(posicion, vida, energia, velocidad, especie, dieta)
        self.imagen_original = PY.image.load("Proyecto/imagenes/vaca.png")  
        self.imagen = PY.transform.scale(self.imagen_original, (cW, cH))
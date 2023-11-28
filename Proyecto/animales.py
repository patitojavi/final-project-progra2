

import pygame as PY
import random as RA
from organismo import Organismo
from constantes import cW, cH, nxC, nyC, min_cW, min_cH, pW, pH



class Animal(Organismo):
    def __init__(self, posicion, vida, energia, velocidad, especie, dieta):
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


    def reproducirse(self, otros):
        for otro in otros:
            if (
                isinstance(otro, type(self))
                and self.especie == otro.especie
                and self.energia > 50
                and otro.energia > 50
                and self.__class__ == otro.__class__
            ):
                nueva_posicion_x = min(max(self.posicion[0] + RA.randint(-1, 1), 0), nxC - 1)
                nueva_posicion_y = min(max(self.posicion[1] + RA.randint(-1, 1), 0), nyC - 1)

                nuevo_animal = type(self)(
                    (nueva_posicion_x, nueva_posicion_y),
                    vida=(self.vida + otro.vida) // 2,
                    energia=(self.energia + otro.energia) // 2,
                    velocidad=self.velocidad,
                    especie=self.especie,
                    dieta=self.dieta
                )

                return nuevo_animal

        return None
            


    def dibujar(self, pantalla, celda_ancho, celda_alto):
        pantalla.blit(self.imagen, (self.posicion[0] * celda_ancho, self.posicion[1] * celda_alto))

        vida_restante = max(self.vida, 0)
        vida_maxima = 100
        ancho_barra = celda_ancho - 4
        alto_barra = 5
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

    def cazar(self, presas, herbivoros):
        if self.dieta == "Carnívoro" and presas:
            presa = RA.choice(presas)
            if isinstance(presa, Animal):
                vida_restante_presa = presa.vida - 20  # Restar 20 de vida a la presa
                presa.vida = max(vida_restante_presa, 0)
                if presa.vida <= 0:
                    if presa in herbivoros:
                        herbivoros.remove(presa)
                    self.energia += RA.randint(1, 3)  # Regenerar energía al carnívoro
                    # Regenerar 10 de vida al carnívoro después de cazar, pero limitar a un máximo de 100
                    self.vida = min(self.vida + 10, 100)

class Lobo(Animal):
    def __init__(self, posicion):
        especie = "Lobo"
        vida = RA.randint(50, 100)
        energia = RA.randint(20, 50)
        velocidad = RA.uniform(5, 2)
        super().__init__(posicion, vida, energia, velocidad, especie, "Carnívoro")
        self.imagen_original = PY.image.load("Proyecto/imagenes/lobo.png")  
        self.imagen = PY.transform.scale(self.imagen_original, (cW, cH))  
        
class Leon(Animal):
    def __init__(self, posicion):
        especie = "Leon"
        vida = RA.randint(50, 100)
        energia = RA.randint(20, 50)
        velocidad = RA.uniform(5, 2)
        super().__init__(posicion, vida, energia, velocidad, especie, "Carnívoro")
        self.imagen_original = PY.image.load("Proyecto/imagenes/leon.png")  
        self.imagen = PY.transform.scale(self.imagen_original, (cW, cH))


class Zorro(Animal):
    def __init__(self, posicion):
        especie = "Zorro"
        vida = RA.randint(50, 100)
        energia = RA.randint(20, 50)
        velocidad = RA.uniform(5, 2)
        super().__init__(posicion, vida, energia, velocidad, especie, "Carnívoro")
        self.imagen_original = PY.image.load("Proyecto/imagenes/zorro.png")  
        self.imagen = PY.transform.scale(self.imagen_original, (cW, cH))



class Guepardo(Animal):
    def __init__(self, posicion):
        especie = "Guepardo"
        vida = RA.randint(50, 100)
        energia = RA.randint(20, 50)
        velocidad = RA.uniform(5, 2)
        super().__init__(posicion, vida, energia, velocidad, especie, "Carnívoro")
        self.imagen_original = PY.image.load("Proyecto/imagenes/guepardo.png")  
        self.imagen = PY.transform.scale(self.imagen_original, (cW, cH))  


class Oso(Animal):
    def __init__(self, posicion):
        especie = "Oso"
        vida = RA.randint(50, 100)
        energia = RA.randint(20, 50)
        velocidad = RA.uniform(5, 2)
        super().__init__(posicion, vida, energia, velocidad, especie, "Carnívoro")
        self.imagen_original = PY.image.load("Proyecto/imagenes/oso.png")  
        self.imagen = PY.transform.scale(self.imagen_original, (cW, cH))



class Cerdo(Animal):
    def __init__(self, posicion):
        especie = "Cerdo"
        vida = RA.randint(50, 100)
        energia = RA.randint(20, 50)
        velocidad = RA.uniform(5, 2)
        super().__init__(posicion, vida, energia, velocidad, especie, "herbivoro")
        self.imagen_original = PY.image.load("Proyecto/imagenes/cerdo.png")  
        self.imagen = PY.transform.scale(self.imagen_original, (cW, cH))  


class Conejo(Animal):
    def __init__(self, posicion):
        especie = "Conejo"
        vida = RA.randint(50, 100)
        energia = RA.randint(20, 50)
        velocidad = RA.uniform(5, 2)
        super().__init__(posicion, vida, energia, velocidad, especie, "herbivoro")
        self.imagen_original = PY.image.load("Proyecto/imagenes/conejo.png")  
        self.imagen = PY.transform.scale(self.imagen_original, (cW, cH))


class Gallina(Animal):
    def __init__(self, posicion):
        especie = "Gallina"
        vida = RA.randint(50, 100)
        energia = RA.randint(20, 50)
        velocidad = RA.uniform(5, 2)
        super().__init__(posicion, vida, energia, velocidad, especie, "herbivoro")
        self.imagen_original = PY.image.load("Proyecto/imagenes/gallina.png")  
        self.imagen = PY.transform.scale(self.imagen_original, (cW, cH)) 

class Oveja(Animal):
    def __init__(self, posicion):
        especie = "Oveja"
        vida = RA.randint(50, 100)
        energia = RA.randint(20, 50)
        velocidad = RA.uniform(5, 2)
        super().__init__(posicion, vida, energia, velocidad, especie, "herbivoro")
        self.imagen_original = PY.image.load("Proyecto/imagenes/oveja.png")  
        self.imagen = PY.transform.scale(self.imagen_original, (cW, cH)) 


class Vaca(Animal):
    def __init__(self, posicion):
        especie = "Vaca"
        vida = RA.randint(50, 100)
        energia = RA.randint(20, 50)
        velocidad = RA.uniform(5, 2)
        super().__init__(posicion, vida, energia, velocidad, especie, "herbivoro")
        self.imagen_original = PY.image.load("Proyecto/imagenes/vaca.png")  
        self.imagen = PY.transform.scale(self.imagen_original, (cW, cH)) 
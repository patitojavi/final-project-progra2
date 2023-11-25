import pygame as PY
import random as RA
from Bioma import Bioma, Desierto, Agua, Tierra,patron_biomas,bioma_dict

PY.init()

# Tamaño de pantalla dinámico
pW = 800
pH = 800
screen = PY.display.set_mode((pW, pH))
PY.display.set_caption("Ecosistema Simulator")

# Color de fondo
#fondo_color = (255, 255, 255)
fondo_color = (0, 0, 0)

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
        self.edad = 0

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

    def dibujar(self, pantalla, celda_ancho, celda_alto):
        pantalla.blit(self.imagen, (self.posicion[0] * celda_ancho, self.posicion[1] * celda_alto))
        pass
    
    def reproducirse(self, otro_animal):
        if self.especie == otro_animal.especie and self.posicion == otro_animal.posicion and self.energia < 50 or otro_animal.energia < 50:
            nuevo_animal = Animal(self.posicion, vida=50, energia=50, velocidad=5, especie=self.especie, dieta=self.dieta)
            return nuevo_animal
        else:
            return None
        
    def envejecer(self):
        self.edad += 1
        if self.edad > 50:
            self.vida -= 1
        if self.vida <= 0:
            self.morir()

class Lobo(Animal):
    def __init__(self, posicion):
        especie = "Lobo"
        vida = RA.randint(50, 100)
        energia = RA.randint(20, 50)
        velocidad = RA.uniform(5, 2)
        super().__init__(posicion, vida, energia, velocidad, especie, "Carnívoro")
        self.imagen_original = PY.image.load("Proyecto/lobo.png")  
        self.imagen = PY.transform.scale(self.imagen_original, (cW, cH))
        
    def cazar(self, presa):
        if self.dieta == "Carnívoro":
            if self.posicion == otro_animal.posicion:
                otro_animal.vida -= 100
                self.energia += 10
                if otro_animal.vida <= 0:
                    otro_animal.morir()
        else:
            return None

class Guepardo(Animal):
    def __init__(self, posicion):
        especie = "Guepardo"
        vida = RA.randint(50, 100)
        energia = RA.randint(20, 50)
        velocidad = RA.uniform(5, 2)
        super().__init__(posicion, vida, energia, velocidad, especie, "Carnívoro")
        self.imagen_original = PY.image.load("Proyecto/guepardo.png")  
        self.imagen = PY.transform.scale(self.imagen_original, (cW, cH))  


class Cerdo(Animal):
    def __init__(self, posicion):
        especie = "Cerdo"
        vida = RA.randint(50, 100)
        energia = RA.randint(20, 50)
        velocidad = RA.uniform(5, 2)
        super().__init__(posicion, vida, energia, velocidad, especie, "Omnivero")
        self.imagen_original = PY.image.load("Proyecto/cerdo.png")  
        self.imagen = PY.transform.scale(self.imagen_original, (cW, cH))  

class Gallina(Animal):
    def __init__(self, posicion):
        especie = "Gallina"
        vida = RA.randint(50, 100)
        energia = RA.randint(20, 50)
        velocidad = RA.uniform(5, 2)
        super().__init__(posicion, vida, energia, velocidad, especie, "herbivoro")
        self.imagen_original = PY.image.load("Proyecto/gallina.png")  
        self.imagen = PY.transform.scale(self.imagen_original, (cW, cH)) 

class Oveja(Animal):
    def __init__(self, posicion):
        especie = "Cerdo"
        vida = RA.randint(50, 100)
        energia = RA.randint(20, 50)
        velocidad = RA.uniform(5, 2)
        super().__init__(posicion, vida, energia, velocidad, especie, "herbivoro")
        self.imagen_original = PY.image.load("Proyecto/oveja.png")  
        self.imagen = PY.transform.scale(self.imagen_original, (cW, cH)) 

class Vaca(Animal):
    def __init__(self, posicion):
        especie = "Vaca"
        vida = RA.randint(50, 100)
        energia = RA.randint(20, 50)
        velocidad = RA.uniform(5, 2)
        super().__init__(posicion, vida, energia, velocidad, especie, "herbivoro")
        self.imagen_original = PY.image.load("Proyecto/vaca.png")  
        self.imagen = PY.transform.scale(self.imagen_original, (cW, cH)) 




class Planta(Organismo):
    def __init__(self, posicion, vida, energia, velocidad, tipo_planta):
        super().__init__(posicion, vida, energia, velocidad)
        self.tipo_planta = tipo_planta

    def crecer(self):
        self.vida += RA.randint(1, 5)
        self.energia += RA.randint(1, 10)

class Ambiente:
    def __init__(self, fact_ambioticos, eve_climaticos):
        self.fac_ambioticos = fact_ambioticos
        self.eve_climaticos = eve_climaticos

class Ecosistema:
    def __init__(self):
        self.organismos = []
        self.plantas = []
        self.ambiente = None


nxC = 50
nyC = 50
cH = pW // nxC
cW = pH // nyC

matriz_biomas = [[[] for _ in range(nxC)] for _ in range(nyC)]

# Colocar el patrón en la matriz
for y, fila in enumerate(patron_biomas):
    for x, caracter in enumerate(fila):
        matriz_biomas[y][x] = bioma_dict[caracter]

num_plantas = 2
num_carnivoros = 2
num_herbivoros = 3

def dibujar_matriz():
    screen.fill(fondo_color)

    for y in range(0, nyC):
        for x in range(0, nxC):
            rect = (x * cW, y * cH, cW, cH)

            tipos_organismos = set()
            colores = set()

            # Dibujar biomas
            matriz_biomas[y][x].image = PY.transform.scale(matriz_biomas[y][x].image, (cW, cH))
            screen.blit(matriz_biomas[y][x].image, (x * cW, y * cH))

            # Verificar si hay organismos y dibujarlos después de los biomas
            for organismo in matriz_espacial[y][x]:
                if isinstance(organismo, Planta):
                    tipos_organismos.add("Planta")
                elif isinstance(organismo, Animal):
                    tipos_organismos.add(organismo.dieta)

            for organismo in matriz_espacial[y][x]:
                if isinstance(organismo, Animal):
                    organismo.dibujar(screen, cW, cH)

            color = max(colores) if colores else (0, 0, 0)
            PY.draw.rect(screen, color, rect, 1)


velocidad_movimiento = 20

plantas = [Planta((RA.randint(0, nxC - 1), RA.randint(0, nyC - 1)), 50, 20, 2, "Tipo1") for _ in range(num_plantas)]
carnivoros = []
carnivoros.extend([Lobo((RA.randint(0, nxC - 1), RA.randint(0, nyC - 1))) for _ in range(num_carnivoros)])
carnivoros.extend([Guepardo((RA.randint(0, nxC - 1), RA.randint(0, nyC - 1))) for _ in range(num_carnivoros)])

herbivoros = []
herbivoros.extend([Cerdo((RA.randint(0, nxC - 1), RA.randint(0, nyC - 1))) for _ in range(num_herbivoros)])
herbivoros.extend([Gallina((RA.randint(0, nxC - 1), RA.randint(0, nyC - 1))) for _ in range(num_herbivoros)])
herbivoros.extend([Oveja((RA.randint(0, nxC - 1), RA.randint(0, nyC - 1))) for _ in range(num_herbivoros)])
herbivoros.extend([Vaca((RA.randint(0, nxC - 1), RA.randint(0, nyC - 1))) for _ in range(num_herbivoros)])

ejecutando = True
contador = 0
min_cW = pW // nxC  
min_cH = pH // nyC
camera_x = 0
camera_y = 0

while ejecutando:
    for evento in PY.event.get():
        if evento.type == PY.QUIT:
            ejecutando = False
    if contador % velocidad_movimiento == 0:
        for carnivoro in carnivoros:
            direccion = RA.choice(["arriba", "abajo", "izquierda", "derecha"])
            carnivoro.moverse(direccion, distancia=1)
            
        for herbivoro in herbivoros:
            direccion = RA.choice(["arriba", "abajo", "izquierda", "derecha"])
            herbivoro.moverse(direccion, distancia=1)
    for i in range(len(carnivoros)):
        for j in range(i + 1, len(carnivoros)):
            nuevo_carnivoro = carnivoros[i].reproducirse(carnivoros[j])
            if nuevo_carnivoro:
                carnivoros.append(nuevo_carnivoro)

    for i in range(len(herbivoros)):
        for j in range(i + 1, len(herbivoros)):
            nuevo_herbivoro = herbivoros[i].reproducirse(herbivoros[j])
            if nuevo_herbivoro:
                herbivoros.append(nuevo_herbivoro)

    contador += 1

    for planta in plantas:
        planta.crecer()

    screen.fill(fondo_color)
    for y in range(0, nyC):
        for x in range(0, nxC):
            # Calcula las posiciones en pantalla teniendo en cuenta la cámara
            screen_x = x * cW - camera_x * cW
            screen_y = y * cH - camera_y * cH
            rect = (screen_x, screen_y, cW, cH)

    matriz_espacial = [[[] for _ in range(nxC)] for _ in range(nyC)]

    for planta in plantas:
        matriz_espacial[planta.posicion[1]][planta.posicion[0]].append(planta)

    for carnivoro in carnivoros:
        matriz_espacial[carnivoro.posicion[1]][carnivoro.posicion[0]].append(carnivoro)

    for herbivoro in herbivoros:
        matriz_espacial[herbivoro.posicion[1]][herbivoro.posicion[0]].append(herbivoro)

    dibujar_matriz()
    PY.display.flip()
PY.quit()

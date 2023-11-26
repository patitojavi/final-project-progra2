import pygame as PY
import random as RA

from bioma import Bioma, Desierto, Agua, Tierra,patron_biomas,bioma_dict
from organismo import Organismo
from animales import Animal, Lobo, Guepardo, Cerdo, Gallina, Oveja, Vaca, Conejo, Oso, Leon, Zorro
from plantas import Planta, Nenufar, ArbolDesierto, ArbolTierra
from constantes import fondo_color, velocidad_movimiento, cW, cH, nxC, nyC, min_cW, min_cH, pW, pH
from ambiente import Ambiente
from ecosistema import Ecosistema


PY.init()

screen = PY.display.set_mode((pW, pH))
PY.display.set_caption("Ecosistema Simulator")

matriz_biomas = [[[] for _ in range(nxC)] for _ in range(nyC)]

# Colocar el patrón en la matriz
for y, fila in enumerate(patron_biomas):
    for x, caracter in enumerate(fila):
        matriz_biomas[y][x] = bioma_dict[caracter]

num_plantas = 2
num_carnivoros = 0
num_herbivoros = 5

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
    contador += 1


    matriz_espacial = [[[] for _ in range(nxC)] for _ in range(nyC)]

    for planta in plantas:
        matriz_espacial[planta.posicion[1]][planta.posicion[0]].append(planta)

    for carnivoro in carnivoros:
        matriz_espacial[carnivoro.posicion[1]][carnivoro.posicion[0]].append(carnivoro)

    for herbivoro in herbivoros:
        matriz_espacial[herbivoro.posicion[1]][herbivoro.posicion[0]].append(herbivoro)

    for carnivoro in carnivoros:
        presas_potenciales = matriz_espacial[carnivoro.posicion[1]][carnivoro.posicion[0]]
        carnivoro.cazar([presa for presa in presas_potenciales if isinstance(presa, Animal)])

    for herbivoro in herbivoros:
        posibles_compañeros = matriz_espacial[herbivoro.posicion[1]][herbivoro.posicion[0]]
        nuevo_animal = herbivoro.reproducirse(
        [otro for otro in posibles_compañeros if isinstance(otro, Animal) and otro != herbivoro]
    )
    if nuevo_animal:  # Agregar verificación aquí para el nuevo animal
        herbivoros.append(nuevo_animal)
    
    dibujar_matriz()
    PY.display.flip()
PY.quit()

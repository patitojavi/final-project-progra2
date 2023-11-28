import pygame as PY
import random as RA

from Bioma import patron_biomas,bioma_dict,Tierra,Agua,Desierto
from organismo import Organismo
from animales import Animal, Lobo, Guepardo, Cerdo, Gallina, Oveja, Vaca, Conejo, Oso, Leon, Zorro
from plantas import Planta, Nenufar, ArbolDesierto, ArbolTierra
from constantes import fondo_color, velocidad_movimiento, cW, cH, nxC, nyC, min_cW, min_cH, pW, pH, num_carnivoros, num_herbivoros, cantidad_nenufares, cantidad_arboles_desierto, cantidad_arboles_tierra, ejecutando, contador
from ambiente import Ambiente
from ecosistema import Ecosistema
from logger import logger

PY.init()

screen = PY.display.set_mode((pW, pH))
PY.display.set_caption("Ecosistema Simulator")


matriz_biomas = [[[] for _ in range(nxC)] for _ in range(nyC)]

# Colocar el patrón en la matriz
for y, fila in enumerate(patron_biomas):
    for x, caracter in enumerate(fila):
        matriz_biomas[y][x] = bioma_dict[caracter]
        



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
            
            for organismo in matriz_espacial[y][x]:
                if isinstance(organismo, Planta):
                    organismo.imagen = PY.transform.scale(organismo.imagen_original, (cW, cH))
                    screen.blit(organismo.imagen, (x * cW, y * cH))  # Pintar la planta en la posición de la celda
                    
                elif isinstance(organismo, Animal):
                    organismo.dibujar(screen, cW, cH)

            color = max(colores) if colores else (0, 0, 0)
            PY.draw.rect(screen, color, rect, 1)


plantas = []

for y in range(nyC):
    for x in range(nxC):
        bioma_actual = matriz_biomas[y][x]
        if isinstance(bioma_actual, Agua) and cantidad_nenufares > 0 and RA.random() > 0.9:
            nenufar = Nenufar((x, y))
            bioma_actual.agregar_planta(nenufar)
            plantas.append(nenufar)
            cantidad_nenufares -= 1

        elif isinstance(bioma_actual, Desierto) and cantidad_arboles_desierto > 0 and RA.random() > 0.9:
            arbol_desierto = ArbolDesierto((x, y))
            bioma_actual.agregar_planta(arbol_desierto)
            plantas.append(arbol_desierto)
            cantidad_arboles_desierto -= 1

        elif isinstance(bioma_actual, Tierra) and cantidad_arboles_tierra > 0 and RA.random() > 0.9:
            arbol_tierra = ArbolTierra((x, y))
            bioma_actual.agregar_planta(arbol_tierra)
            plantas.append(arbol_tierra)
            cantidad_arboles_tierra -= 1
            
    if cantidad_nenufares == 0 and cantidad_arboles_desierto == 0 and cantidad_arboles_tierra == 0:
        # Si ya se han colocado todas las plantas deseadas, salir del bucle externo
        break


carnivoros = []
carnivoros.extend([Lobo((RA.randint(0, nxC - 1), RA.randint(0, nyC - 1))) for _ in range(num_carnivoros)])
carnivoros.extend([Guepardo((RA.randint(0, nxC - 1), RA.randint(0, nyC - 1))) for _ in range(num_carnivoros)])
carnivoros.extend([Leon((RA.randint(0, nxC - 1), RA.randint(0, nyC - 1))) for _ in range(num_carnivoros)])
carnivoros.extend([Zorro((RA.randint(0, nxC - 1), RA.randint(0, nyC - 1))) for _ in range(num_carnivoros)])
carnivoros.extend([Oso((RA.randint(0, nxC - 1), RA.randint(0, nyC - 1))) for _ in range(num_carnivoros)])


herbivoros = []
herbivoros.extend([Cerdo((RA.randint(0, nxC - 1), RA.randint(0, nyC - 1))) for _ in range(num_herbivoros)])
herbivoros.extend([Gallina((RA.randint(0, nxC - 1), RA.randint(0, nyC - 1))) for _ in range(num_herbivoros)])
herbivoros.extend([Oveja((RA.randint(0, nxC - 1), RA.randint(0, nyC - 1))) for _ in range(num_herbivoros)])
herbivoros.extend([Vaca((RA.randint(0, nxC - 1), RA.randint(0, nyC - 1))) for _ in range(num_herbivoros)])
herbivoros.extend([Conejo((RA.randint(0, nxC - 1), RA.randint(0, nyC - 1))) for _ in range(num_herbivoros)])

ejecutando = True
clock = PY.time.Clock()
FPS = 120
matriz_espacial = [[[] for _ in range(nxC)] for _ in range(nyC)]
while ejecutando:
    for evento in PY.event.get():
        if evento.type == PY.QUIT:
            ejecutando = False

    if contador % velocidad_movimiento == 0:
        for carnivoro in carnivoros:
            direccion = RA.choice(["arriba", "abajo", "izquierda", "derecha"])
            carnivoro.moverse(direccion, distancia=1)
            logger.log_event(f"{carnivoro.especie} se movio a {carnivoro.posicion}")
        for herbivoro in herbivoros:
            direccion = RA.choice(["arriba", "abajo", "izquierda", "derecha"])
            herbivoro.moverse(direccion, distancia=1)
            logger.log_event(f"{herbivoro.especie} se movio a {herbivoro.posicion}")
            
            celda_actual = matriz_espacial[herbivoro.posicion[1]][herbivoro.posicion[0]]
            
            # Verificar si hay plantas en la celda actual y consumirlas si es el caso
            plantas_en_celda = [organismo for organismo in celda_actual if isinstance(organismo, Planta)]
            for planta in plantas_en_celda:
                cantidad_comida = planta.valor_comida
                herbivoro.recuperar_energia(cantidad_comida)
                plantas.remove(planta)  # Eliminar la planta de la lista de plantas
                celda_actual.remove(planta)
                logger.log_event(f"{herbivoro.especie} ha consumido una {planta.tipo_planta} y ha recuperado {herbivoro.energia} de energia y ha recuperado {herbivoro.vida} de vida")

    
    contador += 1

    # Actualización de la matriz espacial

    matriz_espacial = [[[] for _ in range(nxC)] for _ in range(nyC)]

    for planta in plantas:
        matriz_espacial[planta.posicion[1]][planta.posicion[0]].append(planta)

    for carnivoro in carnivoros:
        matriz_espacial[carnivoro.posicion[1]][carnivoro.posicion[0]].append(carnivoro)

    for herbivoro in herbivoros:
        matriz_espacial[herbivoro.posicion[1]][herbivoro.posicion[0]].append(herbivoro)

    for carnivoro in carnivoros:
        presas_potenciales = matriz_espacial[carnivoro.posicion[1]][carnivoro.posicion[0]]


    # Proceso de reproducción y adición de nuevos animales
    for y in range(0, nyC):
        for x in range(0, nxC):
            posibles_compañeros = matriz_espacial[y][x]
            for organismo in posibles_compañeros:
                if isinstance(organismo, Animal):
                    nuevo_animal = organismo.reproducirse(
                        [otro for otro in posibles_compañeros if isinstance(otro, Animal) and otro != organismo]
                    )
                    if nuevo_animal:
                        if isinstance(nuevo_animal, Animal):
                            if nuevo_animal.dieta == "herbivoro":
                                herbivoros.append(nuevo_animal)
                            elif nuevo_animal.dieta == "Carnívoro":
                                carnivoros.append(nuevo_animal)
                            # Aquí puedes añadir un mensaje o alguna acción visual para indicar la reproducción
                            print(f"¡Se ha reproducido un nuevo {nuevo_animal.especie}!")


    # Dibujar la matriz y actualizar la pantalla
    dibujar_matriz()
    PY.display.flip()
    clock.tick(FPS)

PY.quit()
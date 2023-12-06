import pygame as PY
import random as RA
import logging

from Bioma import patron_biomas,bioma_dict,Tierra,Agua,Desierto, Lava, Lluvia,Nieve
from animales import Animal, Lobo, Guepardo, Cerdo, Gallina, Oveja, Vaca, Conejo, Oso, Leon, Zorro
from plantas import Planta, Nenufar, ArbolDesierto, ArbolTierra
from constantes import fondo_color, velocidad_movimiento, cW, cH, nxC, nyC, pW, pH, num_carnivoros, num_herbivoros, cantidad_nenufares, cantidad_arboles_desierto, cantidad_arboles_tierra, ejecutando, contador


logging.basicConfig(filename='simulador.txt', level=logging.INFO)

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
    if nieve.nieve_activa:  # Dibuja la nieve solo cuando esté activa
        nieve.dibujar(screen)
    lluvia.dibujar(screen)
    PY.display.flip()

plantas = []

for y in range(nyC):
    for x in range(nxC):
        bioma_actual = matriz_biomas[y][x]
        if not isinstance(bioma_actual, Lava):
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
            break


carnivoros = []
carnivoros.extend([
    Lobo(
        posicion=(RA.randint(0, nxC - 1), RA.randint(0, nyC - 1)),
        vida=RA.randint(50, 100),
        energia=RA.randint(20, 50),
        velocidad=RA.uniform(5, 2),
        especie="Lobo",
        dieta="Carnívoro"
    )
    for _ in range(num_carnivoros)
])

carnivoros.extend([
    Leon(
        posicion=(RA.randint(0, nxC - 1), RA.randint(0, nyC - 1)),
        vida=RA.randint(50, 100),
        energia=RA.randint(20, 50),
        velocidad=RA.uniform(5, 2),
        especie="Leon",
        dieta="Carnívoro"
    )
    for _ in range(num_carnivoros)
])

carnivoros.extend([
    Zorro(
        posicion=(RA.randint(0, nxC - 1), RA.randint(0, nyC - 1)),
        vida=RA.randint(50, 100),
        energia=RA.randint(20, 50),
        velocidad=RA.uniform(5, 2),
        especie="Zorro",
        dieta="Carnívoro"
    )
    for _ in range(num_carnivoros)
])

carnivoros.extend([
    Guepardo(
        posicion=(RA.randint(0, nxC - 1), RA.randint(0, nyC - 1)),
        vida=RA.randint(50, 100),
        energia=RA.randint(20, 50),
        velocidad=RA.uniform(5, 2),
        especie="Guepardo",
        dieta="Carnívoro"
    )
    for _ in range(num_carnivoros)
])

carnivoros.extend([
    Oso(
        posicion=(RA.randint(0, nxC - 1), RA.randint(0, nyC - 1)),
        vida=RA.randint(50, 100),
        energia=RA.randint(20, 50),
        velocidad=RA.uniform(5, 2),
        especie="Oso",
        dieta="Carnívoro"
    )
    for _ in range(num_carnivoros)
])


herbivoros = []
herbivoros.extend([
    Conejo(
        posicion=(RA.randint(0, nxC - 1), RA.randint(0, nyC - 1)),
        vida=RA.randint(50, 100),
        energia=RA.randint(20, 50),
        velocidad=RA.uniform(5, 2),
        especie="Conejo",
        dieta="herbivoro"
    )
    for _ in range(num_herbivoros)
])

herbivoros.extend([
    Cerdo(
        posicion=(RA.randint(0, nxC - 1), RA.randint(0, nyC - 1)),
        vida=RA.randint(50, 100),
        energia=RA.randint(20, 50),
        velocidad=RA.uniform(5, 2),
        especie="Cerdo",
        dieta="herbivoro"
    )
    for _ in range(num_herbivoros)
])

herbivoros.extend([
    Gallina(
        posicion=(RA.randint(0, nxC - 1), RA.randint(0, nyC - 1)),
        vida=RA.randint(50, 100),
        energia=RA.randint(20, 50),
        velocidad=RA.uniform(5, 2),
        especie="Gallina",
        dieta="herbivoro"
    )
    for _ in range(num_herbivoros)
])


herbivoros.extend([
    Oveja(
        posicion=(RA.randint(0, nxC - 1), RA.randint(0, nyC - 1)),
        vida=RA.randint(50, 100),
        energia=RA.randint(20, 50),
        velocidad=RA.uniform(5, 2),
        especie="Oveja",
        dieta="herbivoro"
    )
    for _ in range(num_herbivoros)
])


herbivoros.extend([
    Vaca(
        posicion=(RA.randint(0, nxC - 1), RA.randint(0, nyC - 1)),
        vida=RA.randint(50, 100),
        energia=RA.randint(20, 50),
        velocidad=RA.uniform(5, 2),
        especie="Vaca",
        dieta="herbivoro"
    )
    for _ in range(num_herbivoros)
])

ejecutando = True
pausado = False
activar_lava = False
llenado_progresivo = False
contador_llenado = 0
clock = PY.time.Clock()
FPS = 120
matriz_espacial = [[[] for _ in range(nxC)] for _ in range(nyC)]
lluvia = Lluvia() 
nieve = Nieve()

while ejecutando:
    for evento in PY.event.get():
        if evento.type == PY.QUIT:
            ejecutando = False
        elif evento.type == PY.KEYDOWN:
            if evento.key == PY.K_SPACE:
                lluvia.activar_lluvia()
            elif evento.key == PY.K_n:
                nieve.activar_nieve()
            elif evento.key == PY.K_ESCAPE:
                lluvia.desactivar_lluvia()
            elif evento.key == PY.K_q:
                nieve.desactivar_nieve()  # Desactivar la nieve al presionar Escape
            elif evento.key == PY.K_l:
                llenado_progresivo = True
                contador_llenado = 0
                activar_lava = True

    if not pausado:
        if activar_lava:
            for _ in range(5):  # Ajusta el número de celdas que se llenarán en cada iteración
                x = RA.randint(0, nxC - 1)
                y = RA.randint(0, nyC - 1)
                if matriz_biomas[y][x].image != bioma_dict["L"].image:
                    matriz_biomas[y][x] = bioma_dict["L"]
                    contador_llenado += 1
            # Detener el llenado progresivo después de cierto progreso
            if contador_llenado >= nyC * nxC / 2:
                llenado_progresivo = False
                activar_lava = False
        else:
            if contador % velocidad_movimiento == 0:
                for carnivoro in carnivoros:
                    direccion = RA.choice(["arriba", "abajo", "izquierda", "derecha"])
                    carnivoro.moverse(direccion, distancia=1)
                    nuevo_bioma = matriz_biomas[carnivoro.posicion[1]][carnivoro.posicion[0]]
                    if isinstance(nuevo_bioma, Lava):
                        vida_anterior = carnivoro.vida
                        carnivoro.vida = max(carnivoro.vida - 10, 0)  # Ajusta el valor de reducción de vida
                        logging.info(f"{carnivoro.especie} perdio vida al pisar lava. Vida restante: {carnivoro.vida}")
                    
                for herbivoro in herbivoros:
                    direccion = RA.choice(["arriba", "abajo", "izquierda", "derecha"])
                    herbivoro.moverse(direccion, distancia=1)
                    nuevo_bioma = matriz_biomas[herbivoro.posicion[1]][herbivoro.posicion[0]]
                    if isinstance(nuevo_bioma, Lava):
                        vida_anterior = herbivoro.vida
                        herbivoro.vida = max(herbivoro.vida - 10, 0)  # Ajusta el valor de reducción de vida
                        logging.info(f"{herbivoro.especie} perdio vida al pisar lava. Vida restante: {herbivoro.vida}")
                    
                    celda_actual = matriz_espacial[herbivoro.posicion[1]][herbivoro.posicion[0]]
                    
                    # Verificar si hay plantas en la celda actual y consumirlas si es el caso
                    plantas_en_celda = [organismo for organismo in celda_actual if isinstance(organismo, Planta)]
                    for planta in plantas_en_celda:
                        cantidad_comida = planta.valor_comida
                        vida_anterior = herbivoro.vida  # Almacenar la vida antes de consumir la planta
                        herbivoro.recuperar_energia(cantidad_comida)
                        vida_recuperada = herbivoro.vida - vida_anterior  # Calcular la vida recuperada
                        plantas.remove(planta)  # Eliminar la planta de la lista de plantas
                        celda_actual.remove(planta)
                        logging.info(f"{herbivoro.especie} consumio una planta. Vida recuperada: {vida_recuperada}")
                        
            contador += 1

            # Actualización de la matriz espacial
            matriz_espacial = [[[] for _ in range(nxC)] for _ in range(nyC)]
            for planta in plantas:
                matriz_espacial[planta.posicion[1]][planta.posicion[0]].append(planta)
            for carnivoro in carnivoros:
                matriz_espacial[carnivoro.posicion[1]][carnivoro.posicion[0]].append(carnivoro)
            for herbivoro in herbivoros:
                matriz_espacial[herbivoro.posicion[1]][herbivoro.posicion[0]].append(herbivoro)
            for y in range(0, nyC):
                for x in range(0, nxC):
                    presas = [organismo for organismo in matriz_espacial[y][x] if isinstance(organismo, Animal) and organismo.dieta == "herbivoro"]
                    carnivoros_en_celda = [organismo for organismo in matriz_espacial[y][x] if isinstance(organismo, Animal) and organismo.dieta == "Carnívoro"]
                    
                    for carnivoro in carnivoros_en_celda:
                        vida_anterior = carnivoro.vida
                        energia_anterior = carnivoro.energia
                        carnivoro.cazar(presas, herbivoros)
                        vida_recuperada = carnivoro.vida - vida_anterior
                        energia_recuperada = carnivoro.energia - energia_anterior


            # Proceso de reproducción y adición de nuevos animales
            for y in range(0, nyC):
                for x in range(0, nxC):
                    posibles_compañeros = matriz_espacial[y][x]
                    for organismo in posibles_compañeros:
                        if isinstance(organismo, Animal):
                            nuevo_animal = organismo.reproducirse(
                                [otro for otro in posibles_compañeros if isinstance(otro, Animal) and otro != organismo]
                            )
                            if nuevo_animal is not None:
                                if isinstance(nuevo_animal, Animal):
                                    if nuevo_animal.dieta == "herbivoro":
                                        herbivoros.append(nuevo_animal)
                                    elif nuevo_animal.dieta == "Carnívoro":
                                        carnivoros.append(nuevo_animal)
                                        
    lluvia.actualizar()
    nieve.actualizar()  # Asegúrate de llamar a la función actualizar de la clase Nieve # Dibujar la lluvia en la pantalla
    dibujar_matriz()
    PY.display.flip()
    clock.tick(FPS)

PY.quit()
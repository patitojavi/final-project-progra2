import pygame as PY
import random as RA
import pygame_gui

from Bioma import patron_biomas,bioma_dict,Tierra,Agua,Desierto
from organismo import Organismo
from animales import Animal, Lobo, Guepardo, Cerdo, Gallina, Oveja, Vaca, Conejo, Oso, Leon, Zorro
from plantas import Planta, Nenufar, ArbolDesierto, ArbolTierra
from constantes import fondo_color, velocidad_movimiento, cW, cH, nxC, nyC, min_cW, min_cH, pW, pH
from ambiente import Ambiente
from ecosistema import Ecosistema


PY.init()

screen = PY.display.set_mode((pW, pH))
PY.display.set_caption("Ecosistema Simulator")

# Crear una ventana para la interfaz gráfica
manager = pygame_gui.UIManager((pW, pH))

# Crear un botón para agregar plantas
button_planta = pygame_gui.elements.UIButton(
    relative_rect=PY.Rect((10, 10), (100, 30)),
    text='Agregar Planta',
    manager=manager
)

# Crear un botón para agregar carnívoros
button_carnivoro = pygame_gui.elements.UIButton(
    relative_rect=PY.Rect((10, 50), (100, 30)),
    text='Agregar Carnívoro',
    manager=manager
)

# Crear un botón para agregar herbívoros
button_herbivoro = pygame_gui.elements.UIButton(
    relative_rect=PY.Rect((10, 90), (100, 30)),
    text='Agregar Herbívoro',
    manager=manager
)

matriz_biomas = [[[] for _ in range(nxC)] for _ in range(nyC)]

# Colocar el patrón en la matriz
for y, fila in enumerate(patron_biomas):
    for x, caracter in enumerate(fila):
        matriz_biomas[y][x] = bioma_dict[caracter]
        

num_plantas = 2
num_carnivoros = 0
num_herbivoros = 6

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

cantidad_nenufares = 10
cantidad_arboles_desierto = 10
cantidad_arboles_tierra = 10

plantas = [
    Nenufar((RA.randint(0, nxC - 1), RA.randint(0, nyC - 1))),
    ArbolDesierto((RA.randint(0, nxC - 1), RA.randint(0, nyC - 1))),
    ArbolTierra((RA.randint(0, nxC - 1), RA.randint(0, nyC - 1)))
]

    
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
        carnivoro.cazar([presa for presa in presas_potenciales if isinstance(presa, Animal)], herbivoros)

    # Proceso de reproducción y adición de nuevos animales
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

PY.quit()


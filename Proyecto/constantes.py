import pygame as PY

pW = 800
pH = 800
fondo_color = (0, 0, 0)
nxC = 50
nyC = 50
cH = pW // nxC
cW = pH // nyC
min_cW = pW // nxC
min_cH = pH // nyC
velocidad_movimiento = 30

num_carnivoros = 2
num_herbivoros = 10
cantidad_nenufares = 150
cantidad_arboles_desierto = 150
cantidad_arboles_tierra = 150

ejecutando = True
contador = 0



""" def cargarimagen(nombre):
    return PY.transform.scale(PY.image.load(nombre), (cW, cH))
"""

""" leonImg = cargarimagen("Proyecto/imagenes/leon.png")
guepardoImg = cargarimagen("Proyecto/imagenes/guepardo.png")
loboImg = cargarimagen("Proyecto/imagenes/lobo.png")
osoImg = cargarimagen("Proyecto/imagenes/oso.png")
zorroImg = cargarimagen("Proyecto/imagenes/zorro.png")

conejoImg = cargarimagen("Proyecto/imagenes/conejo.png")
vacaImg = cargarimagen("Proyecto/imagenes/vaca.png")
ovejaImg = cargarimagen("Proyecto/imagenes/oveja.png")
cerdoImg = cargarimagen("Proyecto/imagenes/cerdo.png")
conejoImg = cargarimagen("Proyecto/imagenes/conejo.png")

nenufarImg = cargarimagen("Proyecto/imagenes/nenufar.png")
arbolDesiertoImg = cargarimagen("Proyecto/imagenes/arbolDesierto.png")
arbolTierraImg = cargarimagen("Proyecto/imagenes/arbolTierra.png")

tierraImg = cargarimagen("Proyecto/imagenes/tierra.png")
desiertoImg = cargarimagen("Proyecto/imagenes/desierto.png")
aguaImg = cargarimagen("Proyecto/imagenes/agua.png")
 """
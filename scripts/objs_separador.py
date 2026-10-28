"""
DESCRIPCION:
este script organiza automaticamente todos los objetos seleccionados en Blender
distribuyendolos en una cuadricula sobre el plano X-Y.

es ideal para cuando importas multiples modelos que se enciman en el origen (0,0,0)
y necesitas separarlos visualmente de forma rapida sin moverlos uno por uno

INSTRUCCIONES:
1. selecciona en Blender todos los objetos que quieras ordenar
2. abri el Editor de texto de Blender, pega este codigo y ejecutalo (Run Script)
"""

import bpy
import math

# configuracion
DISTANCIA = 5.0  # espacio en metros entre cada objeto

# obtener objetos seleccionados
objetos = bpy.context.selected_objects

# calcular el tamaño de la cuadricula
columnas = math.ceil(math.sqrt(len(objetos)))

for index, obj in enumerate(objetos):
    # calcular la posicion en la cuadricula
    fila = index // columnas
    columna = index % columnas

    # aplicar la nueva posicion en los ejes X e Y
    obj.location.x = columna * DISTANCIA
    obj.location.y = fila * DISTANCIA
    obj.location.z = 0  # mantiene los objetos en el suelo

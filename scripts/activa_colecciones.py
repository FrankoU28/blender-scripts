"""
DESCRIPCION:
este script activa (incluye) todas las colecciones y subcolecciones dentro de la
Vista Actual (View Layer) de Blender.

es muy util cuando importas archivos complejos donde muchas colecciones vienen
desactivadas o excluidas por defecto y tambien cuando las desactivaste todas por algun motivo
y necesitas que todas sean visibles de golpe en la escena sin tener que habilitarlas una por una en el panel Outliner.

INSTRUCCIONES:
1. abri el Editor de Texto de Blender, pega este codigo y ejecutalo (Run Script)
"""

import bpy


def enable_all_layer_collections(layer_collection):
    layer_collection.exclude = False
    for child in layer_collection.children:
        enable_all_layer_collections(child)


view_layer = bpy.context.view_layer
enable_all_layer_collections(view_layer.layer_collection)

print("Todas las colecciones activadas en la View Layer")

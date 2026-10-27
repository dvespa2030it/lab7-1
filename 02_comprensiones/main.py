"""EJERCICIO 02 — Preparar un catálogo

ENUNCIADO
Cada producto tiene nombre, precio y categoria. Los nombres son únicos.
Devuelve un diccionario con:
- disponibles: lista de nombres con precio <= 20, en el orden original.
- precios: diccionario nombre -> precio de todos los productos.
- categorias: set de todas las categorías.
Usa una comprensión para cada estructura. No uses ciclos explícitos.
No modifiques la entrada. Para [] devuelve las tres estructuras vacías.

Con los datos entregados se espera:
{"disponibles": ["cafe", "te"],
 "precios": {"cafe": 10, "torta": 25, "te": 8},
 "categorias": {"bebida", "postre"}}
El orden de los elementos del set puede cambiar.

ENTREGA
Completa la implementación sin cambiar los nombres ni los parámetros.
Ejecuta el archivo y compara lo impreso con el resultado del enunciado.
Añade al menos otro ejemplo usando print y escribe en un comentario qué esperas.
Al terminar: git commit -m "Resuelve ejercicio 02".
"""

def preparar_catalogo(productos):
    return {
        "disponibles": [
            producto["nombre"]
            for producto in productos
            if producto["precio"] <= 20
        ],
        "precios": {
            producto["nombre"]: producto["precio"]
            for producto in productos
        },
        "categorias": {
            producto["categoria"]
            for producto in productos
        },
    }


# Imprime el catálogo esperado por el enunciado.
productos = [
    {"nombre": "cafe", "precio": 10, "categoria": "bebida"},
    {"nombre": "torta", "precio": 25, "categoria": "postre"},
    {"nombre": "te", "precio": 8, "categoria": "bebida"},
]
print(preparar_catalogo(productos))

# Se esperan las tres estructuras vacías.
print(preparar_catalogo([]))

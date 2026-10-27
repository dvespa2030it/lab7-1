"""EJERCICIO 03 — Precios con recargo

ENUNCIADO
Dentro de la función, define una lambda que reciba un precio y devuelva
ese precio con un recargo del 10 %, redondeado a dos decimales con round.
Aplica la lambda mediante un ciclo y devuelve una lista.
No uses map todavía. Los precios son no negativos. No modifiques la entrada.
Para [] devuelve [].

Entrada: [10, 20, 35]
Resultado esperado: [11.0, 22.0, 38.5]

ENTREGA
Completa la implementación sin cambiar los nombres ni los parámetros.
Ejecuta el archivo y compara lo impreso con el resultado del enunciado.
Añade al menos otro ejemplo usando print y escribe en un comentario qué esperas.
Al terminar: git commit -m "Resuelve ejercicio 03".
"""

def calcular_importes(precios):
    aplicar_recargo = lambda precio: round(precio * 1.10, 2)
    importes = []

    # Se define calcular_importes con un recargo del 10% 

    for precio in precios:
        importes.append(aplicar_recargo(precio))

    #Se crea un ciclo for para agregar el nuevo precio con el recargo
    return importes

    #Se retorna el nuevo importe

# Esperado: [11.0, 22.0, 38.5]
precios = [10, 20, 35]
print(calcular_importes(precios))

# Esperado: [13.75, 0.0]
print(calcular_importes([12.5, 0]))

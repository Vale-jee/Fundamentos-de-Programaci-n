# Buscar valor en Matriz bidimensional
matriz_bidi = [
    [5, 7, 14],
    [19, 18, 10],
    [24, 6, 15]
]

# Buscar un valor en la matriz
valor_bus =  15  # Este es el valor que quiero buscar
encontrado = False  #verificar si el valor fue encontrado

for fila in matriz_bidi:
    if valor_bus in fila:
        fila_posicion = matriz_bidi.index(fila)
        columna_posicion = fila.index(valor_bus)

        print(f"El valor buscado es {valor_bus} y se encontró en la posición {[fila_posicion]},{[columna_posicion]}.")
        encontrado = valor_bus
        break  # Salimos del bucle si encontramos el valor

if not encontrado:
    print(f"El valor {valor_bus} no se encontró en la matriz.")
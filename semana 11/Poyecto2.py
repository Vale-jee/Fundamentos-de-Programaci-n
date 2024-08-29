# Ordenar fila en Matriz 3x3
matriz = [
    [34, 21, 56],
    [12, 89, 45],
    [78, 23, 10]
]

# Imprimir la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Seleccionar la fila que se desea ordenar
fila_seleccionada = 0

# Función Bubble Sort para ordenar la fila seleccionada
def bubble_sort_fila(fila):
    for _ in range(len(fila) - 1):
        for j in range(len(fila) - 1):
            # Comparar elementos adyacentes
            if fila[j] > fila[j + 1]:
                # Intercambiar elementos si están en el orden incorrecto
                fila[j], fila[j + 1] = fila[j + 1], fila[j]

# Ordenar la fila seleccionada usando Bubble Sort
bubble_sort_fila(matriz[fila_seleccionada])

# Imprimir la matriz con la fila ordenada
print(f"\nMatriz con la fila {fila_seleccionada + 1} ordenada:")
for fila in matriz:
    print(fila)
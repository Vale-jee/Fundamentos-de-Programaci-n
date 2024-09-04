# Iteración de arreglos multidimensionales con bucles anidados
# Creo una matriz 3D (ciudad,semana,temperatura)

arre_temperaturas = [
    # Ciudad 1: Ambato
    [[17, 19, 21, 16, 13, 8, 10],  # Semana 1
     [20, 15, 18, 22, 16, 19, 17],  # Semana 2
     [19, 22, 15, 16, 11, 21, 12],  # Semana 3
     [22, 18, 19, 13, 16, 20, 12]],  # Semana 4

    # Ciudad 2: Esmeraldas
    [[26, 27, 26, 29, 28, 27, 30],  # Semana 1
     [31, 27, 30, 29, 28, 26, 27],  # Semana 2
     [28, 30, 26, 27, 29, 31, 28],  # Semana 3
     [30, 29, 28, 29, 31, 27, 26]],  # Semana 4

    # Ciudad 3: Tulcan
    [[12, 13, 13, 18, 14, 9, 10],  # Semana 1
     [21, 15, 12, 10, 20, 19, 11],  # Semana 2
     [19, 20, 13, 10, 17, 16, 19],  # Semana 3
     [20, 15, 13, 18, 16, 12, 17]]  # Semana 4
]
nombres_ciudades = ["Ambato", "Esmeraldas", "Tulcan"]

# Iterar por ciudad
for ciudad in range(len(arre_temperaturas)):
    print(f"Ciudad: {nombres_ciudades[ciudad]}")

    # Iterar por semana
    for semana in range(len(arre_temperaturas[ciudad])):
        acumulador = 0

        # Sumar las temperaturas de la semana
        for temperatura in range(len(arre_temperaturas[ciudad][semana])):
            acumulador = acumulador + arre_temperaturas[ciudad][semana][temperatura]

        # Calcular el promedio
        promedio = acumulador / len(arre_temperaturas[ciudad][semana])

        # Imprimir el promedio de la semana
        print(f"  Semana {semana + 1}: Promedio de temperatura = {promedio:.2f}°C")

    print()  # Espacio en blanco para separar las ciudades
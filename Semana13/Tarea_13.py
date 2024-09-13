#Desarrolla una función que calcule la temperatura promedio de una ciudad durante un período de tiempo
#Lista de ciudades, semanas y temperaturas
ciudades_tem = [
    # Ambato
    [[17, 19, 21, 16, 13, 8, 10],
     [20, 15, 18, 22, 16, 19, 17],
     [19, 22, 15, 16, 11, 21, 12],
     [22, 18, 19, 13, 16, 20, 12]],

    # Esmeraldas
    [[26, 27, 26, 29, 28, 27, 30],
     [31, 27, 30, 29, 28, 26, 27],
     [28, 30, 26, 27, 29, 31, 28],
     [30, 29, 28, 29, 31, 27, 26]],

    # Tulcan
    [[12, 13, 13, 18, 14, 9, 10],
     [21, 15, 12, 10, 20, 19, 11],
     [19, 20, 13, 10, 17, 16, 19],
     [20, 15, 13, 18, 16, 12, 17]]
]

# Lista de ciudades
ciudades = ["Ambato", "Esmeraldas", "Tulcan"]

def calcular_promedio_temperatura(ciudades_tem, ciudad_index):
    # Obtener las temperaturas de la ciudad seleccionada
    temperaturas_ciudad = ciudades_tem[ciudad_index]

    # Calcular el promedio de la temperatura sumando todas las temperaturas y dividiendo por el número total de días
    total_dias = sum(len(semana) for semana in temperaturas_ciudad)
    suma_temperaturas = sum(sum(semana) for semana in temperaturas_ciudad)

    promedio = suma_temperaturas / total_dias

    return promedio

# calcular el promedio de la temperatura para una ciudad dada
ciudad_nombre = "Esmeraldas"  # Escriba el nombre de la ciudad

if ciudad_nombre in ciudades:
    ciudad_index = ciudades.index(ciudad_nombre)   # Obtiene el índice de la ciudad
    promedio_ciudad = calcular_promedio_temperatura(ciudades_tem, ciudad_index)
    print(f"El promedio de temperatura en {ciudad_nombre} es: {promedio_ciudad:.2f} °C")
else:
    print(f"La ciudad {ciudad_nombre} no está en la lista.")

# Operaciones de lectura y escritura en archivos de texto
# Escritura de archivo de texto
# Metodo de apertura: "w" para escritura (write)
archivo_escritura = open("my_notes.txt", "w")

#Metodo write(): Escribir una linea a la vez
# Escribimos tres líneas de notas personales en el archivo
archivo_escritura.write("linea 1: Mi nombre es Valeria Chucchilan.\n")
archivo_escritura.write("linea 2: Estudio en la Universidad Estatal Amazónica.\n")
archivo_escritura.write("linea 3: La carrera de Tecnologías de la Información.\n")

# Cerramos el archivo después de escribir
archivo_escritura.close()

# Metodo de apertura "r" para lectura (readline)
archivo_lectura = open("my_notes.txt", "r")

#Metodo readline(): lee una linea a la vez
linea_1 = archivo_lectura.readline()  # Leemos la primera línea
linea_2 = archivo_lectura.readline()  # Leemos la segunda línea
linea_3 = archivo_lectura.readline()  # Leemos la tercera línea

# Mostramos las líneas leídas
print(linea_1.strip())  # Eliminamos saltos de línea con strip()
print(linea_2.strip())
print(linea_3.strip())

# Cerramos el archivo después de leer
archivo_lectura.close()


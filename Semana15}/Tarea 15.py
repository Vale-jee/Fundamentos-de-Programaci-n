# Diccionario con información personal
informacion_personal = {

"nombre": "Lorena Torres",

"edad": 36,

"ciudad": "Quito",
"profesion": "Arquitecta"
}

# Acceder y modificar la "ciudad"
print("Ciudad original:", informacion_personal["ciudad"])
informacion_personal["ciudad"]= "Guayaquil"
print("Ciudad modificada:", informacion_personal["ciudad"])

# Agregar una nueva  "profesion"

informacion_personal["profesion"] = "Ingeniera Civil"

# Verificar existencia de "telefono"
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987174567"  # Número ficticio

# Eliminar la "edad"
    del informacion_personal["edad"]

# Imprimir la informacion final
print("Información final:", informacion_personal)
#Un articulo en una tienda cuesta $120 y esta en promoción con un 30% de descuento.
# Además hay un cupon adicional que otorgo el 10% de descuento sobre el precio ya rebajado.

# Definir la función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento):
    # Calcular el descuento
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Aplicar el 30% de descuento (promoción inicial)
monto_total = 120
descuento_promocion = calcular_descuento(monto_total, 30)
monto_rebajado = monto_total - descuento_promocion

# Aplicar el 10% de descuento adicional sobre el monto rebajado (cupón)
descuento_cupon = calcular_descuento(monto_rebajado, 10)
monto_final = monto_rebajado - descuento_cupon

#Calcular el descuento total
total_descuento = descuento_promocion + descuento_cupon

# Mostrar los resultados
print(f"Precio original: ${monto_total:.2f}")
print(f"Descuento promocional (30%): ${descuento_promocion:.2f}")
print(f"Precio después del descuento promocional: ${monto_rebajado:.2f}")
print(f"Descuento adicional (10% sobre precio rebajado): ${descuento_cupon:.2f}")
print(f"Monto final a pagar: ${monto_final:.2f}")
print(f"Su descuento total en su compra fue de: ${total_descuento:.2f}")
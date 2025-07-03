# Existen 3 categorías de cliente: - 1 → Frecuente (10% de descuento) - 2 → Corporativo (15%) - 3 → VIP (25%)
# El programa debe recibir el tipo de cliente y el valor de la compra y calcular el valor con
# descuento. Si el tipo es inválido, mostrar un mensaje de error.

print("1 → Frecuente (10%)")
print("2 → Corporativo (15%)")
print("3 → VIP (25%)")

tipo = int(input("Ingresa el codigo del tipo de cliente: "))
compra = int(input("Ingrese el valor de la compra: "))

if tipo == 1:
    descuento = compra * 0.1
    total = compra - descuento
    print(f"Total con descuento: {total}")
elif tipo == 2:
    descuento = compra * 0.15
    total = compra - descuento
    print(f"Total con descuento: {total}")
elif tipo == 3:
    descuento = compra * 0.25
    total = compra - descuento
    print(f"Total con descuento: {total}")
else:
    print("Tipo de cliente no valido")

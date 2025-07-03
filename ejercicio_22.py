# Un sistema de reservas permite elegir entre 3 tipos de evento:
# 1. Cine ($20.000)
# 2. Teatro ($35.000)
# 3. Concierto ($50.000)
# Luego debe ingresar la cantidad de entradas deseadas. Si el compra supera los $100.000, se
# aplica un 10% de descuento. Calcula el compra a pagar.

print("1. Cine ($20.000)")
print("2. Teatro ($35.000)")
print("3. Concierto ($50.000)")

evento = int(input("Seleccione el tipo de evento: "))
entradas = int(input("Ingrese la cantidad de entradas deseadas: "))

if evento == 1:
    valor = 20000
elif evento == 2:
    valor = 35000
elif evento == 3:
    valor = 50000
else:
    print("Opción inválida")

compra = valor * entradas

if compra > 100000:
    descuento = compra * 0.10
    compra -= descuento

print(f"Total a pagar: ${compra}")



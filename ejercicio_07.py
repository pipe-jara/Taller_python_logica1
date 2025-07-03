# En una tienda de tecnología se aplican descuentos por el valor total de la compra: - Sin descuento si es menor a $100.000 - 5% si está entre $100.000 y $200.000 - 10% si supera los $200.000
# Crea un algoritmo que reciba el valor de la compra y muestre qué porcentaje de descuento
# aplica. 


valor_compra = int(input("Ingrese el total de la compra: "))

if valor_compra > 200000:
    descuento = 10
    total = valor_compra - (valor_compra * 0.10)
    print(f"El % descuento que aplica es: {descuento} %")
    print(f"El total de la compra con descuento es {total}")
elif valor_compra >= 100000:
    descuento = 5
    total = valor_compra - (valor_compra * 0.05)
    print(f"El % descuento que aplica es: {descuento} %")
    print(f"El total de la compra con descuento es:$ {total}")
else:
    print("El valor de la compra no aplica para descuento.")
    print(f"El total a pagar es:$ {valor_compra}")
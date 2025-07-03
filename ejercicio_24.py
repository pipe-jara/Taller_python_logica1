# Dependiendo del tipo de actividad, se aplica una retención: - Dependiente → 10% - Independiente → 15% - Empresario → 20%
# Solicita el tipo y el ingreso mensual y calcula el valor del impuesto. Valida que los ingresos
# sean positivos.

print("1. Dependiente → 10%")
print("2. Independiente → 15%")
print("3. Empresario → 20%")

tipo = int(input("ingresa el codigo del tipo de actividad: "))
ingresos = int(input("ingrese el valor de los ingresos: $"))

if ingresos <= 0:
    print("El valor de los ingresos debe ser positivos.")

if tipo == 1:
    retención = ingresos * 0.1
    print(f"El valor del impuesto es: ${retención}")
elif tipo == 2:
    retención = ingresos * 0.15
    print(f"El valor del impuesto es: ${retención}")
elif tipo == 3:
    retención = ingresos * 0.2
    print(f"El valor del impuesto es: ${retención}")
else:
    print("Tipo de actividad no valida")
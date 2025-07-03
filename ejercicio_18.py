# Desarrolla un algoritmo que muestre un menú con las siguientes opciones:
# 1. Sumar
# 2. Restar
# 3. Multiplicar
# 4. Dividir
# El usuario elige una opción e ingresa dos números. El programa debe realizar la operación
# seleccionada y mostrar el resultado. Si la división es por cero, indicar 'No se puede dividir
# por cero'. 

print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = int(input("Seleccione una opcion: "))

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if opcion == 1:
    print("Resultado: " , num1 + num2)
elif opcion == 2:
    print("Resultado: " , num1 - num2)
elif opcion == 3:
    print("Resultado: " , num1 * num2)
elif opcion == 4:
    if num2 == 0:
        print("No se puede dividir por cero")
    else:
        print("Resultado: " , num1 / num2) 



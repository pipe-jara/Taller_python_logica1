# Diseña un algoritmo que reciba un número del 1 al 7 y muestre el día correspondiente de la
# semana. Si se ingresa un número fuera de ese rango, mostrar un mensaje de error. Usa una
# estructura ‘según’ o ‘switch’.

num = int(input("Día de la semana (1-7): "))

if num == 1:
    print("Lunes")
elif num == 2:
    print("Martes")
elif num == 3:
    print("Miércoles")
elif num == 4:
    print("Jueves")
elif num == 5:
    print("Viernes")
elif num == 6:
    print("Sábado")
elif num == 7:
    print("Domingo")
else:
    print("Número fuera de rango")

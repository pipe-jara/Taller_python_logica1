# Crea un programa que lea un número del 1 al 12 y muestre el nombre del mes
# correspondiente. Por ejemplo, 1 → 'Enero', 2 → 'Febrero', etc. Si se ingresa un número
# inválido, mostrar 'Mes no válido'. 

num = int(input("Ingrese un numero de 1 al 12 : "))

if num == 1:
    print("Enero")
elif num == 2:
    print("Febrero")
elif num == 3:
    print("Marzo")
elif num == 4:
    print("Abril")
elif num == 5:
    print("Mayo")
elif num == 6:
    print("Junio")
elif num == 7:
    print("Julio")
elif num == 8:
    print("Agosto")
elif num == 9:
    print("Septiembre")
elif num == 10:
    print("Octubre")
elif num == 11:
    print("Noviembre")
elif num == 12:
    print("Diciembre")
else:
    print("Mes no valido")
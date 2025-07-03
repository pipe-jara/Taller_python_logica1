# Un parqueadero cobra según el tipo de vehículo: - Carro → $5.000/hora - Moto → $2.000/hora - Bicicleta → $500/hora
# Diseña un algoritmo que reciba el tipo de vehículo y el número de horas y calcule el total a pagar.

print("Carro → $5.000/hora")
print("Moto → $2.000/hora")
print("Bicicleta → $500/hora")

vehiculo = int(input("Ingrese el tipo de vehiculo: "))
hora = int(input("Ingrese el tiempo permanecido en el parqueadero: "))


Carro = 5000 
Moto = 2000
Bicicleta = 500

if vehiculo == 1:
    print("Total a pagar: $" , Carro * hora)
elif vehiculo == 2:
    print("Total a pagar: $" , Moto * hora)
elif vehiculo == 3:
    print("Total a pagar: $" , Bicicleta * hora)
else:
    print("Opcion no valida")
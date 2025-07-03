# Una empresa de energía desea categorizar a sus clientes en tres rangos tarifarios según el
# consumo mensual de kilovatios-hora (kWh): - Menor a 100 kWh → 'Estrato bajo' - Entre 100 y 200 kWh → 'Estrato medio' - Mayor a 200 kWh → 'Estrato alto'
# Desarrolla un algoritmo que reciba el consumo y muestre la categoría correspondiente. 


consumo = int(input("Ingrese consumo mensual de kilovatios-hora (kWh): "))

if consumo > 200:
    print("Estrato alto")
elif consumo >= 100:
    print("Estrato medio")
else:
    print("Estrato bajo")
# Para garantizar la seguridad, una montaña rusa permite el ingreso solo a personas que
# tengan una edad igual o mayor a 12 años y una estatura igual o mayor a 1.40 metros. Crea
# un algoritmo que reciba la edad y estatura de una persona y determine si puede subir o no a
# la atracción. 

edad = int(input("Ingrese la edad: "))
estatura = float(input("Ingrese la estatura: "))

if edad >=12 and estatura >= 1.40:
    print("Puede subir a la atracción.")
else:
    print("No tiene permitido subir a la atracción.")
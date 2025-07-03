# Un proveedor de servicios de Internet desea implementar una herramienta que clasifique el
# servicio que tiene un usuario. Se debe ingresar la velocidad del plan en Mbps y mostrar:
# - 'Muy lenta' si es menor a 10 Mbps - 'Aceptable' si es entre 10 y 30 Mbps - 'Buena' si es entre 31 y 100 Mbps - 'Alta velocidad' si es mayor a 100 Mbps


velocidad = int(input("ingrese la velocidad de su plan (en Mbps): "))

if velocidad > 100:
    print("Alta velocidad")
elif velocidad >= 31:
    print("Buena")
elif velocidad >=10:
    print("Aceptable")
else:
    print("Muy lenta")

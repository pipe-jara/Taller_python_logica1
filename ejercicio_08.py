# Una institución educativa aprueba a un estudiante si cumple dos condiciones: una nota final
# igual o superior a 3.0 y una asistencia igual o superior al 80%. Escribe un algoritmo que
# reciba estos dos datos y determine si el estudiante aprueba o reprueba.

nota = float(input("Ingrese la nota del estudiante: "))
asistencia = int(input("Ingrese porcentaje de asistencias: "))

if nota >= 3.0 and asistencia >= 80:
    print("El estudiante aprueba el curso")
else:
    print("El estudiante reprueba el curso")
# Una campaña de donación requiere filtrar a los posibles donantes. Para ser apto, la persona
# debe tener entre 18 y 65 años y pesar al menos 50 kg. Escribe un algoritmo que reciba la
# edad y el peso de una persona, y determine si está apta o no para donar sangre, mostrando
# un mensaje adecuado.

edad = int(input("Ingrese la edad del donante: "))
peso = int(input("Ingrese el peso del donante (Kg): "))

if (edad >= 18 and edad <= 65) and (peso >= 50):
    print("Persona apta para donar sangre.")
else:
    print("Persona no apta para donar sangre.")
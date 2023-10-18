"""Escribir un programa que lea un año indicado por el usuario.
 El programa debe mostrar un mensaje indicando si es un año bisiesto o no."""

#Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400.
#Ejemplo: 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032

#Solicitar año
año = int(input("Ingrese un año: "))

#Verificar si es bisiesto

if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
    print("El año", año, "es bisiesto")
else:
    print("El año", año, "no es bisiesto")

#Fin del programa
print("Fin del programa")





entero = 1
decimal = 1.1
cadena = "Hola"
booleano = True


#Concatenando todas las variables

print("Entero: " + str(entero) + " Decimal: " + str(decimal) + " Cadena: " + cadena + " Booleano: " + str(booleano))


#El límite de las variables de tipo entero es de 2^31 - 1
#El límite de las variables de tipo decimal es de 2^63 - 1
#El límite de las variables de tipo cadena es de 2^63 - 1
#El límite de las variables de tipo booleano es de 2^63 - 1


#Ejercicio de fórmula de suma de los primeros n números pares

n = 100
suma = (n * (n + 1)) / 2
print("La suma de los primeros " + str(n) + " números pares es: " + str(suma))

# TALLER 02 PYTHON
# AUTOR: Esteban david salas cortina
# FECHA: 31/10/2022

from datetime import date
fecha = date.today()
print("Fecha actual: ",fecha)

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))
var = [num1,num2,num3]

print("El valor maximo es: ",max(var))
print("El valor minimo es: ",min(var))
print("La suma de los 3 numeros es: ",sum(var))
print("-------------------------------------------------------------")

dec = float(input("Ingrese un numero decimal cualquiera: "))
redondo=round(dec)
print("El valor de ",dec, "redondeado es: ",redondo)
print("-------------------------------------------------------------")

frase=input("ingrese una frase: ")
print("La frase en mayuscula es: ",frase.upper())
print("La frase en minisculas es: ",frase.lower())
print("La frase con mayuscula inicial es: ",frase.capitalize())
print("La frase con palabras en mayuscula inicial es: ",frase.title())
print("La longitud de la frase es: ",len(frase),"caracteres")
print("-------------------------------------------------------------")
print("FIN")




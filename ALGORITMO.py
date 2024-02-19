#TALLER 3 PYTHON
#AUTOR: Esteban David salas cortina
#FECHA: 10/11/2022

from datetime import date
fecha = date.today()
print("Fecha actual: ",fecha)

a = int(input("Ingrese el valor de A: "))
b = int(input("Ingrese el valor de B: "))
if a>=b:
    print("A es mayor o igual a B","(",a,">=",b,")")
else:
    print("A es menos que B","(",a,"<",b,")")
print("--------------------------------------------------------------------")

curso1 = "Requerimientos"
curso2 = "Algoritmos"
print("El curso 1 es: ",curso1)
print("El curso 2 es: ",curso2)
if curso1 == "Requerimientos" and curso2=="Algoritmos":
    print("Usted estudia desarrollo de software")
else:
    print("Usted estudia otro programa diferente a desarrollo de software")
print("--------------------------------------------------------------------")
print("***    FINAL DEL ANALISIS DEL PROGRAMA DE FORMACION SENA    ***")
print("--------------------------------------------------------------------")

frase = input("Ingrese una frase: ")
print("La frase en mayuscula es: ",frase.upper())
longitud = len(frase)
print("La longitud de la frase es: ",longitud,"caracteres")
if longitud >10:
    print("La frase contiene mas de 10 caracteres")
else:
    print("La frase contiene menos de 11 caracteres")
print()
print("*** FIN DEL ALGORITMO*** ")
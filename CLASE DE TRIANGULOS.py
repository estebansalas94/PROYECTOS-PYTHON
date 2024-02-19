#TALLER 4 PYTHON
#AUTOR: Esteban David salas cortina
#FECHA: 10/11/2022

from datetime import date
fecha = date.today()
print("Fecha actual: ",fecha)
print("---------------------------------------------")
print("EJERCICIO DE LAS CLASES DE TRIANGULOS")
a = int(input("Ingrese el valor de A: "))
b = int(input("Ingrese el valor de B: "))
c = int(input("Ingrese el valor de C: "))

if a==b and a==c and b==c:
    print("EL TRIANGULO ES EQUILATERO")
else:
    if a==b or b==c or a==c:
        print("EL TRIANGULO ES ISOCELES")
    else:
        print("EL TRIANGULO ES ESCALENO")
print("---------------------------------------------")
animal = input("Ingrese un animal: ")
animal = animal.upper()
if animal == "PERRO":
    print("Este animal es el mejor amigo del hombre: ",animal)
elif animal == "GATO":
    print("Este animal persigue a los ratones: ",animal)
elif animal == "OSO":
    print("Este animal vive en el polonorte: ",animal)
else:
    print("No es perro, no es gato, ni es oso... es: ",animal)
print()
print("FIN")
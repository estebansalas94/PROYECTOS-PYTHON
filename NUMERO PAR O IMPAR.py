#EJERCICIO DE NUMERO PAR O IMPAR
print("Ingrese un numero de 1 a 1000")
num=int(input())

if num>=1 and num<=1000:
    if num % 2==0:
     print("El numero es par")
    elif num % 2==1:
     print("El numero es impar")
else:
  print("Numero fuera de rango establecido.")
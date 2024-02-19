#A un trabajador le descuentan de su salario el 10% si su sueldo es menor o igual a 100000,
# por encima de 100000 y hasta 200000 el 5% del adicional, y por encima de 200000 el 3% del adicional. 
# Calcular el descuento y sueldo neto que recibe el trabajador dado su sueldo.

#DESAROLLO
Sueldo = float(input("ingresar el sueldo: "))

descuento1 = Sueldo * 0.10
Total1 = Sueldo - descuento1

descuento2 = Sueldo * 0.05
Total2 = Sueldo - descuento2

descuento3 = Sueldo * 0.03
Total3 = Sueldo - descuento3

if Sueldo <= 100000:
  print("el descuento es ", descuento1, "el total del sueldo es ", Total1)

elif Sueldo > 100000 and Sueldo == 200000:
  print("el descuento es ", descuento2, "el total del sueldo es ", Total2)

elif Sueldo > 200000:
  print("el descuento es ", descuento3, "el total del sueldo es ", Total3)
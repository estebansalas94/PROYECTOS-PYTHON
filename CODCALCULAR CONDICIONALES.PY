num1 = input("Ingrese primer numero: ")
num2 = input("Ingrese segundo numero: ")
signo = input("Ingrese signo: ")

if len(signo) > 0:
  if num1.isnumeric() and num2.isnumeric():
        int_num1 = int(num1)
        int_num2 = int(num2)
        if signo == "+":
            print(f'La suma de los numeros {num1} y {num2} es igual a {int_num1 + int_num2}')
        elif signo == "-":
            print(f'La resta de los numeros {num1} y {num2} es igual a {int_num1 - int_num2}')
        elif signo == "*":
            print(f'La multiplicación de los numeros {num1} y {num2} es igual a {int_num1 * int_num2}')        
        elif signo == "/":
            print(f'La division de los numeros {num1} y {num2} es igual a {int_num1 / int_num2}')        
        else: 
            print("El signo no es correcto!")
  else: 
        print("Los numeros deben ser valores calculables")    
else:
        print("El signo no puede ser vacio!")

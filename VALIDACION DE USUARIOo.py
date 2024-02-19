#EJERCICIO VALIDACION DE USUARIO
print("""
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
■   BIENVENIDO VALIDA TU USUARIO   ■
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

""")

def funcion1():
 print("ingrese nombre de usuario ")
 usuario=input()
 ncaracteres=len(usuario)
 scaracteres=usuario
 if ncaracteres<6:
    print("El nombre de usuario debe contener al menos 6 caracteres")

 elif ncaracteres>12:
    print("El nombre de usuario no puede contener más de 12 caracteres")

 elif scaracteres==False:
    print("El nombre de usuario debe contener solo letras y números")

 else:
    print("usuario correcto.......")

#EJERCICIO INICIO SESION USUARIO Y CONTRASEÑA
#EJERCICIO VALIDACION DE USUARIO

def funcion1():
 while True:
  print("""
■■■■■■■■■■■■■■■■■■■■■■■■■■
■   INGRESAR USUARIO   ■
■■■■■■■■■■■■■■■■■■■■■■■■■■
""")
  print("ingrese nombre de usuario ")
  usuario=input()
  ncaracteres=len(usuario)
  scaracteres=usuario.isalpha()
  if ncaracteres<6:
    print("⊗ El nombre de usuario debe contener al menos 6 caracteres")

  elif ncaracteres>12:
    print("⊗ El nombre de usuario no puede contener más de 12 caracteres")

  elif scaracteres==False:
    print("⊗ El nombre de usuario debe contener solo letras")

  else:
    break
    
#CREADOR DE DICCIONARIO DE COLORES ESPAÑOL A INGLES

diccionario = {"amarillo":"yellow","azul":"blue","rojo":"red"}

def mostrardic():
   for d in diccionario:
    print(d, "=", diccionario[d])
   print("--------------------------------------------------------------------------------------------------------")

 
def agregar():
   n=int(input("ingrese cuantas palabras(colores) va a registrar en el diccionario: "))
   cont=0
   while(cont<n):
    clav=input("ingrese palabra(color) en español: ")
    clave=clav.lower()
    val=input("ingrese significado en ingles: ")
    valor=val.lower()
    diccionario[clave]=valor
    print("agregado exitoso")
    cont=cont+1
   print("-------------------------------------------------------------------------------------------------------")
   

def eliminar():
  elimin=input("ingrese el dato que quiere eliminar: ")
  eliminar=elimin.lower()
  del diccionario[eliminar]
  print("eliminado exitoso")
  print("--------------------------------------------------------------------------------------------------------")


def modificar():
  varr=input("ingrese el color que quiere modificar su valor: ")
  var=varr.lower()
  valorneww=input("ingrese el nuevo valor: ")
  valornew=valorneww.lower()
  for key, d in diccionario.items():
    if key == var:
        diccionario[key] = valornew
  print("modificado exitoso")
  print("--------------------------------------------------------------------------------------------------------")


def buscar():
  opcionn=input("ingrese el color que quiere buscar: ")
  if (opcion := opcionn.lower())==opcion:
    print(opcion, "=",diccionario[opcion])
  print("--------------------------------------------------------------------------------------------------------")
  

def salir():
  print(quit) 
  quit()
  print("ha salido")
   
  
  
def menu():
 while(True):
  print("DICCIONARIO DE COLORES ESPAÑOL A INGLES")

  if (opcion := int(input("elija la accion a realizar \n1)agregar datos al diccionario \n2)mostrar diccionario \n3)buscar por palabra(color) \n4)eliminar datos del diccionario \n5)modificar valores del diccionario \n6)salir del diccionario \n:")))==1:
   agregar()

  if opcion==2:
   mostrardic()

  if opcion == 3:
    buscar()

  if opcion == 4:
    eliminar()

  if opcion == 5:
    modificar()

  if opcion==6:
     salir()


 

while(True):
  menu()
  menu()
 

  break

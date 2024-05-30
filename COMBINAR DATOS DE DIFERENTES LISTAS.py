from random import random
import secrets

animales = ["Gato","Leon","Tigre","Tiburon","Perro"]
cosas = ["Carro","Casa","Moto","Jarra","Telefono"]
lista = []



def agregaranimales():
    nuevoanimal = input("Ingrese un nuevo animal: ")
    nanimal = nuevoanimal.lower()
    animales.append(nanimal)
    print("Animal agregado exitosamente.")
    repetir = int(input("1)Agregar mas \n2)volver al menu \n: "))
    if repetir == 1:
        agregaranimales()
    if repetir == 2:
        menujuego()

def agregarcosas():
    #while(True):
        nuevacosa = input("Ingrese una nueva cosa: ")
        ncosa = nuevacosa.lower()
        cosas.append(ncosa)
        print("Cosa agregada exitosamente.")
        repetir = int(input("1)Agregar mas \n2)Volver al menu \n: "))
        if repetir == 1:
            agregarcosas()
        if repetir == 2:
            menujuego()
    
def descubrir_palabras():
     cantidad_animales = int(input("Cuantos datos de la lista de animales quiere agregar a la nueva lista: "))
     cantidad_cosas = int(input("Cuantos datos de la lista de cosas quiere agregar a la nueva lista: "))
     cantidad_elegir = cantidad_animales + cantidad_cosas
  

     while len(lista) != cantidad_elegir:
         if (secrets.SystemRandom().randint(0,100) % 2 == 0) and cantidad_animales != 0:
             animal_elegido = secrets.choice(animales)
             if animal_elegido not in lista:
                 lista.append(animal_elegido)
                 cantidad_animales -= 1
         elif (cantidad_cosas != 0):
             cosa_elegida = secrets.choice(cosas)
             if cosa_elegida not in lista:
                 lista.append(cosa_elegida)
                 cantidad_cosas -= 1

     for i in range (len(lista)):
         lista[i] = lista[i].lower()
     print (lista)
     palabra_oculta = secrets.choice(lista)
     print(palabra_oculta)
     intentos1 = 3
     intentos = 2
     while (intentos>-1):
          print("ingrese la palabra que usted crea que es, solo tendra",intentos1,"intentos: ")
          palabra_elegida = input()
          palabra_elegidan = palabra_elegida.lower()
          if palabra_oculta == palabra_elegidan:
              print("Felicitaciones has adivinado la palabra oculta ",palabra_oculta)
              juegonuevo = int(input("1) Jugar de nuevo \n2) Ir al menu \n3) Salir del juego \n: "))
              if juegonuevo == 1:
                  descubrir_palabras()
              if juegonuevo == 2:
                  menujuego()
              if juegonuevo == 3:
                  exit()
          else:
              if intentos >0:
                 print("Siga intentando le quedan ",intentos," intentos")
            
          
                  
                     
          intentos -= 1
          intentos1 -= 1
     if intentos1==0:
         print("HAS PERDIDO")
         juegonuevo = int(input("1) Jugar de nuevo \n2) Ir al menu \n3) Salir del juego \n: "))
         if juegonuevo == 1:
            descubrir_palabras()
         if juegonuevo == 2:
            menujuego()
         if juegonuevo == 3:
            exit()
         
    
     
#MENU DEL JUEGO:
def menujuego():
    while(True):
     menu = int(input("""INSTRUCCIONES:
                 
                 Este juego consta de descubrir la palabra oculta que se encuentran en una lista de palabras,
                 dada dos listas una de animales y otra de cosas, usted tendra como ventaja elejir cuantas
                 palabras sobre animales y cosas quiere que aparezcan en la lista de palabras donde usted descubrira
                 la palabra oculta.
                  
                 BIENVENIDO AL MENU DEL JUEGO:
                 \n1) Registrar nuevos animales 
                 \n2) Registrar nuevas cosas 
                 \n3) Descubrir la palabra oculta 
                 \n4) Salir 
                 \n:"""))
     if menu == 1:
         agregaranimales()
     elif menu == 2:
         agregarcosas()
     elif menu == 3:
         descubrir_palabras()
     elif menu == 4:
         exit()
    
#INICIA EL JUEGO:
menujuego()
    
            
            
            
            
            
            
            
            
            
            
            
            
            
            

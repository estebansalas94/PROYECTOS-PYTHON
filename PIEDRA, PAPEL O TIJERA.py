#JUEGO PIEDRA, PAPEL O TIJERA

import secrets

piedra = 1
papel = 2
tijera = 3
print("usuario escoja una opcion: \n1)piedra, \n2)papel , \n3)tijera: ")
usuario= int(input("usuario ingrese la opcion en numero: "))


maquina = secrets.SystemRandom().randint(1,3)
print("opcion de maquina: ",maquina)
if (maquina==1) and (usuario==3):
    print("su eleccion: tijera \neleccion de la maquina: piedra")
    print("ganador es maquina")
elif(maquina==1) and (usuario==2):
    print("su eleccion: papel \neleccion de la maquina: piedra")
    print("gana usted")
elif (maquina==1) and (usuario==1):
    print("su eleccion: piedra \neleccion de la maquina: piedra")
    print("empate")
else: 
     if(maquina==2) and (usuario==3):
          print("su eleccion: tijera \neleccion de la maquina: papel")
          print("gana usted")
     elif (maquina==2) and (usuario==2):
          print("su eleccion: papel \neleccion de la maquina: papel")
          print("empate")
     elif (maquina==2) and (usuario==1):
          print("su eleccion: piedra \neleccion de la maquina: papel")
          print("gana maquina")
     else:
          if (maquina==3) and (usuario==3):
             print("su eleccion: tijera \neleccion de la maquina: tijera")
             print("empate")     
          elif (maquina==3) and (usuario==2):
             print("su eleccion: papel\neleccion de la maquina: tijera ")
             print("gana maquina")
          elif (maquina==3) and (usuario==1):
             print("su eleccion: piedra \neleccion de la maquina: tijera")
             print("gana usted")

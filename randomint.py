import random 

numeromaquina = random.randint(1,5)
while(True):
    if (num := int(input("ingrese un numero de 1 a 5: ")))==numeromaquina:
        print("ha encontrado el numero de la maquina que es ",numeromaquina)
        break
    else:
        print("Siga intentando")
    
    

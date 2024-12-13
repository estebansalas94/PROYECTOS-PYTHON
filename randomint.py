import secrets

numeromaquina = secrets.SystemRandom().randint(1,5)
while(True):
    num = int(input("ingrese un numero de 1 a 5: "))
    if num==numeromaquina:
        print("ha encontrado el numero de la maquina que es ",numeromaquina)
        break
    else:
        print("Siga intentando")
    
    

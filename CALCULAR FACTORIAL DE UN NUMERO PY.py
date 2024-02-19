numero=int(input("Ingrese un numero: "))
factorial=1
cont=1
while(cont<=numero):
  factorial=factorial*cont
  cont=cont+1

print("El factorial del numero",numero,"es",factorial)

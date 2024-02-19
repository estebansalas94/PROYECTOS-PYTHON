from re import X
tablero=[]
cont=0


def ha_ganadx():
	if (tablero [0][0] == "x"  and tablero [0][1]=="x" and tablero[0][2]=="x"or
     tablero [1][0] == "x" and tablero [1][1]=="x" and tablero[1][2]=="x"or
     tablero [2][0] == "x" and tablero [2][1]=="x" and tablero[2][2]=="x"or
     tablero [0][1] == "x" and tablero [1][1]=="x" and tablero[1][1]=="x"or
     tablero [0][0] == "x" and tablero [1][0]=="x" and tablero[2][0]=="x"or
     tablero [0][2] == "x" and tablero [1][2]=="x" and tablero[2][2]=="x"or
     tablero [0][0] == "x" and tablero [1][1]=="x" and tablero[2][2]=="x"or
     tablero [0][2] == "x" and tablero [1][1]=="x" and tablero[2][0]=="x"or
     tablero [2][2] == "x" and tablero [1][1]=="x" and tablero[0][0]=="x"):
             print("equis(x) a ganado" )
            
def ha_ganado():
   if (tablero [0][0] == "o"  and tablero [0][1]=="o" and tablero[0][2]=="o"or
     tablero [1][0] == "o" and tablero [1][1]=="o" and tablero[1][2]=="o"or
     tablero [2][0] == "o" and tablero [2][1]=="o" and tablero[2][2]=="o"or
     tablero [0][1] == "o" and tablero [1][1]=="o" and tablero[1][1]=="o"or
     tablero [0][0] == "o" and tablero [1][0]=="o" and tablero[2][0]=="o"or
     tablero [0][2] == "o" and tablero [1][2]=="o" and tablero[2][2]=="o"or
     tablero [0][0] == "o" and tablero [1][1]=="o" and tablero[2][2]=="o"or
     tablero [0][2] == "o" and tablero [1][1]=="o" and tablero[2][0]=="o"or
     tablero [2][2] == "o" and tablero [1][1]=="o" and tablero[0][0]=="o"):
             print("circulo(o) a ganado " )
        
             
def ha_empatado():
  if (tablero [0][0] == "o"  and tablero [0][1]=="x" and tablero[0][2]=="o"or
     tablero [1][0] == "x" and tablero [1][1]=="o" and tablero[1][2]=="o"or
     tablero [2][0] == "o" and tablero [2][1]=="x" and tablero[2][2]=="o"or
     tablero [0][1] == "o" and tablero [1][1]=="x" and tablero[1][1]=="o"or
     tablero [0][0] == "x" and tablero [1][0]=="o" and tablero[2][0]=="o"or
     tablero [0][2] == "o" and tablero [1][2]=="x" and tablero[2][2]=="o"or
     tablero [0][0] == "x" and tablero [1][1]=="x" and tablero[2][2]=="o"or
     tablero [0][2] == "o" and tablero [1][1]=="x" and tablero[2][0]=="o"or
     tablero [2][2] == "x" and tablero [1][1]=="o" and tablero[0][0]=="o"):
             print("han empatado" )

def nuevo_tablero():
   tablero=[["-","-","-"],["-","-","-"],["-","-","-"]]
   return tablero

def mostrar_tablero():
   for t in range (0,3):
      for h in range(0,3):
        print(tablero[t][h],end="    ") 
       
      print("\n")   

def registrar_jugada():
   while(True): 
     caracter=input("ingrese CIRCULO(O) o EQUIS(X) Para jugar: ")
     
     fila=int(input("ingrese fila: "))
     columna=int(input("ingrese columna: "))

    
     
     if (tablero[fila][columna]=="-"):
         tablero[fila][columna]=caracter
         break
     else:
         print("ya esta ocupado este lugar ")
    

tablero=nuevo_tablero()
mostrar_tablero()
while(cont<=9):
  registrar_jugada()
  mostrar_tablero()
  ha_ganado()
  ha_ganadx()
  ha_empatado()
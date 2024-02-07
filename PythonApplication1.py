import pyodbc

from email import message
from tkinter import messagebox, ttk

import tkinter as tk
from tkinter import*
from cProfile import label

direccion_servidor = 'CNGAPRCIPFSD068\SQLEXPRESS01'
nombre_bd = 'prueba1'
nombre_usuario = 'python1'
password = '123'
try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              direccion_servidor + ';DATABASE=' + nombre_bd + ';UID=' + nombre_usuario + ';PWD=' + password)
    print("conexion exitosa")

except Exception as e:
    
    print("error de conexion ", e)


#--------------------------------------------------------------------------------------------------

def funcion():
    otra_ventana = tk.Toplevel(ventana1)
    otra_ventana.title("Consultar personas")


    v=Frame(otra_ventana)
    v.pack(side="left",expand="true")
    v.config(width="1050",height="630")
    v.config(bg="paleturquoise")
    v.config(relief="groove")
    v.config(bd=5)
    v.config(cursor="arrow")
    text1=tk.Label(v,text="CONSULTA DE PERSONAL",bg="paleturquoise",fg="black",font=("Showcard Gothic",19)).place(x=30,y=20)
    text=tk.Label(v,text="Número de identificacion:",bg="paleturquoise",fg="black",font=("Times New Roman",16)).place(x=300,y=120)
    boton=tk.Button(v,text="BUSCAR",bg="teal",fg="white",font=("Microsoft YaHei",12))
    boton.place(x=780,y=120)
    boton.config(cursor= "circle")
    cuadrotext1=Entry(v)
    cuadrotext1.place(x=600,y=126)
    mostrar=Listbox(v)
    mostrar.place(relx=0.07,rely=0.3,relwidth=0.3,relheight=0.5)
    boton3=Button(v,command=dialogo)
    boton3.place(x=580,y=500)
    boton3.config(text="ELIMINAR",bg="teal",fg="white",font=("Microsoft YaHei",12))
    boton3.config(cursor="circle")
   
#-------------------

def dialogo():
  
       print(messagebox.askquestion(message="¿Desea Eliminar Datos?", title="GESTION DE PERSONAS"))
   



#----------------------------------------------------------------------------------------------------- ------------    -----------------------------------------







ventana1=tk.Tk()
ventana1.title("Gestion de personas",)

v1=Frame()
v1.pack(side="left",expand="true")
v1.config(width="1050",height="630")
v1.config(bg="paleturquoise")
v1.config(relief="groove")
v1.config(bd=5)
v1.config(cursor="arrow")
text1=Label(v1,text="GESTION DE PERSONAS",bg="paleturquoise",fg="black",font=("Showcard Gothic",19)).place(x=30,y=20)
text=Label(v1,text="Número de identificacion:",bg="paleturquoise",fg="black",font=("Times New Roman",16)).place(x=300,y=120)
text=Label(v1,text="Nombre de la persona:",bg="paleturquoise",fg="black",font=("Times New Roman",16)).place(x=300,y=200)
text=Label(v1,text="Correo electronico:",bg="paleturquoise",fg="black",font=("Times New Roman",16)).place(x=300,y=280)
text=Label(v1,text="Número de telefono:",bg="paleturquoise",fg="black",font=("Times New Roman",16)).place(x=300,y=360)

cuadrotext1=Entry(v1)
cuadrotext1.place(x=600,y=126)
cuadrotext1.config(width="30")
cuadrotext2=Entry(v1)
cuadrotext2.place(x=600,y=206)
cuadrotext2.config(width="30")
cuadrotext3=Entry(v1)
cuadrotext3.place(x=600,y=286)
cuadrotext3.config(width="30")
cuadrotext4=Entry(v1)
cuadrotext4.place(x=600,y=366)
cuadrotext4.config(width="30")

boton1=Button(v1)
boton1.place(x=260,y=500)
boton1.config(text="REGISTRAR",bg="teal",fg="white",font=("Microsoft YaHei",12))
boton1.config(cursor="circle")

boton2=Button(v1)
boton2.place(x=460,y=500)
boton2.config(text="ACTUALIZAR",bg="teal",fg="white",font=("Microsoft YaHei",12))
boton2.config(cursor="circle")




boton4=tk.Button(v1,command=funcion)
boton4.place(x=680,y=500)
boton4.config(text="CONSULTAR",bg="teal",fg="white",font=("Microsoft YaHei",12))
boton4.config(cursor= "circle")





ventana1.mainloop()




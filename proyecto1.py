from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image 
import tkinter as tk
from tkinter.filedialog import askopenfilename

ventana=Tk()

def cargar():
    
    direccion=askopenfilename()
    archivo=open(direccion,'r')
    cadena=archivo.read()
    archivo.close()
    pass

anchoventana=int(920)
largoventana=int(650)
x_ventana =(int( ventana.winfo_screenwidth()/2))-(int(anchoventana/2))
y_ventana = int((ventana.winfo_screenheight() -100 )/2)-(int(largoventana/2))
posicion = str(anchoventana) + "x" + str(largoventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
ventana.geometry(posicion)
ventana.title("INICIO")


#FRAMES ---------------
mframe=Frame(ventana,width=300 ,height=60)
mframe.config(bg="#ABB2B9")
mframe.place(x=20,y=15)

mframe2=Frame(ventana,width=200 ,height=500)
mframe2.config(bg="red")
mframe2.place(x=20,y=90)

imgframe1=Frame(ventana,width=650 ,height=500)
imgframe1.config(bg="red")
imgframe1.place(x=240,y=90)


#BOTONES  ---------------


boton1=Button(mframe,text="CARGAR",command=cargar)
boton1.place(x=10,y=10,width=60,height=30)

boton2=Button(mframe,text="ANALIZAR")
boton2.place(x=80,y=10,width=65,height=30)

boton2=Button(mframe,text="REPORTES")
boton2.place(x=155,y=10,width=65,height=30)


bimagen1=Button(mframe2,text="Original")
bimagen1.place(x=45,y=50,width=100,height=40)

bimagen1=Button(mframe2,text="MIRROR  X ")
bimagen1.place(x=45,y=110,width=100,height=40)

bimagen1=Button(mframe2,text="MIRROR Y ")
bimagen1.place(x=45,y=170,width=100,height=40)

bimagen1=Button(mframe2,text="DOBLE MIRROR ")
bimagen1.place(x=45,y=230,width=100,height=40)

















ventana.mainloop()

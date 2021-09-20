from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image 
import tkinter as tk
from tkinter.filedialog import askopenfilename

ventana=Tk()

lcoordenadas=[]
filas=0
columnas=0

def cargar():
    global filas
    global columnas
    direccion=askopenfilename()
    archivo=open(direccion,'r')
    cadena=archivo.read()
    archivo.close()
    cadena2=cadena.split(";")
    filass=cadena2[3]
    columnass=cadena2[4]

    filas=filass
    columnas=columnass
    celdas=cadena2[5]
    celdas=celdas.replace(" ","")
    celdas=celdas.replace("CELDAS={","")
    celdas=celdas.replace("}","")
    celdas=celdas.strip()
    celdas=celdas.replace("[","")
    celdas=celdas.replace("],","")
    coordenadas=celdas.split("\n")
    for i in range(len(coordenadas)-1):
        coordenadas[i]=coordenadas[i].strip("\t")
        partes=coordenadas[i].split(",")
        lcoordenadas.append(partes)
       
    
    print(lcoordenadas[2])

def graficar():
    agrafica=open("Grafica.dot","w")
    agrafica.write("digraph G {\n")
    gtitulo='''digraph structs {
	node [shape=plaintext]
	struct3 [label=<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="7">
    '''

    agrafica.write(gtitulo+'\n')

    for f in range(filas-1):
        agrafica.write('<TR>\n')
        for c in range(columnas-1):

            pass
        agrafica.write('</TR>\n')

    agrafica.close()

    


 


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

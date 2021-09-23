from Analizador import Analizador
from tkinter import *
from tkinter import ttk
from typing import Counter
from PIL import ImageTk, Image 
import tkinter as tk
from tkinter.filedialog import askopenfilename
from Analizador import Analizador


ventana=Tk()

lcoordenadas=[]
filas=0
columnas=0

documento=""

def cargar():
    global filas
    global columnas
    direccion=askopenfilename()
    archivo=open(direccion,'r')
    cadena=archivo.read()
    archivo.close()
    cadena2=cadena.split(";")
    filass=cadena2[3]
    filass=filass.replace(" ","")
    filass=filass.replace("FILAS=","")
    columnass=cadena2[4]
    columnass=columnass.replace(" ","")
    columnass=columnass.replace("COLUMNAS=","")

    filas=int(filass)
    columnas=int(columnass)
  
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
       
    
#def cargar2():
#    global documento
#    base=[]
#    contador0=0
#    contador=0
#    direccion=askopenfilename()
#    documento=""
#    with open(direccion) as f:
#        for l in f :
#            contador0=contador0+1
#
#    with open(direccion) as f:
#        for line in f:
#            contador=contador+1
#            line=line.replace(" ","")
#            documento=documento+line
#            print(line.match("@@@@"))         
#    print(base)

def leerArchivo(ruta):
    archivo = open(ruta, 'r')
    contenido = archivo.read()
    archivo.close()
    return contenido

def cargar2():
    direccion=askopenfilename()
    codigo=leerArchivo(direccion)
    scanner = Analizador()
    scanner.analizar(codigo)
    scanner.imprimirToken()
    


            
  

def graficar():
    agrafica=open("Grafica.dot","w")
    gtitulo='''digraph structs {
	node [shape=plaintext]
	struct3 [label=<<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0" CELLPADDING="50">
    '''

    agrafica.write(gtitulo+'\n')

    for f in range(filas):
        agrafica.write('<TR>\n')
        for c in range(columnas):
            codigo="<TD></TD> \n"
            for i in lcoordenadas:
                if int(i[0])==f and int(i[1])==c and i[2]=="TRUE":
                    codigo='<TD bgcolor="' + str(i[3]) + '"></TD> \n'
       

            agrafica.write(codigo)
              
        agrafica.write('</TR>\n')
        
    agrafica.write('</TABLE>>]}')
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


boton1=Button(mframe,text="CARGAR",command=cargar2)
boton1.place(x=10,y=10,width=60,height=30)

boton2=Button(mframe,text="ANALIZAR",command=graficar)
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

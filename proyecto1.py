from Analizador import Analizador
from tkinter import *
from tkinter import ttk
from typing import Counter
from PIL import ImageTk, Image 
import tkinter as tk
from tkinter.filedialog import askopenfilename
from Analizador import Analizador
import os
from PIL import Image,ImageTk


ventana=Tk()


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
    scanner.datos()
    imagenes=scanner.datos()
    n=0
    for i in imagenes:
            n=n+1
            nombre="Grafica"+str(n)+".dot"
            nombre2="Grafica"+str(n)
            print(i.titulo)
            agrafica=open(nombre,"w")
            gtitulo='''digraph structs {
	        node [shape=plaintext]
	        struct3 [label=<<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0" CELLPADDING="50">
            '''
            agrafica.write(gtitulo+'\n')
            for f in range(int(i.fila)):
                agrafica.write('<TR>\n')
                for c in range(int(i.columna)):
                    codigo="<TD></TD> \n"
                    for j in i.celda:
                        if int(j.x)==f and int(j.y)==c and j.paso=="TRUE":
                            codigo='<TD bgcolor="' + str(j.color) + '"></TD> \n'
                    agrafica.write(codigo)
                agrafica.write('</TR>\n')
            agrafica.write('</TABLE>>]}')
            agrafica.close()
            #_____________________________Crear imagenes____________________________________________
            nombre2=nombre2+".jpg"
            os.system('dot -Tjpg '+ nombre +' -o '+ nombre2) 
            try:
                pass
                 #os.startfile(nombre2)

            except Exception:
                print ("no se encontro")
                


            
  

def graficar():
    filas=1
    columnas=1
    lcoordenadas=[]
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
ventana.resizable(False,False)


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

#canva ---------------


can=Canvas(imgframe1,bd=2,relief=RIDGE,bg="white",scrollregion=(0,0,1000,1000))
can.place(x=0,y=0,width=650,height=500)

yscrol=Scrollbar(can,orient=VERTICAL)
yscrol.pack(side=RIGHT,fill=Y)
yscrol.config(command=can.yview)
can.config(yscrollcommand=yscrol.set)

img=Image.open('Grafica1.jpg')
img=img.resize((400,400),Image.ANTIALIAS)


img=ImageTk.PhotoImage(img)

image=can.create_image((105,50),anchor=NW,image=img)

img2=Image.open('Grafica2.jpg')
img2=img2.resize((400,400),Image.ANTIALIAS)


img2=ImageTk.PhotoImage(img2)

imag2e=can.create_image((105,500),anchor=NW,image=img2)


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

from Analizador import Analizador
from tkinter import *
from tkinter import ttk
from typing import Counter, final
from PIL import ImageTk, Image 
import tkinter as tk
from tkinter.filedialog import askopenfilename
from Analizador import Analizador
import os
from PIL import Image,ImageTk
from tkinter import messagebox
from PP import PP1



ventana=Tk()
imagenes=[]
llave=""
llave2=0
listaErrores=[]
listaTokens=[]
combo=ttk.Combobox()

def leerArchivo(ruta):
    archivo = open(ruta, 'r')
    contenido = archivo.read()
    archivo.close()
    return contenido

def cargar2():
    global imagenes
    direccion=askopenfilename()
    codigo=leerArchivo(direccion)
    scanner = Analizador()
    scanner.analizar(codigo)
    ass=scanner.imprimirToken()

    listaTokens=scanner.Tokenss()
  
    imagenes=scanner.datos()
    
    
def analizar():
    
    n=0
    for i in imagenes:
        temp=i.titulo +""
        titulo1=temp.replace('"','')
        n=n+1
        nombre= titulo1 +".dot"
        nombre2=titulo1
     
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
                    if (int(j.x))==f and int(j.y)==c and j.paso=="TRUE":
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
       
        
        for k in i.filtro:
            if k=="MIRRORX":
                agrafica=open(titulo1 +"x.dot","w")
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
                            if (int(j.x))==f and (int(i.columna) -1 )-int(j.y)==c and j.paso=="TRUE":
                                codigo='<TD bgcolor="' + str(j.color) + '"></TD> \n'
                        agrafica.write(codigo)
                    agrafica.write('</TR>\n')
                agrafica.write('</TABLE>>]}')
                agrafica.close()
                #_____________________________Crear imagenes____________________________________________
                nombre2=nombre2+".jpg"
                os.system('dot -Tjpg '+ titulo1 +"x.dot" +' -o '+ titulo1+"x.jpg") 
                try:
                    pass
                     #os.startfile(nombre2)
                except Exception:
                    print ("no se encontro")
            
            elif k=="MIRRORY":
                agrafica=open(titulo1+"y.dot","w")
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
                            if (int(i.fila) -1 )-(int(j.x))==f and int(j.y)==c and j.paso=="TRUE":
                                codigo='<TD bgcolor="' + str(j.color) + '"></TD> \n'
                        agrafica.write(codigo)
                    agrafica.write('</TR>\n')
                agrafica.write('</TABLE>>]}')
                agrafica.close()
                #_____________________________Crear imagenes____________________________________________
                nombre2=nombre2+".jpg"
                os.system('dot -Tjpg '+ titulo1 +"y.dot" +' -o '+ titulo1 +"y.jpg") 
                try:
                    pass
                     #os.startfile(nombre2)
                except Exception:
                    print ("no se encontro")
            
            elif k=="DOUBLEMIRROR":
                agrafica=open(titulo1 +"d.dot","w")
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
                            if (int(i.fila) -1 )-(int(j.x))==f and (int(i.columna) -1 )-int(j.y)==c and j.paso=="TRUE":
                                codigo='<TD bgcolor="' + str(j.color) + '"></TD> \n'
                        agrafica.write(codigo)
                    agrafica.write('</TR>\n')
                agrafica.write('</TABLE>>]}')
                agrafica.close()
                #_____________________________Crear imagenes____________________________________________
                nombre2=nombre2+".jpg"
                os.system('dot -Tjpg '+ titulo1+"d.dot" +' -o '+ titulo1+"d.jpg") 
                try:
                    pass
                     #os.startfile(nombre2)
                except Exception:
                    print ("no se encontro")

    baceptar.config(state="normal")  
    listaimagen=[]
    for i in imagenes:
        listaimagen.append(i.titulo)
    
    combo["values"]=listaimagen
    

def mostrar():
    n=0
    for i in imagenes:
        n=n+1
        temp=i.titulo + ""
        titulo=temp.replace('"','')
        if i.titulo==combo.get():
            imgframe1=Frame(ventana,width=650 ,height=500)
            imgframe1.config(bg="red")
            imgframe1.place(x=240,y=90)

            imag = Image.open(titulo +".jpg")
            imag1 = ImageTk.PhotoImage(imag.resize((550,500)))

            pintarl = tk.Label(imgframe1, image=imag1)
            pintarl.imag1=imag1

            pintarl.place(x=0, y=0,width=650,height=500)
            


def mirox():
    n=0
    op=0
    titulo=""
    for i in imagenes:
        
        if i.titulo==combo.get():
            for j in i.filtro:
                if j=='MIRRORX':
                    op=1
                    titulo=i.titulo+""
                    break
                else:
                    op=0
    if op==1:
        titulo2=titulo.replace('"','')
        imgframe1=Frame(ventana,width=650 ,height=500)
        imgframe1.config(bg="red")
        imgframe1.place(x=240,y=90)
        imag = Image.open(titulo2 +"x.jpg")
        imag1 = ImageTk.PhotoImage(imag.resize((550,500)))
        pintarl = tk.Label(imgframe1, image=imag1)
        pintarl.imag1=imag1
        pintarl.place(x=0, y=0,width=650,height=500)

    else:
        messagebox.showinfo("Error","Esta imagen no cuenta con este filtro")

def miroy():
    op=0
    titulo=""
    for i in imagenes:
        
        if i.titulo==combo.get():
            for j in i.filtro:
                if j=='MIRRORY':
                    op=1
                    titulo=i.titulo+""
                    break
                else:
                    op=0
    if op==1:
        titulo2=titulo.replace('"','')
        imgframe1=Frame(ventana,width=650 ,height=500)
        imgframe1.config(bg="red")
        imgframe1.place(x=240,y=90)
        imag = Image.open(titulo2 +"y.jpg")
        imag1 = ImageTk.PhotoImage(imag.resize((550,500)))
        pintarl = tk.Label(imgframe1, image=imag1)
        pintarl.imag1=imag1
        pintarl.place(x=0, y=0,width=650,height=500)
        

    else:
        messagebox.showinfo("Error","Esta imagen no cuenta con este filtro")


def mirod():
    op=0
    titulo=""
    for i in imagenes:
        
        if i.titulo==combo.get():
            for j in i.filtro:
                if j=='DOUBLEMIRROR':
                    op=1
                    titulo=i.titulo+""
                    break
                else:
                    op=0
    if op==1:
        titulo2=titulo.replace('"','')
        imgframe1=Frame(ventana,width=650 ,height=500)
        imgframe1.config(bg="red")
        imgframe1.place(x=240,y=90)
        imag = Image.open(titulo2 +"d.jpg")
        imag1 = ImageTk.PhotoImage(imag.resize((550,500)))
        pintarl = tk.Label(imgframe1, image=imag1)
        pintarl.imag1=imag1
        pintarl.place(x=0, y=0,width=650,height=500)
        

    else:
        messagebox.showinfo("Error","Esta imagen no cuenta con este filtro")

def miroo():
    n=0
    for i in imagenes:
        n=n+1
        temp=i.titulo + ""
        titulo=temp.replace('"','')
        if i.titulo==combo.get():
            imgframe1=Frame(ventana,width=650 ,height=500)
            imgframe1.config(bg="red")
            imgframe1.place(x=240,y=90)

            imag = Image.open(titulo +".jpg")
            imag1 = ImageTk.PhotoImage(imag.resize((550,500)))

            pintarl = tk.Label(imgframe1, image=imag1)
            pintarl.imag1=imag1

            pintarl.place(x=0, y=0,width=650,height=500)

def reporte():
    inicio=PP1.primera
    final1=PP1.segunda

    titulo1=PP1.titulop1
    titulo2=PP1.titulop2
    titulo3=PP1.titulop3
    cadenaImagen=""
    tituloImagen=""

    for i in imagenes:
        temp=i.titulo+""
        tituloImagen=temp.replace('"','')
        cadenaImagen=cadenaImagen + titulo1+tituloImagen+titulo2 + ' <img src=" '+ tituloImagen+'.jpg" width=" '+str(i.ancho)+'" height=" '+str(i.alto)+'"'+titulo3

        for l in i.filtro:
            if l=="MIRRORX":
                cadenaImagen=cadenaImagen + titulo1+tituloImagen +  "  Filtro X" +titulo2 + ' <img src=" '+ tituloImagen+'x.jpg" width=" '+str(i.ancho)+'" height=" '+str(i.alto)+'"'+titulo3
            
            elif l=="MIRRORY":
                cadenaImagen=cadenaImagen + titulo1+tituloImagen +  "  Filtro Y" +titulo2 + ' <img src=" '+ tituloImagen+'y.jpg" width=" '+str(i.ancho)+'" height=" '+str(i.alto)+'"'+titulo3

            elif l=="DOUBLEMIRROR":
                cadenaImagen=cadenaImagen + titulo1+tituloImagen +  "  Filtro DOUBLEMIRROR " +titulo2 + ' <img src=" '+ tituloImagen+'d.jpg" width=" '+str(i.ancho)+'" height=" '+str(i.alto)+'"'+titulo3


   
   
    tabla1=PP1.titulotabla1
    tabla12=PP1.titulotabla122
    tabla2=PP1.titultabla2
    tablax="."

    archivo = open("tokens.txt", 'r')
    contenido = archivo.read()
    archivo.close()

    archivo2 = open("error.txt", 'r')
    contenido2 = archivo2.read()
    archivo2.close()
   

    
    pagina=open("inicio2.html","w")
    pagina.write(inicio + cadenaImagen +tabla1+contenido+tabla2 + tabla12 +contenido2+tabla2 +final1)


    pagina.close()
    try:
        os.startfile("inicio2.html")
    except Exception:
        print ("no se encontro")







anchoventana=int(920)
largoventana=int(650)
x_ventana =(int( ventana.winfo_screenwidth()/2))-(int(anchoventana/2))
y_ventana = int((ventana.winfo_screenheight() -100 )/2)-(int(largoventana/2))
posicion = str(anchoventana) + "x" + str(largoventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
ventana.geometry(posicion)
ventana.title("INICIO")
ventana.resizable(False,False)


#FRAMES ---------------
mframe=Frame(ventana,width=350 ,height=60)
mframe.config(bg="#ABB2B9")
mframe.place(x=20,y=15)

mframe2=Frame(ventana,width=200 ,height=500)
mframe2.config(bg="red")
mframe2.place(x=20,y=90)





#BOTONES  ---------------

boton1=Button(mframe,text="CARGAR",command=cargar2)
boton1.place(x=10,y=10,width=60,height=30)

boton2=Button(mframe,text="ANALIZAR",command=analizar)
boton2.place(x=80,y=10,width=65,height=30)

boton2=Button(mframe,text="REPORTES",command=reporte)
boton2.place(x=155,y=10,width=65,height=30)

boton2=Button(mframe,text="SALIR",command=reporte)
boton2.place(x=240,y=10,width=65,height=30)


bimagen1=Button(mframe2,text="Original",command=miroo)
bimagen1.place(x=45,y=50,width=100,height=40)

bimagen1=Button(mframe2,text="MIRROR  X ",command=mirox)
bimagen1.place(x=45,y=110,width=100,height=40)

bimagen1=Button(mframe2,text="MIRROR Y ",command=miroy)
bimagen1.place(x=45,y=170,width=100,height=40)

bimagen1=Button(mframe2,text="DOBLE MIRROR ",command=mirod)
bimagen1.place(x=45,y=230,width=100,height=40)

#combobox---------------
combo=ttk.Combobox(ventana)
combo.place(x=500,y=25)




baceptar=Button(ventana,text="Siguiente",command=mostrar)
baceptar.place(x=670,y=20,width=100,height=40)
baceptar.config(state="disabled")






















ventana.mainloop()

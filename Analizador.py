from Token import Token
from Error import Error
import re
from Imagen import Imagen
from Matriz import Matriz

class Analizador:
    def __init__(self):
        self.listaTokens=[]
        self.listaErrores=[]

    def analizar(self,codigo_fuente):
        self.listaTokens=[]
        self.listaErrores=[]

        linea=1
        columna=1
        buffer=''
        centinela='$'
        estado=0
        codigo_fuente+=centinela
        i=0
        while i< len(codigo_fuente):
            c = codigo_fuente[i]
            
            if estado == 0:
                if c == ':':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'dospuntos', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == '{':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'llaveAbrir', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == '}':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'llaveCerrar', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == '[':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'corcheteAbrir', linea, columna))
                    buffer = ''
                    columna += 1
                
                elif c == ']':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'corcheteCerrar', linea, columna))
                    buffer = ''
                    columna += 1

                elif c == '=':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'Igual', linea, columna))
                    buffer = ''
                    columna += 1

                elif c == ';':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'puntocoma', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == ',':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'coma', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == '\'' or c == '"':
                    buffer += c
                    columna += 1
                    estado = 1
                elif re.search('\d', c):
                    buffer += c
                    columna += 1
                    estado = 2
                elif re.search('[A-Z|a-z]', c):
                    buffer += c
                    columna += 1
                    estado = 3
                
                elif c == '#':
                    buffer += c
                    columna += 1
                    estado=4
                elif c == '@':
                    buffer += c
                    columna += 1
                    estado=5
                elif c == '\n':
                    linea += 1
                    columna = 1
                elif c == '\t':
                    columna += 1
                elif c == '\r':
                    pass
                elif c == ' ':
                    pass
                elif c == centinela:
                    print('Se aceptó la cadena!')
                    break
                else:
                    buffer += c
                    self.listaErrores.append(Error('Caracter: ' + buffer + '  no reconocido en el lenguaje.', 'Léxico', linea, columna))
                    buffer = ''
                    columna += 1


            elif estado == 1:
                if c == '\'' or c == '"':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'cadena', linea, columna))
                    buffer = ''
                    columna += 1
                    estado = 0
                elif c == '\n':
                    buffer += c
                    linea += 1
                    columna = 1
                elif c == '\r':
                    buffer += c
                else:
                    buffer += c
                    columna += 1
            elif estado == 2:
                if re.search('\d', c):
                    buffer += c
                    columna += 1
                else:
                    self.listaTokens.append(Token(buffer, 'entero', linea, columna))
                    buffer = ''
                    i -= 1
                    estado = 0

            elif estado==3:
                if re.search('[A-Z|a-z]', c):
                    buffer=buffer+c
                    columna =columna+1
                else:
                    buffer2=buffer.lower()
                    if buffer == 'TITULO':
                        self.listaTokens.append(Token(buffer, 'TITULO', linea, columna))
                    elif buffer == 'ANCHO':
                        self.listaTokens.append(Token(buffer, 'ANCHO', linea, columna))
                    elif buffer == 'ALTO':
                        self.listaTokens.append(Token(buffer, 'ALTO', linea, columna))
                    elif buffer == 'FILAS':
                        self.listaTokens.append(Token(buffer, 'FILAS', linea, columna))
                    elif buffer == 'COLUMNAS':
                        self.listaTokens.append(Token(buffer, 'COLUMNAS', linea, columna))
                    elif buffer == 'CELDAS':
                        self.listaTokens.append(Token(buffer, 'CELDAS', linea, columna))
                    elif buffer == 'FILTROS':
                        self.listaTokens.append(Token(buffer, 'FILTROS', linea, columna))
                    elif buffer == 'MirrorX' or buffer2=="mirrorx" :
                        self.listaTokens.append(Token(buffer, 'MirrorX', linea, columna))
                    elif buffer == 'MirrorY'  or buffer2=="mirrory" :
                        self.listaTokens.append(Token(buffer, 'MirrorY', linea, columna))
                    elif buffer == 'DoubleMirror' or buffer2=="doublemirror":
                        self.listaTokens.append(Token(buffer, 'DoubleMirror', linea, columna))
                    
                    elif buffer == 'TRUE':
                        self.listaTokens.append(Token(buffer, 'boleano', linea, columna))
                    elif buffer == 'FALSE':
                        self.listaTokens.append(Token(buffer, 'boleano', linea, columna))

                    buffer = ''
                    i -= 1
                    estado = 0
            elif estado==4:
                if re.search('[A-Z|a-z|\d]', c):
                    buffer=buffer+c
                    columna =columna+1
                else:
                    self.listaTokens.append(Token(buffer, 'CodigoColor', linea, columna))
                    buffer = ''
                    i -= 1
                    estado = 0
            elif estado==5:
                if re.search('[@]', c):
                    buffer=buffer+c
                    columna =columna+1
                else:
                    if buffer == '@@@@':
                        self.listaTokens.append(Token(buffer, 'Separador', linea, columna))
                    else:
                        self.listaErrores.append(Error('Caracter : ' + buffer + '   no reconocido en el lenguaje.', 'Lexico', linea, columna))

                    buffer = ''
                    i -= 1
                    estado = 0



            i=i+1
            
    def imprimirToken(self):
        archivo = open('tokens.txt', 'w')
        for p in self.listaTokens:
            lineaa=str(p.linea )+ ""
            columnaa=str(p.columna)+""
            archivo.write("<tr> <th> " + p.lexema+"</th>" +"<th> " + p.tipo+"</th>"  +"<th> " + lineaa+"</th>" +"<th> " + columnaa+"</th>"+  "</tr>\n" )
        archivo.close()
        

        archivo2 = open('error.txt', 'w')
        for t in self.listaErrores:
            lineaa=str(t.linea )+ ""
            columnaa=str(t.columna)+""
            archivo2.write("<tr> <th> " + t.descripcion+"</th>" +"<th> " + t.tipo+"</th>"  +"<th> " + lineaa+"</th>" +"<th> " + columnaa+"</th>"+  "</tr>\n")

        archivo2.close()
        return 1

    def Tokenss(self):
        return self.listaTokens
    
    def Erroress(self):
        return self.listaErrores

    
    def datos(self):
        imagenes=[]
        filtros=[]
        i=0
        temp=Imagen("",0,0,0,0,"","")
        while i<len(self.listaTokens):
            tken=self.listaTokens[i]
            if tken.tipo=="TITULO":
                temp.titulo=self.listaTokens[i+2].lexema
            elif tken.tipo=="ANCHO":
                temp.ancho=self.listaTokens[i+2].lexema
            elif tken.tipo=="ALTO":
                temp.alto=self.listaTokens[i+2].lexema
            elif tken.tipo=="FILAS":
                temp.fila=self.listaTokens[i+2].lexema
            elif tken.tipo=="COLUMNAS":
                temp.columna=self.listaTokens[i+2].lexema
            elif tken.lexema=="{":
                lmatriz=[]
                while tken.lexema!=";":
                    i=i+1
                    tken=self.listaTokens[i]
                    if tken.lexema=="[":
                        lmatriz.append(Matriz(self.listaTokens[i+1].lexema,self.listaTokens[i+3].lexema,self.listaTokens[i+5].lexema,self.listaTokens[i+7].lexema))
                        #temp.celda=Matriz(self.listaTokens[i+1].lexema,self.listaTokens[i+3].lexema,self.listaTokens[i+5].lexema,self.listaTokens[i+7].lexema)
                    elif tken.lexema=="}":
                        temp.celda=lmatriz
            
            elif tken.tipo=="MirrorX" or tken.tipo=="MirrorY" or tken.tipo=="DoubleMirror" :
                filtros.append(tken.lexema)
                if self.listaTokens[i+1].lexema==";":
                    temp.filtro=filtros
                    filtros=[]

            elif tken.tipo=="Separador":
                imagenes.append(temp)
                temp=temp=Imagen("",0,0,0,0,"","")
            
            elif i==len(self.listaTokens)-1:
                imagenes.append(temp)
                temp=temp=Imagen("",0,0,0,0,"","")

            i=i+1

        n=0
        return imagenes
        
        #for i in imagenes:
        #    n=n+1
        #    nombre="Grafica"+str(n)+".dot"
        #    print(i.titulo)
        #    agrafica=open(nombre,"w")
        #    gtitulo='''digraph structs {
	    #    node [shape=plaintext]
	    #    struct3 [label=<<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0" CELLPADDING="50">
        #    '''
        #    agrafica.write(gtitulo+'\n')
        #    for f in range(int(i.fila)):
        #        agrafica.write('<TR>\n')
        #        for c in range(int(i.columna)):
        #            codigo="<TD></TD> \n"
        #            for j in i.celda:
        #                if int(j.x)==f and int(j.y)==c and j.paso=="TRUE":
        #                    codigo='<TD bgcolor="' + str(j.color) + '"></TD> \n'
        #            agrafica.write(codigo)
        #        agrafica.write('</TR>\n')
        #    agrafica.write('</TABLE>>]}')
        #    agrafica.close()
        


        








from Token import Token
from Error import Error
import re

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
        archivo = open('hola.txt', 'w')
        
        for t in self.listaTokens:
            #t.imprimirToken()
            archivo.write(t.getLexema() + "\n")
        archivo.close()

        archivo2 = open('error.txt', 'w')
        for t in self.listaErrores:
             archivo2.write(t.getErrores() + "\n")
        archivo2.close()


        








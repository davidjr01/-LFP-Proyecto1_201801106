class Token:
    def __init__(self,lexema,tipo,linea,columna):
        self.lexema=lexema
        self.tipo=tipo
        self.linea=linea
        self.columna=columna
    
    def imprimirTokens(self):
        return ('Lexema:   ' +self.lexema+ "   " + "   Tipo:  "+ self.tipo + "   Linea   " + str(self.linea) + "   Columna "+ str(self.columna))
    
   
    


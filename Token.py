class Token:
    def __init__(self,lexema,tipo,linea,columna):
        self.lexema=lexema
        self.tipo=tipo
        self.linea=linea
        self.columna=columna
    
    def imprimirToken(self):
        print('Lexema:   ' +self.lexema+ "   " + "   Tipo:  "+ self.tipo + "   Linea   " + str(self.linea) + "   Columna "+ str(self.columna))
    
    def getLexema(self):
        return 'Lexema:   ' +self.lexema+ "   " + "   Tipo:  "+ self.tipo + "   Linea   " + str(self.linea) + "   Columna "+ str(self.columna)

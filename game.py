class Plataforma:

    def __init__(self, code , name):
        self.code = int(code)
        self.name = name

class Juego:

    def __init__(self, code, name, plat):
        self.code= int(code)
        self.name = name
        self.plat = plat



class Nodo:

    def __init__(self, code, name, plat):
        if plat != None:
            self.Juego = Juego(code, name, plat)
        else:
            self.Plataforma = Plataforma(code, name)
        
        self.Next = None

    def  getNext (self):
        return self.Next
        

    def  assNext (self, Nodo):
        self.Next = Nodo

    def getJuego (self):
        return self.Juego

    def getPlataforma(self):
        return self.Plataforma

    def getNumeroJuego (self):
        return self.Juego.code

    def getNameJuego (self):
        return self.Juego.name

    def getPltJuego (self):
        return self.Juego.plat
        
    def getNamePlt (self):
        return self.Plataforma.name    

    def getNumeroPlataforma(self):
        return self.Plataforma.code

    def ImprimirJuego(self):
        
        return 'Codigo Juego '+str(self.Juego.code) + " " +'Nombre '+ str(self.Juego.name)+ ' '+ 'Cod. ' +str(self.Juego.plat) +'|'   


    def ImprimirPlataforma(self):
        y = 'Codigo Plataforma '+str(self.Plataforma.code) + ' '+ 'Nombre '+str(self.Plataforma.name)+'|'

        return y



        


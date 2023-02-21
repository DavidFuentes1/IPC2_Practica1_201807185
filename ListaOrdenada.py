from game import*

class ListaOrdenada:


    def __init__(self):
        self.Cabeza = None
        self.Cola = None
        self.Size = 0

    def InsertarJuego(self, code, name, plat):
            newNodo = Nodo(code, name, plat)
            self.Size += 1
            if self.Cabeza== None:
                self.Cabeza= newNodo
                self.Cola = newNodo
            else:
                self.Cola.assNext(newNodo)
                self.Cola = newNodo
    

    def InsertarPlataforma(self, code, name):
            newNodo = Nodo(code,name,None)
            self.Size += 1 
            if self.Cabeza == None:
                self.Cabeza = newNodo
                self.Cola = newNodo
            else:
                self.Cola.assNext(newNodo)
                self.Cola = newNodo    


    def OrdenarJuego(self):
            for n in range(self.Size):
                apuntadorCabeza = self.Cabeza
                Anterior = None
                while apuntadorCabeza != None:
                    if apuntadorCabeza.Next != None:
                        if apuntadorCabeza.getNumeroJuego() > apuntadorCabeza.Next.getNumeroJuego():
                           
                            if apuntadorCabeza == self.Cabeza:
                               
                                self.Cabeza = apuntadorCabeza.Next
                                apuntadorCabeza.Next = self.Cabeza.Next
                                self.Cabeza.Next = apuntadorCabeza
                               
                            else:
                               
                                Anterior.Next = apuntadorCabeza.Next
                                apuntadorCabeza.Next = apuntadorCabeza.Next.Next
                                Anterior.Next.Next = apuntadorCabeza
                    Anterior = apuntadorCabeza
                    apuntadorCabeza = apuntadorCabeza.Next


    def OrdenarPlataforma(self):
        for i  in range(self.Size):
            apuntadorGuia = self.Cabeza
            Anterior = None
            while apuntadorGuia != None:
                if apuntadorGuia.Next != None:
                    if apuntadorGuia.getNumeroPlataforma() > apuntadorGuia.Next.getNumeroPlataforma():
                        if apuntadorGuia == self.Cabeza:
                            self.Cabeza = apuntadorGuia.Next
                            apuntadorGuia.Next = self.Cabeza.Next
                            self.Cabeza.Next = apuntadorGuia

                        else:
                            Anterior.Next = apuntadorGuia.Next
                            apuntadorGuia.Next = apuntadorGuia.Next.Next
                            Anterior.Next.Next = apuntadorGuia

                Anterior = apuntadorGuia
                apuntadorGuia  = apuntadorGuia.Next


    def Impimir(self):
        Retorno = "Los datos ordenados son (espero) ["
        if self.Cabeza == None:
            return "! AQUI NO HAY NADA¡."
        Auxiliar = self.Cabeza
        while Auxiliar != None:
            Retorno += str(Auxiliar.ImprimirJuego())
            Auxiliar = Auxiliar.Next
        Retorno += "]"
        return Retorno


    def ImprimirPlataforam(self):
        Retorno = "Los datos ordenados son (espero) ["
        if self.Cabeza == None:
            return "! AQUI NO HAY NADA¡."
        Auxiliar = self.Cabeza
        while Auxiliar != None:
            Retorno += str(Auxiliar.ImprimirPlataforma())
            Auxiliar = Auxiliar.Next
        Retorno += "]"
        return Retorno
    

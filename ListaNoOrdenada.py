
class Nodo:
    def __init__(self,datoInicial):
        self.dato = datoInicial
        self.siguiente = None
    
    def obtenerDato(self):
        return self.dato
    
    def obtenerSiguiente(self):
        return self.siguiente
    
    def asignarDato(self, nuevodato):
        self.dato = nuevodato
    
    def asignarSiguiente(self,nuevosiguiente):
        self.siguiente = nuevosiguiente
        

class ListaNoOrdenada:
    def __init__(self):
        self.cabeza = None
    
    def estaVacia(self):
        return self.cabeza == None
    
    def agregar(self, item):
        temp = Nodo(item)
        temp.asignarSiguiente(self.cabeza)
        self.cabeza = temp
    
    def tamanio(self):
        actual = self.cabeza
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.obtenerSiguiente()
        print(contador)   
        return contador
    
    def buscar(self, item):
        actual = self.cabeza
        encontrado = False
        while actual != None and not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                actual = actual.obtenerSiguiente()
        return encontrado
    
    def remover(self, item):
        actual = self.cabeza
        anterior = None
        encontrado = False
        while not encontrado and actual != None:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                anterior = actual
                actual = actual.obtenerSiguiente()
        
        if encontrado:
            if anterior == None:
                self.cabeza = actual.obtenerSiguiente()
            else:
                anterior.asignarSiguiente(actual.obtenerSiguiente())
                
            print("eliminado")
        
        
        



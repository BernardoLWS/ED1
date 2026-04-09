class NodoCircular():
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaCircular():
    def __init__(self):
        self.puntero = None
    
    def agregar(self,dato):
        nuevo = NodoCircular(dato)
        if self.puntero is None:
            self.puntero = nuevo
            nuevo.siguiente = self.puntero
        else:   
            actual = self.puntero
            while actual.siguiente != self.puntero:
                    actual = actual.siguiente      
            nuevo.siguiente = self.puntero
            actual.siguiente = nuevo

    def eliminar(self,dato):   
        if self.puntero == None:
            return
        else:
            ultimo = self.puntero      #actual 1
            if self.puntero.dato == dato:                   
                while ultimo.siguiente != self.puntero:    #ultimo 4
                    ultimo = ultimo.siguiente     
                ultimo.siguiente = self.puntero.siguiente
                self.puntero = self.puntero.siguiente       
            else:
                actual = self.puntero
                while actual.dato != dato:
                    actual = actual.siguiente
                if actual.dato == dato:
                    penultimo = self.puntero
                    while penultimo.siguiente != actual:
                        penultimo = penultimo.siguiente
                    penultimo.siguiente = actual.siguiente
                    self.puntero = self.puntero  

    def modificar(self,pos,dato):
        actual = self.puntero
        for i in range(pos-1):
            actual = actual.siguiente
        actual.dato = dato 

    def buscar(self,dato):
        actual = self.puntero
        contador = 0
        if actual is None:
            return print("lista vacia")
        else:
            while actual.dato != dato and actual.siguiente != None:
                actual = actual.siguiente
                contador += 1
            if actual.dato == dato:        
                return print("Elemento: " + str(dato) + " encontrado, en la posicion: "+str(contador+1))
            return print("Elemento no encontrado") 

    def mostrar(self):
        if self.puntero == None:
            return print("Lista Vacia")
        actual = self.puntero
        salida = " -> " + str(actual.dato) + " -> "
        actual = actual.siguiente
        while  actual.dato != self.puntero.dato: 
            salida += str(actual.dato) + " -> "
            actual = actual.siguiente
        print(salida) 

def main():
    l = ListaCircular()
    l.agregar(1)
    l.agregar(2)
    l.agregar(3)
    l.agregar(4)
    l.mostrar()
    #l.eliminar(2)
    #l.mostrar()
    #l.modificar(3,9)
    l.buscar(3)
    l.mostrar()

if __name__ == "__main__":
    main()


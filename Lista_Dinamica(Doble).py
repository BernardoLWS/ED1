class NodoDoble():
    def __init__(self,dato):
        self.anterior = None
        self.siguiente = None
        self.dato = dato

class ListaDoble():
    def __init__(self):
        self.cabeza = None

    def agregar(self,dato):
         nuevo = NodoDoble(dato)
         if self.cabeza == None:
            self.cabeza = nuevo
         else:
            actual = self.cabeza     
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
            nuevo.anterior = actual

    def eliminar(self,dato):
        actual = self.cabeza
        if actual.dato == dato:
            self.cabeza = actual.siguiente
        else:
            actual = actual.siguiente 
            while actual.siguiente is not None and actual.dato != dato:
                    actual = actual.siguiente                
            if actual.dato == dato:
                actual.anterior.siguiente = actual.siguiente
                actual.siguiente.anterior = actual.anterior
               
    def modificar(self,pos,dato):
        actual = self.cabeza
        for i in range(pos-1):
            actual = actual.siguiente
        actual.dato = dato           

    def buscar(self,dato):
        actual = self.cabeza
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
        salida = ""
        actual = self.cabeza
        while actual is not None :
            salida += str(actual.dato) + " -> "
            actual = actual.siguiente
        return salida + "None"

def main():
    l = ListaDoble()
    l.agregar(1)
    l.agregar(2)
    l.agregar(3)
    l.agregar(4)
    l.agregar(5)
    print(l.mostrar())
    #l.eliminar(2)
   # l.modificar(4,57)
    l.buscar(4)
    print(l.mostrar())

if __name__ == "__main__":
    main()
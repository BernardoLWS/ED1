class NodoSimple():
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None

class ListaSimple():
    def __init__(self):
        self.inicio = None

    def agregar(self,dato):
         if self.inicio == None:
              self.inicio = NodoSimple(dato)
         else:
              actual = self.inicio     
              nuevo = NodoSimple(dato)
              while actual.siguiente is not None:
                    actual = actual.siguiente
              actual.siguiente = nuevo

    def eliminar(self,dato):
         if self.inicio.dato == dato:
            self.inicio = self.inicio.siguiente
         else:
            actual = self.inicio
            while actual.siguiente is not None:
                if actual.siguiente.dato == dato:
                    actual.siguiente = actual.siguiente.siguiente
                else:
                   actual = actual.siguiente

    def modificar(self, pos, dato):
        actual = self.inicio
        for i in range(pos-1):
            actual = actual.siguiente
        actual.dato = dato   

    def buscar(self,dato):
        actual = self.inicio
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
        actual = self.inicio
        while actual != None :
            salida += str(actual.dato) + " -> "
            actual = actual.siguiente
        return salida + "None"

def main():
        l = ListaSimple()  
        l.agregar(8)       
        #l.agregar(9)        
        #l.agregar(10)       
        #l.agregar(11)      
       # l.agregar(12)       
        print(l.mostrar()) 
       # l.eliminar(9)       
      #  print(l.mostrar())  
      #  l.modificar(4,15)
      #  print(l.mostrar())
        l.buscar(11)
        

if __name__ == "__main__":
    main()    

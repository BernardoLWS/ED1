class ListaEstatica:
    def __init__(self,tam):
        self.tam = tam
        self.V = []
class ListaDinamica():
    def __init__(self,tam):
        self.tam = tam
        self.V = []

    def agregar (self,dato):
        if len(self.V) < self.tam :
            self.V.append(dato)
        else:
            print("Lista llena")   

    def eliminar (self,dato):
        if dato in self.V:
            self.V.remove(dato)
        else:
            print("elemento no encontrado")

    def modificar(self,pos,dato):
        if 0 <= pos < len(self.V):
            self.V[pos] = dato
        else:
            print("posicion invalida") 

    def buscar(self,dato):
        for i in range(len(self.V)):
            if self.V[i] == dato:
                return print("Elemento: " + str(dato) + " encontrado, en la posicion: "+str(i+1))
        return print("Elemento no encontrado")        

    def mostrar(self):
        salida = "["
        for i in range(len(self.V)):
            salida += str(self.V[i])
            if i < (len(self.V) - 1):
                salida += ","    
        return salida + "]"

def main():
    tam = int(input("tamaño de la lista : "))
    V = ListaDinamica(tam)
    V.agregar(5)
    V.agregar(6)
    V.agregar(7)
    print(V.mostrar())
    #V.eliminar(5)
    #print(V.mostrar())
   # V.modificar(1,9)
    V.buscar(8)
    #print(V.mostrar())

if __name__ == "__main__":
    main()
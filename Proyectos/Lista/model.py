class nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Lista_Dinamica:
    def __init__(self):
        self.cabeza = None

    def Insertar_Final(self, elemento):
        nuevo = nodo(elemento)
        if self.cabeza == None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def Insertar_Inicio(self, elemento):
        nuevo = nodo(elemento)
        if self.cabeza == None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            self.cabeza = nuevo
            nuevo.siguiente = actual

    def Buscar(self,elemento):
        actual = self.cabeza
        posicion = 0
        while actual:
            if str(actual.dato) == str(elemento):
                return posicion
            else:
                actual = actual.siguiente
                posicion += 1
        return -1

    def Eliminar(self, elemento):
        actual = self.cabeza
        anterior = None
        while actual:
            if str(actual.dato) == str(elemento):
                if anterior is  None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente    
            anterior = actual
            actual = actual.siguiente

    def vaciar(self):
        self.cabeza = None     
    
    def mostrar(self):
        """Devuelve todos los elementos de la lista en forma de lista Python"""
        datos = []
        actual = self.cabeza
        while actual:
            datos.append(actual.dato)
            actual = actual.siguiente
        return datos    


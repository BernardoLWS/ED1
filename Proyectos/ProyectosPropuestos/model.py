class Model:
    def __init__(self):
        self.lista_proyectos = ListaDobleEnlazada()
        self.undo_redo = UndoRedoManager()
        self.cola_prioridad = ColaPrioritaria()
        self.cola_queue = ColaQueue()

"""  ----------------------------------- CLASE LISTA DOBLEMENTE ENLAZADA -------------------------------------------  """
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamaño = 0

    def insertar_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.tamaño += 1
    
    def insertar_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.tamaño += 1

    def Eliminar(self, dato):
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.cola = actual.anterior
                
                self.tamaño -= 1
                return True
            actual = actual.siguiente
        return False

    def Busqueda(self, dato):
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False
    
    def Mostrar_Lista(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" <-> ")
            actual = actual.siguiente
        print("None")


""""   -----------------------------------------------  CLASE PILA -----------------------------------------------  """
class NodoPila:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self.cima = None
        self.tamaño = 0

    def Apilar(self, dato):
        nuevo_nodo = NodoPila(dato)
        nuevo_nodo.siguiente = self.cima
        self.cima = nuevo_nodo
        self.tamaño += 1

    def Desapilar(self):
        if self.cima is not None:
            dato = self.cima.dato
            self.cima = self.cima.siguiente
            self.tamaño -= 1
            return dato
        return None

    def Ver_Cima(self):
        if self.cima is not None:
            return self.cima.dato
        return None

    def Mostrar_Pila(self):
        actual = self.cima
        while actual:
            print("[", actual.dato, "]")
            actual = actual.siguiente
        
class UndoRedoManager:
    def __init__(self):
        self.Pila_undo = Pila()
        self.Pila_redo = Pila()

    def Ejecutar_accion(self, estado):
        self.Pila_undo.Apilar(estado)
        self.Pila_redo = Pila()  # Reiniciar correctamente como Pila vacía

    def Desacer(self, estado_actual):
        if self.Pila_undo.cima is None:
            return None
        else:
            estado_anterior = self.Pila_undo.Desapilar()
            self.Pila_redo.Apilar(estado_actual)
            return estado_anterior

    def Rehacer(self, estado_actual):
        if self.Pila_redo.cima is None:
            return None
        else:
            estado_siguiente = self.Pila_redo.Desapilar()
            self.Pila_undo.Apilar(estado_actual)
            return estado_siguiente

    def Mostrar_Pilas(self):
        undo = self.Pila_undo.cima
        redo = self.Pila_redo.cima
        print("\n", "Pila Undo:")
        while undo:
            print("[", undo.dato, "]")
            undo = undo.siguiente
        print("\n", "Pila Redo:")
        while redo:
            print("[", redo.dato, "]")
            redo = redo.siguiente
        
"""-------------------------------------------------- Clase Cola --------------------------------------------------"""
class NodoColaQueue:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ColaQueue:
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamaño = 0

    def Encolar(self, dato):
        nuevo_nodo = NodoColaQueue(dato)
        if self.final is None:
            self.frente = self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo
        self.tamaño += 1

    def Desencolar(self):
        if self.frente is None:
            return None
        dato = self.frente.dato
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        self.tamaño -= 1
        return dato

    def Ver_Frente(self):
        return self.frente.dato if self.frente else None

    def Mostrar_Cola(self):
        actual = self.frente
        while actual:
            print("[", actual.dato, "]", end=" -> ")
            actual = actual.siguiente
        print("None")



class NodoPrioridad:
    def __init__(self, dato, prioridad):
        self.dato = dato
        self.prioridad = prioridad  # Menor número = mayor prioridad (o viceversa, según prefieras)
        self.siguiente = None

class ColaPrioritaria:
    def __init__(self):
        self.cabeza = None
        self.tamaño = 0

    def Encolar(self, dato, prioridad):
        nuevo_nodo = NodoPrioridad(dato, prioridad)
        
        # Si la cola está vacía o el nuevo elemento tiene mayor prioridad que la cabeza (menor valor numérico)
        if not self.cabeza or prioridad < self.cabeza.prioridad:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        else:
            # Buscar la posición correcta según la prioridad
            actual = self.cabeza
            while actual.siguiente and actual.siguiente.prioridad <= prioridad:
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo
        self.tamaño += 1

    def Desencolar(self):
        if not self.cabeza:
            return None
        dato = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente
        self.tamaño -= 1
        return dato

    def Mostrar_Cola_Prioritaria(self):
        actual = self.cabeza
        while actual:
            print(f"(Dato: {actual.dato}, Prioridad: {actual.prioridad})", end=" -> ")
            actual = actual.siguiente
        print("None")
""" ---------------------------------------------------- MAIN ------------------------------------------------------ """
def main():
    modelo = Model()
    modelo.lista_proyectos.insertar_final("Proyecto A")
    modelo.lista_proyectos.insertar_final("Proyecto B")
    modelo.lista_proyectos.Mostrar_Lista()

    pp = UndoRedoManager()
    pp.Ejecutar_accion("Estado 1")
    pp.Ejecutar_accion("Estado 2")
    pp.Mostrar_Pilas()
    actual = pp.Deshacer("Estado 3")
    pp.Mostrar_Pilas()
    print("estado actual :", actual)


if __name__ == "__main__":
    main()
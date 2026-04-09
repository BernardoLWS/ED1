import pickle
import os

class ConjuntoPersistente:
    def __init__(self, filename):
        self.filename = filename
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as f:
                self.elementos = pickle.load(f)
        else:
            self.elementos = set()

    def agregar(self, elemento):
        self.elementos.add(elemento)
        self.guardar()

    def eliminar(self, elemento):
        if elemento in self.elementos:
            self.elementos.remove(elemento)
            self.guardar()

    def contiene(self, elemento):
        return elemento in self.elementos

    def union(self, otro_conjunto):
        nuevo_conjunto = ConjuntoPersistente(self.filename + '_union')
        nuevo_conjunto.elementos = self.elementos.union(otro_conjunto.elementos)
        nuevo_conjunto.guardar()
        return nuevo_conjunto

    def interseccion(self, otro_conjunto):
        nuevo_conjunto = ConjuntoPersistente(self.filename + '_interseccion')
        nuevo_conjunto.elementos = self.elementos.intersection(otro_conjunto.elementos)
        nuevo_conjunto.guardar()
        return nuevo_conjunto


    def diferencia(self, otro_conjunto):
        nuevo_conjunto = ConjuntoPersistente(self.filename + '_diferencia')
        nuevo_conjunto.elementos = self.elementos.difference(otro_conjunto.elementos)
        nuevo_conjunto.guardar()
        return nuevo_conjunto

    def guardar(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.elementos, f)

    def mostrar(self):
        print(self.elementos)

# Ejemplo de uso
conjunto1 = ConjuntoPersistente('conjunto1.dat')
conjunto1.agregar(1)
conjunto1.agregar(2)
conjunto1.agregar(3)
conjunto1.mostrar()  # Output: {1, 2, 3}

conjunto2 = ConjuntoPersistente('conjunto2.dat')
conjunto2.agregar(3)
conjunto2.agregar(4)
conjunto2.agregar(5)
conjunto2.mostrar() # Output: {3, 4, 5}

conjunto_union = conjunto1.union(conjunto2)
conjunto_union.mostrar()

conjunto_interseccion = conjunto1.interseccion(conjunto2)
conjunto_interseccion.mostrar()

conjunto_diferencia = conjunto1.diferencia(conjunto2)
conjunto_diferencia.mostrar()

conjunto1.eliminar(2)
conjunto1.mostrar()

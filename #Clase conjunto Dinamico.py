class conjunto_Dinamico:
    def __init__ (self):
        self.A = []
        self.B = [] 
    def agregar(self,conjunto,elemento):
        if conjunto == "A":
            self.A.append(elemento)
        elif conjunto == "B":
            self.B.append(elemento)
    def eliminar(self,conjunto,elemento):
        if conjunto == "A":
            if elemento in self.A:
                self.A.remove(elemento)
        elif conjunto == "B":
            if elemento in self.B:
                self.B.remove(elemento)
    def union(self):
        return list(set(self.A) | set(self.B))
    def interseccion(self):
        return list(set(self.A) & set(self.B))
    
def main():
    conjunto = conjunto_Dinamico()
    conjunto.A = list(map(int, input("Ingresar elementos en A separados por coma: ").split(",")))
    conjunto.B = list(map(int, input("Ingresar elementos en B separados por coma: ").split(",")))
    print("A = " , conjunto.A)
    print("B = " , conjunto.B)
    #----------Agregar elementos a los conjuntos---------
    #addA = int(input("Cuanto desea agregar a A: "))
    #addB = int(input("Cuanto desea agregar a B: "))
    #for i in range(addA):
    #    conjunto.agregar("A", int(input("nuevo elemento A: ")))
    #for i in range(addB):
    #    conjunto.agregar("B", int(input("nuevo elemento B: ")))
    #print("A = " , conjunto.A)
    #print("B = " , conjunto.B)
    #-----------Eliminar elementos de los conjuntos---------------
    #delA = int(input("Que elemento desea eliminar de A: "))
    #delB = int(input("Que elemento desea eliminar de B: "))
    #conjunto.eliminar("A", delA)
    #conjunto.eliminar("B", delB)
    #print("A = " , conjunto.A)
    #print("B = " , conjunto.B)
    #-----------Union e interseccion de los conjuntos----------------
    print("Union de A y B: ", conjunto.union())
    print("Interseccion de A y B: ", conjunto.interseccion())
if __name__ == "__main__":
    main()
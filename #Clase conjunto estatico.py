
class conjunto_estatico:
    "definimos la clase con un tamaño especifico"
    def __init__(self,tamA,tamB):
        self.A = []
        self.B = []
        self.tamA = tamA
        self.tamB = tamB
    def agregar(self,conjunto,elemento):
        ""    
        if conjunto == "A":
            if len(self.A) < self.tamA :
                self.A.append(elemento)
            else:
                print("El conjunto A esta lleno, no se pueden agregar el elemento: " + str(elemento))
        if conjunto == "B":
           if len(self.B) < self.tamB :
                self.B.append(elemento)
           else:
                print("El conjunto B esta lleno, no se pueden agregar el elemento: " + str(elemento))
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
        "   ingresamos el tamaño del conjunto A y B   "
        tamA = int(input("Ingrese el tamaño del conjunto A :"))
        tamB = int(input("Ingrese el tamaño del conjunto B :"))
        conjunto = conjunto_estatico(tamA,tamB)
       
        "   ingresamos los elementos en cada conjunto    "
        for i in range(tamA):
            conjunto.agregar("A",int(input("Ingrese el elemento del conjunto A :")))
        for i in range(tamB):
            conjunto.agregar("B", int(input("Ingrese el elemento del conjunto B: ")))
       
        "   mostramos en pantalla     "
        print("Conjunto A:", conjunto.A)
        print("Conjunto B:", conjunto.B)
       
        "   Eliminar elementos de los conjuntos     "
        for i in range(int(input("Cuantos elementos desea eliminar de A: "))):
            conjunto.eliminar("A", int(input("Ingrese el elemento que desea eliminar de A: ")))
        print("Conjunto A:", conjunto.A)
        #for i in range(int(input("Cuantos elementos desea eliminar de B: "))):
        #    conjunto.eliminar("B", int(input("Ingrese el elemento que desea eliminar de B: ")))
        #print("Conjunto B:", conjunto.B) 
        "   agregar un elemento (si el conjunto esta lleno no se podra agregar)     "
        for i in range(int(input("cuantos elemento desea agregar en A"))):
            conjunto.agregar("A",int(input("elemento :")))
        print("Conjunto A:", conjunto.A)
        

if __name__ == "__main__":
     main()
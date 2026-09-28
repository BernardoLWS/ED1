class Nodo:
    def __init__(self, coef, exp):
        self.coef = coef
        self.exp = exp
        self.sig = None

class polinomio:
    def __init__(self):
        self.cabeza = None

    def insertar(self, coef, exp):
        nuevo = Nodo(coef, exp)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.sig:
                actual = actual.sig
            actual.sig = nuevo

    def ordenar(self):
        if not self.cabeza or not self.cabeza.sig:
            return
        cambiado = True
        while cambiado:
            cambiado = False
            actual = self.cabeza
            while actual.sig:
                if actual.exp < actual.sig.exp:
                    actual.coef, actual.sig.coef = actual.sig.coef, actual.coef
                    actual.exp, actual.sig.exp = actual.sig.exp, actual.exp
                    cambiado = True
                actual = actual.sig

    def mostrar(self):
        actual = self.cabeza
        polinomio = ""
        while actual:
            if actual.coef > 0 and polinomio:
                polinomio += "+"
            if actual.exp == 0:
                polinomio += str(actual.coef)
            elif actual.exp == 1:
                polinomio += f"{actual.coef}x"
            else:
                polinomio += f"{actual.coef}x^{actual.exp}"
            actual = actual.sig
        return polinomio

    def evaluar(self, x_val):
        actual = self.cabeza
        resultado = 0
        while actual:
            resultado += actual.coef * (x_val ** actual.exp)
            actual = actual.sig
        return resultado

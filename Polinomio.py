class Polinomio:
    """Clase que representa un polinomio."""

    def __init__(self, coeficientes=None):
        """
        Inicializa el polinomio.
        coeficientes: lista de números, donde el índice es el grado.
        Ejemplo: [2, 0, 3] representa 2 + 0x + 3x^2
        """
        if coeficientes is None:
            coeficientes = []
        self.coeficientes = coeficientes

    def grado(self):
        """Devuelve el grado del polinomio."""
        return len(self.coeficientes) - 1

    def evaluar(self, x):
        """Evalúa el polinomio en un valor x."""
        resultado = 0
        for i, coef in enumerate(self.coeficientes):
            resultado += coef * (x ** i)
        return resultado

    def __str__(self):
        """Devuelve una representación en forma de cadena."""
        partes = []
        for i, coef in enumerate(self.coeficientes):
            if coef != 0:
                if i == 0:
                    partes.append(f"{coef}")
                elif i == 1:
                    partes.append(f"{coef}x")
                else:
                    partes.append(f"{coef}x^{i}")
        return " + ".join(partes) if partes else "0"

    def sumar(self, otro):
        """Suma dos polinomios y devuelve un nuevo polinomio."""
        max_len = max(len(self.coeficientes), len(otro.coeficientes))
        resultado = [0] * max_len

        for i in range(max_len):
            coef1 = self.coeficientes[i] if i < len(self.coeficientes) else 0
            coef2 = otro.coeficientes[i] if i < len(otro.coeficientes) else 0
            resultado[i] = coef1 + coef2

        return Polinomio(resultado)

    def multiplicar(self, otro):
        """Multiplica dos polinomios y devuelve un nuevo polinomio."""
        resultado = [0] * (len(self.coeficientes) + len(otro.coeficientes) - 1)

        for i, coef1 in enumerate(self.coeficientes):
            for j, coef2 in enumerate(otro.coeficientes):
                resultado[i + j] += coef1 * coef2

        return Polinomio(resultado)


# Ejemplo de uso
if __name__ == "__main__":
    p1 = Polinomio([2, 3])       # 2 + 3x
    p2 = Polinomio([1, 0, 4])    # 1 + 4x^2

    print("Polinomio 1:", p1)
    print("Polinomio 2:", p2)

    suma = p1.sumar(p2)
    print("Suma:", suma)

    producto = p1.multiplicar(p2)
    print("Producto:", producto)

    print("Evaluar p1 en x=2:", p1.evaluar(2))

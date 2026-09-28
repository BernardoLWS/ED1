from modelo import polinomio
from vista import ventana

class Controlador:
    def __init__(self, vista, modelo):
        self.vista = vista
        self.modelo = modelo

    def agregar(self):
        self.coef = self.vista.Entry_coef.get()
        self.exp = self.vista.Entry_exp.get()
        self.modelo.insertar(self.coef, self.exp)
    
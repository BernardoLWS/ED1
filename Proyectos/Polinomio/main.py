from vista import ventana
from controlador import Controlador
from modelo import polinomio

def main():
    vista = ventana
    modelo = polinomio
    Controlador = Controlador(vista, modelo)

if __name__ == "__main__":
    main()



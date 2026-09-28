from view import ventana
from controller import controlador
from model import Lista_Dinamica

def main():
    modelo = Lista_Dinamica()
    vista = ventana(None)
    control = controlador(vista, modelo)
    vista.control = control 
    vista.Iniciar()

if __name__ == "__main__":
    main()
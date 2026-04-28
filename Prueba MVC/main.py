from view import Vista
from controller import Controlador

if __name__ == "__main__":
    #  Configuración inicial: Se crea una instancia del controlador y la vista, y se inicia la aplicación.
    controlador = Controlador(None)
    #  La vista necesita una referencia al controlador para poder llamar a sus métodos, por lo que se le pasa el controlador al crear la vista.
    vista = Vista(controlador)
    # El controlador también necesita una referencia a la vista para actualizarla, por lo que se le asigna la vista al controlador después de crearla.
    controlador.vista = vista
    #  Iniciar la aplicación mostrando la ventana.
    vista.iniciar()

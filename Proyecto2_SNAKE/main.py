from model.model import SnakeModel
from view.view import SnakeView
from controller.controller import SnakeController

# Punto de entrada del juego
if __name__ == "__main__":
    # Crear la vista con el tamaño de pantalla y el tamaño de celda definido por defecto
    view = SnakeView()

    # Crear el modelo usando las dimensiones de la vista
    model = SnakeModel(view.width, view.height, view.cell_size)

    # Crear el controlador que conecta la vista y el modelo
    controller = SnakeController(view, model)

    # Ejecutar el bucle principal del juego
    controller.run()

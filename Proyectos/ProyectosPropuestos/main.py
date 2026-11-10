import flet as ft
from view import View
from controller import Controller
from model import Model

def main(page: ft.Page):
    # Inicializamos los componentes del MVC
    modelo = Model()
    vista = View(page)  # Le pasamos la página de Flet a la vista
    controlador = Controller(vista, modelo)

if __name__ == "__main__":
    main()
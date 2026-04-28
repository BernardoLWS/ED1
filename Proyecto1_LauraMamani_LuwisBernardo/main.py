from view.view import AgendaView
from model.model import AgendaModel
from controller.controller import AgendaController


if __name__ == "__main__":
    vista = AgendaView()
    modelo = AgendaModel()
    controlador = AgendaController(vista, modelo)
    vista.iniciar()
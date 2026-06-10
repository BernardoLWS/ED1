from model.model import SnakeModel
from view.view import SnakeView
from controller.controller import SnakeController

if __name__ == "__main__":
    view = SnakeView()
    model = SnakeModel(view.width , view.height, view.cell_size)
    controller = SnakeController(view,model)
    controller.run()

from model.model import SnakeModel
from view.view import SnakeView
from controller.controller import SnakeController

if __name__ == "__main__":
    view = SnakeView()
    model = SnakeModel()
    controller = SnakeController(view,model)
    controller.run()

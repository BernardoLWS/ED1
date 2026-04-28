from model import Usuario
#   Controlador: Gestiona la lógica de la aplicación y la comunicación entre el modelo y la vista.
class Controlador:
    def __init__(self, vista):
        self.vista = vista
        self.usuario = None
#   Método para guardar un usuario, crea una instancia del modelo y actualiza la vista con un mensaje.
    def guardar_usuario(self, nombre):
        self.usuario = Usuario(nombre)
        self.vista.mostrar_mensaje(f"Usuario guardado: {self.usuario.nombre}")

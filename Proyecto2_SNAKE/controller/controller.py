import pygame

class SnakeController:
    def __init__(self,view,model):
        self.view = view
        self.model = model
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():    # devuelve los eventos 
            if event.type == pygame.QUIT:   # pregunta si el evento x fue presionado
                self.running = False        # si es asi deja de correr
            elif event.type == pygame.KEYDOWN:  # eventos de las teclas
                if event.key == pygame.K_UP:    # presiona flecha arriba ?
                    if not self.model.direction == (0, self.model.cell_size): 
                        self.model.direction = (0, -self.model.cell_size)   # apunta arriba
                elif event.key == pygame.K_DOWN:    # preciona flecha abajo ?
                    if not self.model.direction == (0, -self.model.cell_size): 
                        self.model.direction = (0, self.model.cell_size)    # apunta abajo
                elif event.key == pygame.K_LEFT:    # preciona flecha izq ?
                    if not self.model.direction == (self.model.cell_size, 0):
                        self.model.direction = (-self.model.cell_size, 0)   # apunta a la izquierda
                elif event.key == pygame.K_RIGHT:   # preciona flecha der ?
                    if not self.model.direction == (-self.model.cell_size, 0):
                        self.model.direction = (self.model.cell_size, 0)    # apunta a la derecha

    def run(self):
        while self.running:
            self.handle_events()  # manejar eventos

            # mover primero
            if not self.model.move():   # si move devuelve False -> colisión
                self.running = False
            else:
                # dibujar después de mover
                self.view.draw(self.model.snake, self.model.apple)

            self.view.tick()  # velocidad del juego
        self.view.game_over()    
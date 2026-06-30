import pygame

class SnakeController:
    """Controlador principal que coordina entradas, modelo y vista."""

    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.running = True

    def handle_events(self):
        """Procesa los eventos de pygame y actualiza la dirección de la serpiente."""
        for event in pygame.event.get():
            # Si el jugador cierra la ventana, detenemos el bucle principal
            if event.type == pygame.QUIT:
                self.running = False

            # Si el jugador presiona una tecla, cambiamos la dirección
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    # Evitar que la serpiente se mueva en dirección opuesta inmediata
                    if self.model.direction != (0, self.model.cell_size):
                        self.model.direction = (0, -self.model.cell_size)
                elif event.key == pygame.K_DOWN:
                    if self.model.direction != (0, -self.model.cell_size):
                        self.model.direction = (0, self.model.cell_size)
                elif event.key == pygame.K_LEFT:
                    if self.model.direction != (self.model.cell_size, 0):
                        self.model.direction = (-self.model.cell_size, 0)
                elif event.key == pygame.K_RIGHT:
                    if self.model.direction != (-self.model.cell_size, 0):
                        self.model.direction = (self.model.cell_size, 0)

    def run(self):
        """Bucle principal del juego: eventos, movimiento, dibujo y control de velocidad."""
        while self.running:
            self.handle_events()

            # Mover la serpiente y comprobar si la partida continúa
            if not self.model.move():
                self.running = False
            else:
                # Si no hay colisión, dibujar el nuevo estado en pantalla
                self.view.draw(self.model.snake, self.model.apple, self.model.score)

            # Controlar los fotogramas por segundo
            self.view.tick()

        # Cuando el juego termina, mostrar pantalla de fin de juego
        self.view.game_over()

   
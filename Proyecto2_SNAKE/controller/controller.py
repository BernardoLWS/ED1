import pygame

class SnakeController:
    """Controlador principal que coordina entradas, modelo y vista."""

    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.running = True
        self.enemy_move_counter = 0
        self.enemy_move_interval = 2  # La serpiente enemiga se moverá cada 2 fotogramas

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
            self.handle_events() # Procesa los eventos de entrada del jugador

            if not self.model.move():
                self.running = False
            else:
                self.enemy_move_counter += 1  # Incrementa el contador de movimiento de la serpiente enemiga
                if self.enemy_move_counter >= self.enemy_move_interval: # Si ha pasado el intervalo definido, mueve la serpiente enemiga
                    self.model.move_enemy() # Mueve la serpiente enemiga hacia la manzana
                    self.enemy_move_counter = 0 # Reinicia el contador de movimiento de la serpiente enemiga

                if self.model.enemy_hits_player():
                    self.running = False
                else:
                    self.view.draw(
                        self.model.snake,
                        self.model.apple,
                        self.model.score,
                        self.model.enemy_snake,
                    )

            self.view.tick()

        self.view.game_over()

   
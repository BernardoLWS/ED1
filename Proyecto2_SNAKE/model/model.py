import random

class SnakeModel:
    """Modelo de datos del juego Snake: posición de la serpiente, manzana y puntuación."""

    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Lista de segmentos de la serpiente. El primer elemento es la cabeza.
        self.snake = [(100, 100), (80, 100), (60, 100)]

        # Dirección actual de movimiento en píxeles: (dx, dy)
        self.direction = (self.cell_size, 0)

        # Generar la primera manzana y establecer la puntuación inicial
        self.spawn_apple()
        self.score = 0

    def move(self):
        """Avanza la serpiente y devuelve False si hay colisión."""
        head_x, head_y = self.snake[0]
        self.new_head = (head_x + self.direction[0], head_y + self.direction[1])

        # Insertar la nueva cabeza al frente de la lista
        self.snake.insert(0, self.new_head)

        # Si la cabeza está en la manzana, sumar puntos y generar una nueva manzana
        if self.new_head == self.apple:
            self.spawn_apple()
            self.score += 1
        else:
            # Si no come, quitar el último segmento para simular el movimiento
            self.snake.pop()

        # Comprobar si la nueva posición provoca colisión
        if self.collision():
            return False
        return True

    def collision(self) -> bool:
        """Detecta colisión contra paredes o contra el propio cuerpo."""
        x, y = self.new_head

        # Colisión con los bordes de la ventana
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return True

        # Colisión con el cuerpo de la serpiente
        if self.new_head in self.snake[1:]:
            return True

        return False

    def spawn_apple(self):
        """Coloca la manzana en una posición aleatoria que no está ocupada por la serpiente."""
        while True:
            apple_x = random.randint(0, (self.width // self.cell_size) - 1) * self.cell_size
            apple_y = random.randint(0, (self.height // self.cell_size) - 1) * self.cell_size
            new_apple = (apple_x, apple_y)

            # Repetir hasta encontrar una posición libre
            if new_apple not in self.snake:
                self.apple = new_apple
                break
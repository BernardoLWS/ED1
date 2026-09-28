import random

class SnakeModel:
    """Modelo de datos del juego Snake: posición de la serpiente, manzana y puntuación."""

    DIRECTIONS = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
    ]

    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Lista de segmentos de la serpiente principal. El primer elemento es la cabeza.
        self.snake = [(100, 100), (80, 100), (60, 100)]   # cabeza, cuerpo, cola
        self.direction = (self.cell_size, 0)

        # Generar la serpiente enemiga y la primera manzana
        self.spawn_enemy()
        self.spawn_apple()
        self.score = 0

    def move(self):
        """Avanza la serpiente del jugador y devuelve False si hay colisión."""
        head_x, head_y = self.snake[0]
        self.new_head = (head_x + self.direction[0], head_y + self.direction[1])

        self.snake.insert(0, self.new_head)

        if self.new_head == self.apple:
            self.spawn_apple()
            self.score += 1
        else:
            self.snake.pop()

        if self.collision():
            return False
        return True

    def move_enemy(self):
        """Mueve a la serpiente enemiga hacia la manzana, escogiendo una dirección válida."""
        head_x, head_y = self.enemy_snake[0]
        apple_x, apple_y = self.apple
        opposite_dir = (-self.enemy_direction[0], -self.enemy_direction[1])

        valid_directions = []
        for direction in self.DIRECTIONS:
            if direction == opposite_dir:
                continue
            new_head = (head_x + direction[0] * self.cell_size, head_y + direction[1] * self.cell_size)
            if self.is_inside(new_head) and new_head not in self.enemy_snake and new_head not in self.snake:
                valid_directions.append(direction)

        if not valid_directions:
            for direction in self.DIRECTIONS:
                new_head = (head_x + direction[0] * self.cell_size, head_y + direction[1] * self.cell_size)
                if self.is_inside(new_head) and new_head not in self.enemy_snake and new_head not in self.snake:
                    valid_directions.append(direction)

        if not valid_directions:
            return

        def apple_distance(direction): 
            new_head = (head_x + direction[0] * self.cell_size, head_y + direction[1] * self.cell_size)
            return abs(new_head[0] - apple_x) + abs(new_head[1] - apple_y)

        best_distance = min(apple_distance(direction) for direction in valid_directions)
        best_choices = [direction for direction in valid_directions if apple_distance(direction) == best_distance]
        chosen = random.choice(best_choices)

        self.enemy_direction = chosen
        new_head = (head_x + chosen[0] * self.cell_size, head_y + chosen[1] * self.cell_size)
        self.enemy_snake.insert(0, new_head)

        if new_head == self.apple:
            self.spawn_apple()
        else:
            self.enemy_snake.pop()

    def collision(self) -> bool:
        """Detecta colisión contra paredes, el propio cuerpo o la serpiente enemiga."""
        x, y = self.new_head

        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return True

        if self.new_head in self.snake[1:]:
            return True

        if hasattr(self, 'enemy_snake') and self.new_head in self.enemy_snake:
            return True

        return False

    def player_hits_enemy(self) -> bool:
        """Comprueba si la cabeza del jugador impacta a cualquier segmento enemigo."""
        return self.new_head in self.enemy_snake

    def enemy_hits_player(self) -> bool:
        """Comprueba si la cabeza enemiga impacta a la serpiente del jugador."""
        return self.enemy_snake[0] in self.snake

    def spawn_enemy(self):
        """Coloca la serpiente enemiga en una posición aleatoria sin colisión con el jugador."""
        while True:
            head = self.random_grid_position(exclude=set(self.snake))
            direction = random.choice(self.DIRECTIONS)

            body = (head[0] - direction[0] * self.cell_size, head[1] - direction[1] * self.cell_size)
            tail = (body[0] - direction[0] * self.cell_size, body[1] - direction[1] * self.cell_size)

            if self.is_inside(body) and self.is_inside(tail) and body not in self.snake and tail not in self.snake:
                self.enemy_snake = [head, body, tail]
                self.enemy_direction = direction
                break

    def random_grid_position(self, exclude=None):
        if exclude is None:
            exclude = set()

        while True:
            apple_x = random.randint(0, (self.width // self.cell_size) - 1) * self.cell_size
            apple_y = random.randint(0, (self.height // self.cell_size) - 1) * self.cell_size
            position = (apple_x, apple_y)
            if position not in exclude:
                return position

    def is_inside(self, position):
        x, y = position
        return 0 <= x < self.width and 0 <= y < self.height

    def spawn_apple(self):
        """Coloca la manzana en una posición aleatoria que no está ocupada por ninguna serpiente."""
        exclude_positions = set(self.snake)
        if hasattr(self, 'enemy_snake'):
            exclude_positions.update(self.enemy_snake)

        while True:
            apple_x = random.randint(0, (self.width // self.cell_size) - 1) * self.cell_size
            apple_y = random.randint(0, (self.height // self.cell_size) - 1) * self.cell_size
            new_apple = (apple_x, apple_y)

            if new_apple not in exclude_positions:
                self.apple = new_apple
                break
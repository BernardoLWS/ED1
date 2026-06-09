import random

class SnakeModel:
    def __init__(self):
        self.width = 600
        self.height = 400
        self.cell_size = 20
        self.snake = [(100, 100), (80, 100), (60, 100)]     # cabeza, cuerpo, cola
        self.direction = (self.cell_size, 0)                # dirección inicial (x, y)
        self.spawn_apple()

    def move(self):
        head_x, head_y = self.snake[0]
        self.new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.snake.insert(0, self.new_head)

        # Comer manzana
        if self.new_head == self.apple:
            self.spawn_apple()   # genera nueva manzana
        else:
            self.snake.pop()     # si no comió, se mueve normal

        # Verificar colisión
        if self.collition():
            return False
        return True

    def collition(self) -> bool:
        x, y = self.new_head
        #  Colisión con bordes
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return True
        #  Colisión con el propio cuerpo
        if self.new_head in self.snake[1:]:
            return True
        return False
    
    def spawn_apple(self):
        apple_x = random.randint(0, (self.width // self.cell_size) - 1) * self.cell_size
        apple_y = random.randint(0, (self.height // self.cell_size) - 1) * self.cell_size
        self.apple = (apple_x, apple_y)

    def score(self,c=0):
        if self.snake[0] == self.apple:
            c += 1
        return c   
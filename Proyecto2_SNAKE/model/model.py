import random

class SnakeModel:
    def __init__(self,width,height,cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.snake = [(100, 100), (80, 100), (60, 100)]     # cabeza, cuerpo, cola
        self.direction = (self.cell_size, 0)                # dirección inicial (x, y)
        self.spawn_apple()
        self.score = 0

    def move(self):
        head_x, head_y = self.snake[0]
        self.new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.snake.insert(0, self.new_head)
        # Comer manzana
        if self.new_head == self.apple:
            self.spawn_apple()   # genera nueva manzana
            self.score += 1
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
        while True:
            apple_x = random.randint(0, (self.width // self.cell_size) - 1) * self.cell_size
            apple_y = random.randint(0, (self.height // self.cell_size) - 1) * self.cell_size
            new_apple = (apple_x, apple_y)
            if new_apple not in self.snake:
                self.apple = new_apple
                break
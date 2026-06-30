import pygame
import time

class SnakeView:
    """Responsable de dibujar el juego y mostrar la interfaz visual."""

    def __init__(self, width=800, height=600, cell_size=20):
        pygame.init()
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Configurar la pantalla de pygame
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Snake")

        # Colores para el fondo, la serpiente, la manzana y los paneles
        self.BACKGROUND = (15, 15, 60)  # (rojo,verde,azul) colores primarios en escala de 0-255
        self.GRID_COLOR = (30, 30, 80)
        self.SNAKE_COLOR = (102, 255, 102)
        self.SNAKE_BORDER = (0, 120, 0)
        self.APPLE_COLOR = (255, 80, 80)
        self.INFO_BG = (10, 10, 30)
        self.INFO_TEXT = (240, 240, 180)
        self.BORDER_COLOR = (70, 130, 180)

        # Reloj para controlar la velocidad de actualización
        self.clock = pygame.time.Clock()

        # Tiempo de inicio para mostrar el contador de juego
        self.start_time = time.time()

        # Fuente para los textos del juego
        self.font_small = pygame.font.SysFont("Arial", 18)
        self.font_large = pygame.font.SysFont("Arial", 42)

    def draw(self, snake, apple, score):
        """Dibuja la serpiente, la manzana y la información de juego en pantalla."""
        self.draw_background()
        self.draw_border()
        self.draw_snake(snake)
        self.draw_apple(apple)
        self.show_info(score)
        pygame.display.flip() # actualiza la pantalla con todo lo dibujado

    def draw_background(self):
        """Dibuja el fondo con un relleno oscuro y un patrón de cuadrícula sutil."""
        self.screen.fill(self.BACKGROUND)

        # Cuadrícula sutil para dar profundidad al campo de juego
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, self.GRID_COLOR, (x, 0), (x, self.height), 1)
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, self.GRID_COLOR, (0, y), (self.width, y), 1)

    def draw_border(self):
        """Dibuja un borde visible alrededor del área de juego."""
        pygame.draw.rect(self.screen, self.BORDER_COLOR, (0, 0, self.width, self.height), 4)

    def draw_snake(self, snake):
        """Dibuja cada segmento de la serpiente con un borde y relleno brillantes."""
        for segment in snake:
            segment_rect = pygame.Rect(segment[0], segment[1], self.cell_size, self.cell_size)
            pygame.draw.rect(self.screen, self.SNAKE_BORDER, segment_rect)
            inner_rect = segment_rect.inflate(-4, -4)
            pygame.draw.rect(self.screen, self.SNAKE_COLOR, inner_rect)

    def draw_apple(self, apple):
        """Dibuja la manzana con un estilo más atractivo y brillante."""
        apple_rect = pygame.Rect(apple[0], apple[1], self.cell_size, self.cell_size) 
        pygame.draw.rect(self.screen, self.APPLE_COLOR, apple_rect, border_radius=6)
        highlight = apple_rect.inflate(-8, -8)
        pygame.draw.rect(self.screen, (255, 160, 160), highlight, border_radius=4)

    def game_over(self):
        """Muestra el mensaje de fin de juego durante unos segundos."""
        overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        self.screen.blit(overlay, (0, 0))

        text = self.font_large.render("GAME OVER", True, self.APPLE_COLOR)
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2 - 20))
        self.screen.blit(text, text_rect)

        subtext = self.font_small.render("Gracias por jugar. Cierra la ventana para salir.", True, self.INFO_TEXT)
        subtext_rect = subtext.get_rect(center=(self.width // 2, self.height // 2 + 30))
        self.screen.blit(subtext, subtext_rect)

        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.quit()

    def show_info(self, score):
        """Dibuja la puntuación, tiempo y título del juego en la parte superior."""
        game_time = int(time.time() - self.start_time)
        header = self.font_small.render("SNAKE", True, self.INFO_TEXT)
        header_rect = header.get_rect(topleft=(16, 12))

        info_text = self.font_small.render(
            f"Score: {score:03d}   Time: {game_time:03d}", True, self.INFO_TEXT
        )
        info_rect = info_text.get_rect(topleft=(16, 36))

        panel = pygame.Rect(8, 8, 260, 60)
        pygame.draw.rect(self.screen, self.INFO_BG, panel, border_radius=10)
        pygame.draw.rect(self.screen, self.BORDER_COLOR, panel, 2, border_radius=10)

        self.screen.blit(header, header_rect)
        self.screen.blit(info_text, info_rect)

    def tick(self, fps=10):
        """Mantiene una velocidad constante de fotogramas por segundo."""
        self.clock.tick(fps)

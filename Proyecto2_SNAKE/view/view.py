import pygame
import time

class SnakeView:
    def __init__(self,width = 800,height = 600,cell_size = 20):
        pygame.init()   # inicializa pygame
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.screen = pygame.display.set_mode((width, height))  # dimension de la pantalla
        pygame.display.set_caption("Snake MVC")   # titulo del juego 
        self.BLACK = (0,0,0)    # color(rojo, verde, azul)
        self.GREEN = (0,255,0)  # limite de color 8 bits
        self.clock = pygame.time.Clock()    # inicializa el tiempo de ejecucion  
        self.start_time = time.time()

    def draw(self, snake , apple,score):
        self.screen.fill(self.BLACK)    # limpia la pantalla y con color negro
        for segment in snake:   # recorrido de la lista snake
            pygame.draw.rect(self.screen, self.GREEN, (segment[0], segment[1], self.cell_size, self.cell_size)) # dibuja el rectangulo de ña snake
         # Dibujar manzana
        pygame.draw.rect(self.screen, (255, 0, 0), (apple[0],apple[1], self.cell_size, self.cell_size))
        self.show_info(score)
        pygame.display.flip()   # actualiza la pantalla

    def game_over(self):
        font = pygame.font.SysFont("Arial", 50)
        text = font.render("GAME OVER", True, (255, 0, 0))
        text_rect = text.get_rect(center=(self.width // 2,self.height // 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(2000)  # espera 2 segundos
        pygame.quit()

    def show_info(self, score):
        game_time = int(time.time() - self.start_time)
        font = pygame.font.SysFont("Arial", 20)
        text = font.render(f"Tiempo: {game_time:03d}      Score: {score:03d}", True, (255, 255, 0))
        text_rect = text.get_rect(topleft=(10,580))
        self.screen.blit(text, text_rect)
       
    def tick(self, fps=10):
        self.clock.tick(fps)    # velocidad establicada de el snake
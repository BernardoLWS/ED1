import pygame

class SnakeView:
    def __init__(self):
        pygame.init()   # inicializa pygame
        width , height = 600 , 400
        self.cell_size = 20
        self.screen = pygame.display.set_mode((width, height))  # dimension de la pantalla
        pygame.display.set_caption("Snake MVC")   # titulo del juego 
        self.BLACK = (0,0,0)    # color(rojo, verde, azul)
        self.GREEN = (0,255,0)  # limite de color 8 bits
        self.clock = pygame.time.Clock()    # inicializa el tiempo de ejecucion  


    def draw(self, snake , apple):
        self.screen.fill(self.BLACK)    # limpia la pantalla y con color negro
        for segment in snake:   # recorrido de la lista snake
            pygame.draw.rect(self.screen, self.GREEN, (segment[0], segment[1], self.cell_size, self.cell_size)) # dibuja el rectangulo de ña snake
         # Dibujar manzana
        pygame.draw.rect(self.screen, (255, 0, 0), (apple[0],apple[1], self.cell_size, self.cell_size))
        pygame.display.flip()   # actualiza la pantalla

    def game_over(self):
        font = pygame.font.SysFont("Arial", 50)
        text = font.render("GAME OVER", True, (255, 0, 0))
        text_rect = text.get_rect(center=(600 // 2, 400 // 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(2000)  # espera 2 segundos
        pygame.quit()

    def tick(self, fps=10):
        self.clock.tick(fps)    # velocidad establicada de el snake
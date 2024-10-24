from constants import * 
import pygame

class Board:
    def __init__(self, surface):
        self.surface = surface

    def drawBoard(self):
        self.surface.fill(WHITE)
        for i in range(10):
            if i % 3 == 0:
                pygame.draw.rect(self.surface, BLACK, pygame.Rect(i*(WIDTH/9), 0, 10, 800))
                pygame.draw.rect(self.surface, BLACK, pygame.Rect(0, i*(HEIGHT/9), 800, 10))
            else:
                pygame.draw.rect(self.surface, BLACK, pygame.Rect(i*(WIDTH/9), 0, 5, 800))
                pygame.draw.rect(self.surface, BLACK, pygame.Rect(0, (i*(HEIGHT/9)), 800, 5))


if __name__ == "__main__":
    surface = pygame.display.set_mode((WIDTH, HEIGHT)) 
    running = True
    board = Board(surface) 
    board.drawBoard()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        pygame.display.update()

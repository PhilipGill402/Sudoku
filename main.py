import pygame
from constants import *
from board import *

pygame.init()

surface = pygame.display.set_mode((REAL_WIDTH, REAL_HEIGHT))
running = True
board = Board(surface)
game = Game()

while running:
    
    board.drawBoard()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()
    pygame.display.update()

pygame.quit()

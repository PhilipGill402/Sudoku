import pygame
from constants import *
from board import *

def getPos(x, y):
    return (x//SQUARE_SIZE, y//SQUARE_SIZE)

pygame.init()

surface = pygame.display.set_mode((REAL_WIDTH, REAL_HEIGHT))
running = True
board = Board(surface)
game = Game()
board = [
    [0,0,0,2,6,0,7,0,1],
    [6,8,0,0,7,0,0,9,0],
    [1,9,0,0,0,4,5,0,0],
    [8,2,0,1,0,0,0,4,0],
    [0,0,4,6,0,2,9,0,0],
    [0,5,0,0,0,3,0,2,8],
    [0,0,9,3,0,0,0,7,4],
    [0,4,0,0,5,0,0,3,6],
    [7,0,3,0,1,8,0,0,0]]

while running:
    
    board.drawBoard()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()
    pygame.display.update()

pygame.quit()

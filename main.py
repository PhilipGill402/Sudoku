import pygame
from constants import *
from board import *
from game import *

pygame.init()

surface = pygame.display.set_mode((REAL_WIDTH, REAL_HEIGHT))
running = True
GameBoard = Board(surface)
game = Game(surface)
board = GameBoard.board 

while running:
    
    GameBoard.drawBoard()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = game.getPos(pygame.mouse.get_pos())
            game.selectPos(pos, board) 
            print(pos);

    if game.selected: 
        game.highlightSelected()
    pygame.display.flip()
    pygame.display.update()

pygame.quit()

import pygame
from constants import *
from board import *
from game import *

pygame.init()

surface = pygame.display.set_mode((WIDTH, HEIGHT))
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

        elif event.type == pygame.KEYDOWN and game.selected is not None:
            x, y = game.getPos(pygame.mouse.get_pos())
            if event.key == pygame.K_1:
                board[y][x] = Cell(1)
            elif event.key == pygame.K_2:
                board[y][x] = Cell(2)
            elif event.key == pygame.K_3:
                board[y][x] = Cell(3)
            elif event.key == pygame.K_4:
                board[y][x] = Cell(4)
            elif event.key == pygame.K_5:
                board[y][x] = Cell(5)
            elif event.key == pygame.K_6:
                board[y][x] = Cell(6)
            elif event.key == pygame.K_7:
                board[y][x] = Cell(7)
            elif event.key == pygame.K_8:
                board[y][x] = Cell(8)
            elif event.key == pygame.K_9:
                board[y][x] = Cell(9)

    if game.selected is not None: 
        game.highlightSelected(pos, board)
    pygame.display.flip()
    pygame.display.update()

pygame.quit()

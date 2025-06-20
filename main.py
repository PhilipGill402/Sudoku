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

def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j].value, end=", ")
        print()

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
                val = 1
            elif event.key == pygame.K_2:
                val = 2
            elif event.key == pygame.K_3:
                val = 3
            elif event.key == pygame.K_4:
                val = 4
            elif event.key == pygame.K_5:
                val = 5
            elif event.key == pygame.K_6:
                val = 6
            elif event.key == pygame.K_7:
                val = 7
            elif event.key == pygame.K_8:
                val = 8
            elif event.key == pygame.K_9:
                val = 9
            elif event.key == pygame.K_BACKSPACE:
                val = 0
            else:
                continue
            if GameBoard.solvedBoard[y][x].value == val:
                board[y][x] = Cell(val)
            else:
                board[y][x] = Cell(val, RED)

    if game.selected is not None: 
        game.highlightSelected(pos, board)
    pygame.display.flip()
    pygame.display.update()

pygame.quit()

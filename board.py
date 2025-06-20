import pygame
import random
import copy
from constants import *
from cell import *

class Board:
    def __init__(self, surface):
        self.surface = surface
        self.board = self.createBoard()
        self.solvedBoard = self.solve(self.board)
        while self.solvedBoard is None:
            self.solvedBoard = self.solve(self.board)
        
        pygame.font.init()
        self.font = pygame.font.Font("font.ttf", 32)
        
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board[i][j].reduceEntropy(self.board, (j, i))

    def createBoard(self):
        board = [
                [Cell(),Cell(),Cell(),Cell(2),Cell(6),Cell(),Cell(7),Cell(),Cell(1)],
                [Cell(6),Cell(8),Cell(),Cell(),Cell(7),Cell(),Cell(),Cell(9),Cell()],
                [Cell(1),Cell(9),Cell(),Cell(),Cell(),Cell(4),Cell(5),Cell(),Cell()],
                [Cell(8),Cell(2),Cell(),Cell(1),Cell(),Cell(),Cell(),Cell(4),Cell()],
                [Cell(),Cell(),Cell(4),Cell(6),Cell(),Cell(2),Cell(9),Cell(),Cell()],
                [Cell(),Cell(5),Cell(),Cell(),Cell(),Cell(3),Cell(),Cell(2),Cell(8)],
                [Cell(),Cell(),Cell(9),Cell(3),Cell(),Cell(),Cell(),Cell(7),Cell(4)],
                [Cell(),Cell(4),Cell(),Cell(),Cell(5),Cell(),Cell(),Cell(3),Cell(6)],
                [Cell(7),Cell(),Cell(3),Cell(),Cell(1),Cell(8),Cell(),Cell(),Cell()]] 
        """
        board = [] 

        for i in range(9):
            board.append([])
            for j in range(9):
                board[i].append(0)
        """  
        return board

    def drawBoard(self):
        self.surface.fill(BLACK)
        for i in range(9):
            for j in range(9):
                rect = pygame.draw.rect(self.surface, WHITE, pygame.Rect(i * SQUARE_SIZE, j * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 5)
                if self.board[j][i].value != 0:
                    num = self.board[j][i].value
                    text = self.font.render(str(num), True, self.board[j][i].color)
                    textRect = text.get_rect()
                    textRect.center = (i * SQUARE_SIZE + (SQUARE_SIZE//2), j * SQUARE_SIZE + (SQUARE_SIZE//2))
                    self.surface.blit(text, textRect)

    def drawSolvedBoard(self):
        self.surface.fill(BLACK)
        for i in range(9):
            for j in range(9):
                rect = pygame.draw.rect(self.surface, WHITE, pygame.Rect(i * SQUARE_SIZE, j * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 5)
                if self.solvedBoard[j][i].value != 0:
                    num = self.solvedBoard[j][i].value
                    text = self.font.render(str(num), True, WHITE)
                    textRect = text.get_rect()
                    textRect.center = (i * SQUARE_SIZE + (SQUARE_SIZE//2), j * SQUARE_SIZE + (SQUARE_SIZE//2))
                    self.surface.blit(text, textRect)
                    
    def findLowestEntropy(self, board):
        lowestEntropy = []
        lowestNum = 10 #its 10 because none can have more than 9 options (1-9)
        for i in range(len(board)):
            for j in range(len(board[i])):
                cell = board[i][j]
                if len(cell.options) < lowestNum and not cell.collapsed:
                    lowestEntropy = [(j, i)]
                    lowestNum = len(cell.options)
                elif len(cell.options) == lowestNum and not cell.collapsed:
                    lowestEntropy.append((j, i))
                    
        return lowestEntropy

    def isSolved(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j].value == 0:
                    return False

        return True

    def solve(self, board):
        newBoard = copy.deepcopy(self.board)
        #finds the entropy of all cells
        for i in range(len(newBoard)):
            for j in range(len(newBoard[i])):
                newBoard[i][j].reduceEntropy(newBoard, (j, i))
                
        while not self.isSolved(newBoard):
            #choose one cell
            lowestEntropy = self.findLowestEntropy(newBoard)
            idx = random.randint(0, len(lowestEntropy) - 1)
            x,y = lowestEntropy[idx]
            chosenCell = newBoard[y][x]

            #we reached a deadend
            if len(chosenCell.options) == 0:
                return newBoard
            
            #collapse the cell
            idx = random.randint(0, len(chosenCell.options) - 1)
            chosenCell.value = chosenCell.options[idx]
            chosenCell.options = [chosenCell.value]
            chosenCell.collapsed = True

            #calculate entropy of other cells
            for i in range(len(newBoard)):
                for j in range(len(newBoard[i])):
                    newBoard[i][j].reduceEntropy(newBoard, (j, i))

        return newBoard

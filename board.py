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
                self.board[j][i].reduceEntropy(self.board, (i, j))

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
                    text = self.font.render(str(num), True, WHITE)
                    textRect = text.get_rect()
                    textRect.center = (i * SQUARE_SIZE + (SQUARE_SIZE//2), j * SQUARE_SIZE + (SQUARE_SIZE//2))
                    self.surface.blit(text, textRect)

    def findLowestEntropy(self, board):
        lowestEntropy = []
        lowestNum = 10 #its 10 because none can have more than 9 options (1-9)
        for i in range(len(board)):
            for j in range(len(board[i])):
                cell = board[j][i]
                if len(cell.options) < lowestNum and cell.value == 0:
                    lowestEntropy = [(i, j)]
                    lowestNum = len(cell.options)
                elif len(cell.options) == lowestNum:
                    lowestEntropy.append((i, j))
                    
        return lowestEntropy

    def isValid(self, board, num, pos):
        row = board[pos[1]]
        col = []
        box = []
        box.append(pos[0]//3)
        box.append(pos[1]//3)

        for i in range(box[0] * 3, box[0] * 3 + 3):
            for j in range(box[1] * 3, box[1] * 3 + 3):
                if board[j][i].value == num:
                    return False

        for i in board:
            col.append(i[pos[0]])

        for i in row:
            if i.value == num:
                return False
        for i in col:
            if i.value == num:
                return False
        return True

    def isSolved(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j].value == 0:
                    return False

        return True

    def solve(self, board):
        newBoard = copy.deepcopy(self.board)
        while not self.isSolved(newBoard):
            #choose one cell
            lowestEntropy = self.findLowestEntropy(newBoard)
            idx = random.randint(0, len(lowestEntropy) - 1)
            x,y = lowestEntropy[idx]
            chosenCell = newBoard[y][x]

            #we reached a deadend
            if len(chosenCell.options) == 0:
                return None
            
            #collapse the cell
            idx = random.randint(0, len(chosenCell.options) - 1)
            chosenCell.value = chosenCell.options[idx]
            chosenCell.options = [chosenCell.value]

            #calculate entropy of other cells
            for i in range(len(newBoard)):
                for j in range(len(newBoard[i])):
                    newBoard[i][j].reduceEntropy(newBoard, (i, j))

        return newBoard

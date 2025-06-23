import pygame
import random
import copy
from constants import *
from cell import *

class Board:
    def __init__(self, surface):
        self.surface = surface
        self.board = self.loadBoard()          
        self.solvedBoard = self.solve(self.board)
        while not self.isSolved(self.solvedBoard):
            self.solvedBoard = self.solve(self.board)
        
        pygame.font.init()
        self.font = pygame.font.Font("font.ttf", 32)
        
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board[i][j].reduceEntropy(self.board, (j, i))

    def loadBoard(self):
        board = []
        #opens prebuilt boards
        with open("boards.txt") as f:
            #choose a random line 
            lines = f.readlines()
            numLines = len(lines) 
            idx = random.randint(1, numLines//10) - 1
            
            #find all lines in this board and add them to the board 
            for i, line in enumerate(lines):
                if i >= (idx*10) and i < (idx*10) + 9:
                    line = line.rstrip()
                    line = list(line)
                    line = [Cell(int(c)) for c in line] 
                    board.append(line) 
                elif i >= (idx*10) + 9:
                    break
                
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
        #draw borders
        top = pygame.draw.rect(self.surface, GREY, pygame.Rect(0, 0, WIDTH - 6, 5))
        right = pygame.draw.rect(self.surface, GREY, pygame.Rect(WIDTH - 11, 0, 5, HEIGHT - 6))
        left = pygame.draw.rect(self.surface, GREY, pygame.Rect(0, 0, 5, HEIGHT - 6))
        down = pygame.draw.rect(self.surface, GREY, pygame.Rect(0, HEIGHT - 11, WIDTH - 6, 5))
        first = pygame.draw.rect(self.surface, GREY, pygame.Rect((SQUARE_SIZE * 3) - 5, 0, 10, HEIGHT - 6))
        second = pygame.draw.rect(self.surface, GREY, pygame.Rect((SQUARE_SIZE * 6) - 5, 0, 10, HEIGHT - 6))
        topFirst = pygame.draw.rect(self.surface, GREY, pygame.Rect(0, (SQUARE_SIZE * 3) - 5, WIDTH - 6, 10))
        topSecond = pygame.draw.rect(self.surface, GREY, pygame.Rect(0, (SQUARE_SIZE * 6) - 5, WIDTH - 6, 10))

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

    def isUniqueSolution(self, board:int, threshold:int=5) -> bool:
        sol = self.solve(board) 
        while not self.isSolved(sol): 
            sol = self.solve(board)

        copyBoard = copy.deepcopy(board) 
        #iterates over board 
        for i in range(len(copyBoard)):
            for j in range(len(copyBoard[i])):
                cell = copyBoard[i][j]
                #if the cell is empty then try all possible numbers 
                if cell.value == 0:
                    #try all possible numbers
                    for k in range(9):
                        cell.value = k
                        #loops a certain number of times to find a new solution
                        for n in range(threshold):
                            newSol = self.solve(copyBoard)
                            #if there is a new solution and it differs from the original solution then return false
                            if self.isSolved(newSol) and sol == newSol:
                                return False
                        #reset the cell value to its original value
                        cell.value = Cell()

        return True 

    def solve(self, board):
        newBoard = copy.deepcopy(board)
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

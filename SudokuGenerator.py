import random
import copy
from constants import *
from cell import *

class SudokuGenerator:
    def createBoard(self, clues: int) -> list[list[Cell]]:
        #generates a solved full board   
        board = [] 

        for i in range(9):
            board.append([])
            for j in range(9):
                board[i].append(Cell())
        
        while not self.isSolved(board): 
            board = [] 

            for i in range(9):
                board.append([])
                for j in range(9):
                    board[i].append(Cell())

            board = self.solve(board)

        #generates the holes
        holes = 0
        targetHoles = 81 - clues

        while holes < targetHoles:
            #finds a random cell and sets it to zero 
            idx = random.randint(0, 80)
            x = idx // 9
            y = idx % 9
            cell = board[y][x]
            board[y][x] = Cell()    

            #checks if its a unique solution
            if self.isUniqueSolution(board):
                holes += 1
            else:
                board[y][x] = cell


        
        return board

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

if __name__ == "__main__":
    generator = SudokuGenerator()

    #creates i number of boards and puts them in the boards.txt file for later access
    for i in range(5):
        board = generator.createBoard(40)
        with open("boards.txt", "a") as f:
            for i in range(len(board)):
                for j in range(len(board[i])):
                    cell = board[i][j]
                    if j != 8:
                        f.write(f"{cell.value}")
                    else:
                        f.write(f"{cell.value}\n")
            
            f.write("\n")
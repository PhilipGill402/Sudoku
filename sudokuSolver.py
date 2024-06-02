import numpy as np
import re

board = np.array([
[0,4,0,0,0,0,0,2,0],
[0,0,2,3,7,0,0,0,6],
[0,0,0,8,0,0,0,0,0],
[5,0,0,0,0,0,1,0,0],
[0,0,4,2,6,0,0,0,3],
[0,0,0,0,0,9,0,0,0],
[0,0,0,0,0,4,0,0,9],
[0,0,7,0,0,8,0,0,0],
[0,1,0,7,9,0,3,0,0]])

def printBoard (board):
    row = 0
    column = 0
    printedBoard = []
    for i in range(81):
        if (i) % 9 == 0 and i != 0:
            row += 1
            column = 0
        printedBoard.append(board[row, column])
        column += 1
    for i in range(9):
        if i != 9:
            first = i * 9
            print(str(printedBoard[first]) + str(printedBoard[first+1]) + str(printedBoard[first+2]) + '|' + str(printedBoard[first+3]) + str(printedBoard[first+4]) + str(printedBoard[first+5]) + '|' + str(printedBoard[first+6]) + str(printedBoard[first+7]) + str(printedBoard[first+8]))
        if (i+1) % 3 == 0:
            print('---+---+---')

def findEmptySpace(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i,j] == 0:
                return (i, j)
    return False

def isValid(board, num, pos):
    row = board[pos[0]]
    col = []
    box = []
    box.append(pos[0]//3)
    box.append(pos[1]//3)

    for i in range(box[0] * 3, box[0] * 3 + 3):
        for j in range(box[1] * 3, box[1] * 3 + 3):
            if board[i,j] == num:
                return False

    for i in board:
        col.append(i[pos[1]])

    for i in row:
        if i == num:
            return False
    for i in col:
        if i == num:
            return False
    return True

def solve (board):
    if not findEmptySpace(board):
        return True
    zero = findEmptySpace(board)
    row = zero[0]
    col = zero[1]
    for i in range(1,10):
        if isValid(board, i, zero):
            board[row, col] = i
            if solve(board):
                return True
            
            board[row, col] = 0
    return False

printBoard(board)
solve(board)
print('\n')
printBoard(board)
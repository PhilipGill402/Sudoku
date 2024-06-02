import numpy as np
import re

board = np.array([
[0,0,0,2,6,0,7,0,1],
[6,8,0,0,7,0,0,9,0],
[1,9,0,0,0,4,5,0,0],
[8,2,0,1,0,0,0,4,0],
[0,0,4,6,0,2,9,0,0],
[0,5,0,0,0,3,0,2,8],
[0,0,9,3,0,0,0,7,4],
[0,4,0,0,5,0,0,3,6],
[7,0,3,0,1,8,0,0,0]])

solved = np.array([
[4,3,5,2,6,9,7,8,1],
[6,8,2,5,7,1,4,9,3],
[1,9,7,8,3,4,5,6,2],
[8,2,6,1,9,5,3,4,7],
[3,7,4,6,8,2,9,1,5],
[9,5,1,7,4,3,6,2,8],
[5,1,9,3,2,6,8,7,4],
[2,4,8,9,5,7,1,3,6],
[7,6,3,4,1,8,2,5,9],
])

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
            print('------------')


def play():
    while not np.array_equal(board, solved):
        printBoard(board)
        guess = str(input("Enter your guess: "))
        if guess == 'quit':
            break
        splitGuess = re.split(' ', guess)
        coordinates = splitGuess[0]
        row = int(coordinates[1])
        column = int(coordinates[3])
        num = int(splitGuess[1])

        if board[row, column] != 0:
            while board[row, column] != 0:
                print("There is already a number here, please guess again")
                guess = str(input("Enter your guess: "))
                splitGuess = re.split(' ', guess)
                coordinates = splitGuess[0]
                row = int(coordinates[1])
                column = int(coordinates[3])
                num = int(splitGuess[1])

        if solved[row, column] == num:
            board[row, column] = num
            print('Correct!\n')
        else:
            print("That guess was incorrect\n")

    print('Congratulations you solved the board!')


import numpy as np

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

choice = str(input('Do you want to play sudoku or have a bot solve it [p,s]: '))

'''
if choice == 'p':
    sudoku.play()
elif choice == 's':
    sudokuSolver.solve(board)
    sudokuSolver.printBoard(board)
'''

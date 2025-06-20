from constants import *

class Cell:
    def __init__(self, value=0, color=WHITE):
        self.options = [1,2,3,4,5,6,7,8,9]
        self.collapsed = False
        self.value = value
        self.color = color
        if self.value != 0:
            self.options = [self.value]
            self.collapsed = True

    def isValid(self, board, num, pos):
        row = board[pos[1]]
        col = []
        box = []
        box.append(pos[0]//3)
        box.append(pos[1]//3)
        for i in range(box[1] * 3, box[1] * 3 + 3):
            for j in range(box[0] * 3, box[0] * 3 + 3):
                if (i, j) != (pos[0], pos[1]) and board[i][j].value == num:
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

    def reduceEntropy(self, board, pos):
        self.options = []
        if self.value != 0:
            self.options = [self.value]
            return
        for i in range(1,10):
            if self.isValid(board, i, pos):
                self.options.append(i)

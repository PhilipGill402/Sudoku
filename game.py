import pygame
from constants import GREY, SQUARE_SIZE

class Game():

    def __init__ (self, surface):
        self.surface = surface
        self.selected = None        
    
    def getPos(self, pos):
        return (pos[0]//SQUARE_SIZE, pos[1]//SQUARE_SIZE)

    def selectPos(self, pos, board):
        self.selected = board[pos[1]][pos[0]]

        return self.selected

    def highlightSelected(self, pos, board):
        num = board[pos[1]][pos[0]]
        (x, y) = self.getPos(pos) 

        if num == 0:
           pygame.draw.rect(self.surface, GREY, pygame.Rect(x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)) 

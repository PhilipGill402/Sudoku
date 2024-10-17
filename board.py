from constants import * 
import pygame

class Board:
    def __init__(self, surface):
        self.surface = surface

    def drawBoard(self):
        self.surface.fill(WHITE)
        for i in range(10):
            if i % 3 == 0:
                pygame.draw.rect(self.surface, BLACK, pygame.Rect((i*(WIDTH/9), 0), (10, 800)))
            else:
                pygame.draw.rect(self.surface, BLACK, pygame.Rect((i*(WIDTH/9), 0), (5, 800)))

from constants import * 
import pygame

class Board:
    def __init__(self, surface):
        self.surface = surface
        self.board = self.createBoard()
        pygame.font.init()
        self.font = pygame.font.Font("font.ttf", 32)

    def createBoard(self):
        board = [
                [0,0,0,2,6,0,7,0,1],
                [6,8,0,0,7,0,0,9,0],
                [1,9,0,0,0,4,5,0,0],
                [8,2,0,1,0,0,0,4,0],
                [0,0,4,6,0,2,9,0,0],
                [0,5,0,0,0,3,0,2,8],
                [0,0,9,3,0,0,0,7,4],
                [0,4,0,0,5,0,0,3,6],
                [7,0,3,0,1,8,0,0,0]] 
        """
        board = [] 

        for i in range(9):
            board.append([])
            for j in range(9):
                board[i].append(0)
        """  
        return board

    def drawBoard(self):
        self.surface.fill(WHITE)
        y = 0 
        for i in range(13):
            x = 0 
            for j in range(13):
                print(f"(j,i): {(j, i)}")
                print(f"(x,y): {(x, y)}") 
                
                if i % 4 == 0:
                     if j % 4 == 0:
                        pygame.draw.rect(self.surface, BLACK, pygame.Rect(x, y, 10, 10))
                        x += 10
                     else:
                        pygame.draw.rect(self.surface, BLACK, pygame.Rect(x, y, 75, 10))
                        x += 75 
                else:
                    if j % 4 == 0:
                        pygame.draw.rect(self.surface, BLACK, pygame.Rect(x, y, 10, 75))
                        x += 10 
                    else:
                        pygame.draw.rect(self.surface, WHITE, pygame.Rect(x, y, 75, 75))
                        x += 75

            if i % 4 == 0:
                y += 10
            else:
                y += 75

        for i in range(9):
            for j in range(9):
                if self.board[j][i] != 0: 
                    num = self.board[j][i]
                    text = self.font.render(str(num), True, BLACK)
                    textRect = text.get_rect()
                    textRect.center = (i * SQUARE_SIZE + (SQUARE_SIZE//2), j * SQUARE_SIZE + (SQUARE_SIZE//2))
                    self.surface.blit(text, textRect)

if __name__ == "__main__":
    surface = pygame.display.set_mode((REAL_WIDTH, REAL_HEIGHT)) 
    running = True
    board = Board(surface) 
    board.drawBoard()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        pygame.display.update()

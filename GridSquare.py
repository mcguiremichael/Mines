import pygame
import Button



"""
The values of a square correspond as following.
    0:  No mines surrounding and it is not a mine
    1:  One mine surrounding
    2:  "
    3:  "
    4:  "
    5:  "
    6:  "
    7:  "
    8:  "
    9:  It is a mine
    
clicked:
    True if the square has been clicked, and is being revealed. False otherwise.
    
flagged:
    True if the square has been flagged and has not been revealed. False otherwise.
    
hovering:
    True if the mouse has been clicked down, and has not been released, and the mouse is above the current square. False otherwise.

"""
class GridSquare(Button.Button):

    COLOR1 = (100, 100, 255)
    COLOR2 = (0, 255, 0)
    COLOR3 = (255, 0, 0)
    COLOR4 = (0, 0, 130)
    COLOR5 = (130, 0, 0)
    COLOR6 = (0, 150, 150)
    COLOR7 = (0, 0, 0)
    COLOR8 = (100, 100, 100)
    BLACK = (0, 0, 0) 

    def __init__(self, x, y, width, offColor, onColor, surface, value, clicked, flagged, hovering):
        Button.Button.__init__(self, x, y, width, width, offColor, onColor, surface)
        self.value = value
        self.clicked = clicked
        self.flagged = flagged
        self.hovering = hovering
            
    def drawOne(self):
        self.drawClicked()
        pygame.draw.rect(self.surface, GridSquare.COLOR1, (self.x + 1, self.y + 1, self.width - 2, self.width - 2))
        
    def drawTwo(self):
        self.drawClicked()
        pygame.draw.rect(self.surface, GridSquare.COLOR2, (self.x + 1, self.y + 1, self.width - 2, self.width - 2))
        
    def drawThree(self):
        self.drawClicked()
        pygame.draw.rect(self.surface, GridSquare.COLOR3, (self.x + 1, self.y + 1, self.width - 2, self.width - 2))
        
    def drawFour(self):
        self.drawClicked()
        pygame.draw.rect(self.surface, GridSquare.COLOR4, (self.x + 1, self.y + 1, self.width - 2, self.width - 2))
        
    def drawFive(self):
        self.drawClicked()
        pygame.draw.rect(self.surface, GridSquare.COLOR5, (self.x + 1, self.y + 1, self.width - 2, self.width - 2))
    
    def drawSix(self):
        self.drawClicked()
        pygame.draw.rect(self.surface, GridSquare.COLOR6, (self.x + 1, self.y + 1, self.width - 2, self.width - 2))
        
    def drawSeven(self):
        self.drawClicked()
        pygame.draw.rect(self.surface, GridSquare.COLOR7, (self.x + 1, self.y + 1, self.width - 2, self.width - 2))
        
    def drawEight(self):
        self.drawClicked()
        pygame.draw.rect(self.surface, GridSquare.COLOR8, (self.x + 1, self.y + 1, self.width - 2, self.width - 2))
    
    def drawMine(self):
        self.drawClicked()
        pygame.draw.rect(self.surface, GridSquare.BLACK, (self.x + 1, self.y + 1, self.width - 2, self.width - 2))
    
    def drawFlag(self):
        self.drawClicked()
        pygame.draw.rect(self.surface, GridSquare.COLOR1, (self.x + 1, self.y + 1, self.width - 2, self.width - 2))
        
    def drawWrongChoice(self):
        pygame.draw.rect(self.surface, GridSquare.Color1, (self.x + 1, self.y + 1, self.width - 2, self.width - 2))
        
    def drawSquare(self):
        val = self.value
        if (self.clicked == False and self.hovering == True):
            self.drawClicked()
        elif self.clicked == False:
            self.drawUnclicked()
        elif val == 0:
            self.drawClicked()
        elif val == 1:
            self.drawOne()
        elif val == 2:
            self.drawTwo()
        elif val == 3:
            self.drawThree()
        elif val == 4:
            self.drawFour()
        elif val == 5:
            self.drawFive()
        elif val == 6:
            self.drawSix()
        elif val == 7:
            self.drawSeven()
        elif val == 8:
            self.drawEight()
        elif val == 9:
            self.drawMine()
    
    def setClicked(self, isClicked):
        self.clicked = isClicked
    
    def setFlagged(self, isFlagged):
        self.flagged = isFlagged
        
    def setHovering(self, isHovering):
        self.hovering = isHovering
    


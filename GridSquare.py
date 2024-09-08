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

    RED = (255, 0, 0)
    COLOR1 = (100, 100, 255)
    COLOR2 = (0, 255, 0)
    COLOR3 = (255, 0, 0)
    COLOR4 = (0, 0, 130)
    COLOR5 = (130, 0, 0)
    COLOR6 = (0, 150, 150)
    COLOR7 = (0, 0, 0)
    COLOR8 = (100, 100, 100)
    BLACK = (0, 0, 0) 
    FLAGCOLOR = (200, 0, 0)
    
    colors = [COLOR1, COLOR2, COLOR3, COLOR4, COLOR5, COLOR6, COLOR7, COLOR8]

    def __init__(self, x, y, width, offColor, onColor, surface, value, clicked, flagged, hovering):
        Button.Button.__init__(self, x, y, width, width, offColor, onColor, surface)
        self.value = value
        self.clicked = clicked
        self.flagged = flagged
        self.hovering = hovering
        self.font = pygame.font.Font(None, int(self.width * 1.5))
        
    def adjustedX(self):
        return self.x + self.width / 4
    
    def adjustedY(self):
        return self.y + self.height / 20
        
    def drawNumber(self):
        number = self.value
        if (number < 1 or number > 8):
            return
        self.drawClicked()
        self.drawText(str(number), GridSquare.colors[number-1])
    
    def drawMine(self):
        self.drawClicked()
        pygame.draw.circle(self.surface, GridSquare.BLACK, (self.x + self.width / 2, self.y + self.height / 2), self.width / 3)
    
    def drawFlag(self):
        self.drawClicked()
        pygame.draw.rect(self.surface, GridSquare.FLAGCOLOR, (self.x + 1, self.y + 1, self.width - 2, self.width - 2))
        
    def drawWrongChoice(self):
        self.drawMine()
        pygame.draw.line(self.surface, GridSquare.RED, (int(self.x + self.width // 8), int(self.y + self.height // 8)), (int(self.x + (self.width * 7 // 8)), int(self.y + (self.height * 7 // 8))), int(self.width // 8))
        pygame.draw.line(self.surface, GridSquare.RED, (int(self.x + self.width // 8), int(self.y + self.height * 7 / 8)), (int(self.x + (self.width * 7 // 8)), int(self.y + self.width // 8)), int(self.width // 8))
        
    def drawSquare(self):
        val = self.value
        if (val == 10):
            self.drawWrongChoice()
        elif (self.flagged == True):
            self.drawFlag()
        elif (self.clicked == False and self.hovering == True):
            self.drawClicked()
        elif self.clicked == False:
            self.drawUnclicked()
        elif val == 0:
            self.drawClicked()
        elif val == 9:
            self.drawMine()
        else:
            self.drawNumber()
            
    def drawText(self, text, color):
        t = self.font.render(text, True, color)
        self.surface.blit(t, (self.adjustedX(), self.adjustedY()))
    
    def setClicked(self, isClicked):
        self.clicked = isClicked
    
    def setFlagged(self, isFlagged):
        self.flagged = isFlagged
        
    def setHovering(self, isHovering):
        self.hovering = isHovering
        
    def isMine(self):
        return self.value == 9
    


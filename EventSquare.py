import pygame
import Button

class EventSquare(Button.Button):

    Margin = (0, 0, 0)
    
    def __init__(self, x, y, width, offColor, onColor, clicked, surface):
        Button.Button.__init__(self, x, y, width, width, offColor, onColor, surface)
        self.upperX = x + width
        self.upperY = y + width
        self.borderMargin = 1
        self.clicked = False
        
    def drawMargin(self):
        pygame.draw.rect(self.surface, EventSquare.Margin, (self.x - 1, self.y - 1, self.width + 2, self.width + 2))
        
    def drawUnclickedWithMargin(self):
        self.drawMargin()
        self.drawUnclicked()
        
    def drawClickedWithMargin(self):
        self.drawMargin()
        self.drawClicked()
        
    def drawSquare(self):
        if (self.clicked == True):
            self.drawClickedWithMargin()
        else:
            self.drawUnclickedWithMargin()
        

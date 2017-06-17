import pygame

class Button:
    
    def __init__(self, x, y, width, height, offColor, onColor, surface):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.offColor = offColor
        self.onColor = onColor
        self.surface = surface
        
    def drawUnclicked(self):
        pygame.draw.rect(self.surface, self.offColor, (self.x, self.y, self.width, self.height))
        
    def drawClicked(self):
        pygame.draw.rect(self.surface, self.onColor, (self.x, self.y, self.width, self.height))

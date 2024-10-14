# Square class

import pygame
import random

# Set up the colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Square():

    def __init__(self, window, maxWidth, maxHeight):
        self.window = window
        self.widthAndHeight = random.randrange(10, 100)
        self.color = random.choice((RED, GREEN, BLUE))
        self.x = random.randrange(1, maxWidth - 100)
        self.y = random.randrange(25, maxHeight - 100)
        self.rect = pygame.Rect(self.x, self.y, self.widthAndHeight,
                                            self.widthAndHeight)
        self.shapeType = 'Square'

    def __eq__(self, o_other_square):
        if not isinstance(o_other_square, Square):
            raise TypeError('Second object was not a Square')
        if self.widthAndHeight == o_other_square.widthAndHeight:
            return True  # сопоставимо
        else:
            return False  # не сопоставимо
        
    def clickedInside(self, mousePoint):
        clicked = self.rect.collidepoint(mousePoint)
        return clicked

    def getType(self):
        return self.shapeType
    
    def getArea(self):
        theArea = self.widthAndHeight * self.widthAndHeight
        return theArea

    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.widthAndHeight, self.widthAndHeight))

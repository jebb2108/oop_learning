# класс Rectangle
import pygame
import random

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Rectangle:
    def __init__(self, window):
        self.window = window
        self.width = random.choice((20, 30, 40))
        self.height = random.choice((20, 30, 40))
        self.color = random.choice((RED, GREEN, BLUE))
        self.x = random.randrange(0, 400)
        self.y = random.randrange(0, 400)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.area = self.width * self.height

    def clicked_inside(self, mouse_point):
        clicked = self.rect.collidepoint(mouse_point)
        return clicked

    # Вызываем машический метод, когда сравнивается
    # два объекта Rectangle с помошью оператора ==
    def __eq__(self, o_other_rectangle):
        if not isinstance(o_other_rectangle, Rectangle):
            raise TypeError('Second object was not a Rectangle')
        if self.area == o_other_rectangle.area:
            return True
        else:
            return False

    # Вызываем магический метод, когда сравнивается
    # два объекта Rectangle с помошью оператора <
    def __lt__(self, o_other_rectangle):
        if not isinstance(o_other_rectangle, Rectangle):
            raise TypeError('Second object was not a Rectangle')
        if self.area < o_other_rectangle.area:
            return True
        else:
            return False

    # Вызываем магический метод, когда сравнивается
    # два объекта Rectangle с помошью оператора >
    def __gt__(self, o_other_rectangle):
        if not isinstance(o_other_rectangle, Rectangle):
            raise TypeError('Second object was not a Rectangle')
        if self.area > o_other_rectangle.area:
            return True
        else:
            return False

    def get_area(self):
        return self.area

    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.x, self.y,
                                                   self.width, self.height))
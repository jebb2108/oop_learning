# Класс Triangle

import pygame
import random
from shape_basic import *

class Triangle(Shape):
    def __init__(self, window, max_width, max_height):
        super().__init__(window, 'Triangle', max_width, max_height)
        self.width = random.randrange(10, 100)
        self.height = random.randrange(10, 100)
        self.triangle_slope = -1 * (self.height / self.width)
        self.rect = pygame.Rect(self.x, self.y, self.width,
                                self.height)

    def clicked_inside(self, mouse_point):
        in_rect = self.rect.collidepoint(mouse_point)
        if not in_rect:
            return False

        # выполняем некоторые вычисления, чтобы увидеть,
        # находится ли точка внутрр треугольника
        x_offset = mouse_point[0] - self.x
        y_offset = mouse_point[1] - self.y
        if x_offset == 0:
            return True

        point_slope_from_y_intercept = (y_offset - self.height) / x_offset
        if point_slope_from_y_intercept < self.triangle_slope:
            return True
        else:
            return False

    def get_area(self):
        the_area = .5 * self.width * self.height
        return the_area

    def draw(self):
        pygame.draw.polygon(self.window, self.color,
                            ((self.x, self.y + self.height),
                             (self.x, self.y),
                             (self.x + self.width, self.y)))
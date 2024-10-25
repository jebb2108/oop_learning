# Класс Shape

# Должен использоваться как базовый класс для других классов

import random
from abc import ABC, abstractmethod

from pygame.examples.multiplayer_joystick import colors

# Настраиваем цвета
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Shape(ABC):
    def __init__(self, window, shape_type, max_width, max_height):
        self.window = window
        self.shape_type = shape_type
        self.color = random.choice((RED, GREEN, BLUE))
        self.x = random.randrange(1, max_width - 100)
        self.y = random.randrange(1, max_height - 100)

    def get_type(self):
        return self.shape_type

    @abstractmethod
    def clicked_inside(self, mouse_point):
        raise NotImplementedError

    @abstractmethod
    def get_area(self):
        raise NotImplementedError

    @abstractmethod
    def draw(self):
        raise NotImplementedError

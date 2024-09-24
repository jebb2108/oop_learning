# класс SimpleText

import pygame
from pygame.locals import *


class SimpleText:

    def __init__(self, window, loc, value, text_color):
        pygame.font.init()
        self.window = window
        self.loc = loc
        self.font = pygame.font.SysFont(None, 30)
        self.text_color = text_color
        self.text = None  # так что вызов set_value ниже
                          # приведет к созданию изображения текста

        self.set_value(value)  # Настраиваем исходный текст для
                               # отображения

    def set_value(self, new_text):
        if self.text == new_text:
            return None
        self.text = new_text
        self.text_surface = self.font.render(self.text, True,  # noqa
                                             self.text_color)

    def draw(self):
        self.window.blit(self.text_surface, self.loc)

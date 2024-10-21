# Класс InputNumber - разрешает пользователю вводить только числа
from multiprocessing.managers import Value

# Демонстрация наследования

import pygame
from pygame.locals import *
import pygwidgets

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# кортеж допустимых клавиш редактирования
LEGAl_KEYS_TUPLE = (pygame.K_RIGHT, pygame.K_LEFT, pygame.K_HOME,
                    pygame.K_END, pygame.K_DELETE, pygame.K_BACKSPACE,
                    pygame.K_RETURN, pygame.K_KP_ENTER)

# допустимые клавиши для ввода
LEGAL_UNICODE_CHARS = ('0123456789.-')

# InputNumber наследует от InputText

class InputNumber(pygwidgets.InputText):
    def __init__(self, window, loc, value='', fontName=None,
                 fontSize=24, width=200, textColor=BLACK,
                 backgroundColor=WHITE, focusColor=BLACK,
                 initialFocus=False, nickName=None, callback=None,
                 mask=None, keepFocusOnSubmit=False,
                 allowFloatingNumber=True, allowNegativeNumber=True):
        self.allow_floating_number = allowFloatingNumber
        self.allow_negative_number = allowNegativeNumber

        # вызывает метод __init__ базового класса
        super().__init__(window, loc, value, fontName, fontSize, width,
                         textColor, backgroundColor, focusColor, initialFocus,
                         nickName, callback, mask, keepFocusOnSubmit)

    # переопределяет handleEvent, чтобы фильтровать подходящие клавиши
    def handleEvent(self, event):
        if (event.type == pygame.KEYDOWN):
            # Если эта не клавиша редактирования или числовая клавиша,
            # игнорируем ее Значение юникода присутсвует только при нажатии клавиши
            # вниз
            allowable_key = (event.key in LEGAl_KEYS_TUPLE) or (event.unicode in LEGAL_UNICODE_CHARS)

            if not allowable_key:
                return False

            if event.unicode == '-':  # пользователь ввел знак минус
                if not self.allow_negative_number:
                    # Если нет отрицательных величин, не надо передавать
                    return False
                if self.cursorPosition > 0:
                    return False  # нельзя поместить знак минус после 1 символа

                if '-' in self.text:
                    return False  # нельзя ввести второй знак минус
                return True

            if event.unicode == '.':
                if not self.allow_floating_number:
                    # Если нет плавающих точек, не не предаем точку
                    return False
                if '.' in self.text:
                    return False  # нельзя ввести вторую точку
                return True

        # разрешаем клавише перейти к базовому классу
        result = super().handleEvent(event)
        return result

    def get_value(self):
        userString = super().getValue()
        try:
            if self.allow_floating_number:
                returnValue = float(userString)
            else:
                returnValue = int(userString)

        except ValueError:
            raise ValueError('Entry is not a number, needs to have at '
                             'least one digit')
        return returnValue

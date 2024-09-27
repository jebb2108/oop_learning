# pygame демо 9 - 3-кнопочный тест с обратными вызовами

import pygame
from pygame.locals import *
from simple_button import *
import sys

GRAY = (200, 200, 200)
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 100
FRAMES_PER_SECOND = 30


# определяем функцию, которую необходимо использовать в качестве
# "обратного вызова"
def my_call_back_function():
    print('User pressed button B, called my_call_back_function')


class CallBackTest():
    def my_method(self):
        print('User pressed ButtonC, called myMethod of the '
              'CallBackTest object')

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

o_callback_test = CallBackTest()
# создаем экземпляры SimpleButton
# Нет обратного вызова
o_button_a = SimpleButton(window, (25, 30),
                          'images/buttonAUp.png',
                          'images/buttonADown.png')
o_button_b = SimpleButton(window, (150, 30),
                          'images/buttonBUp.png',
                          'images/buttonBDown.png', callback=my_call_back_function)
o_button_c = SimpleButton(window, (275, 30),
                          'images/buttonCUp.png',
                          'images/buttonCDown.png', callback=o_callback_test.my_method)

counter = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # передаем событие кнопке, смотрим была ли она нажата
        if o_button_a.handle_event(event):
            print('User pressed button A, handled in the main loop')

        # У o_button_b и o_button_c есть обратные вызовы,
        # не нужно проверять результаты этих вызовов
        o_button_b.handle_event(event)

        o_button_c.handle_event()

        counter += 1

        window.fill(GRAY)

        o_button_a.draw()
        o_button_b.draw()
        o_button_c.draw()

        pygame.display.update()

        clock.tick(FRAMES_PER_SECOND)
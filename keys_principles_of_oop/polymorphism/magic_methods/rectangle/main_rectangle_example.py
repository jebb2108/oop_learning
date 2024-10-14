from curses.textpad import rectangle

import pygame
import sys
from pygame.locals import *
from rectangle import *

# Настраиваем константы
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_RECTANGLES = 10
FIRST_RECTANGLE = 'first'
SECOND_RECTANGLE = 'second'

# Настраиваем окно
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

rectangles_list = []
for i in range(0, N_RECTANGLES):
    o_rectangle = Rectangle(window)
    rectangles_list.append(o_rectangle)

which_rectangle = FIRST_RECTANGLE

# Основной цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == MOUSEBUTTONDOWN:
            for o_rectangle in rectangles_list:
                if o_rectangle.clicked_inside(event.pos):
                    print('Clicked on', which_rectangle, 'rectangle')

                    if which_rectangle == FIRST_RECTANGLE:
                        o_first_rectangle = o_rectangle
                        which_rectangle = SECOND_RECTANGLE

                    elif which_rectangle == SECOND_RECTANGLE:
                        o_second_rectangle2 = o_rectangle
                        # Пользователь выбрал 2 прямоугольника,
                        # сравниваем их
                        if o_first_rectangle == o_second_rectangle2:
                            print('Rectangles are the same size')

                        elif o_first_rectangle < o_second_rectangle2:
                            print('First rectangle is smaller than'
                                  ' second rectangle')
                        else:  # должен быть больше
                            print('First rectangle is larger than'
                                  ' second rectangle')
                        which_rectangle = FIRST_RECTANGLE

    # Очищаем и рисуем все прямоугольники
    window.fill(WHITE)
    for o_rectangle in rectangles_list:
        o_rectangle.draw()

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)
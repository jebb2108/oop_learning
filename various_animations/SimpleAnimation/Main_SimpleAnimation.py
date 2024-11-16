# пример анимации
# демонстрируется пример объекта SimpleAnimation

# 1 - Импортируем библиотеку
import pygame
from pygame.locals import *
import sys

import pygwidgets
from SimpleAnimation import SimpleAnimation

# 2 - Определяем константы
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BGCOLOR = (0, 128, 128)

# 3 - Инициализируем окружение pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Загружаем элементы: изображения, звуки, etc.
dinosaur_image_tuple = ('images/Dinobike/f1.gif',
                        'images/Dinobike/f2.gif',
                        'images/Dinobike/f3.gif',
                        'images/Dinobike/f4.gif',
                        'images/Dinobike/f5.gif',
                        'images/Dinobike/f6.gif',
                        'images/Dinobike/f7.gif',
                        'images/Dinobike/f8.gif',
                        'images/Dinobike/f9.gif',
                        'images/Dinobike/f10.gif')

# 5 - Инициализируем переменные
o_dinosaur_animation = SimpleAnimation(window, (22, 140),
                                       dinosaur_image_tuple, .1)

o_play_button = pygwidgets.TextButton(window, (20, 240), "Play")

# 6 - Бесконечный цикл
while True:

    # 7 - Проверяем наличие событий и обрабатываем их
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if o_play_button.handleEvent(event):
            o_dinosaur_animation.play()
            print("Animation started")

    # 8 - Выполняем действия в "рамках фрейма"
    o_dinosaur_animation.update()

    # 9 - Очищаем окно, прежде чем рисовать его заново
    window.fill(BGCOLOR)

    # 10 - Нарисовать все элементы экрана
    o_dinosaur_animation.draw()
    o_play_button.draw()

    # 11 - Обновляем окно
    pygame.display.update()

    # 12 - Делаем паузу
    clock.tick(FRAMES_PER_SECOND)

# Демонстрируя пример объекта SimpleSpriteSheetAnimation

# 1 - Импортируем библиотеку
import pygame
from pygame.locals import *
import sys

import pygwidgets
from SimpleSpriteSheetAnimation import SimpleSpriteSheetAnimation

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

# 5 - Инициализируем переменные
o_water_animation = SimpleSpriteSheetAnimation(window, (22, 140),
                                       'images/water_003.png',
                                               50, 192, 192, .05)

o_play_button = pygwidgets.TextButton(window, (60, 320), "Play")

# 6 - Бесконечный цикл
while True:

    # 7 - Проверяем наличие событий и обрабатываем их
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if o_play_button.handleEvent(event):
            o_water_animation.play()
            print("Animation started")

    # 8 - Выполняем действия в "рамках фрейма"
    o_water_animation.update()

    # 9 - Очищаем окно, прежде чем рисовать его заново
    window.fill(BGCOLOR)

    # 10 - Нарисовать все элементы экрана
    o_water_animation.draw()
    o_play_button.draw()

    # 11 - Обновляем окно
    pygame.display.update()

    # 12 - Делаем паузу
    clock.tick(FRAMES_PER_SECOND)

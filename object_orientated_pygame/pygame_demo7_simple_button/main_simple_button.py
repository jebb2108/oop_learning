# pygame демо 7 - тест SimpleButton

# 1 - Импортируем пакеты
import pygame
from pygame.locals import *
import sys
import random

from simple_button import *

# 2 - Определяем константы
GRAY = (150, 150, 150)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# 3 - Инициализируем окружение pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Загружаем элементы: изображения, звуки и т.д.

# 5 - Инициализируем переменные
# создаем экземпляр SimpleButton
o_button = SimpleButton(window, (150, 30),
                        'images/buttonUp.png',
                        'images/buttonDown.png')

# 6 - Бесконечный цикл
while True:

    # 7 - Проверяем наличие событий и обрабатываем их
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # передаем событие кнопке
        if o_button.handle_event(event):
            print('User has clicked the button')
    # 8 - Выполняем действия 'в рамках фрейма'

    # 9 - Очищаем окно
    window.fill(GRAY)

    # 10 - Рисуем все элементы окна
    o_button.draw()

    # 11 - Обновляем окно
    pygame.display.update()

    # 12 - Делаем паузу
    clock.tick(FRAMES_PER_SECOND)
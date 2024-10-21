# Денежный пример

# Демонстрирует переопределение унаследованных методов DisplayText
# и InputText

# 1 - Импортируем пакеты
import pygame
import pygame
from pygame.locals import *
import sys
import pygwidgets
from display_money import *
from input_number import *

# 2 - Опрделяем константы
BLACK = (0, 0, 0)
BLACKISH = (10, 10, 10)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
BACKGROUND_COLOR = (0, 180, 180)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# 3 - Инициализируем окружение pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

#4 Загружаем элементы: изображения, звуки и т.д.

# 5 - Инициализируем переменные
title = pygwidgets.DisplayText(window, (0, 40),
                               'Demo of InputNumber and DisplayMoney'
                               ' fields', fontSize=36, width=WINDOW_WIDTH, justified='center')

input_caption = pygwidgets.DisplayText(window, (20, 150),
                                       'Input money amount:', fontSize=24,
                                       width=190, justified='right')
input_field = InputNumber(window, (230, 150), '', width=150)
ok_button = pygwidgets.TextButton(window, (430, 150), 'OK')

output_caption1 = pygwidgets.DisplayText(window, (20, 300),
                                         'Output dollars & cents: ', fontSize=24,
                                         width=190, justified='right')
money_field1 = DisplayMoney(window, (230, 300), '', textColor=BLACK,
                            backgroundColor=WHITE, width=150)

output_caption2 = pygwidgets.DisplayText(window, (20, 400), 'Output dollars: ', fontSize=24,
                                         width=190, justified='right')

money_field2 = DisplayMoney(window, (230, 400), '', textColor=BLACK,
                            backgroundColor=WHITE, width=150,
                            showCents=False)
# 6 - Бесконечный цикл
while True:

    # 7 - проверяем наличие событий и обрабатываем их
    for event in pygame.event.get():
        # Если событием был щелчок по кнопке закрытия, выходим
        # из pygame и программы
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # нажатие Return/Enter  или щелчок по ОК приводит к действию
        if input_field.handleEvent(event) or ok_button.handleEvent(event):
            try:
                the_value = input_field.getValue()
            except ValueError:  # любая оставшаяся ошибка
                input_field.setValue('(not a number)')
            else:
                the_text = str(the_value)
                money_field1.setValue(the_text)
                money_field2.setValue(the_text)

    # 8 - Выполняем действия "в рамках фрейма"

    # 9 - Очищаем окно
    window.fill(BACKGROUND_COLOR)

    # 10 - Рисуем все элементы окна
    title.draw()
    input_caption.draw()
    input_field.draw()
    ok_button.draw()
    output_caption1.draw()
    money_field1.draw()
    output_caption2.draw()
    money_field2.draw()

    # 11 - Обновляем окно
    pygame.display.update()

    # 12 - Делаем паузу
    clock.tick(FRAMES_PER_SECOND)


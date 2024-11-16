# Пример простого таймера

# 1 - Испорт пакетов
import pygame
from pygame.locals import *
import sys
import pygwidgets
import pyghelpers

# 2 - Определяем константы
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 240
WHITE = (255, 255, 255)
FRAMES_PER_SECOND = 30
TIMER_LENGTH = 2.5  # seconds

# 3 - Инициализируем окружение
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Загружаем данные: изображения, звуки, etc.

# 5 - Инициализируем переменные
header_message = pygwidgets.DisplayText(window, (0, 50), 'Click "Start" to start a ' +
                                       str(TIMER_LENGTH) + ' second timer:',
                                       fontSize=36, justified='center', width=WINDOW_WIDTH)

start_button = pygwidgets.TextButton(window, (200, 100), 'Start')

click_me_button = pygwidgets.TextButton(window, (320, 100), 'Click Me')

timer_message = pygwidgets.DisplayText(window, (0, 160), 'Message showing during timer',
                                      fontSize=36, justified='center', width=WINDOW_WIDTH)

o_timer = pyghelpers.Timer(TIMER_LENGTH)

# 6 - Бесконечный цикл
while True:

    # 7 - Проверяем наличие событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if start_button.handleEvent(event):
            o_timer.start()
            start_button.disable()
            timer_message.show()
            print('Starting timer')

        if click_me_button.handleEvent(event):
            print('Other button was clicked')

    # 8 - Вызываем действия в "рамках фрейма"
    if o_timer.update():
        start_button.enable()
        timer_message.hide()
        print('Timer ended')

    # 9 - Очистить экран
    window.fill(WHITE)

    # 10 - Нарисовать все элементы экрана
    header_message.draw()
    start_button.draw()
    click_me_button.draw()
    timer_message.draw()

    # 11 - Обновить экран
    pygame.display.update()

    # 12 - Делаем паузу
    clock.tick(FRAMES_PER_SECOND)
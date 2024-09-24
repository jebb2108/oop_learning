# pygame демо 8 - SimpleText, SimpleButton и Ball

# 1 - Импортируем пакеты
import pygame
from pygame.locals import *
import sys
import random
from ball import *
from simple_text import *
from simple_button import *

# 2 - Определяем константы
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# 3 - Инициализируем окружение pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Загружаем элементы: изображения, звуки и т.д.

# 5 - Инициализируем переменные
o_ball = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
o_frame_count_label = SimpleText(window, (60, 20),
                                 'Program has run through this many loops: ', WHITE,)
o_frame_count_display = SimpleText(window, (500, 20), '', WHITE)
o_restart_button = SimpleButton(window, (280, 60),
                                'images/restartUp.png', 'images/restartDown.png')

frame_counter = 0

# 6 - Бесконечный цикл
while True:

    # 7 - Проверяем наличие событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if o_restart_button.handle_event(event):
            frame_counter = 0

    # 8 - Выполняем действия в рамках фрейма
    o_ball.update()
    frame_counter = frame_counter + 1
    o_frame_count_display.set_value(str(frame_counter))

    # 9 - Очищаем окно, прежде чем рисовать его заново
    window.fill(BLACK)

    # 10 - Рисуем все элементы окна
    o_ball.draw()
    o_frame_count_label.draw()
    o_frame_count_display.draw()
    o_restart_button.draw()

    # 11- Обновляем окно
    pygame.display.update()

    # 12 - Делаем паузу
    clock.tick(FRAMES_PER_SECOND)

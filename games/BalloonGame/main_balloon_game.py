# основной код игры "Шары"

# 1 - Импорт модулей
from pygame.locals import *
import pygwidgets
import sys
import pygame
from balloon_manager import *


# 2 - Определяем константы
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BACKGROUND_COLOR = (0, 180, 180)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640
PANEL_HEIGHT = 60
USABLE_WINDOW_HEIGHT = WINDOW_HEIGHT - PANEL_HEIGHT
FRAMES_PER_SECOND = 30

# 3 - Инициализируем окружение pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Загружаем элементы: изображение, звук и т.д.
o_score_display = pygwidgets.DisplayText(window, (10, USABLE_WINDOW_HEIGHT + 25),
                                         'Score: 0', textColor=BLACK,
                                         backgroundColor=BACKGROUND_COLOR, width=140,
                                         fontSize=24)

o_status_display = pygwidgets.DisplayText(window, (180,
                                                   USABLE_WINDOW_HEIGHT + 25),'', textColor=BLACK,
                                                   backgroundColor=None, width=300, fontSize=24)
o_start_button = pygwidgets.TextButton(window, (WINDOW_WIDTH - 110, USABLE_WINDOW_HEIGHT + 10), 'Start')


# 5 - Инициализируем переменные
o_balloon_manager = BalloonMgr(window, WINDOW_WIDTH, USABLE_WINDOW_HEIGHT)
playing = False

# 6 - Бесконечный цикл
while True:
    # 7 - Проверяем наличие событий и обрабатываем их
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if playing:
            o_balloon_manager.handleEvent(event)
            the_score = o_balloon_manager.get_score()
            o_score_display.setValue('Score: ' + str(the_score))
        elif o_start_button.handleEvent(event):
            o_balloon_manager.start()
            o_score_display.setValue('Score: 0')
            playing = True
            o_start_button.disable()

    # 8 - Выполняем действия "в рамках фрейма"
    if playing:
        o_balloon_manager.update()
        n_popped = o_balloon_manager.get_count_popped()
        n_missed = o_balloon_manager.get_count_missed()

        o_status_display.setValue('Popped: ' + str(n_popped) +
                                  ' Missed ' + str(n_missed) +
                                  ' ut of ' + str(N_BALLOONS))
        if (n_popped + n_missed) == N_BALLOONS:
            playing = False
            o_start_button.enable()

    # 9 - Очищаем окно
    window.fill(BACKGROUND_COLOR)

    # 10 - Рисуем все элементы окна
    if playing:
        o_balloon_manager.draw()

    pygame.draw.rect(window, GRAY, pygame.Rect(0, USABLE_WINDOW_HEIGHT, WINDOW_WIDTH, PANEL_HEIGHT))
    o_score_display.draw()
    o_status_display.draw()
    o_start_button.draw()

    # 11 - Обновляем окно
    pygame.display.update()

    # 12 - Делаем паузу
    clock.tick(FRAMES_PER_SECOND)
# "Больше-меньше" - версия pygame
# Основная программа

# 1 - Импорт пакетов
import pygame
from pygame.locals import *
import sys
import pygwidgets
from game import *

# 2 - Определение констант
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
FRAMES_PER_SECOND = 30

# 3 - Инициализируем окружение
pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Higher or Lower')

# 4 - Загружаем элементы: изображения, звуки и т.д.
background = pygwidgets.Image(window, (0, 0), 'images/background.png')

new_game_button = pygwidgets.TextButton(window, (20, 530),
                                        'New Game', width=100, height=45)
higher_button = pygwidgets.TextButton(window, (540, 520),
                                      'Higher', width=120, height=55)
lower_button = pygwidgets.TextButton(window, (340, 520),
                                     'Lower', width=120, height=55)
quit_button = pygwidgets.TextButton(window, (880, 530), 'Quit', width=100, height=45)


# 5 - Инициализируем переменные
o_game = Game(window)

# 6 - Бесконечный цикл
while True:
    # 7 - Проверяем наличие событий
    for event in pygame.event.get():
        if ((event.type == pygame.QUIT) or
                ((event.type == pygame.KEYDOWN) and (event.type == pygame.K_ESCAPE) or
                quit_button.handleEvent(event))):
            pygame.quit()
            sys.exit()

        if new_game_button.handleEvent(event):
            o_game.reset()
            lower_button.enable()
            higher_button.enable()

        if higher_button.handleEvent(event):
            game_over = o_game.hit_higher_or_lower(HIGHER)
            if game_over:
                higher_button.disable()
                lower_button.disable()

        if lower_button.handleEvent(event):
            game_over = o_game.hit_higher_or_lower(LOWER)
            if game_over:
                higher_button.disable()
                lower_button.disable()

        # 8 - Выполняем действия "в рамках фрейма"

        # 9 - Очищаем окно, прежде чем нарисовать его заново
        background.draw()

        # 10 - Рисуем элементы окна
        # рисуем игру
        o_game.draw()
        # рисуем остальные компоненты интерфеса пользователя
        new_game_button.draw()
        higher_button.draw()
        lower_button.draw()
        quit_button.draw()

        # 11 - Обновляем окно
        pygame.display.update()

        # 12 - Делаем паузу
        clock.tick(FRAMES_PER_SECOND)





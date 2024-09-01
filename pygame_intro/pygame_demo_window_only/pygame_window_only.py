# pygame demo 0 - только окно

# 1 - Импортируем пакеты.
import pygame
from pygame.locals import *
import sys

# 2 - Определяем константы
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# 3 - Инициализируем окружение pygame.
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Загружаем элементы.

# 5 - Инициализируем переменные.

# 6 - Бесконечный цикл.
while True:
    # 7 Проверяем наличие событий.
    for event in pygame.event.get():
        # Нажата кнопка "Закрыть"?
        # Выходим из pygame и завершаем программу.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8 - Выполняем действия "в рамках фрейма".

    # 9 - Очищаем окно
    window.fill(BLACK)

    # 10 - Рисуем все элементы окна.

    # 11 - Обновляем окно.
    pygame.display.update()

    # 12 - Делаем паузу.
    clock.tick(FRAMES_PER_SECOND)

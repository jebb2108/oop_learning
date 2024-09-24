# pygame демо 6(b) - используя класс Ball, отбивать много мячей

# 1 - Импортируем пакеты
import pygame
from pygame.locals import *
import sys
import random

from ball import *

# 2 - Определяем константы
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_BALLS = 10

# 3 - Инициализируем окружение pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()


# 4 - Загружаем элементы: изображение, звук и т.д.


# 5 - Инициализируем переменные
ball_list = []
for ball in range(0, N_BALLS):
    o_ball = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    ball_list.append(o_ball)

# 6 - Бесконечный цикл
while True:

    # 7 - Проверяем наличие событий и обрабатываем их
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8 - Выполняем действие в рамках "фрейма".
    for o_ball in ball_list:
        o_ball.update()

    # 9 - Очищаем окно, прежде чем рисовать его заново
    window.fill(BLACK)

    # 10 - Рисуем все элементы окна
    for o_ball in ball_list:
        o_ball.draw()

    # 11 - Обновляем окно
    pygame.display.update()

    # 12 - Делаем паузу
    clock.tick(FRAMES_PER_SECOND)


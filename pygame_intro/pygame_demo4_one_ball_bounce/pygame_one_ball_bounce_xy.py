# pygame демо 4(а) - одно изображение от границ окна
# с использованием координат (x, y)

# 1 - Импортируем пакеты
import pygame
from pygame.locals import *
import sys
import random

# 2 - Определяем константы
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 100
N_PIXELS_PER_FRAME = 3

# 3 - Инициализируем окружение pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Загружаем элементы: изображения, звуки и т.д.
ball_image = pygame.image.load('images/ball.png')

# 5 - Инициализируем переменные
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
ball_x = random.randrange(MAX_WIDTH)
ball_y = random.randrange(MAX_HEIGHT)
x_speed = N_PIXELS_PER_FRAME
y_speed = N_PIXELS_PER_FRAME


# 6 - Бесконечный цикл
while True:

    # 7 - Проверяем наличие событий
    for event in pygame.event.get():
        # Нажата кнопка закрытия?
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

    # 8 - Выполняем действие в рамках "фрейма"
    if (ball_x < 0) or (ball_x >= MAX_WIDTH):
        x_speed = -x_speed

    if (ball_y < 0) or (ball_y >= MAX_HEIGHT):
        y_speed = -y_speed

    # Обновляем местоположение мяча, используя скорость
    # в двух направлениях
    ball_x = ball_x + x_speed
    ball_y = ball_y + y_speed

    # 9 - Очищаем окно, прежде чем рисовать его заново
    window.fill(BLACK)

    # 10 - Рисуем все элементы окна
    window.blit(ball_image, (ball_x, ball_y))

    # 11 - Обновляем окно
    pygame.display.update()

    # 12 - Делаем паузу
    clock.tick(FRAMES_PER_SECOND)

# pygame demo 2 - рисуем одно изображение, щелчок и перемещение.

# 1 - Импортируем пакеты.
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
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT

# 3 - Инициализируем окружение pygame.
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Загружаем элементы.
ball_image = pygame.image.load('images/ball.png')

# 5 - Инициализируем переменные.
ball_x = random.randrange(MAX_WIDTH)
ball_y = random.randrange(MAX_HEIGHT)
ball_rect = pygame.Rect(ball_x, ball_y, BALL_WIDTH_HEIGHT,
                        BALL_WIDTH_HEIGHT)

# 6 - Бесконечный цикл.
while True:
    # 7 Проверяем наличие событий.
    for event in pygame.event.get():
        # Нажата кнопка "Закрыть"?
        # Выходим из pygame и завершаем программу.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            # mouse_x, mouse_y = event.pos
            # Могли бы это сделать при необходимости.

            # Проверяем, был ли щелчок в пределах прямоугольника мяча.
            # Если так, выбираем случайным образом новое местоположение.
            if ball_rect.collidepoint(event.pos):
                ball_x = random.randrange(MAX_WIDTH)
                ball_y = random.randrange(MAX_HEIGHT)
                ball_rect = pygame.Rect(ball_x, ball_y, BALL_WIDTH_HEIGHT,
                                        BALL_WIDTH_HEIGHT)

    # 8 - Выполняем действия "в рамках фрейма".

    # 9 - Очищаем окно
    window.fill(BLACK)

    # 10 - Рисуем все элементы окна
    # рисуем мяч на позиции 100 вдоль (х) и 200 вниз по (у).
    window.blit(ball_image, (ball_x, ball_y))

    # 11 - Обновляем окно.
    pygame.display.update()

    # 12 - Делаем паузу.
    clock.tick(FRAMES_PER_SECOND)

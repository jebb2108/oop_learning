# pygame demo 3 - рисуем одно изображение, управление клавиатурой.


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
TARGET_X = 400
TARGET_Y = 320
TARGET_WIDTH_HEIGHT = 120
N_PIXELS_TO_MOVE = 3

# 3 - Инициализируем окружение pygame.
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Загружаем элементы.
ball_image = pygame.image.load('images/ball.png')
target_image = pygame.image.load('images/target.jpg')

# 5 - Инициализируем переменные.
ball_x = random.randrange(MAX_WIDTH)
ball_y = random.randrange(MAX_HEIGHT)
ball_rect = pygame.Rect(ball_x, ball_y, BALL_WIDTH_HEIGHT,
                        BALL_WIDTH_HEIGHT)
target_rect = pygame.Rect(TARGET_X, TARGET_Y, TARGET_WIDTH_HEIGHT,
                          TARGET_WIDTH_HEIGHT)

# 6 - Бесконечный цикл.
while True:
    # 7 Проверяем наличие событий.
    for event in pygame.event.get():
        # Нажата кнопка "Закрыть"?
        # Выходим из pygame и завершаем программу.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ball_x = ball_x - N_PIXELS_TO_MOVE
            elif event.key == pygame.K_RIGHT:
                ball_x = ball_x + N_PIXELS_TO_MOVE
            elif event.key == pygame.K_UP:
                ball_y = ball_y - N_PIXELS_TO_MOVE
            elif event.key == pygame.K_DOWN:
                ball_y = ball_y + N_PIXELS_TO_MOVE

    # 8 - Выполняем действия "в рамках фрейма".
    ball_rect = pygame.Rect(ball_x, ball_y, BALL_WIDTH_HEIGHT,
                            BALL_WIDTH_HEIGHT)
    # 9 - Очищаем окно
    window.fill(BLACK)

    # 10 - Рисуем все элементы окна

    if ball_rect.colliderect(target_rect):
        print('Ball is touching the target')

    window.blit(target_image, (TARGET_X, TARGET_Y))
    window.blit(ball_image, (ball_x, ball_y))

    # 11 - Обновляем окно.
    pygame.display.update()

    # 12 - Делаем паузу.
    clock.tick(FRAMES_PER_SECOND)

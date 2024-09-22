# pygame демо (b) - одно изображение, отскакивает от границ окна
# с помощью rect

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
N_PIXELS_PER_FRAME = 3

# 3 - Инициализируем окружение pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Загружаем элементы: изображение, звуки и т.д.
ball_image = pygame.image.load('images/ball.png')
bounce_sound = pygame.mixer.Sound('sounds/boing.wav')
pygame.mixer.music.load('sounds/background.mp3')
pygame.mixer.music.play(-1, 0.0)

# 5 - Инициализируем переменные
ball_rect = ball_image.get_rect()
MAX_WIDTH = WINDOW_WIDTH - ball_rect.width
MAX_HEIGHT = WINDOW_HEIGHT - ball_rect.height
ball_rect.left = random.randrange(MAX_WIDTH)
ball_rect.top = random.randrange(MAX_HEIGHT)
x_speed = N_PIXELS_PER_FRAME
y_speed = N_PIXELS_PER_FRAME

# 6 - запускаем бесконечный цикл
while True:

    # 7 - Проверяем наличие событий и обрабатываем их
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

    if (ball_rect.left < 0) or (ball_rect.right >= WINDOW_WIDTH):
        x_speed = -x_speed
        bounce_sound.play()

    if (ball_rect.top < 0) or (ball_rect.bottom >= WINDOW_HEIGHT):
        y_speed = -y_speed
        bounce_sound.play()

    # обновляем местоположение мяча,
    # используя скорость в двух направлениях
    ball_rect.left += x_speed
    ball_rect.top += y_speed

    # 9 - Очищаем окно, прежде чем рисовать его заново
    window.fill(BLACK)

    # 10 - Рисуем все элементы окна
    window.blit(ball_image, ball_rect)

    # 11 - Обновляем окно
    pygame.display.update()

    # 12 - Делаем паузу
    clock.tick(FRAMES_PER_SECOND)
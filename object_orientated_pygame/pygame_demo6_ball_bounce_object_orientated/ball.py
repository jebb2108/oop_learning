import pygame
from pygame.locals import *
import random


class Ball():
    def __init__(self, window, window_width, window_height):
        self.window = window  # Запоминаем окно, чтобы мы смогли его
        # нарисовать позднее
        self.window_width = window_width
        self.window_height = window_height
        self.image = pygame.image.load('images/ball.png')

        # Прямоугольник состоит из (x, y, ширина, высота)
        ball_rect = self.image.get_rect()
        self.width = ball_rect.width
        self.height = ball_rect.height
        self.max_width = self.window_width - self.width
        self.max_height = self.window_height - self.height

        # Выбираем произвольную начальную позицию.
        self.x = random.randrange(0, self.max_width)
        self.y = random.randrange(0, self.max_height)

        # Выбираем произвольную скорость между -4 и 4, но не ноль
        # в обоих направлениях x и y
        speed_list = [-4, -3, -2, -1, 1, 2, 3, 4]
        self.x_speed = random.choice(speed_list)
        self.y_speed = random.choice(speed_list)

    def update(self):
        # Проверяем наличие ударов о стену.
        # Если они есть, изменяем направление.
        if (self.x < 0) or (self.x >= self.max_width):
            self.x_speed = -self.x_speed
        if (self.y < 0) or (self.y >= self.max_height):
            self.y_speed = -self.y_speed

        # обновляем x и y Ball, используя скорость в двух направлениях
        self.x = self.x + self.x_speed
        self.y = self.y + self.y_speed

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))

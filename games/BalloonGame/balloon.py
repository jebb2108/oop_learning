# Базовый класс Balloon и 3 подкласса
from random import randrange

import pygame
import random
from pygame.locals import *
import pygwidgets
from balloon_constants import *
from abc import ABC, abstractmethod

class Balloon(ABC):

    pop_sound_loaded = False
    pop_sound = None

    def __init__(self, window, max_width, max_height, ID,
                 o_image, size, n_points, speed_y):
        self.window = window
        self.ID = ID
        self.balloon_image = o_image
        self.size = size
        self.n_points = n_points
        self.speed_y = speed_y
        if not Balloon.pop_sound_loaded:  # загружаем только в первый раз
            Balloon.pop_sound_loaded = True
            Balloon.pop_sound = pygame.mixer.Sound('sounds/'
                                                   'balloonPop.wav')
        balloon_rect = self.balloon_image.getRect()
        self.width = balloon_rect.width
        self.height = balloon_rect.height
        self.x = random.randrange(max_width - self.width)
        self.y = max_height + random.randrange(75)
        self.balloon_image.setLoc((self.x, self.y))

    def clicked_inside(self, mouse_point):
        my_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        if my_rect.collidepoint(mouse_point):
            Balloon.pop_sound.play()
            return True, self.n_points
        else:
            return False, 0

    def update(self):
        self.y = self.y - self.speed_y

        self.balloon_image.setLoc((self.x, self.y))
        if self.y < -self.height:  # вышел за пределы экрана
            return BALLOON_MISSED
        else:
            return BALLOON_MOVING

    def draw(self):
        self.balloon_image.draw()

    def __del__(self):
        print(self.size, 'Balloon', self.ID, 'is going away')


class BalloonSmall(Balloon):
    balloonImage = pygame.image.load('images/redBalloonSmall.png')
    def __init__(self, window, max_width, max_height, ID):
        oImage = pygwidgets.Image(window, (0, 0),
                                  BalloonSmall.balloonImage)
        super().__init__(window, max_width, max_height, ID,
                         oImage, 'Small', 30, 3.1)

class BalloonMedium(Balloon):
    balloonImage = pygame.image.load('images/redBalloonMedium.png')
    def __init__(self, window, max_width, max_height, ID):
        oImage = pygwidgets.Image(window, (0, 0),
                                  BalloonMedium.balloonImage)
        super().__init__(window, max_width, max_height, ID,
                         oImage, 'Medium', 20, 2.2)

class BalloonLarge(Balloon):
    balloonImage = pygame.image.load('images/redBalloonLarge.png')
    def __init__(self, window, max_width, max_height, ID):
        oImage = pygwidgets.Image(window, (0, 0),
                                  BalloonLarge.balloonImage)
        super().__init__(window, max_width, max_height, ID,
                         oImage, 'Large', 10, 1.5)


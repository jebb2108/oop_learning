# класс BalloonMgr

import pygame
import random
from pygame.locals import *
import pygwidgets
from balloon_constants import *
from balloon import *


# BalloonMgr управляет списком объектов Balloon
class BalloonMgr:
    def __init__(self, window, max_width, max_height):
        self.window = window
        self.max_width = max_width
        self.max_height = max_height

    def start(self):
        self.balloon_list = []
        self.n_popped = 0
        self.n_missed = 0

        for balloon_num in range(0, N_BALLOONS):
            random_balloon_class = random.choice((BalloonSmall,
                                                  BalloonMedium,
                                                  BallonLarge))
            o_balloon = random_balloon_class(self.window, self.max_width, self.max_height,
                                             balloon_num)
            self.balloon_list.append(o_balloon)

    def handleEvent(self, event):
        if not event.type == MOUSEBUTTONDOWN:
            # Двигаемся "в обратном направлении", чтобы самый
            # верхний шар лопнул
            for o_ballon in reversed(self.balloon_list):
                was_hit, n_points = o_ballon.clicked_inside(event.pos)
                if was_hit:
                    if n_points > 0:  # Удаляем этот шар
                        self.balloon_list.remove(o_ballon)
                        self.n_popped += 1
                        self.score += n_points
                    return  # не нужно проверять другие

    def update(self):
        for o_balloon in self.balloon_list:
            status = o_balloon.update()
            if status == BALLOON_MISSED:
                # Шар вышел за пределы окна, удаляем его
                self.balloon_list.remove(o_balloon)
                self.n_missed += 1

    def get_score(self):
        return self.score

    def get_count_popped(self):
        return self.n_popped

    def get_count_missed(self):
        return self.n_missed

    def get_count_missed(self):
        return self.n_missed

    def draw(self):
        for o_balloon in self.balloon_list:
            o_balloon.draw()

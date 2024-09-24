# Класс SimpleButton
# Используем подход "конечного автомата"

import pygame
from pygame.locals import *
import sys


class SimpleButton:
    # Используется для отслеживания состояния кнопки
    STATE_IDLE = 'idle'  # кнопка вверх, мышь не на кнопке
    STATE_ARMED = 'armed'  # кнопка вниз, мышь на копке
    STATE_DISARMED = 'disarmed'  # щелчок по кнопке, откат

    def __init__(self, window, loc, up, down):
        self.window = window
        self.loc = loc
        self.surface_up = pygame.image.load(up)
        self.surface_down = pygame.image.load(down)

        # получаем rect кнопки (используется, чтобы увидеть,
        # находится ли мышь на кнопке)
        self.rect = self.surface_up.get_rect()
        self.rect[0] = loc[0]
        self.rect[1] = loc[1]

        self.state = SimpleButton.STATE_IDLE

    def handle_event(self, event_obj):
        # Этот метод вернет значение True, если пользователь щелкнет
        # о кнопке.
        # Обычно возвращает False
        if event_obj.type not in (MOUSEMOTION, MOUSEBUTTONUP,
                                  MOUSEBUTTONDOWN):
            # Кнопка реагирует только на относящиеся к мыши события
            return False

        event_point_in_button_rect = self.rect.collidepoint(event_obj.pos)

        if self.state == SimpleButton.STATE_IDLE:
            if ((event_obj.type == MOUSEBUTTONDOWN)
                    and event_point_in_button_rect):
                self.state = SimpleButton.STATE_ARMED

        elif self.state == SimpleButton.STATE_ARMED:
            if ((event_obj.type == MOUSEBUTTONUP)
                    and event_point_in_button_rect):
                self.state = SimpleButton.STATE_IDLE
                # был щелчок!
                return True

            if ((event_obj.type == MOUSEMOTION) and
                    (not event_point_in_button_rect)):
                self.state = SimpleButton.STATE_DISARMED


        elif self.state == SimpleButton.STATE_DISARMED:
            if event_point_in_button_rect:
                self.state = SimpleButton.STATE_ARMED
            elif event_obj.type == MOUSEBUTTONUP:
                self.state = SimpleButton.STATE_IDLE

        return False

    def draw(self):
        # рисуем текущий вид кнопки в окне
        if self.state == SimpleButton.STATE_ARMED:
            self.window.blit(self.surface_down, self.loc)

        else:  # IDLE или DISARMED
            self.window.blit(self.surface_up, self.loc)

        return None

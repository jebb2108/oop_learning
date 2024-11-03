# Класс Card

import pygame
import pygwidgets

class Card:

    BACK_OF_CARD_IMAGE = pygame.image.load('images/BackOfCard.png')

    def __init__(self, window, rank, suit, value):
        self.window = window
        self.rank = rank
        self.suit = suit
        self.card_name = self.rank + ' of ' + self.suit
        self.value = value
        file_name = 'images/' + self.card_name + '.png'
        # настраиваем некоторые начальное местоположение; для
        # изменения использовать setLoc ниже
        self.images = pygwidgets.ImageCollection(window, (0, 0),
                                                 {'front': file_name,
                                                            'back': Card.BACK_OF_CARD_IMAGE}, 'back' )

    def conceal(self):
        return self.images.replace('back')

    def reveal(self):
        return self.images.replace('front')

    def get_name(self):
        return self.card_name

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def set_loc(self, loc):
        self.images.setLoc(loc)

    def get_loc(self):
        loc = self.images.getLoc()
        return loc

    def draw(self):
        self.images.draw()

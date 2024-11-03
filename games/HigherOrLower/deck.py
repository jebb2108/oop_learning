# Класс Deck

import random
from card import *


class Deck:

    SUIT_TUPLE = ('Spades', 'Hearts', 'Diamonds', 'Clubs')

    STANDARD_DICT = {'Ace': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                     '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13}

    def __init__(self, window, rank_value_dict=STANDARD_DICT):
        # по умолчанию значение rank_value равно STANDARD_DICT,
        # но вы можее вызвать его с другим словарем, например
        # для блек-джека
        self.starting_deck_list = []
        self.playing_deck_list = []
        for suit in Deck.SUIT_TUPLE:
            for rank, value in rank_value_dict.items():
                o_card = Card(window, rank, suit, value)
                self.starting_deck_list.append(o_card)
        self.shuffle()

    def shuffle(self):
        # копировать начальную колоду и сохранить ее в списке
        # игральной колоды
        self.playing_deck_list = self.starting_deck_list.copy()
        for o_card in self.playing_deck_list:
            o_card.conceal()
        random.shuffle(self.playing_deck_list)

    def get_card(self):
        if len(self.playing_deck_list) == 0:
            raise IndexError('No more cards')
        # вытолкнуть одну карту из коолоды и вернуть ее
        o_card = self.playing_deck_list.pop()
        return o_card

    def return_card_to_deck(self, o_card):
        # Вернуть колоду обратно в колоду
        self.deck_list.insert(0, o_card)


# if __name__ == '__main__':
#     # основной код для тестирования класса Deck
#
#     import pygame
#
#     # константы
#     WINDOW_WIDTH = 100
#     WINDOW_HEIGHT = 100
#
#     pygame.init()
#     window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#
#     o_deck = Deck(window)
#     for i in range(0, 53):
#         o_card = o_deck.get_card()
#         print('Name: ', o_card.get_name(), 'Value: ', o_card.get_value())

# Класс Game

import pygwidgets
import pygame

from constants import *
from deck import *
from card import *

class Game:

    CARD_OFFSET = 110
    CARDS_TOP = 300
    CARDS_LEFT = 75
    NCARDS = 8
    POINTS_CORRECT = 15
    POINTS_INCORRECT = 10

    def __init__(self, window):
        self.window = window
        self.o_deck = Deck(self.window)
        self.score = 100
        self.score_text = pygwidgets.DisplayText(window, (450, 164),
                                                 'score: ' + str(self.score),
                                                 fontSize=36, textColor=WHITE)

        self.message_text = pygwidgets.DisplayText(window, (50, 460), '',
                                                   width=900, justified='center',
                                                   fontSize=36, textColor=WHITE)

        self.loser_sound = pygame.mixer.Sound('sounds/loser.wav')
        self.winner_sound = pygame.mixer.Sound('sounds/ding.wav')
        self.card_shuffle_sound = pygame.mixer.Sound('sounds/cardShuffle.wav')

        self.card_x_position_list = []
        this_left = Game.CARDS_LEFT
        # вычисляем координаты x для всех карт, один раз
        for card_num in range(Game.NCARDS):
            self.card_x_position_list.append(this_left)
            this_left += Game.CARD_OFFSET

        self.reset()

    def reset(self):
        self.card_shuffle_sound.play()
        self.card_list = []
        self.o_deck.shuffle()
        for card_index in range(0, Game.NCARDS): # раздаем карты
            o_card = self.o_deck.get_card()
            self.card_list.append(o_card)
            this_x_position = self.card_x_position_list[card_index]
            o_card.set_loc((this_x_position, Game.CARDS_TOP))
        self.show_card(0)
        self.card_number = 0
        self.current_card_name, self.current_card_value = \
                                self.get_card_name_and_value(self.card_number)

        self.message_text.setValue('Starting card is ' + self.current_card_name +
                                   '. Will the next card be higher or lower?')

    def get_card_name_and_value(self, index):
        o_card = self.card_list[index]
        the_name = o_card.get_name()
        the_value = o_card.get_value()
        return the_name, the_value

    def show_card(self, index):
        o_card = self.card_list[index]
        o_card.reveal()

    def hit_higher_or_lower(self, higher_or_lower):
        self.card_number += 1
        self.show_card(self.card_number)
        next_card_name, next_card_value = self.get_card_name_and_value(self.card_number)

        if higher_or_lower == HIGHER:
            if next_card_value == self.current_card_value:
                self.message_text.setValue('The next card is the same value as this one!')
            elif next_card_value > self.current_card_value:
                self.score = self.score + Game.POINTS_CORRECT
                self.message_text.setValue('Yes, the '+ next_card_name + ' was higher')
                self.winner_sound.play()
            else:
                self.score = self.score - Game.POINTS_INCORRECT
                self.message_text.setValue('No, the '+ next_card_name + ' was not higher')
                self.loser_sound.play()

        else: # пользователь нажал на кнопку Lower
            if next_card_value == self.current_card_value:
                self.message_text.setValue('The next card is the same value as this one!')
            elif next_card_value < self.current_card_value:
                self.score = self.score + Game.POINTS_CORRECT
                self.message_text.setValue('Yes, the ' + next_card_name + ' was lower')
                self.winner_sound.play()
            else:
                self.score = self.score - Game.POINTS_INCORRECT
                self.message_text.setValue('No, the ' + next_card_name + ' was not lower')
                self.loser_sound.play()

        self.score_text.setValue('Score: ' + str(self.score))

        self.current_card_value = next_card_value  # настраиваем для следующей карты

        done = (self.card_number == (Game.NCARDS -1)) # мы добрались до последней карты?

        return done

    def draw(self):
        # рисуем карты
        for o_card in self.card_list:
            o_card.draw()
        self.score_text.draw()
        self.message_text.draw()




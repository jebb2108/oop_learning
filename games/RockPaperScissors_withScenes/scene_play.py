import pyghelpers
import pygwidgets
import pygame
from constants import *
import random

class ScenePlay(pyghelpers.Scene):
    def __init__(self, window):
        self.window = window

        self.RPS_tuple = (ROCK, PAPER, SCISSORS)

        self.titleField = pygwidgets.DisplayText(self.window, (15, 40),
                                                 '    Rock               Paper          Scissors',
                                                 fontSize=50, textColor=WHITE, width=610, justified='center')

        self.messageField = pygwidgets.DisplayText(self.window, (30, 395), 'Choose!',
                                                   fontSize=50, textColor=WHITE, width=610, justified='center')

        self.rockButton = pygwidgets.CustomButton(self.window, (25, 120),
                                                  up="images/Rock.png",
                                                  over="images/RockOver.png",
                                                  down="images/RockDown.png")

        self.paperButton = pygwidgets.CustomButton(self.window, (225, 120),
                                                   up="images/Paper.png",
                                                   over="images/PaperOver.png",
                                                   down="images/PaperDown.png")

        self.scissorButton = pygwidgets.CustomButton(self.window, (425, 120),
                                                     up="images/Scissors.png",
                                                     over="images/ScissorsOver.png",
                                                     down="images/ScissorsDown.png")


    def getSceneKey(self):
        return SCENE_PLAY

    def handleInputs(self, eventsList, keyPressedList):
        player_choice = None
        for event in eventsList:
            if self.rockButton.handleEvent(event):
                player_choice = ROCK
            if self.paperButton.handleEvent(event):
                player_choice = PAPER
            if self.scissorButton.handleEvent(event):
                player_choice = SCISSORS

            if player_choice is not None:
                computer_choice = random.choice(self.RPS_tuple)
                data_dict = {
                    'player': player_choice,
                    'computer': computer_choice
                }
                # переходим к сцене Результатов
                self.goToScene(SCENE_RESULTS, data_dict)
                
                # не нужно включать метод Update, по умолчанию используется
                # унаследованный, который ничего не делает

    def draw(self):
        self.window.fill(GRAY)
        self.titleField.draw()
        self.rockButton.draw()
        self.paperButton.draw()
        self.scissorButton.draw()
        self.messageField.draw()




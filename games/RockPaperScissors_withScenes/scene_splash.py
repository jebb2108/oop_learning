import pyghelpers
import pygwidgets
import pygame

from pygame.locals import *
from constants import *

class SceneSplash(pyghelpers.Scene):
    def __init__(self, window):
        self.window = window

        self.message_field = pygwidgets.DisplayText(self.window, (15, 25), 'Welcome to Rock, Paper, Scissors!',
                                                    fontSize=50, textColor=WHITE, width=610, justified='center')

        self.start_button = pygwidgets.CustomButton(self.window, (210, 300), up='images/startButtonUp.png',
                                                down='images/startButtonDown.png',
                                                over='images/startButtonHighlight.png')
        self.rock_image = pygwidgets.Image(self.window, (25, 120), 'images/Rock.png')
        self.paper_image = pygwidgets.Image(self.window, (225, 120), 'images/Paper.png')
        self.scissors_image = pygwidgets.Image(self.window, (425, 120), 'images/Scissors.png')

    def getSceneKey(self):
        return SCENE_SPLASH

    def enter(self, data):
        pass

    def handleInputs(self, eventsList, keyPressedList):
        for event in eventsList:
            if self.start_button.handleEvent(event):
                self.goToScene(SCENE_PLAY)

    def update(self):
        pass

    def draw(self):
        self.window.fill(GRAY)
        self.message_field.draw()
        self.rock_image.draw()
        self.paper_image.draw()
        self.scissors_image.draw()
        self.start_button.draw()

    def leave(self):
        return None

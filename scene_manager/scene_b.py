import pyghelpers
import pygwidgets
import pygame
from pygame.locals import *
from constants import *


class SceneB(pyghelpers.Scene):
    def __init__(self, window):
        self.window = window

        self.message_field = pygwidgets.DisplayText(self.window,
                                                    (15, 25), 'This is Scene B', fontSize=50,
                                                    textColor=WHITE, width=610, justified='center')
        self.go_to_a_button = pygwidgets.TextButton(self.window, (100, 100), 'Go to Scene A')

        self.go_to_b_button = pygwidgets.TextButton(self.window, (250, 100), 'Go to Scene B')

        self.go_to_c_button = pygwidgets.TextButton(self.window, (400, 100), 'Go to Scene C')

        self.go_to_b_button.disable()

    def getSceneKey(self):
        return SCENE_B

    def handleInputs(self, eventsList, keyPressedList):
        for event in eventsList:
            if self.go_to_a_button.handleEvent(event):
                self.goToScene(SCENE_A)
            if self.go_to_c_button.handleEvent(event):
                self.goToScene(SCENE_C)

    def draw(self):
        self.window.fill(GRAY)
        self.message_field.draw()
        self.go_to_a_button.draw()
        self.go_to_b_button.draw()
        self.go_to_c_button.draw()
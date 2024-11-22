import pygwidgets
import pyghelpers
import pygame
from constants import *

class SceneResults(pyghelpers.Scene):
    def __init__(self, window):
        self.window = window
        self.player_score = 0
        self.computer_score = 0

        self.rps_collection_player = pygwidgets.ImageCollection(self.window, (150, 162), {ROCK: 'images/Rock.png',
                                                                                        PAPER: 'images/Paper.png',
                                                                                        SCISSORS: 'images/Scissors.png'}, '')
        self.rps_collection_computer = pygwidgets.ImageCollection(self.window, (450, 162), {ROCK: 'images/Rock.png',
                                                                                           PAPER: 'images/Paper.png',
                                                                                           SCISSORS: 'images/Scissors.png'}, '')
        self.youComputerField = pygwidgets.DisplayText(
            window, (22, 25),
            'You                     Computer',
            fontSize=50, textColor=WHITE, width=610, justified='center')

        self.resultsField = pygwidgets.DisplayText(
            self.window, (20, 275), '',
            fontSize=50, textColor=WHITE,
            width=610, justified='center')

        self.restartButton = pygwidgets.CustomButton(
            self.window, (220, 310),
            up='images/restartButtonUp.png',
            down='images/restartButtonDown.png',
            over='images/restartButtonHighlight.png')

        self.playerScoreCounter = pygwidgets.DisplayText(
            self.window, (86, 315), 'Score:',
            fontSize=50, textColor=WHITE)

        self.computerScoreCounter = pygwidgets.DisplayText(
            self.window, (384, 315), 'Score:',
            fontSize=50, textColor=WHITE)
        # Sounds
        self.winnerSound = pygame.mixer.Sound("sounds/ding.wav")
        self.tieSound = pygame.mixer.Sound("sounds/push.wav")
        self.loserSound = pygame.mixer.Sound("sounds/buzz.wav")

    def getSceneKey(self):
        return SCENE_RESULTS

    def enter(self, data):
        # данные являются словарем (получен из сцены Игры), который выглядит следующим образом:
        # { 'player': player_choice, 'computer': computer_choice }
        player_choice = data['player']
        computer_choice = data['computer']

        # Настраиваем изображения игрока и компьютера
        self.rps_collection_player.replace(player_choice)
        self.rps_collection_computer.replace(computer_choice)

        # оцениваем условия игры выиграл/проиграл/ничья
        if player_choice == computer_choice:
            self.resultsField.setText('It is a tie!')
            self.tieSound.play()

        elif player_choice == ROCK and computer_choice == SCISSORS:
            self.resultsField.setValue("Rock breaks Scissors. You win!")
            self.player_score = self.player_score + 1
            self.winnerSound.play()

        elif player_choice == ROCK and computer_choice == PAPER:
            self.resultsField.setValue("Rock is covered by Paper. You lose.")
            self.computer_score = self.computer_score + 1
            self.loserSound.play()

        elif player_choice == SCISSORS and computer_choice == PAPER:
            self.resultsField.setValue("Scissors cuts Paper. You win!")
            self.player_score = self.player_score + 1
            self.winnerSound.play()

        elif player_choice == SCISSORS and computer_choice == ROCK:
            self.resultsField.setValue("Scissors crushed by Rock. You lose.")
            self.computer_score = self.computer_score + 1
            self.loserSound.play()

        elif player_choice == PAPER and computer_choice == ROCK:
            self.resultsField.setValue("Paper covers Rock. You win!")
            self.player_score = self.player_score + 1
            self.winnerSound.play()

        elif player_choice == PAPER and computer_choice == SCISSORS:
            self.resultsField.setValue("Paper is cut by Scissors. You lose.")
            self.computer_score = self.computer_score + 1
            self.loserSound.play()

        # отображаем очки игрока и компьютера
        self.playerScoreCounter.setValue(
            'Score: ' + str(self.player_score))
        self.computerScoreCounter.setValue(
            'Score: ' + str(self.computer_score))

    def handleInputs(self, eventsList, keyPressedList):
        for event in eventsList:
            if self.restartButton.handleEvent(event):
                self.goToScene(SCENE_PLAY)

    def draw(self):
        self.window.fill(GRAY)
        self.youComputerField.draw()
        self.rps_collection_player.draw()
        self.rps_collection_computer.draw()
        self.resultsField.draw()
        self.restartButton.draw()
        self.playerScoreCounter.draw()
        self.computerScoreCounter.draw()

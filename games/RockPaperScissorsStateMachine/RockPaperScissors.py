import pygame
from pygame.locals import *
import pygwidgets
import random
import sys

GRAY = (100, 100, 100)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

ROCK = 'Rock'
PAPER = 'Paper'
SCISSORS = 'Scissors'

# Настриаваем константы для каждого из трех состояний
STATE_SPLASH = 'Splash'
STATE_PLAYER_CHOICE = 'Player choice'
STATE_SHOW_RESULTS = 'ShowResults'

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

messageField = pygwidgets.DisplayText(window, (15, 25),  'Welcome to Rock, Paper, Scissors!',
                                    fontSize=50, textColor = WHITE, width = 610, justified = 'center')

rockImage = pygwidgets.Image(window, (25, 120), 'images/Rock.png')
paperImage = pygwidgets.Image(window, (225, 120), 'images/Paper.png')
scissorsImage = pygwidgets.Image(window, (425, 120), 'images/Scissors.png')

startButton = pygwidgets.CustomButton(window, (210, 300),
                                           up='images/startButtonUp.png',
                                           down='images/startButtonDown.png',
                                           over='images/startButtonHighlight.png')


rockButton = pygwidgets.CustomButton(window, (25, 120),
                                 up = 'images/Rock.png',
                                 over = 'images/RockOver.png',
                                 down = 'images/RockDown.png')

paperButton =  pygwidgets.CustomButton(window, (225, 120),
                                 up = 'images/Paper.png',
                                 over = 'images/PaperOver.png',
                                 down = 'images/PaperDown.png')

scissorButton =  pygwidgets.CustomButton(window, (425, 120),
                                 up = 'images/Scissors.png',
                                 over = 'images/ScissorsOver.png',
                                 down = 'images/ScissorsDown.png')

chooseText = pygwidgets.DisplayText(window, (15, 395), 'Choose!',
                                    fontSize=50, textColor = WHITE, width = 610, justified = 'center')

resultsField = pygwidgets.DisplayText(window, (20, 275), '',
                                    fontSize=50, textColor=WHITE, width=610, justified='center')

# For results
rpsCollectionPlayer = pygwidgets.ImageCollection(window, (50, 62),
                    {ROCK:'images/Rock.png', PAPER:'images/Paper.png', SCISSORS:'images/Scissors.png'}, '')
rpsCollectionComputer = pygwidgets.ImageCollection(window, (350, 62),
                    {ROCK:'images/Rock.png', PAPER:'images/Paper.png', SCISSORS:'images/Scissors.png'}, '')

restartButton = pygwidgets.CustomButton(window, (220, 310),
                                    up='images/restartButtonUp.png',
                                    down='images/restartButtonDown.png',
                                    over='images/restartButtonHighlight.png')

playerScoreCounter = pygwidgets.DisplayText(window, (15, 315), 'Player Score:',
                                    fontSize=50, textColor = WHITE)

computerScoreCounter = pygwidgets.DisplayText(window, (300, 315), 'Computer Score:',
                                    fontSize=50, textColor = WHITE)


winnerSound = pygame.mixer.Sound('sounds/ding.wav')
tieSound = pygame.mixer.Sound('sounds/push.wav')
loserSound = pygame.mixer.Sound('sounds/buzz.wav')

# 5 - Инициализируем переменные
player_score = 0
computer_score = 0
state = STATE_SPLASH

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if state == STATE_SPLASH:
            if startButton.handleEvent(event):
                state = STATE_PLAYER_CHOICE

        elif STATE_PLAYER_CHOICE:
            player_choice = ''
            if rockButton.handleEvent(event):
                player_choice = ROCK
                rpsCollectionPlayer.replace(ROCK)

            elif paperButton.handleEvent(event):
                player_choice = PAPER
                rpsCollectionPlayer.replace(PAPER)

            elif scissorButton.handleEvent(event):
                player_choice = SCISSORS
                rpsCollectionComputer.replace(SCISSORS)

            if player_choice != '':
                # Компьютер выбирает из кортежа ходов
                rps = (ROCK, PAPER, SCISSORS)
                computer_choice = random.choice(rps)

                rpsCollectionComputer.replace(computer_choice)

                # Оценить игру
                if player_choice == computer_choice: # ничья
                    resultsField.setValue('It is a tie!')

                    tieSound.play()

                elif player_choice == ROCK and computer_choice == SCISSORS:
                    resultsField.setValue('Rock breaks Scissors. You win!')
                    player_score += 1
                    winnerSound.play()

                elif player_choice == ROCK and computer_choice == PAPER:
                    resultsField.setValue('Rock is covered by Paper. You loose')
                    computer_score += 1
                    loserSound.play()

                elif player_choice == SCISSORS and computer_choice == PAPER:
                    resultsField.setValue('Scissors cuts Paper. You win!')
                    player_score += 1
                    winnerSound.play()

                elif player_choice == SCISSORS and computer_choice == ROCK:
                    resultsField.setValue('Scissors crushed by Rock. You loose')
                    computer_choice += 1
                    loserSound.play()

                elif player_choice == PAPER and computer_choice == ROCK:
                    resultsField.setValue('Paper covers Rock. You win!')
                    player_score += 1
                    winnerSound.play()

                elif player_choice == PAPER and computer_choice == SCISSORS:
                    resultsField.setValue('Paper is cut by Scissors. You loose')
                    computer_score += 1
                    loserSound.play()

                # Отображаем очки пользователя
                playerScoreCounter.setValue('Your Score:' + str(player_score))

                # Отображаем очки компьютера
                computerScoreCounter.setValue('Computer Score:' + str(computer_score))

                state = STATE_SHOW_RESULTS

        elif state == STATE_SHOW_RESULTS:
            if restartButton.handleEvent(event):
                state = STATE_PLAYER_CHOICE
        else:
            raise ValueError('Unknown value for state:', state)

    # 8 - Выполняем действия в рамках фрейма
    if state == STATE_PLAYER_CHOICE:
        messageField.setValue('     ROCK        PAPER       SCISSORS')
    elif state == STATE_SHOW_RESULTS:
        messageField.setValue('YOU                      COMPUTER')

    window.fill(GRAY)

    messageField.draw()

    if state == STATE_SPLASH:
        rockImage.draw()
        paperImage.draw()
        scissorsImage.draw()
        startButton.draw()

    elif state == STATE_PLAYER_CHOICE:
        rockButton.draw()
        paperButton.draw()
        scissorButton.draw()
        chooseText.draw()

    elif state == STATE_SHOW_RESULTS:
        resultsField.draw()
        rpsCollectionPlayer.draw()
        rpsCollectionComputer.draw()
        playerScoreCounter.draw()
        computerScoreCounter.draw()
        restartButton.draw()

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)










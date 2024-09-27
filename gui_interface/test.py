import pygame
import pygwidgets
import sys
import random

BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

o_text_button = pygwidgets.TextButton(window, (50, 50), 'Click me')
o_text_field = pygwidgets.DisplayText(window, (10, 400),
                                      value='Hello world!', textColor=(255, 255, 255))
o_input_field = pygwidgets.InputText(window, (10, 100))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if o_text_button.handleEvent(event):
            print('click')
            o_text_field.setValue('Yes, you did it!')

        if o_input_field.handleEvent(event):
            user_text = o_input_field.getValue()
            o_text_field.setValue(user_text)

    window.fill(BLACK)

    o_text_button.draw()
    o_input_field.draw()
    o_text_field.draw()

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)




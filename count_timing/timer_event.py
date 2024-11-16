import pygame
import sys
import pygwidgets

FRAMES_PER_SECOND = 30
TIMER_LENGTH = 2.5
TIMER_EVENT_ID = pygame.event.custom_type()

pygame.init()
window = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

time_running = False

start_button = pygwidgets.TextButton(window, (50, 50), 'Start')
text = pygwidgets.DisplayText(window, (100, 200),'Timer started', fontSize=28)
text.hide()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if start_button.handleEvent(event):
            pygame.time.set_timer(TIMER_EVENT_ID, int(TIMER_LENGTH * 1000), True)
            start_button.disable()
            text.show()


        if event.type == TIMER_EVENT_ID:
            start_button.enable()
            text.hide()

    window.fill((180, 180, 180))
    start_button.draw()
    text.draw()
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)

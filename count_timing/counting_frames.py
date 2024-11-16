import pygame
import pygwidgets
import sys

FRAMES_PER_SECOND = 30
TIMER_LENGTH = 2.5

pygame.init()
window = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

time_running = False
n_frames_elapsed = 0
n_frames_to_wait = 0

start_button = pygwidgets.TextButton(window, (50, 50), 'Start')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if start_button.handleEvent(event):
            n_frames_elapsed = 0
            time_running = True
            n_frames_to_wait = int(FRAMES_PER_SECOND * TIMER_LENGTH)
            start_button.disable()

    if time_running:
        n_frames_elapsed += 1

        if n_frames_elapsed >= n_frames_to_wait:

            start_button.enable()
            time_running = False

    window.fill((180, 180, 180))
    start_button.draw()
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)

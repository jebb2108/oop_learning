import pygame
from pygame.locals import *
import sys

black = (0, 0, 0)
window_width = 640
window_height = 480
frames_per_second = 30

pygame.init()
window = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill(black)
    pygame.display.update()
    clock.tick(frames_per_second)

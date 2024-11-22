import pygame
import pyghelpers

from scene_a import *
from scene_b import *
from scene_c import *

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 180
FRAMES_PER_SECOND = 30

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# cоздаем экземпляры всех сцен и сохраняем их в список
scene_list = [SceneA(window),
              SceneB(window),
              SceneC(window)]

# создаем менеджен сцен, передавая список сцен и FPS
o_scene_mgr = pyghelpers.SceneMgr(scene_list, FRAMES_PER_SECOND)

# просим менеджер сцен начать выполнение
o_scene_mgr.run()




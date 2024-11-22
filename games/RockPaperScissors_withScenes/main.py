import pygame
import pyghelpers

from scene_play import ScenePlay
from scene_splash import SceneSplash
from scene_results import SceneResults

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# cоздаем экземпляры всех сцен и сохраняем их в список
scene_list = [SceneSplash(window),
              ScenePlay(window),
              SceneResults(window)]

# создаем менеджен сцен, передавая список сцен и FPS
o_scene_mgr = pyghelpers.SceneMgr(scene_list, FRAMES_PER_SECOND)

# просим менеджер сцен начать выполнение
o_scene_mgr.run()

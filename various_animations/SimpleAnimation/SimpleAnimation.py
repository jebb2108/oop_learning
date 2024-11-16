# класс SimpleAnimation

import pygame
import time

class SimpleAnimation:
    def __init__(self, window, loc, pic_paths, duration_per_image):
        self.window = window
        self.loc = loc
        self.image_list = []
        for pic_path in pic_paths:
            image = pygame.image.load(pic_path) # загружаем картинку
            image = pygame.Surface.convert_alpha(image) # оптимизируем блиттинг
            self.image_list.append(image)

        self.playing = False
        self.duration_per_image = duration_per_image
        self.n_images = len(self.image_list)
        self.index = 0

    def play(self):
        if self.playing:
            return
        self.playing = True
        self.image_start_time = time.time()
        self.index = 0

    def update(self):
        if not self.playing:
            return

        # сколько времени прошло с момента начала демонстрации этого
        # изображения
        self.elapsed = time.time() - self.image_start_time
        print(self.elapsed)

        # если прошло достаточно времени, переходим к следующему
        # изображению
        if self.elapsed > self.duration_per_image:
            self.index = self.index + 1

            if self.index < self.n_images:
                self.image_start_time = time.time()
            else:  # анимация завершена
                self.playing = False
                self.index = 0  # сбрасываем на начало

    def draw(self):
        # предполагается, что self.index была установлена ранее -
        # в методе update()
        # Используется в качестве индекса в image_list для поиска
        # текущего изображения
        the_image = self.image_list[self.index] # выбираем изображение для отображения
        self.window.blit(the_image, self.loc)





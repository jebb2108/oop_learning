# Класс SimpleSpriteSheetAnimation

import pygame
import time

class SimpleSpriteSheetAnimation:
    def __init__(self, window, loc, image_path, n_images, width, height,
                 duration_per_image):
        self.window = window
        self.loc = loc
        self.n_images = n_images
        self.images_list = []

        # загружаем лист спрайта
        sprite_sheet_image = pygame.image.load(image_path)
        # оптимизируем блиттинг
        sprite_sheet_image = pygame.Surface.convert_alpha(sprite_sheet_image)
        # считаем количество столбцов в начальном изображении
        n_cols = sprite_sheet_image.get_width() // width
        # разбиваем начальное изображение на подизображения
        row = 0
        col = 0
        for image_num in range(n_images):
            x = col * width
            y = row * height

            # создаем подповерхность из большего spriteSheet
            subsurface_rect = pygame.Rect(x, y, width, height)
            image = sprite_sheet_image.subsurface(subsurface_rect)
            self.images_list.append(image)

            # переходим к следующему подизображению
            col += 1
            if col == n_cols:
                col = 0
                row += 1

        self.duration_per_image = duration_per_image
        self.playing = False
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
        the_image = self.images_list[self.index] # выбираем изображение для отображения
        self.window.blit(the_image, self.loc)
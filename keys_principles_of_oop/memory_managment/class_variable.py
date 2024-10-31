# класс Sample
from random import sample


class Sample:
    n_objects = 0 # переменная класса (статическая)
    def __init__(self, name):
        self.name = name
        Sample.n_objects = Sample.n_objects + 1

    def how_many(self):
        print('There are', Sample.n_objects, 'sample objects')

    def __del__(self):
        Sample.n_objects -= 1

o_sample1 = Sample('A')
o_sample2 = Sample('B')
o_sample3 = Sample('C')
o_sample4 = Sample('D')

# удаляем 1 объект
del o_sample3

# определяем, сколько у нас есть
o_sample1.how_many()

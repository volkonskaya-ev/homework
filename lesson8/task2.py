# Напишите класс Trigon, для инициализации передаётся неизвестное кол-во атрибутов

# В классе при инициализации происходит проверка на корректность переданных данных и генерируются следующие исключения:

# 1) Если хотя бы одна сторона передана не числом,
# то падаем с TypeError и текстом 'Стороны должны быть числами'

# 2) Если хотя бы одна сторона передана нулем или отрицательным числом,
# то падаем с ValueError и текстом 'Стороны должны быть положительными'

# 3) Если не соблюдается неравество треугольника,
# то Exception и текст "Не треугольник"

# 4) Если передано не 3 аргумента, то IndexError "Передано {n} аргументов, а ожидается 3", где n - кол-во аргументов

import unittest  # Не удалять


# Здесь пишем код
#
# !!! Тест не проверяет условия соблюдения неравенства треугольника
# !!! Если закомментировать проверку, то тест все равно проходит
class Trigon:
    def __init__(self, *triangle_sides):
        n = len(triangle_sides)
        if n != 3:
            raise IndexError(f"Передано {n} аргументов, а ожидается 3")
        try:
            if triangle_sides[0] <= 0 or triangle_sides[1] <= 0 or triangle_sides[2] <= 0:
                raise ValueError("Стороны должны быть положительными")
        except TypeError:
            raise TypeError("Стороны должны быть числами")
        if triangle_sides[0]+triangle_sides[1] <= triangle_sides[2] \
                or triangle_sides[0]+triangle_sides[2] <= triangle_sides[1] \
                or triangle_sides[1]+triangle_sides[2] <= triangle_sides[0]:
            raise Exception("Не треугольник")

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


class MyTestCase(unittest.TestCase):

    def test(self):
        data = [(3, '7', 5), (-3, 7, 5), (2, 5, 2), (3, 4, 5, 6), (3, 4), (3, 4, 5)]

        test_data = [('Стороны должны быть числами', 'TypeError'),
                     ('Стороны должны быть положительными', 'ValueError'),
                     ("Не треугольник", 'Exception'),
                     ("Передано 4 аргументов, а ожидается 3", 'IndexError'),
                     ("Передано 2 аргументов, а ожидается 3", 'IndexError'),
                     0]
        for i, d in enumerate(data):
            try:
                Trigon(*data[i])
            except Exception as e:
                assert e.args[0] == test_data[i][0], 'Исключение имеет неправильный текст'
                assert type(e).__name__ == test_data[i][1], 'У исключения неправильный тип'

        print('Всё ок')


if __name__ == '__main__':
    unittest.main()

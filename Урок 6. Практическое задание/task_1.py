"""
1.	Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.


ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""


from pympler import asizeof


class Hex_add_mult:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def __add__(self, other):
        return list(hex(int(''.join(self.num_1), 16) + int(''.join(other.num_2), 16)))[2:]

    def __mul__(self, other):
        return list(hex(int(''.join(self.num_1), 16) * int(''.join(other.num_2), 16)))[2:]


class Hex_slot:
    __slots__ = ('num_1', 'num_2')
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def __add__(self, other):
        return list(hex(int(''.join(self.num_1), 16) + int(''.join(other.num_2), 16)))[2:]

    def __mul__(self, other):
        return list(hex(int(''.join(self.num_1), 16) * int(''.join(other.num_2), 16)))[2:]


FIRST = 'A2'
SECOND = 'C4F'

a = Hex_add_mult(FIRST, SECOND)
b = Hex_add_mult(FIRST, SECOND)

x = Hex_slot(FIRST, SECOND)
y = Hex_slot(FIRST, SECOND)

print(a + b)
print(a * b)
print()
print(x + y)
print(x * y)
print()

print(a.__dict__)
print(asizeof.asizeof(a))
print()

print(x.__slots__)
print(asizeof.asizeof(x))


'''
(Python 3.8 32-bit; Windows 10x64; PyCharm 2019.3.2)

Использование атрибута __slots__ при создании класса ограничивает в некоторых случаях
динамическое присвоение атрибутов, но дает почти трехкратный выигрыш в использовании
памяти
""{'num_1': 'A2', 'num_2': 'C4F'}
216

('num_1', 'num_2')
88"
т.к. кортеж компактнее словаря
'''
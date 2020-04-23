"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).
Идея доработки: если за проход по списку не совершается ни одной сортировки, то завершение
Обязательно сделайте замеры времени обеих реализаций

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""

import timeit
import random


def bubble_sort(orig_list):
    """Сортирует массив в порядке убывания методом пузырька"""
    n = len(orig_list)
    for bypass in range(1, n):
        for i in range(0, n-bypass):
            if orig_list[i] < orig_list[i+1]:
                orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]

def bubble_sort_mod(orig_list):
    """ Сортирует массив в порядке убывания методом пузырька и прекращает после прохода,
        когда не происходит перестановок - flag не изменяется"""
    n = len(orig_list)
    for bypass in range(1, n):
        flag = True
        for i in range(0, n-bypass):
            if orig_list[i] < orig_list[i+1]:
                orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]
                flag = False
        if flag:
            break


ORIG_LIST = [random.randrange(-100, 100) for _ in range(20)]
print(ORIG_LIST)
bubble_sort(ORIG_LIST)
print(ORIG_LIST)

print()
ORIG_LIST = [random.randrange(-100, 100) for _ in range(20)]
print(ORIG_LIST)
bubble_sort_mod(ORIG_LIST)
print(ORIG_LIST)

# замеры 10
print('\nРезультаты замеров времени при длине массива 10:')

ORIG_LIST = [random.randrange(-100, 100) for _ in range(10)]

print(timeit.timeit("bubble_sort(ORIG_LIST)", \
    setup="from __main__ import bubble_sort, ORIG_LIST", number=1000))

ORIG_LIST = [random.randrange(-100, 100) for _ in range(10)]

print(timeit.timeit("bubble_sort_mod(ORIG_LIST)", \
    setup="from __main__ import bubble_sort_mod, ORIG_LIST", number=1000))

# замеры 100
print('\nРезультаты замеров времени при длине массива 100:')

ORIG_LIST = [random.randrange(-100, 100) for _ in range(100)]

print(timeit.timeit("bubble_sort(ORIG_LIST)", \
    setup="from __main__ import bubble_sort, ORIG_LIST", number=1000))

ORIG_LIST = [random.randrange(-100, 100) for _ in range(100)]

print(timeit.timeit("bubble_sort_mod(ORIG_LIST)", \
    setup="from __main__ import bubble_sort_mod, ORIG_LIST", number=1000))

# замеры 1000
print('\nРезультаты замеров времени при длине массива 1000:')

ORIG_LIST = [random.randrange(-100, 100) for _ in range(1000)]

print(timeit.timeit("bubble_sort(ORIG_LIST)", \
    setup="from __main__ import bubble_sort, ORIG_LIST", number=1000))

ORIG_LIST = [random.randrange(-100, 100) for _ in range(1000)]

print(timeit.timeit("bubble_sort_mod(ORIG_LIST)", \
    setup="from __main__ import bubble_sort_mod, ORIG_LIST", number=1000))

"""
randrange - чтобы исключить вхождение верхней границы (по условию).
Функции ничего не возвращают, потому что изменение исходного массива происходит
внутри функций.
Первая функция выполняет все проходы методом пузырька.
Вторая прекращает цикл, когда массив уже отсортирован.

Результаты замеров:

Результаты замеров времени при длине массива 10:
0.012036900000000003
0.0026371000000000033

Результаты замеров времени при длине массива 100:
0.9193196
0.021130899999999952

Результаты замеров времени при длине массива 1000:
92.8780249
0.34334929999999986

При многократных запусках общая статистика затрат времени сохраняется и показывает,
что функция, выполняющая все проходы, затрачивает гораздо больше времени.
Это особенно заметно на больших массивах, что очевидно, т.к. сортировка по своей сути
квадратичная, и число выполнений соответствует квадрату длины массива.
"""

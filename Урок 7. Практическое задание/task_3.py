"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""


"""Решение с использованием метода сортировки подсчетом. Только для целых чисел.
Сначала реализовал для натуральных чисел от нуля, затем отредактировал для
всех целых чисел.

Суммируем количество элементов, начиная с наименьшего. Когда сумма достигает
величины середины списка, это и есть элемент, который бы стоял в середине
отсортированного списка.
Для проверки соответствия параллельно запускается statistics.median"""


import statistics
import random

m = random.randint(1, 50)
ORIG_LIST = [random.randint(-100, 100) for _ in range(2*m+1)]


def med(orig_list):
    """ Находит медиану через частотную характеристику для целых положительных
        чисел от нуля"""
    freq = [0] * (max(orig_list) + 1)
    for num in orig_list:
        freq[num] += 1

    half = len(orig_list) // 2 + 1
    s = 0
    for i in range(len(freq)):
        if freq[i] != 0:
            s += freq[i]
            if s >= half:
                median = i
                break
    return median

def med_all(orig_list):
    """ Находит медиану через частотную характеристику для целых чисел"""
    m = min(orig_list)
    freq = [0] * (max(orig_list) - m + 1)
    for num in orig_list:
        freq[num-m] += 1

    half = len(orig_list) // 2 + 1
    s = 0
    for i in range(len(freq)):
        if freq[i] != 0:
            s += freq[i]
            if s >= half:
                median = i + m
                break
    return median

print(ORIG_LIST)

print(med_all(ORIG_LIST))
print()
print(statistics.median(ORIG_LIST))

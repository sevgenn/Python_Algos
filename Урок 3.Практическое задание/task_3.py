"""
Задание_3.	В массиве случайных целых чисел поменять
местами минимальный и максимальный элементы.

Пример:
В данном массиве чисел максимальное число   88 стоит на
0 позиции, а минимальное число  -49 стоит на    6 позиции
Заменяем их
[88, 26, 41, 75, 23, 52, -49, 60, 69, -18]
В данном массиве чисел максимальное число   88 стоит на
6 позиции, а минимальное число  -49 стоит на    0 позиции
[-49, 26, 41, 75, 23, 52, 88, 60, 69, -18]
"""

######   Второй вариант почему-то срабатывает нестабильно, через раз.(   #######

from random import randint

###############   1 VARIANT  подробная запись   #########################

NUM = int(input('Enter the length of array - '))
ARR_RAND = [randint(-100, 100) for _ in range(NUM)]
print(ARR_RAND)

MAX_ITEM = max(ARR_RAND)
MIN_ITEM = min(ARR_RAND)
MAX_IND = ARR_RAND.index(MAX_ITEM)
MIN_IND = ARR_RAND.index(MIN_ITEM)
ARR_RAND[MAX_IND], ARR_RAND[MIN_IND] = ARR_RAND[MIN_IND], ARR_RAND[MAX_IND]
print(
    f'Для первого варианта: \nMAX = {MAX_ITEM} \nMIN = {MIN_ITEM} \n{ARR_RAND} \n')


###############   2 VARIANT  краткая запись   #########################
NUM = int(input('Enter the length of array - '))
ARR_RAN = [randint(-100, 100) for _ in range(NUM)]
print(ARR_RAN)

ARR_RAN[ARR_RAN.index(min(ARR_RAN))], ARR_RAN[ARR_RAN.index(max(ARR_RAN))] =\
    ARR_RAN[ARR_RAN.index(max(ARR_RAN))], ARR_RAN[ARR_RAN.index(min(ARR_RAN))]

print(f'Для второго варианта: \n{ARR_RAN} \n')
print('Finish.')

"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def sum_natural_row(num):
    '''Функция рекурсивно вычисляет сумму членов натурального ряда'''
    if num == 1:
        return 1
    return num + sum_natural_row(num - 1)


NUM = int(input('Enter some natural number: '))
print(
    f'The left side is {sum_natural_row(NUM)}\nThe right side is {NUM * (NUM + 1) // 2}\n')
print('Finish.')

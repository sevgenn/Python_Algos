"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

Пример:
Введите количество чисел: 2
Введите число: 23
Введите число: 2
Наибольшее число по сумме цифр: 23, сумма его цифр: 5

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

##############   1 VARIANT  2 рекурсивные фкнкции   ##################

def sum_digits(num):
    '''Рекурсивная функция суммирующая цифры числа'''
    if num == 0:
        return 0
    return int(num % 10) + sum_digits(num//10)

def selection(quantity):
    '''Рекурсивная функция отбирает максимальное значение из вводимых чисел'''
    global MAX_SUM
    global MAX_NUM
    if quantity > 0:
        number = int(input('Введите число - '))

        if sum_digits(number) > MAX_SUM:
            MAX_SUM = sum_digits(number)
            MAX_NUM = number
        selection(quantity-1)

QUANTITY = int(input('Введите количество чисел - '))
MAX_SUM = 0
selection(QUANTITY)
print(f'Наибольшее число по сумме цифр: {MAX_NUM}, сумма его цифр: {MAX_SUM}')


##############   2 VARIANT  1 функция и цикл   ##################

QUANTITY = int(input('Введите количество чисел - '))
MAX_SUM = 0

for i in range(1, QUANTITY + 1):
    NUMBER = int(input(f'Введите {i} число - '))

    if sum_digits(NUMBER) > MAX_SUM:
        MAX_SUM = sum_digits(NUMBER)
        MAX_NUM = NUMBER
print(f'Наибольшее число по сумме цифр: {MAX_NUM}, сумма его цифр: {MAX_SUM}')

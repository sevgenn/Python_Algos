"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.

Пример:
Сколько будет чисел? - 2
Какую цифру считать? - 3
Число 1: 223
Число 2: 21
Было введено 1 цифр '3'

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

################  1 VARIANT  с глобальной переменной  #####################

def digit_repeat(num, digit):
    '''Рекурсивная функция считает повторы цифры в числе'''
    global COUNT
    if num > 0:
        COUNT += int(num % 10 == digit)
        digit_repeat(num//10, digit)

QUANTITY = int(input('Сколько будет чисел? - '))
DIGIT = int(input('Какую цифру считать? - '))
COUNT = 0
for i in range(1, QUANTITY + 1):
    NUMBER = int(input(f'Enter the {i} number - '))
    digit_repeat(NUMBER, DIGIT)
print(f'Было введено {COUNT} цифр "{DIGIT}"')


################  2 VARIANT  без глобальной  #####################

def digit_repeat_2(num, digit):
    '''Рекурсивная функция считает повторы цифры в числе'''
    if num == 0:
        return 0
    return int(num % 10 == digit) + digit_repeat_2(num//10, digit)

QUANTITY = int(input('Сколько будет чисел? - '))
DIGIT = int(input('Какую цифру считать? - '))
COUNT = 0
for i in range(1, QUANTITY + 1):
    NUMBER = int(input(f'Enter the {i} number - '))
    COUNT += digit_repeat_2(NUMBER, DIGIT)
print(f'Было введено {COUNT} цифр "{DIGIT}"')

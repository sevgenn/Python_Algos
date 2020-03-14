"""
Задание 4. Написать программу, которая генерирует в указанных пользователем границах:
    случайное целое число;
    случайное вещественное число;
    случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

Подсказка:
Нужно обойтись без ф-ций randint() и uniform()
Использование этих ф-ций = задание не засчитывается

Функцию random() использовать можно
Опирайтесь на пример к уроку
"""

########     Попытка реализовать все в одном цикле     #########

from random import random

while True:
    VAR = input('Enter "i" - for integer number, "r" - for real number, "s" - for symbol'
                '"q" - for exit: ')
    if VAR.lower() == 'i':
        try:
            LEFT = int(float(input('Lower bound: ')))   # float для вещественного числа
            RIGHT = int(float(input('Upper bound: ')))
            if LEFT < RIGHT:
                INT_NUMB = int(random() * (RIGHT - LEFT + 1)) + LEFT
                print(f'Pseudorandom integer number - {INT_NUMB}\n')
            else:
                print('Lower bound must be less than upper bound. Try again.')
                continue
        except ValueError:
            print('Enter the numbers.')
            continue
    elif VAR.lower() == 'r':
        try:
            LEFT = float(input('Lower bound: '))
            RIGHT = float(input('Upper bound: '))
            if LEFT < RIGHT:
                REAL_NUMB = random() * (RIGHT - LEFT) + LEFT
                print(f'Pseudorandom real number - {round(REAL_NUMB,2)}\n')
            else:
                print('Lower bound must be less than upper bound. Try again.')
                continue
        except ValueError:
            print('Enter the numbers.')
            continue
    elif VAR.lower() == 's':
        LEFT = input('Lower bound: ').lower()
        RIGHT = input('Upper bound: ').lower()
        if LEFT.isalpha() and RIGHT.isalpha():      # введена не цифра
            LEFT = ord(LEFT)
            RIGHT = ord(RIGHT)
            if LEFT < RIGHT:
                S_NUMB = int(random() * (RIGHT - LEFT + 1)) + LEFT
                print(f'Pseudorandom symbol - {chr(S_NUMB)}')
            else:
                print('Lower bound must be to the left. Try again.')
                continue
        else:
            print('Enter the symbols.')
    elif VAR.lower() == 'q':
        print('Game over!')
        break
    else:
        print('Something is wrong. Try again.')

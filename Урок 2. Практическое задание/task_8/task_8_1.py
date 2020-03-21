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

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

while True:
    ACT = input('Приступим (Y) или закончим (N)? - ')
    if ACT.lower() == 'y':
        QUANTITY = int(input('Сколько будет чисел? - '))
        DIGIT = int(input('Какую цифру считать? - '))
        COUNT = 0
        for i in range(1, QUANTITY + 1):
            NUMBER = int(input(f'Enter the {i} number - '))
            while NUMBER > 0:
                if NUMBER % 10 == DIGIT:
                    COUNT += 1
                NUMBER //= 10
        print(f'Было введено {COUNT} цифр "{DIGIT}"')
    elif ACT.lower() == 'n':
        break
    else:
        print('I do not understand. Repeat please.\n')
        continue
print('Finish.')
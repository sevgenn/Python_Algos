"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""

while True:
    try:
        NUMB_A = int(input('The first number a = '))
        NUMB_B = int(input('The second number b = '))
        NUMB_C = int(input('The third number c = '))
        if NUMB_A == NUMB_B == NUMB_C:
            print('No solution, a = b = c.')
        else:
            if NUMB_A <= NUMB_B <= NUMB_C or NUMB_C <= NUMB_B <= NUMB_A:
                print(f'In-between number is b = {NUMB_B}.')
            elif NUMB_A <= NUMB_C <= NUMB_B or NUMB_B <= NUMB_C <= NUMB_A:
                print(f'In-between number is c = {NUMB_C}.')
            else:
                print(f'In-between number is a = {NUMB_A}.')

        if NUMB_A == NUMB_B and NUMB_B != NUMB_C:
            print('a = b')
        elif NUMB_A == NUMB_C and NUMB_A != NUMB_B:
            print('a = c')
        elif NUMB_B == NUMB_C and NUMB_A != NUMB_B:
            print('b = c')
    except ValueError:
        print('Not a number. Try again.')
        continue

    ACTION = input('One more (any key) or exit (q): ')
    if ACTION.lower() == 'q':
        break
print('Game over!')

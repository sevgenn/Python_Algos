"""
7. По длинам трех отрезков, введенных пользователем,
определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует,
то определить, является ли он разносторонним, равнобедренным или равносторонним.
"""

ACTION = True
while ACTION:
    print('Enter lengths of the segments:')
    try:
        SEGMENT_A = float(input('A = '))
        SEGMENT_B = float(input('B = '))
        SEGMENT_C = float(input('C = '))

        if SEGMENT_C >= SEGMENT_A + SEGMENT_B or SEGMENT_B >= SEGMENT_A + \
                SEGMENT_C or SEGMENT_A >= SEGMENT_B + SEGMENT_C:
            print('Triangle does not exist.')
        elif SEGMENT_A == SEGMENT_B == SEGMENT_C:
            print('The equilateral triangle.')            # равносторонний
        elif SEGMENT_A != SEGMENT_B != SEGMENT_C:
            print('The scalene triangle.')                # разносторонний
        else:
            print('The isosceles triangle.')              # равнобедренный
    except ValueError:
        print('It is not a number. Try again.')
    ACTION = input('Continue (any key) or exit (q): ')
    if ACTION.lower() == 'q':
        ACTION = False
print('Game over!')

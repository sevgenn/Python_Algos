"""
Задание 3. По введенным пользователем координатам двух
точек вывести уравнение прямой,
проходящей через эти точки.

Подсказка:
Запросите у пользователя значения координат X и Y для первой и второй точки
Найдите в учебнике по высшей математике формулы расчета:
k – угловой коэффициент (действительное число), b – свободный член (действительное число)
Сформируйте уравнение прямой по формуле: y = kx + b – функция общего вида

Пример:
X1_VAL = 2, Y1_VAL = 3, X2_VAL = 4, Y2_VAL = 5
Уравнение прямой, проходящей через эти точки: y = 1.0x + 1.0
"""

print('The program for getting the linear equation.\n')
ACTION = True
while ACTION:
    ACTION = input('Enter "y" to continue or "n" to exit: ')
    if ACTION.lower() == 'y':
        try:
            # X1_VAL = int(input('Enter the abscissa x1 for the first point: '))
            # Y1_VAL = int(input('Enter the ordinate y1 for the first point: '))
            # X2_VAL = int(input('Enter the abscissa x2 for the second point: '))
            # Y2_VAL = int(input('Enter the abscissa y2 for the second point: '))
            X1_VAL, Y1_VAL, X2_VAL, Y2_VAL = [int(x) for x in input(
                'Enter the coordinates for two points (x1 y1 x2 y2): ').split()]

            K_VAL = (Y1_VAL - Y2_VAL) / (X1_VAL - X2_VAL)   # коэффициент
            B_VAL = Y1_VAL - K_VAL * X1_VAL                 # свободный член
            if B_VAL != 0:
                print(f'The linear equation: y={K_VAL:.2f}*x{B_VAL:+.2f}')
            else:
                print(f'The linear equation: y={K_VAL:.2f}*x')
        except ValueError:
            print('It is not a number. Pay attantion.')
            continue
    elif ACTION.lower() == 'n':
        ACTION = False
    else:
        print('What do you mean?')
print('Game over!')

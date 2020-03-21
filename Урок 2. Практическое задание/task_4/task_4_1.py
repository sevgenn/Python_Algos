"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

FLAG = 1
while FLAG:
    try:
        NUM = int(input('Enter a quantity of the elements: '))
    except ValueError:
        print('It is not a number. Try again.')
        continue
    SUM = 0
    for i in range(NUM):
        SUM = SUM + 1 / (-2) ** i
    print(f'Количество элементов - {NUM}, их сумма - {SUM}')

    while True:
        ACT = input('Are you planning to continue (Y) or to exit (N): ')
        if ACT.lower() == 'y':
            FLAG = 1
            break
        elif ACT.lower() == 'n':
            FLAG = 0
            break
        else:
            print('What do you mean? Try again.')
            continue
print('Finish.')

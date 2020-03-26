"""
Задание_8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки
и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.

1-я строка:
3
3
3
3
2-я строка:
3
3
3
3
3-я строка:
3
3
3
3
4-я строка:
3
3
3
3
5-я строка:
3
3
3
3

[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
"""

################   1 VARIANT  Вложенный цикл   ################
SEQ = []
for i in range(5):
    SEQ.append([int(j) for j in input('Введите 4 элемента массива - ').split()])

print('Исходная матрица:')
for rw in SEQ:
    for el in rw:
        print(f'{el:>4}', end='')
    print()

for i in range(5):
    SUM_ROW = 0
    for j in range(4):
        SUM_ROW += SEQ[i][j]
    SEQ[i].append(SUM_ROW)

print('Результирующая матрица: ')
for rw in SEQ:
    print(rw)

################   2 VARIANT  Обычный цикл   ################

SEQ_2 = [[int(j) for j in input('Введите 4 элемента массива - ').split()] for i in range(5)]

print('Исходная матрица:')
for rw in SEQ_2:
    for el in rw:
        print(f'{el:>4}', end='')
    print()

for i in range(5):
    SEQ_2[i].append(sum(SEQ_2[i]))

print('Результирующая матрица: ')
for rw in SEQ_2:
    for el in rw:
        print(f'{el:>4}', end='')
    print()

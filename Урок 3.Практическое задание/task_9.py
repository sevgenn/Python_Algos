"""
Задание_9.Найти максимальный элемент среди минимальных элементов столбцов матрицы.

Пример:

Задайте количество строк в матрице: 3
Задайте количество столбцов в матрице: 4
 36 20 42 38
 46 27  7 33
 13 12 47 15
[13, 12, 7, 15] минимальные значения по столбцам
Максимальное среди них = 15
"""

from random import randint

COL = 4
ROW = 3
SEQ = [[randint(1, 100) for _ in range(COL)] for _ in range(ROW)]
for rw in SEQ:
    for el in rw:
        print(f'{el:<5}', end="")
    print()

SEQ_MIN_COL = []
for j in range(COL):
    SEQ_MIN_COL += [min(SEQ[i][j] for i in range(ROW))]

print(f'{SEQ_MIN_COL} минимальные значения по столбцам')
print(f'Максимальное среди них = {max(SEQ_MIN_COL)}')

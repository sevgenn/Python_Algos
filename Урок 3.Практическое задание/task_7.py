"""
Задание_7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.

Пример:
Исходный массив: [28, -86, 44, -37, -7, -52, -19, -3, -15, -73]
Наименьший элемент: -86, встречается в этом массиве 1 раз
Второй наименьший элемент: -73
"""


SEQ = [28, -86, 44, -37, -7, -52, -19, -3, -15, -73]

MIN_1 = min(SEQ)
if SEQ.count(MIN_1) > 1:
    print(f'Наименьший элемент: {MIN_1}, встречается в этом массиве 2 раза.')
else:
    SEQ.remove(MIN_1)
    MIN_2 = min(SEQ)
    print(f'Наименьший элемент: {MIN_1}, встречается в этом массиве 1 раз.\n'
          f'Второй наименьший элемент: {MIN_2}.')

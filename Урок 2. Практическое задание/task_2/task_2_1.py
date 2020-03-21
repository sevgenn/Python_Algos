"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
Для извлечения цифр числа используйте арифм. операции

Пример:
Введите натуральное число: 44
В числе 44 всего 2 цифр, из которых 2 чётных и 0 нечётных

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

while True:
    try:
        NUM = input('Enter some natural number or "Q" to exit: ')
        if NUM.lower() == 'q':
            break
        NUMBER = int(NUM)
    except ValueError:
        print('It is not a number. Try again.')
        continue
    EVEN = 0
    ODD = 0
    for i in range(len(NUM)):
        if NUMBER % 10 % 2 == 0:
            EVEN += 1
        else:
            ODD += 1
        NUMBER //= 10
    print(f'В числе {NUM} всего {len(NUM)} цифр, из которых {EVEN} чётных и {ODD} нечётных')
print('Finish.')

"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.

Подсказка:
Используйте арифм операции для формирования числа, обратного введенному

Пример:
Введите число: 123
Перевернутое число: 321

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
    INVERSE_NUMBER = ''
    for i in range(len(NUM)):
        INVERSE_NUMBER += str(NUMBER % 10)
        NUMBER //= 10
#    INVERSE_NUMBER = int(INVERSE_NUMBER)    # если только необходимо для других условий
    print(f'Перевернутое число: {INVERSE_NUMBER}')
print('Finish.')

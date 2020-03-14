"""
Задание 1.
Найти сумму и произведение цифр трехзначного числа,
которое вводит пользователь.
#print(124 // 100) = 1 - отбросить остаток
#print((124 // 10) % 10) = 2 - остаток от деления числа 12 на 10
#print(124 % 10) = 4 - остаток от деления числа 124 на 10

Пример: Целое трехзначное число 123
Сумма = 6
Произведение = 6

Подсказка: для получения отдельных цифр числа используйте арифм. операции
и НЕ ИСПОЛЬЗУЙТЕ операции с массивами
"""

while True:
    NUM_A = input('Enter a number (3-digits) or "q" to leave the program: ')
    if NUM_A.lower() == 'q':
        break
    try:
        NUM_A = int(NUM_A)
        if len(str(NUM_A)) == 3 and NUM_A > 0:        # проверка на разрядность
            print(f'The sum of digits of {NUM_A} '
                  f'is {NUM_A // 100 + (NUM_A % 100) // 10 + NUM_A % 10}.')
            print(
                f'The product of digits of {NUM_A} '
                f'is {(NUM_A // 100) * ((NUM_A % 100) // 10) * (NUM_A % 10)}')
        else:
            print("I'd like to see three digits. Try again.")
            continue
    except ValueError:
        print('It is not a number. Pay attantion.')
print('Game over')

"""
Задание 6.	Пользователь вводит номер буквы в алфавите.
Определить, какая это буква.

Пример:
Введите номер буквы: 4
Введёному номеру соответствует буква: d

Подсказка: используйте ф-ции chr() и ord()
"""

while True:
    try:
        NUM_LETTER = int(
            input('Enter the number of the letter or "0" to exit: '))
        if 1 <= NUM_LETTER <= 26:
            print(f'This is the letter {chr(NUM_LETTER + 96)}')
        elif NUM_LETTER == 0:
            break
        else:
            print('There are not so many letters.')
            continue
    except ValueError:
        print('It is not a number. Try again.')
        continue
print('Game over!')

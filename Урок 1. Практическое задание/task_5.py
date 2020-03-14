"""
Задание 5.
Пользователь вводит две буквы. Определить,
на каких местах алфавита они стоят, и сколько между ними находится букв.

Подсказка:
Вводим маленькие латинские буквы.
Обратите внимание, что ввести можно по алфавиту, например, a,z
а можно наоборот - z,a
В обоих случаях программа должна вывести корректный результат.
В обоих случаях он 24, но никак не -24
"""

print('The program determines the position of letters.\n')
ACTION = True
while ACTION:
    FIRST_LETTER, LAST_LETTER = [ord(x) for x in input(
        'Enter two letters: ').lower().split()]
    print(f'Position of the first letter - {FIRST_LETTER - 96}')
    print(f'Position of the last letter - {LAST_LETTER - 96}')
    print(
        f'Interval between these letters - {abs(LAST_LETTER - FIRST_LETTER) - 1} letters.\n')
    ACTION = input('Continue (any key) or exit (q): ')
    if ACTION.lower() == 'q':
        ACTION = False
print('Game over!')

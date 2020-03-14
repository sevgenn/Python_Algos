"""
Задание 8.	Определить, является ли год, который ввел пользователем,
високосным или не високосным.

Подсказка:
Год является високосным в двух случаях: либо он кратен 4,
но при этом не кратен 100, либо кратен 400.

Попробуйте решить задачу двумя способами:
1. Обычное ветвление
2. Тернарный оператор

П.С. - Тернарные операторы, также известные как условные выражения,
представляют собой операторы, которые оценивают что-либо на основе условия,
являющегося истинным или ложным. Он был добавлен в Python в версии 2.5 .
Он просто позволяет протестировать условие в одной строке,
заменяя многострочное if-else, делая код компактным.
"""

print('Let`s determine leap years.')
while True:
    ANSWER = input('Continue (any key) or exit (q): ')
    print()
    if ANSWER.lower() == 'q':
        break
    try:
        YEAR = int(input('Enter the year: '))

########## 1 VARIANT ########################
        if (YEAR % 4 == 0 and YEAR % 100 != 0) or YEAR % 400 == 0:
            print('1 VARIANT - It is a leap year.')
        else:
            print('1 VARIANT - It is not a leap year.')

########## 2 VARIANT ########################
        print(
            '2 VARIANT - It is a leap year.'
            if (YEAR % 4 == 0 and YEAR % 100 != 0) or YEAR % 400 == 0
            else '2 VARIANT - It is not a leap year.')
    except ValueError:
        print('Enter correct data.')
        continue
print('Game over!')

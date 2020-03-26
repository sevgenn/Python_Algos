"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

from random import random

def guess(number, count):
    '''
    Рекурсивная функция принимает число попыток и сравнивает ответ с заданным значением,
    отслеживает счетчик попыток
    '''
    if count == 0:
        print('Sorry! It was the last effort. You lose!\n')
    else:
        answer = int(input('Enter your answer: '))
        if answer == number:
            print('You are right! You won!\n')
        if answer > number:
            print(f'Too much. Try again. You have {count-1} tries.')
            guess(number, count - 1)                                    # рекурсия
        elif answer < number:
            print(f'Too little. Try again. You have {count-1} tries.')
            guess(number, count-1)                                      # рекурсия


while True:
    NUMBER = int(random() * 101)
    print('Guess the number I am thinking of.')
    ACT = input('Are you ready? (Y or N): ')

    if ACT.lower() == 'y':
        COUNT = int(input('Enter the number of tries: '))
        print()
        guess(NUMBER, COUNT)
    elif ACT.lower() == 'n':
        break
    else:
        print('What do you mean?\n')
        continue
print('Finish.')

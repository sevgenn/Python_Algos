"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

from random import random

##############  1 VARIANT  ##################
'''С циклом for в теле функции'''

def guess(number):
    '''Принимает число попыток и сравнивает ответ с заданным значением.'''
    count = int(input('Enter the number of tries: '))
    for i in range(count):
        answer = int(input('Enter your answer: '))
        if answer > number:
            print('Too much. Try again.')
        elif answer < number:
            print('Too little. Try again.')
        else:
            print('You are right! You won!\n')
            break
    if answer != number:
        print('Sorry! It was the last effort. You lose!\n')


while True:
    NUMBER = int(random() * 101)
    print('Guess the number I am thinking of.')
    ACT = input('Are you ready? (Y or N): ')

    if ACT.lower() == 'y':
        guess(NUMBER)
    elif ACT.lower() == 'n':
        break
    else:
        print('What do you mean?\n')
        continue
print('Finish.')

##############  2 VARIANT  ##################
'''С циклом while'''

while True:
    NUMBER = int(random() * 101)
    print('Guess the number I am thinking of.')
    ACT = input('Are you ready? (Y or N): ')

    if ACT.lower() == 'y':
        COUNT2 = int(input('Enter the number of tries: '))
        N = 1
        while N <= COUNT2:
            ANSWER = int(input('Enter your answer: '))
            if ANSWER > NUMBER:
                print('Too much. Try again.')
            elif ANSWER < NUMBER:
                print('Too little. Try again.')
            else:
                print('You are right! You won!\n')
                break
            N += 1
        else:
            print('Sorry! It was the last effort. You lose!\n')
    elif ACT.lower() == 'n':
        break
    else:
        print('What do you mean?\n')
        continue
print('Finish.')

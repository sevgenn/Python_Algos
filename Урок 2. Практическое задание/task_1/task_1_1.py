"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Постарайтесь решить задачу двумя способами:
1. Через цикл
Вариант исполнения: в бесконечном цикле запрашивайте вид операции, например, +, - или *
Проверяйте вид операции и запускайте соответствующую команду
Предусмотрите выход из бесконечного цикла
2. Рекурсией.
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, /
- условие завершения рекурсии - введена операция 0

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 45
Введите второе число: 56
Результат 45 + 56 = 101
Введите операцию (+, -, *, / или 0 для выхода): rth
Неверная операция. Повторите ввод
Введите операцию (+, -, *, / или 0 для выхода):

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

###################   1 VARIANT   ######################

LIST_OPERATIONS = ["+", "-", "*", "/"]
while True:
    OPERATION = input(
        'Enter a symbol of the arithmetical operator ("+", "-", "*", "/") or "0" to exit: ')
    if OPERATION == '0':
        break
    elif OPERATION not in LIST_OPERATIONS:
        print('What do you mean? Try again.')
        continue
    else:
        while True:
            try:
                FIRST_NUMBER = float(input('Enter the first number: '))
                SECOND_NUMBER = float(input('Enter the second number: '))

                if OPERATION == '+':
                    RESULT = FIRST_NUMBER + SECOND_NUMBER
                elif OPERATION == '-':
                    RESULT = FIRST_NUMBER - SECOND_NUMBER
                elif OPERATION == '*':
                    RESULT = FIRST_NUMBER * SECOND_NUMBER
                else:
                    RESULT = FIRST_NUMBER / SECOND_NUMBER
                print(f'{FIRST_NUMBER} {OPERATION} {SECOND_NUMBER} = {RESULT}')
                break
            except ZeroDivisionError:
                print('Do you try to divide by zero? Take another divisor, please.')
            except ValueError:
                print('Enter a NUMBER, please.')
                continue
print('Finish.')


###################   2 VARIANT   ######################

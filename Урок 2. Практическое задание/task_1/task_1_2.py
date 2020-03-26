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
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def operators():
    '''this function calls two numbers'''
    global FIRST_NUMBER
    global SECOND_NUMBER
    while True:
        try:
            FIRST_NUMBER = float(input('Enter the first number: '))
            SECOND_NUMBER = float(input('Enter the second number: '))
            break
        except ValueError:
            print('Enter a NUMBER, please.\n')


def add(x, y):
    '''This function adds two numbers'''
    print(f'{x} + {y} = {x + y}')


def subtract(x, y):
    '''This function subtracts two numbers'''
    print(f'{x} - {y} = {x - y}')


def multiply(x, y):
    '''This function multiplies two numbers'''
    print(f'{x} * {y} = {x * y}')


def divide(x, y):
    '''This function divides two numbers'''
    print(f'{x} / {y} = {x / y}')


def calc():
    '''This function return result of arithmetical operations'''
    list_operations = ["+", "-", "*", "/"]
    operation = input('Enter a symbol of the arithmetical operator'
                      '("+", "-", "*", "/") or "0" to exit: ')
    if operation == '0':
        print('Finish.')
        return None
    elif operation not in list_operations:
        print('What do you mean? Try again.\n')
    else:
        operators()
        if operation == '+':
            add(FIRST_NUMBER, SECOND_NUMBER)
        elif operation == '-':
            subtract(FIRST_NUMBER, SECOND_NUMBER)
        elif operation == '*':
            multiply(FIRST_NUMBER, SECOND_NUMBER)
        elif operation == '/':
            while True:
                try:
                    divide(FIRST_NUMBER, SECOND_NUMBER)
                    break
                except ZeroDivisionError:
                    print('Do you try to divide by zero? Take another divisor, please.\n')
                    operators()
    return calc()                           # рекурсивный вызов


calc()

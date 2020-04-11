"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""

from collections import deque


FIRST = deque(input('Enter the first number - ').upper())
SECOND = deque(input('Enter the second number - ').upper())
print(FIRST, SECOND)

##########################################################################
'''Самая короткая реализация'''

S = hex(int(''.join(FIRST), 16) + int(''.join(SECOND), 16))
M = hex(int(''.join(FIRST), 16) * int(''.join(SECOND), 16))
print(int(''.join(FIRST), 16))
print(int(''.join(SECOND), 16))
print(S[2:])
print(M[2:])



##########################################################################
'''Реализация с произвольным модулем через циклы с использованием DEQUE'''

def sum_hex(first, second, mod=16):
    '''Функция сложения'''
# Генерирование базового спмска 16-ричных значений:
    list_hex = [str(i) for i in range(10)] + [chr(j) for j in range(65, 71)]
    # print(list_hex)
# Выравниваем количество разрядов в складываемых числах, заполняя 0:
    diff = abs(len(first) - len(second))
    first.extendleft(['0'] * diff) if len(second) > len(first) else second.extendleft(['0'] * diff)

    result_sum = deque()
    rest = 0
    for i in range(-1, -(len(first) + 1), -1):
        result_sum.appendleft(
            list_hex[(list_hex.index(first[i]) + list_hex.index(second[i]) + rest) % mod])
        if (list_hex.index(first[i]) + list_hex.index(second[i]) + rest) >= mod:
            rest = 1
        else:
            rest = 0
    if rest:
        result_sum.appendleft(1)
    result = f"Сумма чисел списком: {list(result_sum)}\nсумма чисел строкой {''.join(result_sum)}"
    return result

# print(sum_hex(FIRST, SECOND))


def mult_hex(first, second, mod=16):
    '''Функция умножения'''
    list_hex = [str(i) for i in range(10)] + [chr(j) for j in range(65, 71)]
    # print(list_hex)
# Создание результирующего списка с разрядностью n+m:
    n = len(first)
    m = len(second)
    temp = [0] * (m + n)
# Заполнение разрядов:
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            temp[i + j + 1] += list_hex.index(first[i]) * list_hex.index(second[j])
# Обработка по модулю:
    rest = 0
    for k in range(-1, -(len(temp)), -1):
        cell = temp[k] + rest
        if (temp[k] + rest) >= mod:
            temp[k] = (temp[k] + rest) % mod
            rest = cell // mod
        else:
            rest = 0

    if rest > 0:
        temp[0] = rest
    else:
        temp.pop(0)

    result_mult = [list_hex[x] for x in temp]
    result = f"Произведение чисел списком: {list(result_mult)}\nпроизведение чисел строкой {''.join(result_mult)}"
    return result


# print(mult_hex(FIRST, SECOND))



##########################################################################
'''Реализация через класс'''

class Hex_add_mult:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def __add__(self, other=0):
        return list(hex(int(''.join(self.num_1), 16) + int(''.join(self.num_2), 16)))[2:]

    def __mul__(self, othe=0):
        return list(hex(int(''.join(self.num_1), 16) * int(''.join(self.num_2), 16)))[2:]
        # self.mult_result = list(hex(int(''.join(self.num_1), 16) * int(''.join(other), 16)))[2:]
        # return f"Произведение чисел списком: {self.mult_result}"


# x = Hex_add_mult(FIRST, SECOND)
# y = Hex_add_mult(FIRST, SECOND)
#
# print(x + y)
# print(x * y)


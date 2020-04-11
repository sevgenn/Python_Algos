"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога

Предприятия, с прибылью ниже среднего значения: Копыта
"""

import timeit
from random import randint
from collections import Counter
from collections import namedtuple
from collections import deque


"""Стандартный вариант с обычным словарем сделал не по заданию, а из любопытства,
    чтобы в дальнейшем протестировать и сопоставить.
    На тесте показал лучшее время: 0.1754446."""

COMPANIES = {}
N = int(input("Количество предприятий: "))


def common_func(n):
    """Использование обычного словаря"""
    total_profit = 0
    for i in range(n):
        # name = f"common_{i}"      # использовалось для замера времени выполнения алгоритма
        # profit = [float(randint(0, 100)) for _ in range(4)]   #
        # использовалось для замера времени выполнения алгоритма
        name = input(str(i + 1) + "-й предприятие: ")
        profit = list(map(float, input(
            'Через пробел введите прибыль данного предприятия за каждый квартал: ').split()))
        COMPANIES[name] = profit
        total_profit += sum(profit)
    avrg_profit = total_profit / n

    print(f'\nСредняя годовая прибыль всех предприятий: {avrg_profit}')
    print('\nПредприятия, с прибылью выше среднего значения:')
    for i in COMPANIES:
        if sum(COMPANIES[i]) > avrg_profit:
            print(i)
    print('\nПредприятия, с прибылью ниже среднего значения:')
    for i in COMPANIES:
        if sum(COMPANIES[i]) < avrg_profit:
            print(i)

# common_func(N)
# print(COMPANIES)



##########################################################################
"""В последний момент к стандартному словарю добавил DEQUE для количества.
    Но на тесте показало: 0.16620430000000003.
    Может быть, сэкономило на добавлении и извлечении при выводе."""

# COMPANIES = {}
# N = int(input("Количество предприятий: "))


def deque_func(n):
    """Использование обычного словаря и deque"""
    total_profit = 0
    for i in range(n):
        # name = f"common_{i}"      # использовалось для замера времени выполнения алгоритма
        # profit = [float(randint(0, 100)) for _ in range(4)]   #
        # использовалось для замера времени выполнения алгоритма
        name = input(str(i + 1) + "-й предприятие: ")
        profit = list(map(float, input(
            'Через пробел введите прибыль данного предприятия за каждый квартал: ').split()))
        COMPANIES[name] = profit
        total_profit += sum(profit)
    avrg_profit = total_profit / n

    more_avrg = deque()
    less_avrg = deque()
    for i in COMPANIES:
        if sum(COMPANIES[i]) > avrg_profit:
            more_avrg.append(i)
        elif sum(COMPANIES[i]) < avrg_profit:
            less_avrg.append(i)

    print(f'\nСредняя годовая прибыль всех предприятий: {avrg_profit}')
    print('\nПредприятия, с прибылью выше среднего значения:')
    for name in more_avrg:
        print(name)
    print('\nПредприятия, с прибылью ниже среднего значения:')
    for name in less_avrg:
        print(name)

# deque_func(N)
# print(COMPANIES)



##########################################################################
"""Вариант с использованием COUNTER писал только для того, чтоб было.
    На тесте время выполнения лишь немного уступило варианту с обычным словарем: 0.2575118."""

# COMPANIES = {}
# N = int(input("Количество предприятий: "))


def counter_func(n):
    """Использование Counter"""
    for i in range(n):
        # name = f"count_{i}"       # использовалось для замера времени выполнения алгоритма
        # q = [float(randint(0, 100)) for _ in range(4)]    # использовалось для замера
        name = input(str(i + 1) + "-й предприятие: ")
        q = [float(
            input(f'Введите по запросу прибыль данного предприятия за {j+1} квартал: '))
             for j in range(4)]
        COMPANIES[name] = Counter(q_1=q[0], q_2=q[1], q_3=q[2], q_4=q[3])

    total = Counter()
    for k in COMPANIES:
        # total += COMPANIES[k]         # как вариант расчета
        total.update(COMPANIES[k])
    avrg_profit = sum(total.values()) / len(COMPANIES)

    print(f'\nСредняя годовая прибыль всех предприятий: {avrg_profit}')
    print('\nПредприятия, с прибылью выше среднего значения:')
    for name in COMPANIES:
        if sum(COMPANIES[name].values()) > avrg_profit:
            print(name)
    print('\nПредприятия, с прибылью ниже среднего значения:')
    for name in COMPANIES:
        if sum(COMPANIES[name].values()) < avrg_profit:
            print(name)

# counter_func(N)
# print(COMPANIES)



##########################################################################
"""Вариант с использованием NAMEDTUPLE изначально напрашивался сам собой.
    На тесте время выполнения худшее из всех вариантов: 0.30894900000000003.
    Возможно, я где-то криво написал программу."""

# COMPANIES = {}
# N = int(input("Количество предприятий: "))


def tuple_func(n):
    """Использование namedtuple"""
    Company = namedtuple('Company', 'q_1 q_2 q_3 q_4 year_profit')
    for i in range(n):
        # name = f"tuple_{i}"       # использовалось для замера времени выполнения алгоритма
        # profit = [float(randint(0, 100)) for _ in range(4)]  # использовалось
        # для замера времени выполнения алгоритма
        name = input(str(i + 1) + "-й предприятие: ")
        profit = [float(x) for x in input(
            'Через пробел введите прибыль данного предприятия за каждый квартал: ').split()]
        year_profit = sum(profit)
        COMPANIES[name] = Company(*profit, year_profit)

    total_profit = 0
    for name in COMPANIES:
        total_profit += COMPANIES[name].year_profit
    avrg_profit = total_profit / len(COMPANIES)

    print()
    print(f'Средняя годовая прибыль всех предприятий: {avrg_profit}')
    print('\nПредприятия, с прибылью выше среднего значения:')
    for name in COMPANIES:
        if COMPANIES[name].year_profit > avrg_profit:
            print(name)
    print('\nПредприятия, с прибылью ниже среднего значения:')
    for name in COMPANIES:
        if COMPANIES[name].year_profit < avrg_profit:
            print(name)

# tuple_func(N)
# print(COMPANIES)


N = 10
COMPANIES = {}
"""
Тесты запускал по очереди, чтобы не было конфликтов из-за словаря COMPANIES,
сформированного разными методами.
"""
######## Цикл:
# print(timeit.timeit('common_func(n)', setup='from __main__ import common_func, n', number=1000))
######## Counter:
# print(timeit.timeit('counter_func(n)', setup='from __main__ import counter_func, n', number=1000))
######## NAMEDTUPLE:
# print(timeit.timeit('tuple_func(n)', setup='from __main__ import tuple_func, n', number=1000))
######## DEQUE:
# print(timeit.timeit('deque_func(n)', setup='from __main__ import deque_func, n', number=1000))

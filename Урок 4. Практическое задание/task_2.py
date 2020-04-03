"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

import math
import timeit

###########   Не решето   ################
def prime(k):
    # k <= 1.5 * k * math.log(k)      - простое к-ое не больше, чем 1.5 k log(k)
    stop = int(1.5 * k * math.log(k)) + 1
    result = [2]
    for i in range(3, stop+1, 2):
        if i > 10 and i % 10 == 5:
            continue
        for j in result:
            if j > round((math.sqrt(i)) + 1):
                result.append(i)
                break
            if i % j == 0:
                break
        else:
            result.append(i)
    return result[k-1]

# K = int(input('Enter the number - '))
# print(prime(K))


###########   Решето   ################
def f_erat(k):
    stop = int(1.5 * k * math.log(k)) + 1
    numbers = list(range(2, stop+1))

    divider = 2
    while divider ** 2 <= stop:
        for i in range(divider ** 2, stop+1, divider):
            numbers[i-2] = 0

        divider += 1
        while divider ** 2 <= stop and numbers[divider-2] == 0:
            divider += 1

    primes = [i for i in numbers if i != 0]
    del numbers
    return primes[K-1]


# K = int(input('Enter the number - '))
# print(f_erat(K))

K = 100

print(timeit.timeit("prime(K)", setup="from __main__ import prime, K", number=100))
print(timeit.timeit("f_erat(K)", setup="from __main__ import f_erat, K", number=100))

'''
Первый алгоритм отрабатывает быстрее, поскольку сложность алгоритма квадратичная,
а во втором случае сложность, скорее всего, линейно-логарифмическая.
Поэтому при увеличении значения К время выполнения первого алгоритма увеличивается
в значительной степени.

Но оба алгоритма не доведены до ума из-за нехватки времени.
В основе лежит перебор от начала списка. Имеет смысл в этом
случае вести перебор от конца списка, что должно снизить
временные затраты.
Пока отправляю в таком виде. Когда появится свободное время,
постараюсь переделать.
'''

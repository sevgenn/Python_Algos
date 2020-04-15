"""
1.	Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.


ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

"""
Задание_4. Определить, какое число в массиве встречается чаще всего
"""


import time
import memory_profiler
from random import randint
from memory_profiler import profile
from guppy import hpy



###########   1 VARIANT  (ЦИКЛ) ################

# @profile
def frequent_number_1(num):
    seq = [randint(-10, 10) for _ in range(num)]
    set_seq = set(seq)
    max_count = 0
    for i in set_seq:
        quant = seq.count(i)
        if quant > max_count:
            max_count = quant
            max_item = i
    print(seq)
    print('Первый вариант:')
    print(f'Число {max_item} в массиве встречается чаще всего: {max_count} раз(а).')



###########   2 VARIANT  (MAX, KEY) ################

# @profile
def frequent_number_2(num):
    seq = [randint(-10, 10) for _ in range(num)]
    print(seq)
    print('Второй вариант:')
    print(f'Число {max(seq, key=seq.count)} встречается '
          f'{seq.count(max(seq, key=seq.count))} раз.')



h = hpy()
frequent_number_1(40000)
print(h.heap())
print()

h = hpy()
frequent_number_2(40000)
print(h.heap())


# if __name__ == '__main__':
#
#     t1 = time.process_time()
#     m1 = memory_profiler.memory_usage()
#
#     frequent_number_1(40000)
#     frequent_number_2(40000)
#
#     t2 = time.process_time()
#     m2 = memory_profiler.memory_usage()
#
#     time_diff = t2 - t1
#     mem_diff = m2[0] - m1[0]
#     print(f"Выполнение frequent_number_1 заняло {time_diff} сек and {mem_diff} Мб")




##################      РЕЗУЛЬТАТЫ      ########################

# Выполнение frequent_number_1 заняло 0.109375 сек and 0.11328125 Мб
# Выполнение frequent_number_2 заняло 60.0 сек and 0.06640625 Мб

##################   PROFILE   #########################

# Первый вариант:
# Число -3 в массиве встречается чаще всего: 1971 раз(а).
# Filename: F:/GeekBrains/Algorithms/DZ/Урок 6. Практическое задание/task_3.py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     28     13.6 MiB     13.6 MiB   @profile
#     29                             def frequent_number_1(num):
#     30     14.0 MiB      0.1 MiB       seq = [randint(-10, 10) for _ in range(num)]
#     31     14.0 MiB      0.0 MiB       set_seq = set(seq)
#     32     14.0 MiB      0.0 MiB       max_count = 0
#     33     14.0 MiB      0.0 MiB       for i in set_seq:
#     34     14.0 MiB      0.0 MiB           quant = seq.count(i)
#     35     14.0 MiB      0.0 MiB           if quant > max_count:
#     36     14.0 MiB      0.0 MiB               max_count = quant
#     37     14.0 MiB      0.0 MiB               max_item = i
#     38     13.9 MiB      0.0 MiB       print(seq)
#     39     13.9 MiB      0.0 MiB       print('ПЕрвый вариант:')
#     40     13.9 MiB      0.0 MiB       print(f'Число {max_item} в массиве встречается чаще всего: {max_count} раз(а).')


# Второй вариант:
# Число -4 встречается 1998 раз.
# Filename: F:/GeekBrains/Algorithms/DZ/Урок 6. Практическое задание/task_3.py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     45     13.7 MiB     13.7 MiB   @profile
#     46                             def frequent_number_2(num):
#     47     14.0 MiB      0.1 MiB       seq = [randint(-10, 10) for _ in range(num)]
#     48     13.9 MiB      0.0 MiB       print(seq)
#     49     13.9 MiB      0.0 MiB       print('Второй вариант:')
#     50     13.8 MiB      0.0 MiB       print(f'Число {max(seq, key=seq.count)} встречается '
#     51                                       f'{seq.count(max(seq, key=seq.count))} раз.')



##################   HEAP   #########################

# Первый вариант:
# Число -4 в массиве встречается чаще всего: 1972 раз(а).
# Partition of a set of 55772 objects. Total size = 3875952 bytes.
#  Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
#      0  16918  30  1168736  30   1168736  30 str
#      1   7783  14   440358  11   1609094  42 bytes
#      2  11915  21   418532  11   2027626  52 tuple
#      3   3934   7   410922  11   2438548  63 types.CodeType
#      4   3856   7   262208   7   2700756  70 function
#      5    623   1   259248   7   2960004  76 type
#      6    623   1   186164   5   3146168  81 dict of type
#      7    149   0   144136   4   3290304  85 dict of module
#      8    500   1   105500   3   3395804  88 dict (no owner)
#      9   1222   2    43992   1   3439796  89 types.WrapperDescriptorType


# Второй вариант:
# Число -5 встречается 2026 раз.
# Partition of a set of 55721 objects. Total size = 3874796 bytes.
#  Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
#      0  16918  30  1168736  30   1168736  30 str
#      1   7783  14   440358  11   1609094  42 bytes
#      2  11915  21   418532  11   2027626  52 tuple
#      3   3934   7   410922  11   2438548  63 types.CodeType
#      4   3856   7   262208   7   2700756  70 function
#      5    623   1   259248   7   2960004  76 type
#      6    623   1   186164   5   3146168  81 dict of type
#      7    149   0   144136   4   3290304  85 dict of module
#      8    500   1   105500   3   3395804  88 dict (no owner)
#      9   1222   2    43992   1   3439796  89 types.WrapperDescriptorType

'''
(Python 3.8 32-bit; Windows 10x64; PyCharm 2019.3.2)

Тесты с использованием модулей guppy и profile дали почти одинаковые результаты для обоих вариантов.
Существенного инкремента памяти в ходе выполнения не наблюдается.
Второй вариант с исподьзованием параметра key чуть меньше нагружает память по результатам profile.
Но этот же вариант тратит очень много времени на обработку при больших размерах обрабатываемого
списка.
Экономия памяти достигается за счет того, что не выделяется место под новые переменные.
Но из-за того, что каждый раз приходится вычислять значение max, многократно возрастают временные
затраты. Если в теле функции создать 2 временные переменные М - для max и N - для max_count,
то по результатам замеров время сократится в два раза.
'''

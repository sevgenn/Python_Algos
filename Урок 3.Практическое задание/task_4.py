"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""

from random import randint

SEQUENCE = [randint(-10, 10) for _ in range(21)]

###########   1 VARIANT  (ЦИКЛ) ################

SET_SEQ = set(SEQUENCE)
MAX_COUNT = 0
for i in SET_SEQ:
    QUANT = SEQUENCE.count(i)
    if QUANT > MAX_COUNT:
        MAX_COUNT = QUANT
        MAX_ITEM = i
print(SEQUENCE)
print('ПЕрвый вариант:')
print(f'Число {MAX_ITEM} в массиве встречается чаще всего: {MAX_COUNT} раз(а).')
print()

###########   2 VARIANT  (MAX, KEY) ################

print('Второй вариант:')
print(f'Число {max(SEQUENCE, key=SEQUENCE.count)} встречается '
      f'{SEQUENCE.count(max(SEQUENCE, key=SEQUENCE.count))} раз.')

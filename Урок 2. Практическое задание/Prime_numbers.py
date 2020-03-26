import math

#############   1 VARIANT   ERATOSPHEN   #################

STOP = int(input('Enter the final number - '))
NUMBERS = list(range(2, STOP+1))

DIVIDER = 2
while DIVIDER * DIVIDER <= STOP:
    for i in range(DIVIDER * DIVIDER, STOP+1, DIVIDER):
        NUMBERS[i-2] = 0

    DIVIDER += 1
    while DIVIDER *DIVIDER <= STOP and NUMBERS[DIVIDER-2] == 0:
        DIVIDER += 1

PRIMES = [i for i in NUMBERS if i != 0]
del NUMBERS
print('Простые числа в ряду:')
print(PRIMES)


#############   2 VARIANT   #################
'''
Вариант, возможно, кривой, но мой.
Когда-то давно заметил закономерность простых чисел, проявляющуюся в 3-ичной системе
(во всяком случае на относительно малых отрезках).
К сожалению при четком следовании этой закономерности в список попадают числа,
не являющиеся простыми.
Алгоритм строится на том, чтобы изначально не загружать память созданием и перебором полного ряда
натуральных чисел, а сформировать список только простых чисел и входящих исключений.
Затем удалить исключения. 
В конечном итоге просматривать нужно не весь ряд натуральных чисел, а укороченный.
На сколько это экономит время (и экономит ли вообще) не могу судить.
'''

STOP_2 = int(input('Enter the final number - '))
NUMBERS_2 = list(range(0, STOP_2+1))            # для справки
print(NUMBERS_2)
RESULT = [2,3]

COUNT = 1
for i in range(5, STOP_2+1, 2):
    if COUNT % 3 != 0 :
        RESULT.append(NUMBERS_2[i])
        COUNT += 1
    else:
        COUNT += 1
        continue
print(RESULT)               # список приближенный к списку простых

for i in range(len(RESULT)):                            # исключение лишних вхождений
    for j in range(3, round(math.sqrt(RESULT[-1]))+1):
        if RESULT[i] % j == 0 and RESULT[i] // j > 1:
            RESULT[i] = 0

PRIMES_2 = [i for i in RESULT if i != 0]
print(PRIMES_2)
